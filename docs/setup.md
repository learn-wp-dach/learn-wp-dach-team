# Setup-Anleitung (Admin)

Diese Anleitung beschreibt die einmalige Einrichtung des Repositories für neue Instanzen oder nach einem Repository-Transfer.

> **Stand Oktober 2026:** Das Repository gehört der Organisation [learn-wp-dach](https://github.com/learn-wp-dach), das Kanban-Board ist das Org-Projekt Nr. 1 unter `https://github.com/orgs/learn-wp-dach/projects/1`. Owner der Organisation sind Rico (`rfluethi`) und Andy (`Bigod`). Die Sitzungen werden nicht mehr in der README geführt, sondern auf [learn-wp-dach.org](https://learn-wp-dach.org/termine/monatliche-treffen/) angezeigt.

---

## Voraussetzungen

- GitHub-Account mit Admin-Rechten auf dem Repository
- [GitHub CLI](https://cli.github.com) installiert (`brew install gh`) und eingeloggt (`gh auth login`)
- Git installiert

---

## Schritt 1: Repository erstellen

1. GitHub.com → **New repository**
2. Name: `learn-wp-dach-team`
3. Sichtbarkeit: **Private** (zum Testen) oder **Public** (nach Teamentscheid)
4. README: Ja (ankreuzen)
5. **Create repository**

---

## Schritt 2: Issue-Vorlagen einfügen

```bash
# Repository klonen
git clone https://github.com/DEIN-USERNAME/learn-wp-dach-team.git
cd learn-wp-dach-team

# Ordner erstellen
mkdir -p .github/ISSUE_TEMPLATE
```

Die drei Vorlagen-Dateien in `.github/ISSUE_TEMPLATE/` ablegen:

- `sitzung.yml`
- `thema.yml`
- `aufgabe.yml`

```bash
git add .github/
git commit -m "Issue-Vorlagen für Sitzungen, Themen und Aufgaben"
git push
```

**Prüfen:** Issues → **New issue** → Alle drei Vorlagen erscheinen.

---

## Schritt 3: Labels erstellen

```bash
REPO="DEIN-USERNAME/learn-wp-dach-team"

gh label create "sitzung"         --repo "$REPO" --color "0075ca" --description "Monatliches Team-Meeting (Themen + Protokoll)" --force
gh label create "thema"           --repo "$REPO" --color "e4e669" --description "Vorgeschlagenes Diskussionsthema für nächste Sitzung" --force
gh label create "aufgabe"         --repo "$REPO" --color "f4a261" --description "Action Item / Task aus einer Sitzung" --force
gh label create "beschluss"       --repo "$REPO" --color "0e8a16" --description "Entscheidung gefällt" --force
gh label create "blockiert"       --repo "$REPO" --color "d73a4a" --description "Aufgabe hat einen Blocker oder Abhängigkeit" --force
gh label create "überprüfung"     --repo "$REPO" --color "f9c513" --description "Aufgabe erledigt – wartet auf Kontrolle durch eine zweite Person" --force
gh label create "nächste-sitzung" --repo "$REPO" --color "bfd4f2" --description "Vertagt – kommt in die nächste Sitzung" --force
gh label create "lerngruppe"      --repo "$REPO" --color "7057ff" --description "Thema rund um Lerngruppen" --force
gh label create "webseite"        --repo "$REPO" --color "cfd3d7" --description "Thema rund um learn-wp-dach.org" --force
gh label create "übersetzung"     --repo "$REPO" --color "006b75" --description "Übersetzungsprojekte" --force
gh label create "organisation"    --repo "$REPO" --color "e99695" --description "Organisatorische Aufgaben" --force
```

**Prüfen:** Issues → **Labels** → 10 Labels sichtbar.

---

## Schritt 4: GitHub Project (Kanban Board) erstellen

1. GitHub → Tab **Projects** → **New project**
2. Vorlage: **Board**
3. Name: `Learn WP DACH – Aufgaben`
4. Spalten erstellen (Themen, Offen, In Arbeit, Blockiert, Überprüfung, Erledigt):

   | Spalte | Beschreibung |
   | --- | --- |
   | Themen | Vorgeschlagene Diskussionsthemen |
   | Offen | Aufgaben, noch nicht begonnen |
   | In Arbeit | Aufgaben aktiv in Bearbeitung |
   | Blockiert | Aufgaben mit Blocker oder Abhängigkeit |
   | Überprüfung | Aufgabe erledigt – wartet auf Kontrolle durch eine zweite Person |
   | Erledigt | Abgeschlossene und geprüfte Aufgaben |

5. Automation einrichten: Project → **Workflows** (Knopf oben rechts)
   - *Auto-add to project* → Repository `learn-wp-dach-team`, Filter `is:issue is:open`
   - *Item added to project* → Status: **Offen**
   - *Item closed* → Status: **Erledigt**
   - *Item reopened* → Status: **Offen**

   GitHub schlägt bei *Auto-add* den Filter `is:issue,pr is:open` vor. Das `,pr` entfernen, sonst landen auch Pull Requests im Board. Im Plan GitHub Free erlaubt jedes Projekt nur **eine** Auto-add-Regel und damit nur ein Repository. Regel bei uns: ein Board pro Repository. Das Aufgaben-Board bleibt dem Team-Repository vorbehalten, ein neues Repository (etwa für das Handbuch) bekommt ein eigenes Board.
6. Feld **Estimate** erstellen: Project → **`...`** → **Settings** → **Custom fields** → **Add field**
   - Typ: **Number**
   - Name: `Estimate`
   - Dieses Feld nimmt den geschätzten Zeitbedarf pro Thema in Minuten auf und erlaubt eine Gesamtschätzung der Sitzungsdauer.

---

## Schritt 5: Sitzungsdaten für die Website

Die Sitzungen werden **nicht** in der `README.md` geführt. Der frühere Workflow `protokoll-index.yml`, der die README automatisch neu geschrieben hat, wurde im September 2026 entfernt. Grund: Jeder automatische Commit auf `main` erscheint dauerhaft in der Kontributoren-Anzeige des Repositories, und diese Einträge lassen sich nachträglich nicht mehr entfernen. Auf `main` committen deshalb nur noch Menschen.

Die Sitzungsdaten liefert stattdessen der Workflow `sitzungen-json.yml` auf den `data`-Branch, von dort holt sie das WordPress-Plugin Training Meeting Tracker für die Seite [Unsere Treffen](https://learn-wp-dach.org/termine/monatliche-treffen/).

### Hinweis: sitzungen.json für das WordPress-Plugin

Im Repo `learn-wp-dach-team` läuft die Action `sitzungen-json.yml` weiter und schreibt `sitzungen.json` auf den `data`-Branch. Sie wird vom neuen Plugin (Training Meeting Tracker) genauso konsumiert wie vom alten. Hier ist nichts zu ändern, sofern die Datenquelle gleich bleiben soll.

Die Workflow-Datei liegt unter `.github/workflows/sitzungen-json.yml`. Sie nutzt das Python-Skript `.github/scripts/build-sitzungen-json.py` und legt den `data`-Branch beim ersten Lauf automatisch als Orphan-Branch an. Der Branch hat eine eigene Historie ohne Verbindung zu `main`; Commits dort zählen nicht für die Kontributoren-Anzeige. Trigger sind Issue-Events mit dem Label `sitzung`, ein 12-Stunden-Cron und manueller Start über die Actions-Oberfläche.

---

## Schritt 6: Thema-Workflow einrichten

Dieser Workflow verschiebt Issues mit dem Label `thema` automatisch in die Spalte **Themen** des Kanban Boards.

### 6a: Fine-grained Personal Access Token erstellen

Das normale `GITHUB_TOKEN` hat keinen Zugriff auf Projekte der Organisation. Deshalb braucht es einen fine-grained PAT. Er gehört dem Konto eines Owners, ist aber der Organisation zugeordnet, die ihn zentral sehen und widerrufen kann.

1. GitHub.com → Avatar → **Settings** → **Developer settings** → **Personal access tokens** → **Fine-grained tokens**
2. **Generate new token**
3. Token name: `learn-wp-dach thema-board` (aktueller Token, ausgestellt am 3. Oktober 2026 auf `rfluethi`, gültig bis 4. Oktober 2027)
4. **Resource owner:** `learn-wp-dach` (die Organisation, nicht das eigene Konto)
5. **Expiration:** 366 Tage. Für das Ablaufdatum einen Kalendereintrag bei beiden Owners zwei Wochen vorher anlegen. Bewusst kein Issue: Es würde im Aufgaben-Board erscheinen und in jeder Sitzung auftauchen.
6. **Repository access:** Only select repositories → `learn-wp-dach-team`
7. Berechtigungen, genau zwei. Im Kasten **Permissions** gibt es die Reiter **Repositories** und **Organizations**; «Add permissions» fügt nur für den gerade aktiven Reiter hinzu:
   - Reiter **Organizations** → **Projects:** Read and write
   - Reiter **Repositories** → **Issues:** Read-only (Metadata Read-only setzt GitHub automatisch)
8. **Generate token** → Token kopieren

Läuft der Token ab, landen neue Themen nicht mehr automatisch in der Spalte Themen und müssen von Hand ins Board gezogen werden. Die Sitzungsdaten für die Website sind nicht betroffen, dieser Workflow läuft über den eingebauten Token.

### 6b: Token als Repository-Secret speichern

1. Repository → **Settings** → **Secrets and variables** → **Actions**
2. **New repository secret**
3. Name: `GH_PAT` (genau so)
4. Secret: den kopierten Token einfügen
5. **Add secret**

> Den Token nie in den Code oder in einen Chat einfügen – immer nur als Secret speichern.

Per GitHub CLI, ohne dass der Token in der Terminal-Historie landet (zsh):

```bash
read -s "T?Token einfügen und Enter: "; echo
T="${T//[^A-Za-z0-9_]/}"          # unsichtbare Zeichen aus dem Browser entfernen
echo "${T:0:11}… Länge ${#T}"     # Erwartet: github_pat_… Länge 93
GH_TOKEN=$T gh api graphql -f query='query{organization(login:"learn-wp-dach"){projectV2(number:1){title}}}'
printf %s "$T" | gh secret set GH_PAT --repo learn-wp-dach/learn-wp-dach-team
unset T
```

### 6c: Workflow-Datei einfügen

```bash
# Datei thema-board.yml in .github/workflows/ ablegen
git add .github/workflows/thema-board.yml
git commit -m "Workflow: Thema automatisch ins Board einordnen"
git push
```

**Prüfen:** Ein neues Issue mit Vorlage "Thema" erstellen → erscheint nach ca. 30 Sekunden in der Spalte **Themen**.

---

## Schritt 7: Copilot Coding Agent deaktivieren

> **Wichtig:** Ohne diese Einstellung übernimmt der Copilot Coding Agent Issues und verschiebt sie ins Kanban Board.

1. GitHub.com → Avatar → **Settings**
2. **Copilot** → **Coding agent**
3. **Repository access** → **"Selected repositories"**
4. `learn-wp-dach-team` **nicht** aufnehmen

---

## Schritt 8: Copilot-Training deaktivieren *(bei öffentlichem Repo)*

1. GitHub.com → Avatar → **Settings**
2. **Copilot** → **Features**
3. Abschnitt **Privacy** → **"Allow GitHub to use my data for AI model training"** → **Disabled**

> Bei privaten Repositories nicht zwingend nötig.

---

## Schritt 9: Teammitglieder einladen

Teammitglieder werden in die Organisation eingeladen, nicht ins Repository: Organisation → **People** → **Invite member**. Alle brauchen einen GitHub-Account.

Rollen, zwei getrennte Ebenen:

| Ebene | Rolle für Mitglieder | Wo einstellen |
| --- | --- | --- |
| Repository | **Write** (nötig, um Text in fremden Issues zu bearbeiten, z.B. Themen im Sitzungs-Issue nachtragen) | Repository → Settings → Collaborators and teams |
| Projekt (Board) | **Write** über die Base role der Organisation | Projekt → Settings → Manage access |

Owner der Organisation haben automatisch Admin auf beiden Ebenen. Base permission der Organisation steht auf **Read** (Organisation → Settings → Member privileges), damit neue Repositories nicht automatisch für alle beschreibbar sind.

> Alle neuen Teammitglieder sollten [CONTRIBUTING.md](../CONTRIBUTING.md) und [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md) lesen, bevor sie aktiv werden.

---

## Schritt 10: Branch-Protection einrichten

Seit kein Workflow mehr auf `main` committet, kann der Branch ohne Ausnahmen geschützt werden. Eingerichtet am 3. Oktober 2026 als Ruleset «Schutz main und archiv-main».

| Einstellung | Wert |
| --- | --- |
| Ziel | Standard-Branch (`main`) und `archiv-main` |
| Branch löschen | verboten |
| Historie überschreiben (Force-Push) | verboten |
| Änderungen | nur per Pull Request mit **1 Freigabe** (sonst könnten Mitglieder mit Write ihre eigenen Pull Requests selbst mergen) |
| Ausnahme | Organization admins (Owner) dürfen im Notfall direkt pushen |

Ansehen und ändern: Repository → **Settings** → **Rules** → **Rulesets**. Kontrolle per CLI: `gh api repos/learn-wp-dach/learn-wp-dach-team/rules/branches/main`. Der `data`-Branch ist bewusst nicht geschützt, dorthin schreibt der Website-Workflow.

Issues und Board sind davon nicht betroffen, nur Änderungen an Dateien laufen über Pull Requests.

---

## Troubleshooting

### Workflow schlägt fehl

**Symptom:** GitHub Actions zeigt roten Fehler beim `thema-board.yml` oder `sitzungen-json.yml`.

**Vorgehen:**

1. Repository → **Actions** → fehlgeschlagenen Run öffnen → Fehlermeldung lesen
2. Häufige Ursachen:

| Fehlermeldung | Ursache | Lösung |
| --- | --- | --- |
| `Could not resolve to a node with the global id` | PAT fehlt die Berechtigung Projects oder Issues | PAT prüfen (Schritt 6a), Secret `GH_PAT` aktualisieren |
| `Resource not accessible by integration` | `GH_PAT` Secret fehlt oder ist abgelaufen | Repository → Settings → Secrets → `GH_PAT` prüfen oder neu setzen |
| `Projekt nicht gefunden` | Project-Nummer in Workflow stimmt nicht | Workflow-Datei: `projectV2(number: ...)` auf aktuelle Nummer prüfen |
| `jq: error` | Unerwartete API-Antwort | Run nochmals manuell starten; falls Problem anhält, API-Response im Log prüfen |

3. Manuell testen: Repository → **Actions** → **sitzungen.json aktualisieren** → **Run workflow**

### PAT erneuern

Der Token läuft nach 366 Tagen ab, der aktuelle am **4. Oktober 2027**. Die Erinnerung kommt über einen Kalendereintrag beider Owner (20. September 2027), zusätzlich schickt GitHub dem Besitzer des Tokens vor Ablauf eine E-Mail.

1. GitHub.com → Avatar → **Settings** → **Developer settings** → **Personal access tokens** → **Fine-grained tokens**
2. Bestehenden Token wählen → **Regenerate token** → neue Laufzeit wählen
3. Token kopieren → Repository → **Settings** → **Secrets and variables** → **Actions** → `GH_PAT` → **Update secret**
4. Kalendereintrag für beide Owner auf das neue Ablaufdatum minus zwei Wochen verschieben
5. Testen: Actions → **Thema ins Board einordnen** läuft beim nächsten Themen-Issue grün

Fällt der Owner aus, dem der Token gehört, läuft der Token bis zum Ablauf weiter. Der andere Owner kann ihn unter Organisation → Settings → Personal access tokens widerrufen und nach Schritt 6a einen eigenen anlegen.

---

## Repository-Umzug

Der Umzug in die Organisation `learn-wp-dach` ist am 3. Oktober 2026 per Transfer erfolgt. Alle Issues, Kommentare, Labels und Zuweisungen sind erhalten geblieben, die alten Adressen unter `rfluethi/learn-wp-dach-team` leiten weiter.

**Regel:** Unter dem Konto `rfluethi` darf nie wieder ein Repository namens `learn-wp-dach-team` angelegt werden. Sobald der alte Name belegt ist, enden alle Weiterleitungen auf einen Schlag: alte Links in Slack, in Protokollen, in Lesezeichen und im Plugin.

Das alte Board `users/rfluethi/projects/11` ist geschlossen, aber nicht gelöscht. Ältere Issues verlinken darauf, und auf Projekte greift keine Weiterleitung. **Nie löschen.**

Das WordPress-Plugin Training Meeting Tracker (produktiv und staging) liest seit dem Umzug `https://raw.githubusercontent.com/learn-wp-dach/learn-wp-dach-team/data/sitzungen.json`. Das Plugin speichert Abrufe 12 Stunden zwischen, nach einer Änderung der Quelle im Plugin auf «Jetzt aktualisieren» klicken.

### Neue Historie auf main

Ziel: In der Kontributoren-Anzeige erscheinen nur Menschen. Der Transfer hatte die alte Historie mit über 350 Bot-Commits übernommen, eine frühere Bereinigung per Force-Push (April 2026) hatte nicht gewirkt. Deshalb hat `main` seit dem 3. Oktober 2026 einen neuen Anfangscommit (`41814c5`) mit identischem Inhalt. Die vollständige alte Historie liegt im Branch `archiv-main`.

Vorgehen: `git checkout --orphan neu-main`, ein Commit, Push; dann `main` in `archiv-main` umbenennen, `neu-main` zum Standard-Branch machen und in `main` umbenennen. Der Wechsel des Standard-Branchs hat die Kontributoren-Anzeige sofort neu berechnet. GitHub zählt nur Commits auf dem Standard-Branch, `archiv-main` und `data` zählen nicht.

**Regeln:**

- `archiv-main` **nie** in `main` mergen und den Knopf «Compare & pull request» für `archiv-main` nie benutzen. Das brächte die alte Historie samt Bot-Commits zurück.
- Kein Workflow committet auf `main`. Automatische Commits gehören auf `data`.
- Commits auf `main` ohne KI-Signaturen (keine `Co-Authored-By`-Zeilen von Werkzeugen).
