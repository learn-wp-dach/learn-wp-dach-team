---
name: handbuch-autor
description: >-
  Erstellt, prüft, überarbeitet und teilt Inhalte für unser Team-Handbuch auf
  und bereitet sie für die Erfassung in WordPress vor. Setze diesen Skill IMMER
  ein, wenn der Mensch eine Handbuch-Seite schreiben, überarbeiten, prüfen,
  strukturieren, aufteilen oder in WordPress erfassen will, oder wenn von
  "Anleitung", "How-to", "Prozessbeschreibung", "Tool-Übersicht",
  "Rollenbeschreibung", "FAQ" oder "Hintergrundseite" für das interne Handbuch
  die Rede ist. Nutze ihn auch, wenn der Mensch nur sagt "ich muss noch was
  fürs Handbuch schreiben", "kannst du das fürs Wiki dokumentieren" oder "diese
  Seite ist ein Mischmasch, kannst du sie aufräumen", ohne den Seitentyp
  explizit zu nennen. Der Skill stellt sicher, dass jede Seite dem Regelwerk
  Handbuch-Erstellung folgt: ein Hauptzweck pro Seite (Diátaxis), Progressive
  Disclosure mit beschreibend betitelten Aufklappbereichen und verifizierten
  weiterführenden Links, Verlinkung statt Duplizierung, Verantwortung über
  Rollen, Metadaten als Transport-Block (in WordPress als Felder), amtliche
  deutsche Rechtschreibung mit ß und konsistente Markdown-Struktur für GitHub
  und WordPress.
---

# Skill: handbuch-autor

Dieser Skill unterstützt beim Erstellen, Prüfen, Überarbeiten, **Aufteilen** und **Erfassen** von Seiten für unser Team-Handbuch. Er setzt das [Regelwerk Handbuch-Erstellung](../../handbuch/Handbuch-Erstellung/README.md) um. Bei Widersprüchen gilt das Regelwerk.

## Wann triggern

Setze diesen Skill ein, sobald jemand:

* eine **neue Seite** für das Handbuch schreiben will,
* eine **bestehende Seite überarbeiten** möchte,
* eine Seite **reviewen** oder gegen die Qualitätskriterien prüfen will,
* einen **bestehenden, gemischten Inhalt aufteilen** will (z.B. eine alte Wiki-Seite, die mehrere Themen vermischt),
* eine fertige Seite **in WordPress erfassen** will,
* unsicher ist, ob ein Inhalt überhaupt ins Handbuch gehört oder wie er strukturiert werden soll,
* allgemein über „Doku", „Anleitung", „Prozess dokumentieren", „Wiki-Eintrag", „aufräumen" oder „fürs Handbuch" spricht.

## Grundsätze, die dieser Skill konsequent umsetzt

Diese Grundsätze stammen aus den [Leitprinzipien](../../handbuch/Handbuch-Erstellung/leitprinzipien.md) des Regelwerks. Halte dich an sie auch dann, wenn der Mensch sie nicht nennt.

