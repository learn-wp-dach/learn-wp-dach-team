# Repository-Umzug: learn-wp-dach-team – Informationen für den Administrator

> **Archiv.** Dieses Dokument beschreibt den Zustand des Repositories vor dem Umzug und die damals geplanten Optionen. Der Umzug ist im September 2026 per Transfer in die Organisation `learn-wp-dach` erfolgt, siehe [Setup-Anleitung](setup.md). Alle Angaben unten (Adressen, Projektnummer, Workflows) sind historisch und werden nicht mehr gepflegt.

Erstellt: 2026-04-24

---

## 1. Beschreibung des Repositories

**Repository-Name:** `learn-wp-dach-team`  
**Aktueller Standort:** https://github.com/rfluethi/learn-wp-dach-team  
**Lizenz:** CC BY 4.0  
**Sichtbarkeit:** Öffentlich (lesbar ohne GitHub-Account)

Das Repository verwaltet die Sitzungsplanung, Beschlussprotokolle und Aufgaben des **Learn WP DACH Teams** vollständig über GitHub Issues und ein Kanban-Board. Das Team trifft sich monatlich (letzter Dienstag, 20:00 Uhr).

Das Kernprinzip: **Ein Issue = eine Sitzung.** Vor der Sitzung dient das Issue als Themenliste, nach der Sitzung als Beschlussprotokoll. Aufgaben aus Sitzungen werden als eigene Issues im Kanban-Board verwaltet.

### Inhalte des Repositories

| Bereich | Beschreibung |
| --- | --- |
| `README.md` | Einstiegsseite mit automatisch generiertem Protokoll-Index (via GitHub Actions) |
| `docs/` | Konzept, Benutzeranleitung und Setup-Anleitung (3 Markdown-Dateien) |
| `.github/ISSUE_TEMPLATE/` | 3 Issue-Vorlagen: `sitzung.yml`, `thema.yml`, `aufgabe.yml` |
| `.github/workflows/` | 3 GitHub Actions Workflows (siehe unten) |
| `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `LICENSE` | Standard Community-Dateien |

### Branches

- `main` (Hauptbranch)
- `data` (automatisch durch `sitzungen-json.yml` gepflegt, enthält `sitzungen.json` für das WordPress-Plugin)

### GitHub Actions Workflows

**1. `protokoll-index.yml` – Protokoll-Index aktualisieren**  
Wird ausgelöst, wenn ein Issue mit dem Label `sitzung` geschlossen wird (oder manuell). Der Workflow liest alle abgeschlossenen Sitzungs-Issues via GitHub API aus und generiert daraus automatisch den Protokoll-Index in der `README.md`. Er braucht Zugriff auf das GitHub-Projekt (ProjectV2), um den Board-Status der offenen Sitzungen zu ermitteln.

**2. `thema-board.yml` – Thema ins Board einordnen**  
Wird ausgelöst, wenn ein Issue mit dem Label `thema` erstellt oder gelabelt wird. Der Workflow fügt das Issue automatisch in die Spalte „Themen" des Kanban-Boards ein.

**3. `sitzungen-json.yml` – sitzungen.json auf dem `data`-Branch aktualisieren**  
Im Repo `learn-wp-dach-team` läuft die Action `sitzungen-json.yml` weiter und schreibt `sitzungen.json` auf den `data`-Branch. Sie wird vom neuen Plugin (Training Meeting Tracker) genauso konsumiert wie vom alten. Hier ist nichts zu ändern, sofern die Datenquelle gleich bleiben soll.

### Verknüpftes GitHub-Projekt (ProjectV2)

Das Kanban-Board **„Learn WP DACH – Aufgaben"** ist ein **benutzer-weites Projekt** (aktuell unter `users/rfluethi`, Projektnummer 11). Es ist nicht direkt an das Repository gebunden, sondern dem GitHub-Account des Admins zugeordnet. Das Board hat folgende Spalten:

> Themen → Offen → In Arbeit → Blockiert → Überprüfung → Erledigt

---

## 2. Was beim Umzug zu beachten ist

### 2.1 Git-Historie (Code, Commits, Branches)

Das Repository hat nur noch einen Branch (`main`). Der automatisch vom GitHub Copilot Coding Agent erstellte Branch `copilot/update-meeting-time-and-access` wurde bereits gelöscht.

Die Git-Historie kann vollständig und verlustfrei übertragen werden:

```bash
git clone --mirror https://github.com/rfluethi/learn-wp-dach-team.git
cd learn-wp-dach-team.git
git remote set-url origin https://github.com/NEUE-ORG/NEUES-REPO.git
git push --mirror
```

Damit werden alle Commits, Branches und Tags übertragen.

---

### 2.2 Issues – kritischer Punkt: Issue-Nummern

Issues lassen sich **nicht** per `git push` übertragen. Sie müssen separat migriert werden. Dabei gilt:

**Das zentrale Problem:** Beim Umzug bekommen alle Issues neue Nummern (z.B. aus `#5` wird `#1`). Das betrifft:

