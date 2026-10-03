# Markdown-Konventionen

Markdown ist bei uns **Entwurfsformat**, WordPress (Block-Editor) ist die Single Source of Truth. Diese Konventionen sorgen dafür, dass ein Entwurf verlustfrei in den Block-Editor übertragen werden kann. Die für alle verbindliche Fassung steht im Regelwerk: [Schreibregeln und Markdown-Konventionen](../../../handbuch/Handbuch-Erstellung/schreibregeln-und-markdown.md).

## Dateiname = WordPress-Slug (Pflicht)

Der Dateiname eines Entwurfs ist der spätere **WordPress-Slug** der Seite: Kleinbuchstaben, Bindestriche, keine Umlaute, keine Leerzeichen (z.B. `handbuch-seite-anlegen.md` → Seite mit Slug `handbuch-seite-anlegen`). Dadurch ist jeder interne Link mechanisch und eindeutig in einen WordPress-Link übersetzbar; nichts muss interpretiert werden.

**Ausnahme, Startseite eines Handbuchs:** Die Hauptseite jedes Bereichs ist immer die `README.md` des Ordners (Startseiten-Regel in der [SKILL.md](../SKILL.md)). Ihr Slug ist nicht `readme`, sondern der Bereichsname in Slug-Form (z.B. `aufgaben-und-sitzungsverwaltung`); er steht im Transport-Block in der Zusatzzeile `Slug:`.

## Überschriften

* **Der Seitentitel steht im Entwurf als `#` (H1) zuoberst**; der Markdown-Import übernimmt ihn als WordPress-Seitentitel.
* **Im Inhalt darunter beginnt die Gliederung bei `##`** (H2); keine weitere H1 im Inhalt, eine doppelte H1 bricht Seitenstruktur und Barrierefreiheit.
* `##` für Hauptabschnitte, `###` für Unterabschnitte, maximal vier Ebenen.
* **Regel- und Prinzipiensammlungen gliedern:** eine Unterüberschrift pro Regel oder Prinzip, Titel getrennt vom Text, Beispiele als eigener Absatz; keine fettgedruckten Absatzanfänge als Ersatz für Überschriften.

## Aufklappbereiche

```html
<details>
<summary>Kategorie: worum es geht</summary>

Inhalt in normalem Markdown.

</details>
```

**Regeln:**

* Maximal eine Ebene, keine Verschachtelung.
* **Titel nach dem Muster „Kategorie: worum es geht"** (z.B. „Hintergrund: Wozu Labels dienen", „Hinweis: Wartung der View-Links", „Grundlagen: Board-Status vs. Issue-Status"). Die Kategorie ordnet ein, der Teil nach dem Doppelpunkt sagt konkret, worum es geht. Generische Sammeltitel wie „Für neue Mitglieder" oder „Mehr Infos" sind ausgeschlossen. Ausnahme: FAQ-Seiten, dort ist der Titel die Frage.
* **Formatierung für GitHub und WordPress (Pflicht):** Nach `</summary>` und vor `</details>` je eine Leerzeile, sonst rendert GitHub den Markdown-Inhalt nicht. Inhalt in normalem Markdown (Absätze, Listen, Links, Fett), kein zusätzliches HTML im Block.
* Keine kritischen Inhalte; der Pflichtweg funktioniert ohne Aufklappen.
* Sparsam: mehr als zwei bis drei pro Seite ist ein Aufteilungs-Signal.
* Beim Übertrag nach WordPress wird jedes `<details>` ein **Details-Block** (Kernblock ab WordPress 6.3).

## Listen, Links, Code, Hervorhebungen, Tabellen

* Aufzählungen mit `*`; nummerierte Listen nur bei zwingender Reihenfolge; pro Punkt ein Gedanke.
* **Interne Links in Entwürfen: relativer `.md`-Link auf die Zieldatei** (funktioniert auf GitHub). Beim Erfassen in WordPress werden sie anhand der Slug-Konvention auf die Zielseiten umgestellt (siehe `wordpress-erfassung.md`); ein `.md`-Link in einer veröffentlichten Seite ist immer ein Fehler.
* **Links auf Nur-Repo-Dateien** (Skill-Dateien, Vorlagen, Hintergrunddokumente) stehen als absolute GitHub-URL. Diese Dateien werden nicht als Seiten importiert; ein relativer `.md`-Link bliebe nach dem Import tot.
* **Verweise immer als Link:** Nie „siehe Anleitung, Kapitel 3" oder bloße Dateinamen schreiben; immer den klickbaren Link auf die Zielseite setzen.
* **Veränderliche Adressen nur an einer Stelle:** Von Hand gepflegte Adressen (z.B. Download-Links) stehen genau einmal im Handbuch; alle anderen Stellen verlinken auf die Seite mit der Adresse.
* Externe Links mit vollem URL; Linktext beschreibt das Ziel, kein „hier klicken".
* **Externe Links müssen verifiziert sein:** vor der Übergabe aufrufen und prüfen; bevorzugt offizielle, stabile Quellen. Wo immer möglich eine vertiefende externe Quelle anbieten.
* **Informieren, nicht verkaufen:** Keine Shop- oder Katalogseiten verlinken (z.B. Normen-Verkaufsportale). Stattdessen informierende Quellen: freie Spezifikationen, Wikipedia-Artikel, frei lesbare Norm-Auszüge (z.B. ISO Online Browsing Platform).
* Inline-Code mit Backticks, Codeblöcke mit Sprachangabe.
* **Fett** für wichtige Begriffe und UI-Elemente, *kursiv* für Eigennamen und Bildschirmbeschriftungen, beides sparsam.
* Tabellen nur bei vergleichendem oder mehrdimensionalem Inhalt.

