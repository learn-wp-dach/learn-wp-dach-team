# Erstellungs- und Pflegeprozess

## Kurzbeschreibung

Diese Seite beschreibt, wie eine Handbuch-Seite vom Bedarf bis zur Veröffentlichung entsteht und wie sie danach gepflegt wird. Sie richtet sich an Autor:innen, Reviewer:innen und inhaltsverantwortliche Rollen.

## Auslöser

* Eine neue Handbuch-Seite ist nötig (Bedarf erkannt, neue Aufgabe, neues Tool).
* Eine bestehende Seite muss aktualisiert werden (Prozessänderung, Tool-Wechsel, Fehler).
* Eine Seite ist zur regelmäßigen Prüfung fällig.

## Beteiligte Rollen

| Rolle | Aufgabe |
|---|---|
| **Autor:in** | Schreibt den Entwurf, pflegt die Seite. |
| **Reviewer:in** | Prüft fachlich und gemäß Schreibregeln. |
| **Inhaltsverantwortliche Rolle** | Erteilt Freigabe zur Veröffentlichung; ist langfristig für die Korrektheit der Seite zuständig. Welche Rolle dies konkret ist, hängt vom Inhaltsbereich ab (z.B. Technik, Organisation, Mitgliederwesen). |

Wir ordnen Verantwortlichkeiten über Rollen zu, nicht über Personen (Prinzip P7 aus den [Leitprinzipien](leitprinzipien.md)). Welche Person aktuell welche Rolle innehat, pflegen wir zentral an einer Stelle.

## Ablauf

### Erstellung einer neuen Seite

