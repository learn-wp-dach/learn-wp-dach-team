# Vorlage: Prozessbeschreibung

## Frageleitfaden (Modus A)

1. **Wie heißt der Prozess?** (Substantiv, kurz)
2. **Was löst ihn aus?** (Ereignis, Frist, Antrag; konkret, nicht „bei Bedarf")
3. **Welche Rollen sind beteiligt?** (jede mit ihrer Aufgabe; nur eine Rolle → Anleitung, `vorlage-anleitung.md`)
4. **Welche Schritte gibt es?** (chronologisch, mit Rollenzuordnung und Übergaben)
5. **Was liegt am Ende vor?** (Ergebnis, Output, Zustand)
6. **Welchen Kontext brauchen Neueinsteiger?** (Aufklappbereich mit beschreibendem Titel, z.B. „Hintergrund" oder „Weitere Informationen")
7. **Welche Rolle ist für die Korrektheit verantwortlich?** (Transport-Block)

## Vorlage

```markdown
## Kurzbeschreibung

[Welcher Ablauf, wann ausgelöst, mit welchem Ergebnis?]

<details>
<summary>Hintergrund: [worum es geht]</summary>

[Optional: Einordnung für Neueinsteiger.]

</details>

## Auslöser

[Was startet diesen Prozess?]

## Beteiligte Rollen

* [Rolle]: [Aufgabe]

## Ablauf

1. [Schritt: welche Rolle macht was?]
2. [Schritt: welche Rolle macht was?]

## Ergebnis

[Was liegt am Ende vor?]

<details>
<summary>Hintergrund: Warum ist dieser Prozess so gestaltet?</summary>

[Optional]

</details>

## Verwandte Seiten / Tools

* [Link]
```

Danach den **Transport-Block** aus `markdown-konventionen.md` anhängen.

## Hinweise zum Ausfüllen

* **Rollen, nicht Personen:** „Mitglieder-Verantwortung", nicht „Anna".
* **Rolle pro Schritt sichtbar machen:** „Die Mitglieder-Verantwortung sendet das Begrüßungsmail."
* **Übergaben explizit machen:** Wer gibt wem was, in welchem Zustand?
* **Hintergrund nur in den Aufklappbereich**, nicht in den Ablauf.
