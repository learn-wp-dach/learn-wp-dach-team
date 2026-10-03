# Leitprinzipien des Handbuchs

## Kurzbeschreibung

Diese Seite beantwortet die Frage: **Nach welchen Grundsätzen erstellen wir Handbuch-Inhalte und warum?** Sie richtet sich an alle Personen, die am Handbuch mitwirken.

## Worum geht es

Das Handbuch hat zwei Zielgruppen mit konkurrierenden Bedürfnissen, und es gibt neun Leitprinzipien, mit denen wir beide Gruppen mit *einem* Dokument bedienen.

## Zwei Zielgruppen, ein Dokument

Das Handbuch hat zwei Zielgruppen mit konkurrierenden Bedürfnissen:

| Zielgruppe | Bedürfnis | Was sie brauchen |
|---|---|---|
| **Neue Teammitglieder** (Onboarding) | Lernen, Verstehen, Kontext aufbauen | Einordnung, „Warum machen wir das?", Beispiele, mehr Hintergrund |
| **Bestehende Teammitglieder** (Nachschlagen) | Schnell finden, schnell erledigen | Knappe Schritte, klare Struktur, kein Ballast |

### Unsere Lösung

Wir erstellen **kein zweites Handbuch** für Neueinsteiger. Doppelte Pflege führt erfahrungsgemäß zu Versionsabweichungen und Mehraufwand.

Stattdessen kombinieren wir zwei etablierte Ansätze:

