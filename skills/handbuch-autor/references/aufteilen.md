# Mischform erkennen und bestehenden Inhalt aufteilen

Diese Referenz beschreibt, wie ein bestehender Inhalt analysiert und in saubere Einzelseiten aufgeteilt wird. Aufteilen ist immer **Modus A** (beratend): Die Strukturentscheidung trifft der Mensch.

## Warum aufteilen wichtig ist

Mischformen verletzen P1 („ein Hauptzweck pro Seite") und führen zu zwei Problemen:

* **Lesende finden nicht, was sie suchen.** Wer nachschlagen will, muss durch Lernmaterial waten; wer lernen will, stolpert über knappe Referenzen.
* **Pflege ist schwer.** Eine Seite mit fünf Themen hat fünf Auslöser für Aktualisierung; sauber getrennte Seiten je einen.

## Phase 1, Mischform erkennen

Prüfe den Inhalt gegen folgende **Symptome**. Trifft auch nur eines klar zu, liegt eine Mischform vor.

1. **Titel mit „und" oder mehreren Substantiven:** „WordPress, Übersicht und Anleitung zum Login" → Tool-Übersicht **und** Anleitung.
2. **Mehrere Diátaxis-Typen im selben Text.** Prüfe absatzweise: Schritt-für-Schritt-Imperative (Anleitung), wer-macht-was mit Übergaben (Prozess), Listen/Tabellen/neutrale Beschreibung (Referenz), Begründungen („Warum machen wir das so") (Hintergrund). Zwei oder mehr Kategorien im selben Text: Mischform.
3. **Zielgruppenwechsel mitten im Text:** erst basale Erklärungen für Neue, dann knappe Power-User-Befehle. Das löst ein Kontext-Aufklappbereich (z.B. „Hintergrund") eleganter.
4. **„Außerdem"-Absätze:** „Außerdem", „Übrigens", „In diesem Zusammenhang", „Ergänzend" leiten oft thematisch fremde Inhalte ein: Kandidaten für Auslagerung.
5. **Langer Hintergrund-Block in einer Anleitung:** mehr als ein paar Sätze gehören in einen Aufklappbereich oder, falls eigenständig wertvoll, in eine eigene Konzeptseite.
6. **Abgeschriebene Hersteller-Dokumentation:** verletzt P2; entfällt bei der Aufteilung und wird durch einen Link ersetzt.
7. **Wachsende Fragensammlung auf einer Sachseite:** Frage-Antwort-Blöcke, die sich auf einer Anleitung oder Übersicht ansammeln, gehören in eine FAQ-Seite des Bereichs (`vorlage-faq.md`), sofern die Antworten auf maßgebliche Seiten verlinken können.

## Phase 2, Inhalt absatzweise klassifizieren

1. Nummeriere die Absätze gedanklich durch.
2. Weise jedem Absatz einen der sechs Seitentypen zu, oder „entfällt" (Hersteller-Doku-Duplikat).
3. Notiere unsichere Zuordnungen mit Begründung.

Beispiel:

| Absatz | Inhalt | Klassifikation |
|---|---|---|
| 1 | „WordPress ist unser zentrales CMS." | Tool-Übersicht |
| 2 | „Hersteller-Doku unter wordpress.org" | Tool-Übersicht (Verlinkung) |
| 3 | „Bei uns nutzt es die Redaktion" | Tool-Übersicht (Wer nutzt es) |
| 4–5 | „Um einen Beitrag anzulegen, klicke auf …" | Anleitung |
| 6 | „Wir haben uns entschieden, weil Open Source" | Hintergrund/Konzept |

## Phase 3, Cluster bilden und Seitenstruktur ableiten

Fasse Absätze derselben Klassifikation zu Clustern zusammen; jedes Cluster wird tendenziell eine Seite.

**Aufteilung lohnt sich, wenn mindestens eins zutrifft:** Ein Cluster hat Substanz für eine eigene Seite (mehr als 2 bis 3 Absätze); die Inhalte werden unabhängig voneinander aktualisiert; die Inhalte bedienen unterschiedliche Lesesituationen.

**Aufteilung lohnt sich nicht, wenn:** ein Cluster nur 1 bis 2 Sätze hat (dann Aufklappbereich); die Inhalte nur gemeinsam Sinn ergeben; die Hauptseite dadurch zu dünn würde.

## Phase 4, Verlinkungsmuster

* **Tool-Übersicht als Knotenpunkt:** verlinkt Hersteller-Doku (extern), alle Anleitungen mit diesem Tool (intern), die Konzeptseite mit der Auswahl-Begründung (intern).
* **Anleitung verweist nach oben:** unter „Verwandte Seiten" auf die Tool-Übersicht und auf Anleitungen derselben Aufgabenkette.
* **Konzeptseite als Begründungsanker:** wird vor allem aus Aufklappbereichen anderer Seiten verlinkt, nicht im Hauptfluss.
* **FAQ als Wegweiser:** verlinkt auf die maßgeblichen Seiten des Bereichs; nie umgekehrt Inhalte aus Seiten in die FAQ ziehen.

## Phase 5, Vorschlag formulieren

```markdown
## Mischform-Befund

Ich habe folgende Symptome erkannt:
- [Symptom mit Beispielzitat aus dem Text]

## Aufteilungs-Vorschlag

Aus der bestehenden Seite werden N neue Seiten:

1. **[Titel]** ([Seitentyp])
   - Inhalt aus den Quellabsätzen: [Liste]
   - Verlinkung zu: [andere neue Seiten]

## Was wegfällt

- [Hersteller-Doku-Duplikate, ersetzt durch Verlinkung]

## Alternative

Statt aufzuteilen könnten wir auch [z.B. Aufklappbereiche nutzen]. Das wäre weniger eingreifend, hätte aber den Nachteil [Begründung].

## Frage

Soll ich so aufteilen, anders aufteilen, oder die Alternative umsetzen?
```

Warte auf Bestätigung, **bevor** du die neuen Seiten erstellst.
