# Handbuch-Erstellung

## Kurzbeschreibung

Dieser Bereich enthält das Regelwerk für unser Team-Handbuch: die Festlegungen, **wie** wir Inhalte erstellen, prüfen und pflegen. Er richtet sich an Teammitglieder, die als Autor:innen oder Reviewer:innen am Handbuch mitwirken.

## Geltungsbereich

Das Regelwerk gilt für alle Seiten des Handbuchs, unabhängig vom Thema (Tools, Prozesse, Organisation, Rollen).

**Format:** Entwürfe entstehen in Markdown im Repository und werden über den Markdown-Import in WordPress veröffentlicht; WordPress ist die Single Source of Truth der veröffentlichten Inhalte.

## So nutzt du dieses Regelwerk

Du musst nicht alles auf einmal lesen. Je nachdem, was du vorhast, gibt es einen kurzen Einstieg.

* **Du willst zum ersten Mal eine Seite schreiben.** Lies zuerst die [Leitprinzipien](leitprinzipien.md) (warum wir es so machen), dann [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md) (welchen Seitentyp du brauchst). Die Details zu Sprache und Format holst du dir beim Schreiben aus [Schreibregeln und Markdown-Konventionen](schreibregeln-und-markdown.md).
* **Du willst nur schnell nachschlagen**, wie eine bestimmte Regel lautet: direkt in [Schreibregeln und Markdown-Konventionen](schreibregeln-und-markdown.md).
* **Du lässt dich von KI unterstützen.** Der [Skill handbuch-autor](skill-handbuch-autor.md) kennt dieses Regelwerk und wendet es an; die Seite erklärt, wie du ihn herunterlädst und nutzt.
* **Du willst verstehen, woran das Regelwerk sich orientiert:** [Standards-Abgleich](standards-abgleich.md). Hintergrundwissen; einmal lesen genügt.

<details>
<summary>Grundlagen: Das Problem, das dieses Regelwerk löst</summary>

Ein Handbuch bedient zwei Gruppen mit gegensätzlichen Bedürfnissen: Neue wollen lernen und Kontext, Erfahrene wollen schnell nachschlagen. Schreibt man für beide getrennt, entstehen zwei Handbücher, die auseinanderdriften. Unsere Antwort ist **ein** Dokument, das den Pflichtweg kurz und sichtbar hält und die Tiefe in Aufklappbereichen versteckt. Die [Leitprinzipien](leitprinzipien.md) erklären diese Lösung im Detail.

</details>

## Abgrenzung zur Handbuch-Applikation

Das Regelwerk und die [Handbuch-Applikation](../Handbuch-Applikation/README.md) sind bewusst zwei getrennte Bereiche, mit dieser Grenzregel:

* **Ins Regelwerk** gehört alles, was unabhängig vom Werkzeug gilt: was eine gute Seite ist, Seitentypen, Sprache, Markdown-Konventionen, der Prozess bis zum fertigen Entwurf.
* **In die Handbuch-Applikation** gehört alles, was Bedienung von WordPress ist: Import, Felder setzen, Wartung, Menü-Verhalten.
* **Faustregel:** Würde der Satz auch bei einem anderen System stimmen, gehört er ins Regelwerk.

Begründung der Trennung: Die App-Dokumentation ändert sich mit jeder Version, das Regelwerk selten; getrennte Bereiche erlauben eigene Prüfintervalle, verantwortliche Rollen und Zugriffsgruppen. Berührungspunkte (z.B. der Transport-Block: Definition hier, Bedienung dort) werden verlinkt, nicht doppelt beschrieben. Die Trennung wird bei der Neuschreibung der Handbuch-Applikation überprüft.

## Seiten in diesem Bereich

| Datei | Seitentyp | Beschreibung |
|---|---|---|
| [leitprinzipien.md](leitprinzipien.md) | Hintergrund / Konzept | Zielgruppen und die neun Grundsätze unserer Handbuch-Arbeit. Orientierung, bevor du anfängst zu schreiben. |
| [inhaltstypen-und-vorlagen.md](inhaltstypen-und-vorlagen.md) | Hintergrund / Konzept | Sechs Seitentypen plus Bereichs-Übersicht, Seitenaufbau, Aufklappbereiche, Verweis auf die Vorlagen. |
| [schreibregeln-und-markdown.md](schreibregeln-und-markdown.md) | Hintergrund / Konzept | Sprachregeln, Terminologie und Seiten-Glossar, externe Dokus, Markdown-Konventionen inkl. Diagramme. Verbindlich. |
| [erstellungs-und-pflegeprozess.md](erstellungs-und-pflegeprozess.md) | Prozessbeschreibung | Schritte, Rollen, Pflege; Verweis auf die Review-Checkliste. |
| [skill-handbuch-autor.md](skill-handbuch-autor.md) | Tool-Übersicht | Der Skill handbuch-autor: Zweck, die fünf Workflows, Download und Einbindung in den KI-Assistenten. |
| [standards-abgleich.md](standards-abgleich.md) | Hintergrund / Konzept | Wo wir Normen folgen und wo wir bewusst abweichen. Hintergrundwissen. |