## Diagramme

* **Mermaid statt ASCII (Pflicht).** ASCII-Diagramme rendern auf den Handbuch-Seiten schlecht und sind verboten. Diagramme entstehen als Mermaid-Codeblock (```` ```mermaid ````); der Markdown-Import wandelt ihn in einen Mermaid-Block um, der im Editor und Frontend gerendert wird.
* **Ablaufdiagramme hochkant:** Flussdiagramme standardmäßig vertikal (`flowchart TD`); die Inhaltsspalte ist schmal, horizontale Diagramme werden klein. `flowchart LR` nur, wenn das Diagramm sonst unnötig hoch würde.
* **Aktiv einsetzen:** Wo ein Diagramm die Beschreibung verdeutlicht und kürzt (Abläufe mit Übergaben, Zustandswechsel, Hierarchien, Seiten-Zusammenhänge), ersetzt es den langen Text (P5: ersetzen, nicht verdoppeln).
* **Vektorgrafiken (SVG):** Für Inhalte, die Mermaid nicht abbilden kann (Oberflächen-Skizzen, Icons, präzise Layouts), eine SVG-Datei im Ordner `_attachments` des Bereichs ablegen und mit Alt-Text einbinden.

## Screenshots

* **Bei UI-Anleitungen pro Hauptschritt prüfen**, ob ein Screenshot zeigt, wo geklickt oder hingeschaut werden muss; wenn ja, einplanen.
* **Ablage:** Bilder im Ordner `_attachments` des Bereichs, Dateinamen klein und ohne Umlaute, Einbindung mit beschreibendem Alt-Text.
* **Fehlende Bilder:** an der Zielstelle ein HTML-Kommentar mit der fertigen Bildzeile (`<!-- SCREENSHOT: ![Alt-Text](assets/datei.webp) -->`) und Eintrag in der Screenshot-Arbeitsliste; Screenshots liefert der Mensch, der Skill erfindet keine Bilder.

## Transport-Block am Ende des Entwurfs (Pflicht)

In WordPress leben Metadaten **ausschließlich in Feldern** (Meta-Box, Taxonomien, Seiten-Attribute, Textauszug); das Template zeigt sie automatisch an. Damit beim Entwurf nichts verloren geht, endet jeder Markdown-Entwurf mit einem klar markierten **Transport-Block**. Er wird bei der Erfassung in die Felder übertragen und **aus dem Inhalt gelöscht** (siehe `wordpress-erfassung.md`).

```markdown
---

## Transport-Metadaten (beim Erfassen in Felder übertragen, dann diesen Block löschen)

* Seitentyp: [Anleitung|Prozessbeschreibung|Tool-Übersicht|Rolle / Organisation|Hintergrund / Konzept|FAQ|Bereichs-Übersicht (nur Startseite)]
* Verantwortliche Rolle: [Rolle]
* Thema: [Begriff]
* Zielgruppe: [Alle Mitglieder|Inhalts-Ersteller:innen|Organisation/Koordination|Technik; Mehrfachnennung möglich]
* Eltern-Seite: [Titel oder „oberste Ebene"]
* Reihenfolge: [Zahl]
* Textauszug: [wortgleich der erste Satz der Kurzbeschreibung]
* Letzte Aktualisierung: [JJJJ-MM-TT]
* Letzte Prüfung: [JJJJ-MM-TT]
* Prüfintervall: [Tage; Startwerte: Tool 90, Anleitung/Prozess 180, sonst 365]
```

**Regeln:**

* Der Transport-Block ist **kein Seiteninhalt**. Er darf nie mitveröffentlicht werden.
* Unbekannte Werte bleiben Platzhalter; nichts raten (insbesondere Rolle, Eltern-Seite, Reihenfolge).
* **Textauszug = erster Satz der Kurzbeschreibung, wortgleich.** So gibt es keine zwei driftenden Zusammenfassungen; wer die Kurzbeschreibung ändert, zieht den Auszug nach.
* **Zielgruppe ist funktionsbasiert** (Entscheid 2026-07-05): Für wen ist die Seite? „Alle Mitglieder" nur, wenn wirklich alle die Seite brauchen; sonst die konkrete Gruppe. Der Lesemodus Onboarding/Nachschlagen ist **kein** Schlagwort; ihn lösen die zugeklappten Kontext-Aufklappbereiche.
* **Nur bei der Startseite (README.md):** Zusatzzeile `Slug: [bereichsname]` im Transport-Block, weil dort die Regel Dateiname = Slug nicht gilt; Seitentyp der Startseite ist „Bereichs-Übersicht".
* Ein **Seiten-Glossar** (falls vorhanden) steht **vor** dem Transport-Block und ist echter Seiteninhalt.
