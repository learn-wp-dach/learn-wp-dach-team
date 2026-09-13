# Schreibregeln und Markdown-Konventionen

## Kurzbeschreibung

Diese Seite legt die verbindlichen Schreibregeln, Terminologie-Konventionen und Markdown-Konventionen für alle Handbuch-Seiten fest. Sie richtet sich an Autor:innen und Reviewer:innen.

## Wer nutzt es

Alle Personen, die Inhalte verfassen, formatieren oder reviewen. Beim Schreiben jeder Seite anwendbar.

## Sprache und Stil

Die folgenden Regeln sind eine vereinfachte Auswahl aus der [tekom-Leitlinie „Regelbasiertes Schreiben, Deutsch für die Technische Kommunikation"](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf) und dem internationalen Standard [IEC/IEEE 82079-1](https://de.wikipedia.org/wiki/IEC/IEEE_82079).

### S1: Aktiv statt passiv

* Richtig: „Klicke auf *Speichern*."
* Falsch: „Auf *Speichern* muss geklickt werden."

### S2: Kurze, einfache Sätze

Faustregel: ein Gedanke pro Satz. Sätze über 20 Wörter prüfen und meist teilen. Keine Schachtelsätze: höchstens ein Nebensatz oder Einschub pro Satz. Semikolon-Reihungen und Klammer-Einschübe sind Warnsignale; meist sind zwei Sätze klarer.

### S3: Imperativ in Anleitungen

Anleitungsschritte sind Befehle: „Öffne …", „Wähle …", „Speichere …". Standardsatzmuster für Schritte: Verb zuerst, ein Schritt, eine Handlung, sichtbares Ergebnis benennen.

### S4: Konkrete Wörter statt abstrakter

* Richtig: „das Formular"
* Falsch: „die entsprechende Eingabemaske"

### S5: Eine Bedeutung, ein Begriff

Verwende für dieselbe Sache immer dasselbe Wort. Nicht abwechselnd „Mitglied", „Person", „Teilnehmer:in", wenn dasselbe gemeint ist (siehe Abschnitt *Terminologie* weiter unten).

### S6: Anrede konsistent

In Anleitungen sprechen wir die lesende Person mit „du" (kleingeschrieben) an. Konventionen formulieren wir mit „wir". Regeln und Kriterien stehen unpersönlich. Diese Trennung halten wir über alle Seiten ein.

### S7: Keine Füllwörter

Streiche „eigentlich", „grundsätzlich", „im Prinzip", „natürlich".

### S8: Gendergerecht und lesbar

Wir verwenden den Doppelpunkt („Mitarbeiter:innen") oder geschlechtsneutrale Formulierungen („das Team", „die Mitglieder"). Konsistent über alle Seiten.

### S9: Rechtschreibung

Amtliche deutsche Rechtschreibung **mit ß** („regelmäßig", „heißt"). Die Schweizer Schreibweise (ss statt ß) wird im Handbuch nicht verwendet. Prüfe Entwürfe aktiv darauf; „grosse", „heisst" sind häufige Fehler aus Schweizer Tastaturen.

### S10: Begriffe vor Gebrauch einführen

Verwende keinen Fachbegriff, den die lesende Person nicht kennen kann. Führe jeden Begriff bei der ersten Nennung in einem kurzen Satz ein, oder verlinke die Seite, die ihn erklärt. Ein Begriff darf nie vor seiner Erklärung benutzt werden, auch nicht innerhalb derselben Seite. Schreibe aus der Sicht der lesenden Person, nicht aus der Sicht des Systems.

### S11: Keine internen Kürzel ohne Klartext

Kürzel wie P7, S2 oder W3 stehen nie allein. Nenne zuerst den Inhalt in Worten, das Kürzel höchstens in Klammern dahinter: „Rollen statt Personen (P7)". Schreibe Listen so, dass niemand zum Verstehen an eine andere Stelle scrollen muss.

### S12: Leseransicht vor Repo-Sicht

Schreibe für die Person, die die Seite in WordPress liest. Verwende in Fließtext und Diagrammen die Seitentitel, nicht die Dateinamen. Dateinamen gehören nur in technische Zusammenhänge, zum Beispiel als Linkziel oder in Tabellen über das Repository.

### Minimalismus-Prüffrage

Prüfe für jeden Absatz: **Unterstützt diese Information eine Handlung oder eine Entscheidung der lesenden Person?** Wenn nein: streichen, in einen Aufklappbereich verschieben oder auf eine Konzeptseite auslagern (übernommen aus [IEC/IEEE 82079-1](https://de.wikipedia.org/wiki/IEC/IEEE_82079)).

## Terminologie und Konsistenz

**Seiten-Glossar pflegen:** Begriffe, die eine Seite spezifisch verwendet (Tool-Begriffe, Rollenbezeichnungen, interne Abkürzungen), definiert die Seite selbst in ihrem Seiten-Glossar am Ende, vor dem Transport-Block. Es gibt bewusst **kein zentrales Begriffsregister**: Taucht derselbe Begriff auf mehreren Seiten auf, wird dieselbe Definition wortgleich wiederverwendet (die einzige erlaubte Ausnahme vom Prinzip der einen Quelle, P5).

**Schreibweisen festlegen:** Tool- und Eigennamen schreiben wir in der vom Hersteller verwendeten Schreibweise (z.B. „WordPress", nicht „Wordpress" oder „wordpress").

**Konsistenz vor Eleganz:** Wenn zwei Formulierungen gleich gut wären, gewinnt die, die wir bereits verwenden.

**Verweise immer als Link:** Nie „siehe Anleitung, Kapitel 3", Kapitelnummern oder bloße Dateinamen; immer den klickbaren Link auf die Zielseite setzen.

<details>
<summary>Weiterführend: Warum Terminologiekontrolle?</summary>

Inkonsistente Begriffe sind die häufigste Ursache für Missverständnisse in technischer Dokumentation. Die [tekom-Leitlinie](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf) empfiehlt explizit eine Terminologieliste als Grundlage konsistenter Texte.

</details>

## Umgang mit externen Tool-Dokumentationen

**Wir duplizieren keine Hersteller-Dokumentation** (Prinzip P2 aus den [Leitprinzipien](leitprinzipien.md)). Stattdessen:

| Wir dokumentieren | Wir verlinken |
|---|---|
| Wie **wir als Gruppe** das Tool einsetzen | Wie das Tool grundsätzlich funktioniert |
| Unsere **spezifischen Konfigurationen** und Konventionen | Hersteller-Tutorials und Referenzen |
| Unsere **Prozesse**, in denen das Tool vorkommt | Allgemeine Funktionsbeschreibungen |
| **Wann** wir welches Tool wofür nutzen | Versionshinweise des Herstellers |

**Praktisch heißt das:**
Eine „Tool-Übersicht"-Seite enthält:

1. Wofür wir das Tool nutzen (1 bis 3 Sätze).
2. Wer Zugang erhält und wie.
3. Unsere Konventionen (z.B. Namensschemata, Ordnerstruktur).
4. Verlinkung der offiziellen Dokumentation.
5. Verlinkung unserer eigenen Anleitungen, die dieses Tool betreffen.

**Vorteil:** Wenn der Hersteller seine Doku aktualisiert, profitieren wir automatisch. Wir pflegen nur die Stellen, die wir wirklich selbst kontrollieren.

## Markdown-Konventionen

### Dateiname = WordPress-Slug

Der Dateiname eines Entwurfs ist der spätere WordPress-Slug der Seite: Kleinbuchstaben, Bindestriche, keine Umlaute, keine Leerzeichen (z.B. `handbuch-seite-anlegen.md`). So ist jeder interne Link mechanisch in einen WordPress-Link übersetzbar. **Ausnahme:** Die Startseite eines Bereichs ist immer die `README.md`; ihr Slug ist der Bereichsname in Slug-Form und steht im Transport-Block in der Zusatzzeile `Slug:`.

### Überschriften

* Der Seitentitel steht im Entwurf als `#` (H1) zuoberst; der Markdown-Import übernimmt ihn als WordPress-Seitentitel.
* Im Inhalt darunter beginnt die Gliederung bei `##`; keine weitere H1 im Inhalt (doppelte H1 bricht Seitenstruktur, SEO und Barrierefreiheit).
* `##` für Hauptabschnitte, `###` für Unterabschnitte, maximal vier Ebenen.
* **Regel- und Prinzipiensammlungen sichtbar gliedern:** eine Unterüberschrift pro Regel oder Prinzip, der Titel getrennt vom Text, Beispiele als eigener Absatz. Keine Sammlungen aus fettgedruckten Absatzanfängen; sie machen die Seite zur Textwüste.

### Aufklappbereiche

Da wir das Handbuch in WordPress veröffentlichen, verwenden wir HTML innerhalb des Markdowns:

```html
<details>
<summary>Kategorie: worum es geht</summary>

Inhalt des Aufklappbereichs in normalem Markdown.

</details>
```

* **Titel nach dem Muster „Kategorie: worum es geht"** (z.B. „Hintergrund: Wozu Labels dienen", „Hinweis: Wartung der View-Links"). Die Kategorie ordnet ein, der Teil nach dem Doppelpunkt sagt konkret, worum es geht. Generische Sammeltitel wie „Für neue Mitglieder" sind ausgeschlossen. Ausnahme: FAQ-Seiten, dort ist der Titel die Frage.
* **Formatierung (Pflicht):** Nach `</summary>` und vor `</details>` je eine Leerzeile, sonst rendert GitHub den Markdown-Inhalt nicht. Inhalt in normalem Markdown, kein zusätzliches HTML im Block.
* Beim Übertrag nach WordPress wird jedes `<details>` ein **Details-Block**.

**So wirkt es:** Auf GitHub und im Handbuch erscheint zunächst nur die Titelzeile mit einem Dreieck; erst ein Klick zeigt den Inhalt. Fehlt eine der beiden Pflicht-Leerzeilen, zeigt GitHub den Inhalt als rohen Text (sichtbare Sternchen und Klammern statt Fettschrift und Links). Das ist der häufigste Formfehler bei Aufklappbereichen; die Leerzeilen sind darum nicht optional.

Wann und wie Aufklappbereiche eingesetzt werden, steht in [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md).

### Diagramme

* **Mermaid statt ASCII (Pflicht).** ASCII-Diagramme rendern auf den Handbuch-Seiten schlecht und sind verboten. Diagramme entstehen als Mermaid-Codeblock (```` ```mermaid ````); der Markdown-Import macht daraus einen gerenderten Mermaid-Block.
* **Ablaufdiagramme hochkant.** Flussdiagramme stehen standardmäßig vertikal (`flowchart TD`): Die Inhaltsspalte ist schmal, horizontale Diagramme werden unlesbar klein. Quer (`flowchart LR`) nur, wenn das Diagramm sonst unnötig hoch würde.
* **Aktiv einsetzen**, wo ein Diagramm die Beschreibung verdeutlicht und kürzt (Abläufe mit Übergaben, Zustandswechsel, Hierarchien). Das Diagramm ersetzt Text, es verdoppelt ihn nicht (P5).
* **Vektorgrafiken (SVG)** für Inhalte, die Mermaid nicht abbilden kann, im `assets`-Ordner des Bereichs ablegen und mit Alt-Text einbinden.

### Listen

* **Aufzählungen** mit `*` (Sternchen, einheitlich).
* **Nummerierte Listen** nur bei Schrittfolgen, in denen die Reihenfolge zwingend ist.
* Pro Listenpunkt ein Gedanke; sonst Fließtext oder Unterliste.

### Links

* **Interne Links** auf andere Handbuch-Seiten: relativer `.md`-Link auf die Zieldatei (funktioniert auf GitHub; beim Erfassen werden sie anhand der Slug-Konvention konvertiert).
* **Externe Links** (Hersteller-Dokus, Quellen) immer mit vollem URL; Linktext beschreibt das Ziel: richtig: „[Diátaxis-Framework](https://diataxis.fr/)"; falsch: „[hier klicken](https://...)".
* **Externe Links müssen verifiziert sein:** vor der Übergabe aufrufen und prüfen; bevorzugt offizielle, stabile Quellen. Wo immer möglich eine vertiefende externe Quelle anbieten.
* **Informieren, nicht verkaufen:** Keine Shop- oder Katalogseiten verlinken (z.B. Normen-Verkaufsportale). Stattdessen informierende Quellen: freie Spezifikationen, Wikipedia-Artikel, frei lesbare Norm-Auszüge.
* **Verweise immer als Link**, nie als Kapitelnummer oder bloßer Dateiname ohne Link.
* **Links auf Nur-Repo-Dateien** (z.B. die Skill-Dateien unter `skills/`) stehen als absolute GitHub-URL. Diese Dateien werden nicht als Seiten importiert; ein relativer `.md`-Link bliebe nach dem Import tot.
* **Veränderliche Adressen nur an einer Stelle.** Adressen, die von Hand gepflegt werden (z.B. Download-Links), stehen genau einmal im Handbuch. Alle anderen Stellen verlinken auf die Seite mit dieser Adresse; so muss bei einer Änderung nur ein Link angepasst werden.

### Screenshots

Bei Anleitungen mit Benutzeroberfläche prüfe pro Hauptschritt: Zeigt ein Screenshot, wo die lesende Person klicken oder hinschauen muss? Wenn ja, plane ihn ein. Bilder liegen im `assets`-Ordner des Bereichs und werden mit beschreibendem Alt-Text eingebunden. Liegt das Bild noch nicht vor, kommt an die Stelle ein HTML-Kommentar mit der fertigen Bildzeile (Ziel-Dateiname und Alt-Text), und die Datei wird in einer Screenshot-Arbeitsliste erfasst. So bleibt der Text schreibbar, und kein Bild geht vergessen.

### Anker für Sprungziele

Wir nutzen für stabile Sprungziele manuelle HTML-Anker (`<a name="anker-name"></a>`) direkt nach der jeweiligen Überschrift. Begründung: Automatische Markdown-Anker können sich bei Umformulierung der Überschrift ändern und Links brechen.

### Code und Befehle

* Inline-Code mit Backticks: `` `Befehl` ``.
* Codeblöcke mit Sprachangabe für Syntax-Highlighting.

### Hervorhebungen

* **Fett** (`**...**`) für wichtige Begriffe und UI-Elemente.
* *Kursiv* (`*...*`) für Eigennamen, Zitate, Bildschirmbeschriftungen.
* Sparsam einsetzen: Wenn alles hervorgehoben ist, ist nichts hervorgehoben.

### Tabellen

Tabellen verwenden, wenn Inhalte vergleichend oder mehrdimensional sind. Bei einfachen Aufzählungen lieber Listen verwenden.

### Transport-Block

Jeder Markdown-Entwurf endet mit dem **Transport-Block**: Er trägt Seitentyp, verantwortliche Rolle, Thema, Zielgruppe, Eltern-Seite, Reihenfolge, Textauszug und Aktualitäts-Daten. Beim Erfassen wird er in Felder übertragen und aus dem Inhalt gelöscht. Das exakte Muster steht in [markdown-konventionen.md](https://github.com/learn-wp-dach/learn-wp-dach-team/blob/main/skills/handbuch-autor/references/markdown-konventionen.md) des Skills.

<details>
<summary>Hinweis: Häufige Formfehler und wie du sie vermeidest</summary>

Diese Fehler tauchen bei uns am häufigsten auf; die zugehörige Regel steht jeweils oben auf dieser Seite.

* **„grosse", „heisst" mit ss statt ß.** Typisch für Schweizer Tastaturen. Amtlich ist „große", „heißt" (S9). Achtung: Nach kurzem Vokal ist ss richtig („muss", „dass"); ß steht nach langem Vokal oder Doppellaut.
* **Fehlende Leerzeile im Aufklappbereich.** Ohne Leerzeile nach `</summary>` oder vor `</details>` bleibt der Inhalt auf GitHub roher Text.
* **`.md` aus internen Links entfernt.** Das bricht die spätere Link-Konvertierung. Interne Links behalten im Entwurf ihr `.md`.
* **„hier klicken" als Linktext.** Der Linktext beschreibt das Ziel, z.B. „[Diátaxis-Framework]".
* **Verweis ohne Link** („siehe Anleitung, Kapitel 3"). Immer ein klickbarer Link, nie eine Kapitel- oder Dateinennung.
* **ASCII-Diagramm.** Verboten; als Mermaid-Block neu zeichnen.

</details>

## Verwandte Seiten

* [Regelwerk-Übersicht](README.md)
* [Leitprinzipien](leitprinzipien.md) – warum wir diese Regeln haben (P2, P5, P8)
* [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md) – wann und wie Aufklappbereiche eingesetzt werden

## Seiten-Glossar

| Begriff | Definition |
|---|---|
| Seiten-Glossar | Tabelle am Ende einer Seite (vor dem Transport-Block), die die Fachbegriffe dieser Seite verbindlich definiert. |
| Transport-Block | Block am Ende jedes Markdown-Entwurfs, der die Metadaten zur Erfassung transportiert; wird beim Import in WordPress-Felder übertragen und aus dem Inhalt gelöscht. |

## Transport-Metadaten (beim Erfassen in Felder übertragen, dann diesen Block löschen)

* Seitentyp: Hintergrund / Konzept
* Verantwortliche Rolle: GitHub-Spezialist
* Thema: Organisation
* Zielgruppe: Inhalts-Ersteller:innen
* Eltern-Seite: Handbuch-Erstellung
* Reihenfolge: 30
* Textauszug: Diese Seite legt die verbindlichen Schreibregeln, Terminologie-Konventionen und Markdown-Konventionen für alle Handbuch-Seiten fest.
* Letzte Aktualisierung: 2026-07-28
* Letzte Prüfung: 2026-05-03
* Prüfintervall: 365