- **Issue-Bodies:** Sitzungs-Issues verweisen in ihrem Inhalt auf andere Issues (`#42`, `#43` als Diskussionsthemen; Aufgaben-Issues als `#23 @rfluethi`).
- **Issue-Kommentare:** Verlinkungen in Kommentaren zeigen auf alte Issue-Nummern.
- **`README.md`:** Der automatisch generierte Protokoll-Index enthält direkte Links auf einzelne Issues (z.B. `https://github.com/rfluethi/learn-wp-dach-team/issues/5`).
- **`sitzung.yml` Issue-Template:** Enthält Hardlinks auf das Aufgaben-Board (`https://github.com/users/rfluethi/projects/11`).

**Empfehlung für die Issue-Migration:**  
Das offizielle Tool ist der **GitHub Enterprise Importer** (GEI) bzw. für kleinere Repos das Tool `gh-gei`. Alternativ kann die [GitHub REST API](https://docs.github.com/en/rest/issues) genutzt werden, um Issues skriptbasiert zu migrieren und die Nummernzuordnung zu dokumentieren. Nach der Migration müssen alle Querverweise manuell oder skriptbasiert angepasst werden.

> **Wichtig:** Vor dem Umzug eine vollständige Liste aller Issues mit ihren Nummern exportieren (`gh issue list --limit 200 --json number,title,url`), um die Umschlüsselung nachvollziehen zu können.

---

### 2.3 GitHub-Projekt (Kanban-Board)

Das Projekt ist aktuell ein **benutzer-weites ProjectV2** unter `rfluethi`. Beim Umzug in eine Organisation muss das Projekt neu erstellt oder zu einem **org-weiten Projekt** migriert werden.

Folgendes muss im neuen Projekt übernommen werden:
- Spaltenstruktur: Themen, Offen, In Arbeit, Blockiert, Überprüfung, Erledigt
- Das Feld **„Estimate"** (Minuten, für Zeitplanung bei Themen-Issues)
- Alle bestehenden Issue-Verlinkungen im Board (abhängig von der Issue-Migration)

> GitHub bietet derzeit **kein automatisches Migrationstool für ProjectV2**. Das Board muss manuell neu aufgebaut werden. Bestehende Board-Einträge können über die GraphQL-API ausgelesen und im neuen Board neu verknüpft werden.

---

### 2.4 Labels

Die folgenden Labels müssen im neuen Repository angelegt werden (exakt gleiche Schreibweise, da Workflows und Issue-Templates darauf angewiesen sind):

| Label             | Verwendung                                                       |
| ----------------- | ---------------------------------------------------------------- |
| `sitzung`         | Meeting-Issues (löst Protokoll-Index-Workflow aus)               |
| `thema`           | Vorgeschlagene Diskussionsthemen (löst Board-Workflow aus)       |
| `aufgabe`         | Action Items / Tasks                                             |
| `blockiert`       | Aufgaben mit Blocker                                             |
| `überprüfung`     | Aufgabe erledigt – wartet auf Kontrolle durch eine zweite Person |
| `nächste-sitzung` | Vertagte Themen                                                  |
| `lerngruppe`      | Lerngruppen-Themen                                               |
| `webseite`        | Themen rund um learn-wp-dach.org                                 |
| `übersetzung`     | Übersetzungsprojekte                                             |
| `organisation`    | Organisatorische Aufgaben                                        |

---

### 2.5 GitHub Actions – Secrets und Anpassungen

Die beiden Workflows verwenden folgende Secrets und hartcodierten Werte, die nach dem Umzug aktualisiert werden müssen:

**Secret `GH_PAT`:**  
Ein Personal Access Token (PAT) mit den Scopes `repo` und `project`. Muss im neuen Repository unter *Settings → Secrets and variables → Actions* als `GH_PAT` gespeichert werden. Empfehlung: neuen PAT mit dem Account des neuen Admins erstellen.

**Hartcodierte Werte in den Workflows (müssen angepasst werden):**

| Datei | Wert | Muss ersetzt werden durch |
| --- | --- | --- |
| `protokoll-index.yml` | `user(login: "rfluethi")` | neuer GitHub-Username/Org |
| `protokoll-index.yml` | `projectV2(number: 11)` | neue Projektnummer |
| `protokoll-index.yml` | Link auf `https://github.com/users/rfluethi/projects/11` im README-Template | neuer Projekt-Link |
| `thema-board.yml` | `user(login: "rfluethi")` | neuer GitHub-Username/Org |
| `thema-board.yml` | `projectV2(number: 11)` | neue Projektnummer |

**Hartcodierte Werte in Issue-Templates (müssen angepasst werden):**

| Datei | Wert |
| --- | --- |
| `sitzung.yml` | Link auf `https://github.com/users/rfluethi/projects/11` |
| `thema.yml` | Link auf `https://github.com/users/rfluethi/projects/11` |

---

### 2.6 Workflow-Berechtigungen

Der Workflow `protokoll-index.yml` benötigt im neuen Repository explizit die Berechtigung, in den Code schreiben zu dürfen (`contents: write`). Diese ist im Workflow bereits deklariert, muss aber auch auf Repository-Ebene aktiviert sein:  
*Settings → Actions → General → Workflow permissions → „Read and write permissions"*

---

### 2.7 README.md – Links auf Issues

Die `README.md` enthält direkte Links auf Issue-Nummern (z.B. `https://github.com/rfluethi/learn-wp-dach-team/issues/5`). Nach der Migration werden diese Links auf das alte Repository zeigen. Da der Protokoll-Index automatisch durch den Workflow neu generiert wird (beim nächsten Schliessen eines Sitzungs-Issues oder per manuell ausgelöstem Workflow), aktualisieren sich die Links im README automatisch – sobald der Workflow einmal manuell gestartet wird.

---

## 3. Zusammenfassung: Checkliste für den Admin

- [ ] Neues Repository anlegen
- [ ] Git-Historie via `--mirror` übertragen (`main`)
- [ ] Labels anlegen (9 Labels, siehe Abschnitt 2.4)
- [ ] Issues exportieren (alte Nummernliste sichern), dann migrieren (z.B. via gh-gei oder API)
- [ ] Querverweise in Issues und Kommentaren nach der Migration auf neue Nummern aktualisieren
- [ ] Neues GitHub-Projekt (ProjectV2) erstellen mit identischer Spaltenstruktur (inkl. Spalte „Überprüfung") und Estimate-Feld
- [ ] Issues im neuen Board verknüpfen
- [ ] Neuen PAT erstellen (Scopes: `repo`, `project`) und als Secret `GH_PAT` hinterlegen
- [ ] Workflows anpassen: `rfluethi` und Projektnummer `11` durch neue Werte ersetzen
- [ ] Issue-Templates anpassen: Board-Links aktualisieren
- [ ] Workflow-Berechtigungen prüfen (`contents: write` unter Settings → Actions)
- [ ] Protokoll-Index-Workflow manuell auslösen, um README.md zu aktualisieren
- [ ] Alle Links in der Dokumentation (`docs/`, `SECURITY.md`) auf neue Repository-URL prüfen