1. **Inhaltstypen klar trennen** ([Diátaxis-Framework](https://diataxis.fr/)). Eine Seite hat **einen** Hauptzweck, entweder Anleitung, Erklärung oder Nachschlagewerk. Mischformen vermeiden wir.
2. **Progressive Disclosure** ([Nielsen Norman Group, 1995](https://www.nngroup.com/articles/progressive-disclosure/)). Kontextinformationen für Neueinsteiger platzieren wir in Aufklappbereichen mit Titeln nach dem Muster „Kategorie: worum es geht" (z.B. „Hintergrund: Wozu Labels dienen"). Wer schnell nachschlagen will, sieht sie nicht. Wer lernen will, klappt sie auf.

Wie wir das praktisch umsetzen, steht in [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md).

<details>
<summary>Beispiel: Wie eine Seite beide Gruppen bedient</summary>

Nimm die Anleitung „Ein Thema für die Sitzung vorschlagen". Ein erfahrenes Mitglied sieht oben nur die drei Schritte und ist in zwanzig Sekunden fertig. Ein neues Mitglied klappt den Aufklappbereich „Grundlagen: Was ein Thema-Issue ist" auf und versteht, wozu das Ganze dient und wo die Themen später landen. Beide lesen dieselbe Seite; die eine Gruppe überspringt, was die andere braucht. Ohne Progressive Disclosure müssten wir entweder die Neuen mit knappen Befehlen alleinlassen oder die Erfahrenen durch Erklärungen zwingen, die sie längst kennen.

</details>

## Die neun Prinzipien

Diese Grundsätze gelten für jede Seite des Handbuchs.

### P1: Eine Seite, ein Hauptzweck

Jede Seite ist entweder Anleitung, Erklärung oder Nachschlagewerk, nie alles gleichzeitig. Mischformen verwirren beide Zielgruppen.

*Beispiel:* Die Seite „Sitzung durchführen" beschreibt den Ablauf. Die Frage „Warum treffen wir uns am letzten Dienstag?" gehört nicht daneben, sondern in einen Aufklappbereich oder eine eigene Konzeptseite. Siehe [Diátaxis-Framework](https://diataxis.fr/start-here/).

### P2: Nicht duplizieren, verlinken

Externe Tool-Dokumentationen (Hersteller, offizielle Quellen) verlinken wir, wir kopieren sie nicht. Wir dokumentieren nur, was unsere Gruppe spezifisch betrifft.

*Beispiel:* Statt zu erklären, wie ein GitHub-Issue technisch funktioniert, verlinken wir die GitHub-Doku. Wir beschreiben nur, wie **wir** Issues labeln. Details in [Schreibregeln und Markdown-Konventionen](schreibregeln-und-markdown.md).

### P3: Progressive Disclosure

Pflichtinformationen stehen oben und sichtbar. Hintergrund, Begründungen und Detailwissen für Neueinsteiger gehören in Aufklappbereiche.

*Beispiel:* Die Pflichtschritte einer Anleitung stehen offen. Die Begründung „Wozu dient das Label *priorität*?" steht zugeklappt darunter.

### P4: Aktion vor Theorie

Bei Anleitungen kommt zuerst, was zu tun ist. Das Warum folgt, falls nötig, im Aufklappbereich.

*Beispiel:* „Aufgabe erfassen" beginnt mit „Klicke auf *New issue*", nicht mit einem Absatz über die Philosophie der Aufgabenverwaltung.

### P5: Eine Quelle pro Information

Jede Information existiert an genau **einer** Stelle im Handbuch (englisch: Single Source of Truth). Andere Stellen verlinken dorthin. So bleibt das Handbuch pflegbar.

*Beispiel:* Die Uhrzeit des Monatsmeetings steht an einer Stelle; die FAQ verlinkt dorthin, statt sie zu wiederholen. Sonst müsste man bei einer Änderung zwei Stellen finden.

### P6: Aktualität sichtbar machen

Jede Seite zeigt, wann wir sie zuletzt aktualisiert und zuletzt geprüft haben und welche Rolle dafür verantwortlich ist. Diese Angaben leben in WordPress als Felder; die Fußzeile zeigt sie automatisch an. In Markdown-Entwürfen reisen sie im Transport-Block mit.

*Beispiel:* Unten steht „Zuletzt geprüft: 2026-05-03", auch wenn sich am Inhalt nichts geändert hat. So weiß man, dass die Information nicht bloß vergessen wurde.

### P7: Rollen statt Personen

Verantwortlichkeiten weisen wir über **Rollen** zu, nicht über konkrete Personen. So müssen wir bei einem personellen Wechsel nicht das ganze Handbuch überarbeiten.

*Beispiel:* In einer Prozessbeschreibung steht „Die Protokoll-Verantwortung gibt frei", nicht „Anna gibt frei". Die Zuordnung Person zu Rolle pflegen wir an einer einzigen, zentralen Stelle.

### P8: Nutzerperspektive vor Tool-Logik

Anleitungen organisieren wir nach **Aufgaben** („So buchst du eine Reise"), nicht nach **Tool-Menüpunkten**.

*Beispiel:* Die Anleitung heißt „So schlägst du ein Thema vor", nicht „Das Menü *Issues → New issue*". Das gilt besonders für [How-to-Guides](https://diataxis.fr/how-to-guides/).

### P9: Handbook-first

Ändert sich ein Prozess oder ein Tool, aktualisieren wir die betroffene Seite im selben Arbeitsgang. Das Handbuch läuft der Realität nicht hinterher.

*Beispiel:* Wechselt das Team das Board-Tool, wird die betroffene Seite sofort angepasst, nicht „irgendwann später".

## Was bedeutet das für unsere Arbeit

Die Prinzipien bilden die Basis aller anderen Regelwerk-Seiten:

* **Eine Seite, ein Hauptzweck (P1):** die Grundlage der sechs Seitentypen in [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md).
* **Nicht duplizieren, verlinken (P2):** prägt den Umgang mit externen Dokumentationen in den [Schreibregeln und Markdown-Konventionen](schreibregeln-und-markdown.md).
* **Progressive Disclosure (P3) und Aktion vor Theorie (P4):** bestimmen den Aufbau jeder Seite, siehe [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md).
* **Eine Quelle pro Information (P5):** der Grund, warum Vorlagen und Review-Checkliste nur an einem Ort liegen, siehe [Erstellungs- und Pflegeprozess](erstellungs-und-pflegeprozess.md).
* **Aktualität sichtbar machen (P6):** die Grundlage der Metadaten-Felder und des Transport-Blocks.
* **Rollen statt Personen (P7):** prägt den [Erstellungs- und Pflegeprozess](erstellungs-und-pflegeprozess.md).
* **Nutzerperspektive vor Tool-Logik (P8):** die Grundregel beim Schreiben von Anleitungen.
* **Handbook-first (P9):** hält das Handbuch aktuell, siehe [Erstellungs- und Pflegeprozess](erstellungs-und-pflegeprozess.md).

<details>
<summary>Beispiel: Alle Prinzipien an einer einzigen Seite</summary>

Angenommen, wir schreiben „So erfasst du eine Aufgabe". Dann wirken die Prinzipien so zusammen: Die Seite ist reine Anleitung (P1). Sie beginnt mit dem ersten Klick statt mit Theorie (P4, P8). Die Begründung „Warum wir Aufgaben in GitHub führen" steht zugeklappt (P3) und verlinkt auf die Konzeptseite, statt sie zu wiederholen (P5). Wie GitHub grundsätzlich funktioniert, verlinken wir statt es abzuschreiben (P2). Zuständig ist „die GitHub-Verantwortung", keine Person (P7). Unten stehen Prüfdatum und verantwortliche Rolle (P6). Ändert sich der Ablauf, wird genau diese Seite sofort nachgezogen (P9). Neun Prinzipien, eine Seite, kein Widerspruch.

</details>

## Verwandte Seiten

* [Regelwerk-Übersicht](README.md)
* [Inhaltstypen und Vorlagen](inhaltstypen-und-vorlagen.md)
* [Schreibregeln und Markdown-Konventionen](schreibregeln-und-markdown.md)
* [Erstellungs- und Pflegeprozess](erstellungs-und-pflegeprozess.md)

## Seiten-Glossar

| Begriff | Definition |
|---|---|
| Aufklappbereich | HTML-`<details>`-Element für ergänzende Informationen, mit Titel nach dem Muster „Kategorie: worum es geht" (z.B. „Hintergrund: Wozu Labels dienen"). |
| Rolle | Funktionsbezeichnung im Team, der Verantwortlichkeiten zugeordnet sind (nicht eine konkrete Person). |
| Transport-Block | Block am Ende jedes Markdown-Entwurfs, der die Metadaten zur Erfassung transportiert; wird beim Import in WordPress-Felder übertragen und aus dem Inhalt gelöscht. |

## Transport-Metadaten (beim Erfassen in Felder übertragen, dann diesen Block löschen)

* Seitentyp: Hintergrund / Konzept
* Verantwortliche Rolle: GitHub-Spezialist
* Thema: Organisation
* Zielgruppe: Inhalts-Ersteller:innen
* Eltern-Seite: Handbuch-Erstellung
* Reihenfolge: 10
* Textauszug: Diese Seite beantwortet die Frage: Nach welchen Grundsätzen erstellen wir Handbuch-Inhalte und warum?
* Letzte Aktualisierung: 2026-07-27
* Letzte Prüfung: 2026-05-03
* Prüfintervall: 365