Der Erstellungsprozess folgt einem schlanken, an [ISO/IEC/IEEE 26515:2018](https://www.iso.org/obp/ui/#!iso:std:70880:en) angelehnten Vorgehen für agile Dokumentationsentwicklung. Der [Skill handbuch-autor](skill-handbuch-autor.md) unterstützt alle Schritte mit KI: vom ersten Entwurf über Überarbeiten und Aufteilen bis zu Review und Erfassung.

```mermaid
flowchart TD
    B["Bedarf klären"] --> S["Seitentyp bestimmen,<br>Vorlage wählen"]
    S --> E["Entwurf schreiben<br>(mit Transport-Block)"]
    E --> C["Selbst-Check mit<br>Review-Checkliste"]
    C --> R["Peer-Review"]
    R --> F["Freigabe durch die<br>verantwortliche Rolle"]
    F --> I["Markdown-Import<br>in WordPress"]
    I --> V["Veröffentlichen,<br>Links konvertieren"]
```

1. **Bedarf klären.** Welche Frage soll die Seite beantworten? Für wen?
2. **Seitentyp festlegen** nach [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md). Bei Mischform: aufteilen.
3. **Vorlage wählen** (verlinkt in [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md)).
4. **Entwurf schreiben** nach den [Schreibregeln und Markdown-Konventionen](schreibregeln-und-markdown.md), inklusive Transport-Block am Ende.
5. **Selbst-Check** mit der [Review-Checkliste](https://github.com/learn-wp-dach/learn-wp-dach-team/blob/main/skills/handbuch-autor/references/review-checkliste.md).
6. **Peer-Review** durch mindestens eine weitere Person, die das Thema fachlich kennt.
7. **Freigabe** durch die inhaltsverantwortliche Rolle.
8. **Erfassung in WordPress** über den Markdown-Import; der Transport-Block wird dabei zu Feldern.
9. **Veröffentlichen** und nach der letzten Seite eines Bereichs die `.md`-Links konvertieren.

<details>
<summary>Beispiel: Eine Seite von der Idee bis zur Veröffentlichung</summary>

So sehen die neun Schritte an einem echten Fall aus. In drei Sitzungen fragten neue Mitglieder, wie man ein Thema einreicht (**Bedarf**). Weil nur eine Person eine Aufgabe erledigt, ist es eine **Anleitung**, keine Prozessbeschreibung (**Seitentyp**), also greift `vorlage-anleitung.md` (**Vorlage**). Die Autor:in schreibt die Datei `ein-thema-vorschlagen.md` (**Entwurf**): drei Schritte offen sichtbar, der Aufklappbereich „Grundlagen: Was ein Thema-Issue ist" für Neue. Dazu kommt der Transport-Block mit der verantwortlichen Rolle *Community-Koordination* und der Eltern-Seite *Aufgaben und Sitzungsverwaltung*.

Der **Selbst-Check** mit der Review-Checkliste fällt auf: der Textauszug fehlt, er wird als erster Satz der Kurzbeschreibung nachgetragen. Im **Peer-Review** merkt eine Kollegin an, dass Schritt 2 zwei Klicks in einem Punkt bündelt; sie werden in zwei Schritte getrennt (ein Schritt, eine Handlung). Die *Community-Koordination* erteilt die **Freigabe**. Beim **Import** wird der Transport-Block zu Feldern, die `<details>` werden zu Details-Blöcken. Nach dem **Veröffentlichen** steht die Seite im Menü; nach der letzten Seite des Bereichs konvertiert der Dashboard-Knopf die `.md`-Links. Gesamtaufwand: rund eine halbe Stunde, weil die Vorlage die Struktur vorgibt und der Skill die Regeln durchsetzt.

</details>

<details>
<summary>Leitsatz: Warum Pflege entscheidend ist</summary>

Dokumentation ohne Pflege wird falsch. Falsche Dokumentation ist schlechter als keine.

</details>

### Pflege bestehender Seiten

#### Verteilte Verantwortung

Es gibt **keine einzelne Rolle, die für das gesamte Handbuch verantwortlich ist**. Wir verteilen die Verantwortung nach Inhaltsbereichen: Jede Seite hat eine inhaltsverantwortliche Rolle, die in den Metadaten-Feldern der Seite hinterlegt ist. Diese Rolle pflegt die Seite.

#### Regelmäßige Prüfung

Jede Seite wird **regelmäßig** durch die zuständige Rolle auf Aktualität geprüft. Was „regelmäßig" konkret bedeutet, ergibt sich aus dem Inhaltsbereich:

* Seiten zu **schnell veränderlichen Themen** (z.B. genutzte Tools, externe Dienste) prüfen wir häufiger.
* Seiten zu **stabilen Themen** (z.B. Grundsätze, Organisationsstruktur) prüfen wir seltener.

Das Datum der letzten Prüfung steht in der Fußzeile jeder Seite. So kann jede:r erkennen, wie aktuell eine Information ist, auch wenn keine inhaltliche Änderung nötig war.

#### Anlassbezogene Aktualisierung

Eine Seite wird **sofort** aktualisiert, wenn:

* sich ein Prozess ändert,
* ein Tool gewechselt oder eingestellt wird,
* ein Fehler in der Dokumentation gefunden wird,
* mehrere Personen die gleiche Frage stellen, weil das Handbuch sie nicht beantwortet.

Wer einen Fehler oder eine veraltete Information bemerkt, meldet das der inhaltsverantwortlichen Rolle der betroffenen Seite oder behebt es selbst (mit anschließendem Review).

#### Versionierung

Da wir das Handbuch in WordPress veröffentlichen, nutzen wir die WordPress-Revisionen als technische Versionierung. Inhaltlich wichtige Änderungen halten wir in einem **Änderungsprotokoll** auf der jeweiligen Seite (am Ende, im Aufklappbereich) fest, jedoch nur, wenn die Änderung für Lesende relevant ist (z.B. geänderter Ablauf), nicht für reine Tippfehler.

## Review-Checkliste

Die verbindliche Checkliste liegt als einzige Quelle beim Skill: [review-checkliste.md](https://github.com/learn-wp-dach/learn-wp-dach-team/blob/main/skills/handbuch-autor/references/review-checkliste.md) . So gibt es nur eine Fassung, die nicht driften kann. Sie deckt Mischform-Check, Inhalt, Struktur, Sprache und Auffindbarkeit ab und ist die Grundlage von Selbst-Check und Peer-Review.

## Ergebnis

Eine Handbuch-Seite, die freigegeben, veröffentlicht und gepflegt ist. Korrektheit, Aktualität und Verständlichkeit sind durch Selbst-Check, Peer-Review und Freigabe abgesichert.

## Verwandte Seiten

* [Regelwerk-Übersicht](README.md)
* [Leitprinzipien](leitprinzipien.md) – Prinzipien P6, P7 und P9 prägen den Pflegeprozess
* [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md) – Schritt 2 und 3 des Erstellungsprozesses
* [Schreibregeln und Markdown-Konventionen](schreibregeln-und-markdown.md) – Schritt 4 des Erstellungsprozesses
* [Skill handbuch-autor](skill-handbuch-autor.md) – KI-Unterstützung für alle Schritte des Prozesses

## Seiten-Glossar

| Begriff | Definition |
|---|---|
| Rolle | Funktionsbezeichnung im Team, der Verantwortlichkeiten zugeordnet sind (nicht eine konkrete Person). |
| Inhaltsverantwortliche Rolle | Die Rolle, die für die Korrektheit und Pflege einer bestimmten Seite zuständig ist. Wird in den Metadaten-Feldern jeder Seite genannt. |

## Transport-Metadaten (beim Erfassen in Felder übertragen, dann diesen Block löschen)

* Seitentyp: Prozessbeschreibung
* Verantwortliche Rolle: GitHub-Spezialist
* Thema: Organisation
* Zielgruppe: Inhalts-Ersteller:innen
* Eltern-Seite: Handbuch-Erstellung
* Reihenfolge: 40
* Textauszug: Diese Seite beschreibt, wie eine Handbuch-Seite vom Bedarf bis zur Veröffentlichung entsteht und wie sie danach gepflegt wird.
* Letzte Aktualisierung: 2026-07-28
* Letzte Prüfung: 2026-05-03
* Prüfintervall: 180
