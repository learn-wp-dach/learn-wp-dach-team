# Review-Checkliste

Gehe diese Checkliste systematisch durch. Sie ist die einzige Review-Checkliste des Regelwerks; der [Erstellungs- und Pflegeprozess](../../../handbuch/Handbuch-Erstellung/erstellungs-und-pflegeprozess.md) verweist hierher. Bei jedem Punkt: prüfen, Befund festhalten, ggf. Korrekturvorschlag formulieren.

## Vorab-Check: Mischform?

* [ ] Die Seite hat **einen** klar erkennbaren Hauptzweck. Falls Mischform: in den Befund aufnehmen und auf Workflow W3 (Aufteilen) hinweisen.

## Inhalt

* [ ] Der **Seitentyp** ist klar erkennbar (Anleitung / Prozess / Tool-Übersicht / Rolle / Hintergrund / FAQ; Bereichs-Übersicht nur bei Startseiten).
* [ ] Die Information ist **fachlich korrekt** und **aktuell**.
* [ ] Jeder Absatz **unterstützt eine Handlung oder Entscheidung** der lesenden Person (82079-Prüffrage); reiner Ballast ist gestrichen oder ausgelagert.
* [ ] Die Information steht auf der **richtigen Dokumentenebene** (Konzept / Prozess / Anleitung; Nachweise gehören nicht ins Handbuch).
* [ ] Externe Tool-Inhalte sind **verlinkt, nicht kopiert**.
* [ ] Bei FAQ: Antworten kurz, **jede verlinkt auf die maßgebliche Seite**, keine neuen Fakten.

## Struktur

* [ ] **Titel** ist aussagekräftig und aufgabenorientiert.
* [ ] **Erste Überschrift im Inhalt ist H2**, keine H1 im Inhalt.
* [ ] **Kurzbeschreibung** beantwortet „Was?" und „Für wen?".
* [ ] **Regelsammlungen sind gegliedert:** eine Unterüberschrift pro Regel oder Prinzip, Titel getrennt vom Text; keine fettgedruckten Absatzanfänge als Ersatz für Überschriften.
* [ ] **Aufklappbereich-Titel folgen dem Muster „Kategorie: worum es geht"** (z.B. „Hintergrund: Wozu Labels dienen"); keine generischen Sammeltitel. Inhalte nur ergänzend, nichts Kritisches; nicht verschachtelt; höchstens zwei bis drei pro Seite.
* [ ] **Aufklappbereiche sind sauber formatiert:** Leerzeile nach `</summary>` und vor `</details>`, Inhalt in normalem Markdown (rendert auf GitHub und WordPress).
* [ ] **Tiefe vorhanden:** Hintergrund (Warum) und weiterführende, verifizierte externe Links sind zugeklappt bzw. unter „Offizielle Dokumentation"/„Verwandte Seiten" verfügbar; fehlen sie ganz, ist das ein Befund.
* [ ] **Screenshots geprüft:** Bei UI-Anleitungen ist pro Hauptschritt entschieden, ob ein Screenshot hilft; fehlende Bilder sind als Kommentar-Platzhalter mit Alt-Text markiert und in der Screenshot-Arbeitsliste erfasst.
* [ ] **Diagramm geprüft:** Abläufe, Übergaben und Zusammenhänge sind als Mermaid-Diagramm dargestellt, wo das die Beschreibung verdeutlicht und kürzt; keine ASCII-Diagramme; Ablaufdiagramme hochkant (`flowchart TD`).
* [ ] **Transport-Block** vorhanden (Markdown-Entwurf) bzw. **entfernt und in Felder übertragen** (WordPress-Fassung).
* [ ] **Eltern-Seite und Reihenfolge** sind bestimmt (Transport-Block bzw. Seiten-Attribute); daraus entsteht der Menüplatz.
* [ ] **Verantwortlichkeit** ist über eine **Rolle** zugewiesen, nicht über eine Person.
* [ ] **Zielgruppe** ist funktionsbasiert gesetzt (Alle Mitglieder / Inhalts-Ersteller:innen / Organisation/Koordination / Technik); „Alle Mitglieder" nur, wenn wirklich alle die Seite brauchen.

## Sprache

* [ ] Aktiv und Imperativ (wo zutreffend), Standardsatzmuster für Schritte.
* [ ] Sätze kurz und einfach (über 20 Wörter: teilen; keine Schachtelsätze, keine Semikolon-Reihungen); keine Füllwörter, keine doppelten Verneinungen.
* [ ] **Kein Fachbegriff vor seiner Erklärung** (S10): Jeder Begriff ist bei der ersten Nennung erklärt oder verlinkt; die Seite ist aus Sicht der lesenden Person geschrieben, nicht aus Sicht des Systems.
* [ ] **Keine internen Kürzel ohne Klartext** (S11): P-, S- und W-Kürzel stehen nie allein; zuerst der Inhalt in Worten.
* [ ] **Leseransicht vor Repo-Sicht** (S12): Fließtext und Diagramme nennen Seitentitel, keine Dateinamen.
* [ ] Begriffe konsistent (Seiten-Glossar ist die verbindliche Termliste).
* [ ] **Amtliche Rechtschreibung mit ß** (S9); keine Schweizer ss-Schreibung.
* [ ] Tool-Namen in Hersteller-Schreibweise.

## Auffindbarkeit

* [ ] Die Seite ist mit verwandten Seiten **verlinkt**.
* [ ] Fachbegriffe der Seite sind im **Seiten-Glossar** am Ende erklärt (vor dem Transport-Block).
* [ ] Linktexte beschreiben das Ziel, kein „hier klicken"; **Verweise auf Regelwerk und andere Seiten immer als Link, nie als Kapitel- oder Dateinennung ohne Link.**
* [ ] **Veränderliche Adressen** (z.B. Download-Links) stehen nur an einer Stelle; andere Seiten verlinken dorthin.
* [ ] **Textauszug ist wortgleich der erste Satz der Kurzbeschreibung** (Transport-Block bzw. Auszug-Feld).

## Befund-Format

> **Abschnitt:** [Name oder Position]
> **Befund:** [was beobachtet]
> **Vorschlag:** [konkrete Korrektur]