* **P1, ein Hauptzweck pro Seite** ([Diátaxis-Framework](https://diataxis.fr/)). Eine Seite ist Anleitung **oder** Erklärung **oder** Nachschlagewerk, nicht alles gleichzeitig.
* **P2, nicht duplizieren, verlinken.** Hersteller-Dokumentationen werden verlinkt, nie kopiert.
* **P3, Progressive Disclosure.** Pflichtinformationen sichtbar; Hintergrund und Kontext in Aufklappbereichen. Titel folgen dem Muster **„Kategorie: worum es geht"** (z.B. „Hintergrund: Wozu Labels dienen", „Grundlagen: Board-Status vs. Issue-Status"); generische Sammeltitel wie „Für neue Mitglieder" oder „Mehr Infos" sind ausgeschlossen.
* **P4, Aktion vor Theorie.** Bei Anleitungen kommt zuerst, was zu tun ist.
* **Keine internen Kürzel ohne Klartext.** P-, S- und W-Kürzel nie allein verwenden; zuerst der Inhalt in Worten, das Kürzel höchstens in Klammern („Rollen statt Personen (P7)").
* **Leseransicht vor Repo-Sicht.** In Fließtext und Diagrammen Seitentitel verwenden, keine Dateinamen; Dateinamen nur in technischen Zusammenhängen.
* **P5, Single Source of Truth.** Jede Information existiert genau einmal; andere Stellen verlinken. Einzige Ausnahme: wortgleiche Glossar-Definitionen auf mehreren Seiten.
* **P6, Aktualität sichtbar machen.** Verantwortliche Rolle, letzte Aktualisierung und letzte Prüfung werden in WordPress **als Felder** gepflegt und vom Template angezeigt. In Markdown-Entwürfen reisen sie im Transport-Block mit (siehe `references/markdown-konventionen.md`).
* **P7, Rollen statt Personen.** Verantwortlichkeit über Rollen; Urheberschaft (wer schrieb, wer prüfte) ist davon getrennt und personengebunden.
* **P8, Nutzerperspektive vor Tool-Logik.** Anleitungen sind nach Aufgaben strukturiert, nicht nach Tool-Menüs.
* **P9, Handbook-first-Kultur.** Ändert sich ein Prozess oder Tool, wird die betroffene Seite im selben Arbeitsgang aktualisiert.

## Startseite eines Handbuchs: immer die README

Jedes Handbuch (Bereichsordner im Repo) hat genau eine Haupt- und Einstiegsseite: die `README.md` des Ordners.

* **Doppelrolle:** Auf GitHub dient die README als Ordner-Übersicht; in WordPress wird dieselbe Datei als Startseite des Bereichs erfasst.
* **Aufbau:** Kurzbeschreibung des Bereichs, Tabelle aller Seiten (Datei, Seitentyp, Beschreibung), optional Verlinkungs-Skizze und „Wie die Seiten zusammenhängen".
* **Hierarchie:** Die Startseite steht auf der obersten Ebene. Alle übrigen Seiten des Bereichs tragen die Startseite als Eltern-Seite, sofern der Mensch nichts anderes bestimmt; die Reihenfolge folgt der Seitentabelle der README.
* **Slug-Ausnahme:** `readme` taugt nicht als Slug, weil jeder Bereich denselben hätte. Die Startseite erhält den Bereichsnamen in Slug-Form (z.B. `aufgaben-und-sitzungsverwaltung`); er steht im Transport-Block in der Zusatzzeile `Slug:`. Alle übrigen Seiten folgen unverändert der Regel Dateiname = Slug (`references/markdown-konventionen.md`).
* **Seitentyp:** Die Startseite trägt den Seitentyp **Bereichs-Übersicht** (Diátaxis: Reference). Er ergänzt die sechs Seitentypen, gilt nur für Startseiten und muss im Datenmodell (Seitentyp-Schlagworte) vorhanden sein.
* **W1 und W5:** Beim Anlegen eines neuen Bereichs entsteht die README zuerst; beim Erfassen wird sie zuerst importiert, damit die übrigen Seiten ihre Eltern-Seite finden.

## Diagramme: Mermaid statt ASCII

Prüfe bei jedem Entwurf und jeder Überarbeitung, ob ein Diagramm die Beschreibung **verdeutlicht und kürzt**: Abläufe mit mehreren Rollen oder Übergaben, Zustandswechsel, Hierarchien, Zusammenhänge zwischen Seiten, Entscheidungswege. Wenn ja, erstelle es aktiv, statt lange Textabschnitte zu schreiben.

* **Format:** Mermaid-Codeblock (```` ```mermaid ````). Der Markdown-Import wandelt ihn in einen Mermaid-Block um, der im Editor und Frontend gerendert wird.
* **ASCII-Diagramme sind verboten.** Sie rendern auf den Handbuch-Seiten schlecht. Bestehende ASCII-Diagramme werden bei jeder Überarbeitung (W2) in Mermaid umgewandelt.
* **Ablaufdiagramme hochkant:** Flussdiagramme standardmäßig vertikal (`flowchart TD`); die Inhaltsspalte ist schmal, horizontale Diagramme werden klein. `flowchart LR` nur, wenn das Diagramm sonst unnötig hoch würde.
* **Robuste Syntax:** Alle Knoten- und Kantentexte in gerade Anführungszeichen setzen; keine typografischen Anführungszeichen in Labels (sie brechen den Parser).
* **Vektorgrafiken (SVG):** Für Inhalte, die Mermaid nicht abbilden kann (Oberflächen-Skizzen, Icons, präzise Layouts), eine SVG-Datei im Ordner `_attachments` des Bereichs ablegen und mit Alt-Text einbinden.
* **Sparsam und lesbar:** Ein Diagramm pro Sachverhalt, kurze Knotentexte, keine Deko. Das Diagramm ersetzt Text, es verdoppelt ihn nicht (P5).
* **Screenshots bei UI-Anleitungen:** Prüfe pro Hauptschritt, ob ein Screenshot hilft. Fehlende Bilder als HTML-Kommentar-Platzhalter mit Ziel-Dateiname (`_attachments/`) und Alt-Text einfügen und in einer Screenshot-Arbeitsliste festhalten; die Bilder liefert der Mensch.

## Tiefe trotz Kürze: Hintergrund und weiterführende Links (Pflichtprüfung)

Der sichtbare Teil jeder Seite bleibt kurz und klar; die Tiefe liegt zugeklappt in Aufklappbereichen (P3). Prüfe bei **jeder** neuen Seite (W1) und jeder Überarbeitung (W2) drei Fragen:

1. **Fehlt das Warum?** Ergänze einen kurzen Hintergrund-Aufklappbereich. Existiert eine Konzeptseite zum Thema, fasst der Block in ein bis zwei Sätzen zusammen und verlinkt dorthin (P5: verlinken statt duplizieren).
2. **Fehlt Kontext für Neue?** Ergänze einen Kontext-Aufklappbereich: Grundbegriffe der Seite erklärt, Einstiegspunkt genannt, weiterführende Quelle verlinkt.
3. **Fehlen weiterführende Links?** Externe, vertiefende Quellen gehören wo immer möglich auf die Seite: im passenden Aufklappbereich oder in den Abschnitten „Offizielle Dokumentation" bzw. „Verwandte Seiten". **Nur verifizierte Links:** vor der Übergabe aufrufen und prüfen; bevorzugt offizielle Quellen (Hersteller-Dokumentation, Standards).

Jeder Titel folgt dem Muster **„Kategorie: worum es geht"** (Entscheid vom 2026-07-12), z.B. „Hintergrund: Wozu Labels dienen". Formatiere Aufklappbereiche streng nach `references/markdown-konventionen.md` (Leerzeile nach `</summary>` und vor `</details>`, Inhalt in normalem Markdown), damit sie auf GitHub und auf der Webseite sauber rendern.

Die Grenzen bleiben bestehen: höchstens zwei bis drei Aufklappbereiche pro Seite (mehr ist ein Aufteilungs-Signal), keine kritischen Inhalte zugeklappt, der Pflichtweg funktioniert ohne Aufklappen. Hat eine Seite die Grenze erreicht, wird nichts ergänzt.

## Verweise: immer als Link

Verweise auf andere Handbuch-Seiten, das Regelwerk oder externe Quellen stehen **immer als klickbarer Link**. Formulierungen wie „siehe Anleitung, Kapitel 3", bloße Dateinamen oder Kapitelnummern ohne Link sind verboten: Niemand zählt Kapitel, und unbenannte Quellen sind nicht auffindbar.

## Annahmen: direkt Werte eintragen, keine Markierungen

Entwürfe enthalten **immer konkrete Werte oder Text**, nie Markierungen wie `[ANNAHME: …]` im Seiteninhalt oder Transport-Block.

* Gibt es einen plausiblen Wert aus dem Kontext (bestehende Seiten, Rollenliste, README-Tabelle), trage ihn direkt ein.
* **Nenne alle getroffenen Annahmen gesammelt bei der Übergabe im Chat**, damit der Mensch sie bestätigen oder korrigieren kann.
* Gibt es keinen plausiblen Wert, frage nach. Nur wenn keine Antwort möglich ist, bleibt ein neutraler Platzhalter wie `[Rolle]` oder `[JJJJ-MM-TT]`.

## Arbeitsmodus: zwei Wege je nach Bedarf

### Modus A, beratend („KI fragt, schlägt vor, Mensch entscheidet")

Nutze diesen Modus, wenn das Thema fachlich komplex ist, die Seite organisatorische Festlegungen enthält (Rollen, Befugnisse), der Mensch Unsicherheit signalisiert, oder eine **Aufteilung** ansteht (immer beratend, weil Strukturentscheidung).

Vorgehen: Stelle gezielte Fragen (Frageleitfaden der jeweiligen Vorlage), formuliere Strukturvorschläge, lass den Menschen entscheiden, schreibe dann den Entwurf.

### Modus B, generierend („KI erstellt direkt einen Entwurf")

Nutze diesen Modus, wenn der Mensch eine klare Aufgabe beschreibt, die nötigen Informationen bereits vorliegen oder er ausdrücklich um einen direkten Entwurf bittet.

Vorgehen: Erstelle direkt einen vollständigen Markdown-Entwurf nach der passenden Vorlage. Trage konkrete Werte ein und nenne die getroffenen Annahmen bei der Übergabe (siehe Abschnitt „Annahmen").

**Nicht raten bei:** verantwortlichen Rollen, internen Tool-Konventionen, organisatorischen Abläufen, Eltern-Seite und Reihenfolge im Menü. Gibt es dafür keinen plausiblen Wert aus dem Kontext, frage nach; erst wenn keine Antwort möglich ist, bleibt ein neutraler Platzhalter (`[Rolle]`, `[wird ergänzt]`).

## Die fünf Workflows im Überblick

| Workflow | Wann einsetzen |
|---|---|
| W1, neue Seite | Es gibt noch keinen Inhalt; eine Seite soll von Grund auf entstehen. |
| W2, bestehende Seite überarbeiten | Inhalt existiert, Seitentyp ist eindeutig, nur die Form soll verbessert werden. |
| W3, bestehenden Inhalt aufteilen | Inhalt existiert, vermischt aber mehrere Seitentypen oder Themen. |
| W4, Review | Nur prüfen, nicht ändern. Befunde melden. |
| W5, WordPress-Erfassung | Ein fertiger Entwurf soll in WordPress eingepflegt werden. |

**Wichtig:** Bei einer Überarbeitungsanfrage (W2) prüfst du immer **zuerst**, ob in Wahrheit W3 nötig ist. Diese Entscheidung trifft `references/aufteilen.md`.

## W1, neue Seite

Folge diesen Schritten in dieser Reihenfolge. Überspringe keinen.

1. **Seitentyp bestimmen.** Lade `references/inhaltstypen.md`. Passen mehrere Typen, ist es vermutlich eine Mischform: nachfragen.
2. **Passende Vorlage laden.** Nur die eine passende Datei:

   | Seitentyp | Referenzdatei |
   |---|---|
   | Anleitung (How-to) | `references/vorlage-anleitung.md` |
   | Prozessbeschreibung | `references/vorlage-prozess.md` |
   | Tool-Übersicht | `references/vorlage-tool.md` |
   | Rollen-/Organisationsbeschreibung | `references/vorlage-rolle.md` |
   | Hintergrund / Konzept | `references/vorlage-konzept.md` |
   | FAQ | `references/vorlage-faq.md` |

3. **Inhalte sammeln** (Modus A) oder **direkt entwerfen** (Modus B) nach dem Frageleitfaden der Vorlage. Frage dabei immer aktiv: **„Welche Begriffe dieser Seite brauchen einen Glossar-Eintrag?"** Das Seiten-Glossar steht am Ende vor dem Transport-Block; es leer zu lassen ist erlaubt, es zu vergessen nicht.
4. **Schreibregeln anwenden.** Lade `references/schreibregeln.md`.
5. **Markdown-Konventionen prüfen.** Lade `references/markdown-konventionen.md` (inkl. Dateiname = Slug, Transport-Block und Diagramm-Regeln).
6. **Selbst-Check.** Lade `references/review-checkliste.md` und prüfe systematisch.
7. **Übergabe.** Liefere den Entwurf und nenne: den gewählten Seitentyp, alle getroffenen Annahmen, alle Platzhalter, jede bewusste Abweichung von der Vorlage. Biete an, mit **W5** die WordPress-Erfassung zu begleiten.

## W2, bestehende Seite überarbeiten

1. **Vollständig lesen**, bevor du etwas tust.
2. **Mischform-Check (kritisch).** Lade `references/aufteilen.md`. Mischform erkannt: wechsle zu W3, bevor du irgendetwas umschreibst.
3. **Seitentyp bestätigen** (`references/inhaltstypen.md`).
4. **Vorlage laden und vergleichen.** Abweichungen auflisten.
5. **Schreibregeln und Markdown-Konventionen anwenden** (inkl. ASCII-Diagramme durch Mermaid ersetzen, Kapitel-Verweise durch Links ersetzen).
6. **Übergabe mit Änderungsliste**: überarbeitete Fassung plus kurze Liste der Änderungen mit Begründung, damit der Mensch einzelne Änderungen ablehnen kann.

## W3, bestehenden Inhalt aufteilen

Aufteilen ist immer **Modus A** (beratend). Die Strukturentscheidung trifft der Mensch.

1. Inhalt vollständig lesen.
2. `references/aufteilen.md` laden und der Methode folgen (Symptome, absatzweise Klassifikation, Cluster, Seitenstruktur).
3. Aufteilungs-Vorschlag präsentieren: erkannte Symptome, neue Seiten mit Typ, Verlinkung, wegfallende Inhalte, Alternative (z.B. nur Aufklappbereiche).
4. **Bestätigung abwarten.** Tue nichts, bevor der Mensch entschieden hat.
5. Aufteilung ausführen: pro neuer Seite ein Entwurf nach Vorlage, Verlinkungs-Übersicht, Liste der Quellabsätze.
6. Fragen, ob die neuen Seiten direkt nach W2 überarbeitet werden sollen oder der Mensch das selbst tut.

## W4, Review

1. Seitentyp bestimmen.
2. Mischform prüfen (`references/aufteilen.md`); Befund festhalten.
3. `references/review-checkliste.md` Punkt für Punkt durchgehen.
4. Konkrete Funde mit Stellenverweis liefern (Format in der Checkliste).
5. Verbesserungen vorschlagen, **nicht ungefragt umschreiben**.

## W5, WordPress-Erfassung

Wenn ein Entwurf fertig ist und in WordPress eingepflegt werden soll: Lade `references/wordpress-erfassung.md` und führe den Menschen durch die Erfassung (Slug = Dateiname bzw. Slug-Zeile bei Startseiten, Inhalt übertragen, Details-Blöcke, Seiten-Attribute für das Menü, Schlagworte, Textauszug, Metadaten-Felder, Transport-Block löschen, interne `.md`-Links auf die WordPress-Seiten umstellen).

## Was dieser Skill bewusst nicht tut

* Er **schreibt keine Hersteller-Dokumentationen ab** (P2); er verlinkt sie.
* Er **erfindet keine Rollennamen, Verantwortlichkeiten, Eltern-Seiten oder Menü-Reihenfolgen**. Bei Unbekanntem fragt er nach oder setzt einen neutralen Platzhalter; nie eine `[ANNAHME: …]`-Markierung.
* Er **setzt keine Datumsangaben**, die er nicht kennt (`[JJJJ-MM-TT]`).
* Er **teilt nicht ungefragt auf** und **verwendet keine Mischformen**. Lieber zwei kurze Seiten als eine vermischte.
* Er **schreibt Metadaten nie als dauerhaften Seiteninhalt**. Im Markdown-Entwurf reisen sie im Transport-Block mit; in WordPress leben sie ausschließlich in Feldern.
* Er **baut keine ASCII-Diagramme**; Diagramme entstehen als Mermaid-Codeblöcke oder als SVG in `_attachments`.
* Er **verweist nie auf Kapitel oder Dateinamen ohne Link**; jeder Verweis ist ein klickbarer Link.

## Quellen, auf denen dieser Skill basiert

* [Regelwerk Handbuch-Erstellung](../../handbuch/Handbuch-Erstellung/README.md) (intern). **Bei Widersprüchen gilt das Regelwerk.**
* [Diátaxis-Framework](https://diataxis.fr/) für die Inhaltstypen.
* [Progressive Disclosure (Nielsen Norman Group)](https://www.nngroup.com/articles/progressive-disclosure/) für die Doppel-Zielgruppe.
* [tekom-Leitlinie „Regelbasiertes Schreiben"](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf) für die Schreibregeln.
* Normen-Abgleich mit begründeten Abweichungen: [standards-abgleich.md](../../handbuch/Handbuch-Erstellung/standards-abgleich.md) (nicht zur Laufzeit laden, Hintergrunddokument).


## Menschenlesbare Beschreibung und Download

Eine für Menschen geschriebene Übersicht dieses Skills (Zweck, die fünf Workflows W1 bis W5, die zwei Arbeitsmodi, Einbindung in den KI-Assistenten) steht im Regelwerk unter [skill-handbuch-autor.md](../../handbuch/Handbuch-Erstellung/skill-handbuch-autor.md). Dort steht auch, wo der Skill als ZIP heruntergeladen werden kann. Bei Widersprüchen zwischen dieser Beschreibung und dem Regelwerk gilt das Regelwerk.
