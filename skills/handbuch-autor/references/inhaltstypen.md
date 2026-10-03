# Inhaltstypen bestimmen

Bevor eine Seite geschrieben wird, muss der Seitentyp feststehen. Das ist die wichtigste Strukturentscheidung; sie bestimmt Aufbau, Tonalität und Vorlage.

## Die sechs Seitentypen

| Seitentyp | Diátaxis-Typ | Zweck | Beispieltitel |
|---|---|---|---|
| **Anleitung** | How-to-Guide | Eine konkrete Aufgabe Schritt für Schritt erledigen | „So legst du eine neue Mitgliederliste an" |
| **Prozessbeschreibung** | How-to-Guide | Wiederkehrenden Ablauf mit mehreren Beteiligten dokumentieren | „Aufnahme eines neuen Mitglieds" |
| **Tool-Übersicht** | Reference | Was wir nutzen, wofür, mit Verweis auf die Hersteller-Doku | „Übersicht: WordPress" |
| **Rollen-/Organisationsbeschreibung** | Reference / Explanation | Struktur der Gruppe, Verantwortlichkeiten | „Rollen im Team" |
| **Hintergrund/Konzept** | Explanation | Warum-Fragen, Zusammenhänge, Designentscheidungen | „Warum wir Markdown verwenden" |
| **FAQ** | Einstiegshilfe (kein eigener Diátaxis-Typ) | Wiederkehrende Fragen bündeln und zur maßgeblichen Seite führen | „Häufige Fragen zur Sitzungsverwaltung" |

**Sonderregeln für FAQ (wahren die Single Source of Truth):**

* Jede Antwort ist **kurz** (ein bis drei Sätze) und **verlinkt auf die maßgebliche Seite**, auf der die Information lebt.
* Eine FAQ-Seite führt **keine neuen Fakten** ein. Fehlt die maßgebliche Seite, wird sie zuerst erstellt (oder die Information dort ergänzt).
* Häufen sich Fragen zum selben Thema, ist das ein Signal, die betroffene Seite zu verbessern (P9), nicht die FAQ auszubauen.

## Trennkriterium Anleitung vs. Prozessbeschreibung

Eine **Anleitung** beschreibt, wie eine Person eine Aufgabe selbst erledigt (du-Perspektive). Eine **Prozessbeschreibung** beschreibt, wie mehrere Rollen einander Arbeit übergeben (wer-macht-was, mit Auslöser und Übergaben). **Faustregel: Kommt im Ablauf mehr als eine Rolle vor, ist es eine Prozessbeschreibung.**

## Entscheidungsfragen

Beantworte diese Fragen in dieser Reihenfolge:

**Frage 1: Was tut die lesende Person mit dieser Seite?**

* Eine Aufgabe **erledigen**? → Anleitung oder Prozessbeschreibung (Faustregel oben)
* Etwas **nachschlagen**? → Tool-Übersicht oder Rollenbeschreibung
* Etwas **verstehen**? → Hintergrund/Konzept
* Eine **schnelle Antwort mit Wegweiser** finden? → FAQ (nur wenn die maßgeblichen Seiten existieren)

**Frage 2: Wenn „nachschlagen", was ist das Subjekt?**

* Ein **Tool** → Tool-Übersicht
* Eine **Rolle** oder **Organisationseinheit** → Rollenbeschreibung

## Einordnungsfrage nach Dokumentenebene (aus ISO 10013 übernommen)

Prüfe zusätzlich, auf welcher Ebene die Information hingehört:

| Ebene | Bei uns | Beispiel |
|---|---|---|
| Grundsatz / Politik | Hintergrund/Konzept | „Warum wir GitHub für Aufgaben nutzen" |
| Prozess | Prozessbeschreibung | „Sitzung durchführen" |
| Arbeitsanweisung | Anleitung | „Aufgabe erfassen" |
| Nachweis | **kein Handbuch-Inhalt**; entsteht im Tool | Sitzungsprotokolle, erledigte Issues |

Nachweise (Protokolle, erledigte Aufgaben) gehören nicht ins Handbuch; das Handbuch verlinkt höchstens den Ort, wo sie liegen.

## Wenn der Seitentyp unklar ist

Stelle dem Menschen folgende Frage:

> „Was soll die lesende Person mit dieser Seite tun: eine Aufgabe erledigen, etwas nachschlagen, oder etwas verstehen?"

## Wenn mehrere Seitentypen passen

Das ist ein Hinweis auf eine **Mischform**. Lade `aufteilen.md` und folge Workflow W3.
