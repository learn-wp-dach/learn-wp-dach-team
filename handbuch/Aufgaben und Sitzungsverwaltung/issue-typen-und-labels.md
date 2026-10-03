# Issue-Typen und Labels

## Kurzbeschreibung

Diese Seite listet die Issue-Typen und Labels, mit denen wir Sitzungen, Themen und Aufgaben im Repository kennzeichnen. Sie ist das Nachschlagewerk für alle Teammitglieder (Stand September 2026, vor der geplanten Label-Bereinigung).

<details>
<summary>Hintergrund: Wozu Labels dienen</summary>

Labels sind Schlagworte an GitHub-Issues; sie machen Issues filterbar und speisen die Ansichten des [Aufgaben-Boards](aufgaben-board.md). Die Typ-Labels setzen die Issue-Vorlagen automatisch, alle weiteren setzt du bei Bedarf von Hand. Grundlagen: [GitHub-Dokumentation zu Labels](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels).

</details>

## Issue-Typen

| Typ | Label | Zweck |
|---|---|---|
| Sitzung | `sitzung` | Themenliste und Beschlussprotokoll |
| Thema | `thema` | Diskussionsthema für die nächste Sitzung |
| Aufgabe | `aufgabe` | Action Item mit Verantwortlichen und Fälligkeit |

Die Issue-Vorlagen (Sitzung, Thema, Aufgabe) setzen das jeweilige Typ-Label automatisch. Nur bei einem leeren Issue (*Blank issue*) musst du das Typ-Label von Hand setzen; ohne Label greifen weder die Board-Automatisierung noch die Ansichten.

## Labels

### Typ-Labels (automatisch durch die Vorlagen)

| Label | Verwendung |
|---|---|
| `sitzung` | Sitzungs-Issues |
| `thema` | Vorgeschlagene Diskussionsthemen |
| `aufgabe` | Action Items |

### Bereichs-Labels (von Hand setzen)

| Label | Verwendung |
|---|---|
| `lerngruppe` | Themen rund um Lerngruppen |
| `webseite` | Themen rund um learn-wp-dach.org |
| `übersetzung` | Übersetzungsprojekte |
| `organisation` | Organisatorische Aufgaben |

### Prozess-Labels (von Hand setzen)

| Label | Verwendung |
|---|---|
| `beschluss` | Themen, die zu einem formellen Entscheid geführt haben |
| `nächste-sitzung` | Vertagte Themen |

<details>
<summary>Hinweis: Label-Bereinigung steht an</summary>

Der Label-Bestand ist historisch gewachsen und wird bereinigt. Im Repository existieren weitere Labels, die hier bewusst nicht als Konvention geführt werden: die GitHub-Standardlabels `bug`, `documentation`, `duplicate`, `enhancement`, `good first issue`, `help wanted`, `invalid`, `question` und `wontfix` (ohne definierte Verwendung bei uns) sowie `blockiert` (doppelt die gleichnamige Board-Spalte). Über die Bereinigung ist noch nicht entschieden; bis dahin gilt: Verwende die oben dokumentierten Labels, setze keine neuen ein.

</details>

## Verwandte Seiten

* [GitHub-basierte Sitzungsverwaltung](konzept.md) – warum wir mit Issues und Labels arbeiten
* [Sitzung durchführen](sitzung-durchfuehren.md) – wo die Labels im Ablauf gesetzt werden
* [Aufgaben-Board](aufgaben-board.md) – Ansichten, die auf diesen Labels aufbauen
* [Thema vorschlagen](thema-vorschlagen.md) und [Aufgabe erfassen](aufgabe-erfassen.md) – Anleitungen mit den Vorlagen

## Seiten-Glossar

| Begriff | Definition |
|---|---|
| Action Item | Eine aus einem Beschluss entstandene Aufgabe mit verantwortlicher Person und Fälligkeit, geführt als eigenes Issue. |

## Transport-Metadaten (beim Erfassen in Felder übertragen, dann diesen Block löschen)

* Seitentyp: Tool-Übersicht
* Verantwortliche Rolle: GitHub-Spezialist
* Thema: Organisation
* Zielgruppe: Alle Mitglieder
* Eltern-Seite: Aufgaben und Sitzungsverwaltung
* Reihenfolge: 50
* Textauszug: Diese Seite listet die Issue-Typen und Labels, mit denen wir Sitzungen, Themen und Aufgaben im Repository kennzeichnen.
* Letzte Aktualisierung: 2026-09-29
* Letzte Prüfung: 2026-07-28
* Prüfintervall: 90
