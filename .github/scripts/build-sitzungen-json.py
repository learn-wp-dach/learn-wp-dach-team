#!/usr/bin/env python3
"""
Liest Issues mit Label 'sitzung' und erzeugt sitzungen.json
gemäß dem Schema v2.

Pfad-Empfehlung: .github/scripts/build-sitzungen-json.py
im Repo learn-wp-dach-team.

Aufruf:
    python3 build-sitzungen-json.py \\
        --input issues.json \\
        --repo owner/name \\
        --output sitzungen.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

# Schema-Version – bei Breaking Changes hochsetzen.
# v2 (2026-05): drei Listen (upcoming, in_progress, past); title aus
# Body-Feld "Veranstaltung:"; Einordnung anhand Label "Erledigt".
SCHEMA_VERSION = 2

# Label, das ein Issue als "fertig protokolliert" markiert.
LABEL_DONE = "erledigt"

# Datum im Titel: das erste YYYY-MM-DD-Vorkommen gewinnt.
TITLE_DATE_RE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")

# Body-Feld "Veranstaltung:". Wir akzeptieren drei Formen:
#   Veranstaltung: Sitzung          (Plain-Text, häufigste bei manuellen Issues)
#   **Veranstaltung:** Sitzung      (Bold)
#   ### Veranstaltung               (Heading mit Wert in der nächsten Zeile)
#   Sitzung
EVENT_INLINE_RE = re.compile(
    r"^\s*\*{0,2}\s*Veranstaltung\s*:\s*\*{0,2}\s*(.+?)\s*$",
    re.MULTILINE | re.IGNORECASE,
)
EVENT_HEADING_RE = re.compile(
    r"^###\s*Veranstaltung\s*$\n+^\s*(.+?)\s*$",
    re.MULTILINE | re.IGNORECASE,
)

# Body-Feld "Uhrzeit:". Drei Formen analog zu Veranstaltung.
TIME_INLINE_RE = re.compile(
    r"^\s*\*{0,2}\s*Uhrzeit\s*:\s*\*{0,2}\s*(\d{1,2}:\d{2})",
    re.MULTILINE | re.IGNORECASE,
)
TIME_HEADING_RE = re.compile(
    r"^###\s*Uhrzeit\s*$\n+^\s*(\d{1,2}:\d{2})",
    re.MULTILINE | re.IGNORECASE,
)


def extract_session_date(title: str) -> str | None:
    """Liefert das erste YYYY-MM-DD aus dem Titel oder None."""
    match = TITLE_DATE_RE.search(title or "")
    return match.group(1) if match else None


def extract_event_name(body: str, fallback_title: str) -> str:
    """Liefert den String hinter "Veranstaltung:" aus dem Body.

    Fällt auf den Issue-Titel ohne Datum zurück, wenn das Feld fehlt.
    """
    body = body or ""
    match = EVENT_INLINE_RE.search(body)
    if not match:
        match = EVENT_HEADING_RE.search(body)
    if match:
        value = match.group(1).strip()
        if value:
            return value
    # Fallback: Issue-Titel minus Datum, getrimmt.
    name = TITLE_DATE_RE.sub("", fallback_title or "").strip()
    return name or (fallback_title or "")


def extract_session_time(body: str) -> str:
    """Liefert HH:MM aus dem Body oder leerer String."""
    body = body or ""
    match = TIME_INLINE_RE.search(body)
    if not match:
        match = TIME_HEADING_RE.search(body)
    if not match:
        return ""
    hh, mm = match.group(1).split(":")
    return f"{int(hh):02d}:{mm}"


def extract_minutes_date(closed_at: str | None) -> str:
    """Liefert YYYY-MM-DD aus closedAt oder leerer String."""
    if not closed_at:
        return ""
    try:
        dt = datetime.fromisoformat(closed_at.replace("Z", "+00:00"))
        return dt.date().isoformat()
    except ValueError:
        return ""


def has_label(issue: dict, label_name: str) -> bool:
    """True, wenn Issue das Label trägt (case-insensitive)."""
    target = label_name.lower()
    for lbl in issue.get("labels", []) or []:
        name = (lbl.get("name") or "") if isinstance(lbl, dict) else str(lbl)
        if name.lower() == target:
            return True
    return False


def is_done(issue: dict) -> bool:
    """True, wenn das Issue als 'erledigt' gilt.

    Erledigt heisst:
      - explizit per Label "Erledigt" (case-insensitive) markiert, ODER
      - Issue ist geschlossen (state == "CLOSED").

    Beides ergibt im Frontend einen Eintrag im Protokoll-Block.
    """
    if has_label(issue, LABEL_DONE):
        return True
    state = (issue.get("state") or "").upper()
    return state == "CLOSED"


def build(issues: list[dict], repo: str, today: date | None = None) -> dict:
    """Baut die JSON-Struktur.

    Einordnung:
    - Erledigt (Label "Erledigt" ODER state=CLOSED)
        → past_sessions (mit minutes_date)
    - sonst, session_date >= heute
        → upcoming_sessions (mit session_time)
    - sonst, session_date < heute
        → in_progress_sessions (mit session_time)
    """
    today = today or date.today()

    upcoming: list[dict] = []
    in_progress: list[dict] = []
    past: list[dict] = []

    for issue in issues:
        title = issue.get("title", "")
        session_date = extract_session_date(title)
        if not session_date:
            # Issue mit Label 'sitzung' ohne erkennbares Datum → überspringen.
            continue

        url = issue.get("url", "")
        body = issue.get("body", "") or ""
        event_name = extract_event_name(body, title)
        done = is_done(issue)

        if done:
            past.append(
                {
                    "title": event_name,
                    "session_date": session_date,
                    "minutes_date": extract_minutes_date(issue.get("closedAt")),
                    "url": url,
                }
            )
            continue

        try:
            session_date_obj = date.fromisoformat(session_date)
        except ValueError:
            continue

        record = {
            "title": event_name,
            "session_date": session_date,
            "session_time": extract_session_time(body),
            "url": url,
        }

        if session_date_obj >= today:
            upcoming.append(record)
        else:
            in_progress.append(record)

    # Upcoming: aufsteigend (die als nächstes anstehende oben).
    upcoming.sort(key=lambda s: (s["session_date"], s.get("session_time") or ""))
    # In progress: absteigend (die jüngste, also am dringendsten zu protokollieren, oben).
    in_progress.sort(key=lambda s: s["session_date"], reverse=True)
    # Past: absteigend nach session_date.
    past.sort(key=lambda s: s["session_date"], reverse=True)

    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source_repo": repo,
        "upcoming_sessions": upcoming,
        "in_progress_sessions": in_progress,
        "past_sessions": past,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Pfad zur Issues-JSON (gh issue list ...)")
    parser.add_argument("--repo", required=True, help="owner/name, z. B. learn-wp-dach/learn-wp-dach-team")
    parser.add_argument("--output", required=True, help="Pfad zur Ausgabe-JSON")
    args = parser.parse_args()

    issues_path = Path(args.input)
    if not issues_path.exists():
        print(f"Input-Datei nicht gefunden: {issues_path}", file=sys.stderr)
        return 1

    with issues_path.open("r", encoding="utf-8") as fh:
        issues = json.load(fh)

    if not isinstance(issues, list):
        print("Erwarte JSON-Array von Issues.", file=sys.stderr)
        return 1

    payload = build(issues, args.repo)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    print(f"Geschrieben: {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
