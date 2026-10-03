# Vorlage: FAQ

FAQ-Seiten bündeln wiederkehrende Fragen zu einem Themenbereich und führen zur maßgeblichen Seite. Sie sind eine **Einstiegshilfe**, kein Wissensspeicher.

**Gestaltungsregel (Entscheid 2026-07-05):** Jede Frage ist ein **eigener Aufklappbereich** (Frage = Titelzeile, Antwort = Inhalt). So überfliegt man nur Fragen und öffnet gezielt. Die Sparsamkeitsregel «höchstens zwei bis drei Aufklappbereiche pro Seite» gilt für FAQ-Seiten ausdrücklich **nicht**.

## Sonderregeln (wahren die Single Source of Truth, P5)

1. **Antworten sind kurz:** ein bis drei Sätze.
2. **Jede Antwort verlinkt auf die maßgebliche Seite**, auf der die Information lebt.
3. **Keine neuen Fakten.** Fehlt die maßgebliche Seite, wird zuerst sie erstellt oder ergänzt; erst dann bekommt die FAQ den Eintrag.
4. **Häufungs-Signal:** Sammeln sich Fragen zum selben Thema, verbessere die betroffene Seite (P9), statt die FAQ wachsen zu lassen.

## Frageleitfaden (Modus A)

1. **Zu welchem Themenbereich** gehört die FAQ? (eine FAQ pro Bereich, nicht eine globale)
2. **Welche Fragen kommen wirklich vor?** (aus Sitzungen, Chats, Suchanfragen; nicht ausgedacht)
3. **Wo lebt die jeweilige Antwort?** (maßgebliche Seite pro Frage)
4. **Welche Rolle ist verantwortlich?** (Transport-Block)

## Vorlage

```markdown
## Kurzbeschreibung

[Häufige Fragen zu (Themenbereich). Jede Frage ist aufklappbar; die Antworten
verweisen auf die maßgeblichen Seiten.]

<details>
<summary>[Frage 1 im Wortlaut der Fragenden]</summary>

[Kurze Antwort, 1 bis 3 Sätze.] Details: [Link zur maßgeblichen Seite].

</details>

<details>
<summary>[Frage 2]</summary>

[Kurze Antwort.] Details: [Link].

</details>

## Verwandte Seiten

* [Link zum Themenbereich / zur Übersicht]
```

Danach den **Transport-Block** aus `markdown-konventionen.md` anhängen.

## Hinweise zum Ausfüllen

* **Fragen im Wortlaut**, wie Menschen sie stellen.
* **Reihenfolge:** häufigste Fragen zuerst.
* **Einschränkung Suche:** Zugeklappte Antworten sind für die Volltextsuche weiterhin auffindbar (der Text steht im Inhalt), erscheinen aber nicht im Seiten-Inhaltsverzeichnis, weil die Fragen keine Überschriften sind. Das ist bei FAQ gewollt.