Ein zentrales Glossar gibt es bewusst nicht: Jede Seite definiert ihre Fachbegriffe im eigenen **Seiten-Glossar** (siehe [Schreibregeln und Markdown-Konventionen](schreibregeln-und-markdown.md)).

## Skill handbuch-autor

Der Skill `handbuch-autor` ist die maschinenlesbare Umsetzung dieses Regelwerks: Ein KI-Assistent lädt ihn und schreibt, überarbeitet, teilt, prüft oder erfasst dann Handbuch-Seiten regelkonform. Menschen lesen die Regelwerk-Seiten, die KI liest den Skill; bei Widersprüchen gilt das Regelwerk.

* **Was er kann, wie er aufgebaut ist, Download und Einbindung:** [skill-handbuch-autor.md](skill-handbuch-autor.md).
* **Quelldateien:** im Repository unter [skills/handbuch-autor/](https://github.com/learn-wp-dach/learn-wp-dach-team/tree/main/skills/handbuch-autor/). Sie liegen bewusst außerhalb des Handbuch-Ordners, damit der Handbuch-Import sie nicht miterfasst.

## Wie die Seiten zusammenhängen

```mermaid
flowchart TD
    R["Handbuch-Erstellung (Startseite)"] --> L["Leitprinzipien des Handbuchs"]
    R --> I["Inhaltstypen und Vorlagen"]
    R --> S["Schreibregeln und<br>Markdown-Konventionen"]
    R --> E["Erstellungs- und Pflegeprozess"]
    R --> K["Skill handbuch-autor"]
    R --> ST["Standards-Abgleich"]
    I -- "verweist auf die Vorlagen" --> A["Skill-Dateien im Repository"]
    E -- "verweist auf die Review-Checkliste" --> A
    K -- "erklärt und verlinkt" --> A
```

## Verbindlichkeit

* Die Regeln in [Schreibregeln und Markdown-Konventionen](schreibregeln-und-markdown.md) sind **verbindlich**.
* Die [Leitprinzipien](leitprinzipien.md) und Strukturvorgaben aus [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md) gelten als Standardweg. Abweichungen begründen wir im Review.

## Verwendete Quellen und Standards

### Frameworks und Methoden

* [Diátaxis-Framework](https://diataxis.fr/) — Daniele Procida. Strukturansatz für Dokumentation (vier Inhaltstypen).
* [Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/) — Jakob Nielsen / Nielsen Norman Group. Prinzip zum Umgang mit komplexen Inhalten.

### Internationale Standards

* [ISO/IEC/IEEE 26514:2022](https://www.iso.org/obp/ui/#!iso:std:77451:en) — *Systems and software engineering, Design and development of information for users.* Anforderungen an Struktur, Inhalt und Format von Nutzerdokumentation.
* [ISO/IEC/IEEE 26515:2018](https://www.iso.org/obp/ui/#!iso:std:70880:en) — *Developing information for users in an agile environment.* Prozesse für agile Dokumentationsentwicklung.
* [IEC/IEEE 82079-1](https://de.wikipedia.org/wiki/IEC/IEEE_82079) — *Preparation of information for use (instructions for use) of products, General principles and detailed requirements.*

Die Links führen zu informierenden Quellen (Wikipedia, frei lesbare Norm-Auszüge), nicht zu Verkaufsseiten.

### Deutsche Quellen

* [tekom-Leitlinie „Regelbasiertes Schreiben, Deutsch für die Technische Kommunikation"](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf) — Leseprobe (PDF). Standard für deutschsprachige technische Texte.

### Praxisbeispiele zur Inspiration

* [Cloudflare Developer Docs](https://developers.cloudflare.com/) — setzt Diátaxis konsequent um.
* [GitLab Pajamas Design System, Progressive Disclosure](https://design.gitlab.com/patterns/progressive-disclosure/)

---

## Transport-Metadaten (beim Erfassen in Felder übertragen, dann diesen Block löschen)

* Seitentyp: Bereichs-Übersicht
* Slug: handbuch-erstellung
* Verantwortliche Rolle: GitHub-Spezialist
* Thema: Organisation
* Zielgruppe: Inhalts-Ersteller:innen
* Eltern-Seite: oberste Ebene
* Reihenfolge: 30
* Textauszug: Dieser Bereich enthält das Regelwerk für unser Team-Handbuch: die Festlegungen, wie wir Inhalte erstellen, prüfen und pflegen.
* Letzte Aktualisierung: 2026-07-28
* Letzte Prüfung: 2026-05-03
* Prüfintervall: 365
