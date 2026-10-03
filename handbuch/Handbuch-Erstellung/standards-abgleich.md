# Standards-Abgleich

## Kurzbeschreibung

Diese Seite zeigt, wo unser Regelwerk anerkannten Normen und Leitlinien folgt und wo wir bewusst von ihnen abweichen. Sie richtet sich an alle, die die Herkunft der Regeln verstehen wollen; für die tägliche Handbuch-Arbeit wird sie nicht gebraucht.

## Worum geht es

Pro Standard steht, was er fordert, was wir in das [Regelwerk Handbuch-Erstellung](README.md) und den Skill [handbuch-autor](https://github.com/learn-wp-dach/learn-wp-dach-team/blob/main/skills/handbuch-autor/SKILL.md) übernommen haben und wo wir begründet abweichen. Die Links führen zu informierenden Quellen (Wikipedia, freie Spezifikationen, frei lesbare Norm-Auszüge), nicht zu Verkaufsseiten.

## Einordnung

Unser Handbuch ist ein **internes Organisations- und Arbeitshandbuch** eines kleinen Teams (Tools, Prozesse, Rollen), kein Produkthandbuch mit Sicherheitsrelevanz und kein zertifiziertes Managementsystem. Die Standards sind darum Steinbruch, nicht Pflichtenheft: Wir übernehmen Prinzipien, die unsere Qualität heben, und lassen Formalismus weg, der auf Zertifizierung oder Produkthaftung zielt.

## Technische Dokumentation

### [IEC/IEEE 82079-1:2019](https://de.wikipedia.org/wiki/IEC/IEEE_82079) (Nutzungsinformation, Grundnorm)

**Fordert u.a.:** Zielgruppenanalyse, Informationsarten trennen (instruktiv/konzeptionell/referenziell), Minimalismus (nur handlungs- oder entscheidungsrelevante Information), Verständlichkeit, definierte Erstellungs- und Prüfprozesse, qualifizierte Ersteller, Sicherheits- und Warnhinweise.

**Übernommen:** Trennung der Informationsarten (über Diátaxis, strenger als die Norm), Zielgruppenanalyse (zwei definierte Zielgruppen mit Progressive Disclosure), Minimalismus als Prüffrage in [Schreibregeln](schreibregeln-und-markdown.md) und [Review-Checkliste](https://github.com/learn-wp-dach/learn-wp-dach-team/blob/main/skills/handbuch-autor/references/review-checkliste.md) („unterstützt dieser Absatz eine Handlung oder Entscheidung?"), definierter [Erstellungs- und Reviewprozess](erstellungs-und-pflegeprozess.md). Dazu Warnungen vor irreversiblen Schritten, platziert **vor** dem Schritt.

**Abweichungen, begründet:**

* **Keine formale Konformitätserklärung und kein Warnhinweis-System nach Signalwortstufen** (GEFAHR/WARNUNG/VORSICHT). Unser Inhalt hat keine Personenschutz-Relevanz; ein fetter Hinweis vor irreversiblen Schritten genügt und hält die Seiten lesbar.
* **Keine formal nachgewiesene Erstellerqualifikation.** Ersatz: Peer-Review-Pflicht plus Skill [handbuch-autor](https://github.com/learn-wp-dach/learn-wp-dach-team/blob/main/skills/handbuch-autor/SKILL.md), der die Regeln maschinell durchsetzt. Für ein Team dieser Größe ist gelebte Prüfung wirksamer als Qualifikationsnachweise.

### [ISO 12100](https://de.wikipedia.org/wiki/ISO_12100), [ISO 20607](https://www.iso.org/obp/ui/#!iso:std:68519:en), [ANSI Z535.6](https://en.wikipedia.org/wiki/ANSI_Z535) (Maschinensicherheit)

**Nicht anwendbar.** Wir dokumentieren keine Maschinen und erstellen keine Betriebsanleitungen im Sinne der Maschinenverordnung. Keine Übernahme; bewusst keine Warnhinweis-Taxonomie nach Z535.6 (siehe oben).

### ISO/IEC/IEEE 26511 bis 26515 (Software-Nutzerdokumentation)

Die Reihe, je als frei lesbarer Norm-Auszug: [26511 Management](https://www.iso.org/obp/ui/#!iso:std:70879:en), [26512 Beschaffung](https://www.iso.org/obp/ui/#!iso:std:72088:en), [26513 Test und Review](https://www.iso.org/obp/ui/#!iso:std:67417:en), [26514 Gestaltung](https://www.iso.org/obp/ui/#!iso:std:77451:en), [26515 agile Entwicklung](https://www.iso.org/obp/ui/#!iso:std:70880:en).

**Fordert u.a.:** Management-, Beschaffungs-, Test-, Gestaltungs- und Agile-Prozesse für Nutzerdokumentation.

**Übernommen:** 26514 (Gestaltung) ist im [Regelwerk](README.md) als Referenz verankert (Struktur- und Formatanforderungen). 26515 (agil) prägt unseren schlanken [Erstellungsprozess](erstellungs-und-pflegeprozess.md): dokumentieren im selben Arbeitsgang wie die Änderung (P9), kleine Einheiten, Review statt Big-Bang-Abnahme.

**Abweichungen, begründet:** **Keine getrennten Management- und Beschaffungsprozesse** (26511/26512): Bei einem Team ohne Doku-Abteilung und ohne Zulieferer wäre das Prozess-Theater. Die Testperspektive (26513) deckt unsere Review-Checkliste plus der Praxistest „neues Mitglied folgt der Anleitung" ab.

### [VDI 4500](https://www.vdi.de/richtlinien/details/vdi-4500-blatt-1-technische-dokumentation-begriffsdefinitionen-und-rechtliche-grundlagen) (Technische Dokumentation, Richtlinienreihe)

**Fordert u.a.:** systematische Gliederung, Terminologiemanagement, Lebenszyklus der Dokumentation.

**Übernommen:** Terminologie-Disziplin (S5, Seiten-Glossar als verbindliche Termliste), Lebenszyklus-Gedanke über Prüfintervalle und Wartungsübersicht.

**Abweichungen, begründet:** **Kein zentrales Terminologie-Register.** Wir führen Seiten-Glossare mit wortgleich wiederverwendeten Definitionen; das ist eine bewusste Ausnahme von P5 zugunsten in sich verständlicher Seiten. Ein zentrales Register lohnt erst ab deutlich größerem Begriffsbestand; die Wortgleichheits-Regel hält die Tür dafür offen.

### [tekom-Leitlinie „Regelbasiertes Schreiben"](https://www.tekom.de/fileadmin/tekom.de/Die_tekom/Publikationen/Leseproben/2013_RBS_Deutsch_fuer_die_TK_Leseprobe.pdf)

**Übernommen:** Kern unserer Schreibregeln S1 bis S8 (Aktiv, kurze Sätze, Imperativ, Konkretheit, Ein-Begriff-Regel, konsistente Anrede, keine Füllwörter) plus Standardsatzmuster für Handlungsschritte. S10 (Begriffe vor Gebrauch einführen) folgt der Verständlichkeits-Anforderung aus IEC/IEEE 82079-1.

**Abweichungen, begründet:** Wir übernehmen die **vereinfachte Auswahl**, nicht das volle Regelwerk (über 100 Regeln). Der Nutzen zusätzlicher Regeln fällt bei internen How-tos steil ab; die Einstiegshürde für schreibende Teammitglieder stiege dagegen deutlich.

### [DITA 1.3 (OASIS)](https://docs.oasis-open.org/dita/dita/v1.3/os/part0-overview/dita-v1.3-os-part0-overview.html)

**Fordert u.a.:** modulare Topic-Typen (concept/task/reference), Wiederverwendung über Referenzierung, strikte Trennung Inhalt/Ausgabe.

**Übernommen:** Die Topic-Typen-Idee, umgesetzt über Diátaxis-Seitentypen; Wiederverwendung über Verlinkung (P5); Pflicht-Kurzbeschreibung entspricht DITAs `shortdesc`.

**Abweichungen, begründet:** **Keine DITA-Toolchain (XML, Spezialeditoren).** Autorenschaft im WordPress-Block-Editor ist Kernanforderung des Konzepts (niedrige Schwelle für alle Teammitglieder); eine XML-Pipeline würde genau die Menschen ausschließen, die schreiben sollen.

### [ASD-S1000D](https://s1000d.org/)

**Nicht anwendbar.** Luftfahrt-/Verteidigungsstandard mit Datenmodul-Verwaltung; für ein Teamhandbuch massiv überdimensioniert. Keine Übernahme.

### [ASD-STE100](https://www.asd-ste100.org/) (Simplified Technical English)

**Fordert u.a.:** kontrolliertes Vokabular, harte Satzlängenlimits, ein Wort = eine Bedeutung.

**Übernommen:** die Prinzipien, auf Deutsch übertragen: S5 (eine Bedeutung, ein Begriff), S2 mit harter 20-Wörter-Prüfung und Schachtelsatz-Verbot, Standardsatzmuster für Schritte.

**Abweichungen, begründet:** **Kein kontrolliertes Wörterbuch.** STE100 ist für Englisch definiert und lebt vom gepflegten Dictionary; für Deutsch existiert kein Äquivalent, und der Pflegeaufwand stünde in keinem Verhältnis. Die Glossar-Disziplin pro Seite ist unser verhältnismäßiger Ersatz.

## Organisationsdokumentation

### [ISO 9001:2015](https://de.wikipedia.org/wiki/ISO_9001) / [ISO 10013:2021](https://www.iso.org/obp/ui/#!iso:std:75736:en) (dokumentierte Information)

**Fordert u.a.:** Dokumentenhierarchie (Politik → Prozesse → Arbeitsanweisungen → Nachweise), Lenkung dokumentierter Information (Erstellung, Prüfung, Freigabe, Änderung, Versionierung), Aktualität.

**Übernommen:** Die **Dokumentenhierarchie als Einordnungsfrage** im Skill (Konzeptseite = Grundsatz, Prozessbeschreibung = Prozess, Anleitung = Arbeitsanweisung; Nachweise wie Protokolle und erledigte Issues leben im Tool, nicht im Handbuch). Lenkung: definierter [Erstellungsprozess](erstellungs-und-pflegeprozess.md) mit Review und Freigabe, Versionierung über WordPress-Revisionen, Aktualität über Prüfintervalle.

**Abweichungen, begründet:** **Keine formale Dokumentenlenkung mit Freigabevermerken, Verteilerlisten und gelenkten Kopien.** Wir sind kein zertifiziertes Managementsystem; WordPress-Revisionen plus sichtbare Prüf-Metadaten leisten die Nachvollziehbarkeit mit einem Bruchteil des Aufwands. **Kein systematisches Änderungsprotokoll pro Seite:** WordPress-Revisionen genügen; nur für Lesende relevante Änderungen (z.B. geänderter Ablauf) werden auf der Seite in einem Aufklappbereich festgehalten ([Erstellungs- und Pflegeprozess](erstellungs-und-pflegeprozess.md)).

### [ISO/IEC 27001](https://de.wikipedia.org/wiki/ISO/IEC-27000-Reihe), [ISO 15489-1](https://www.iso.org/obp/ui/#iso:std:iso:15489:-1:ed-2:v1:en), [ISO 30301](https://www.iso.org/obp/ui/#iso:std:iso:30301:en) (Informationssicherheit, Records Management)

**Nicht übernommen als System.** Relevanter Einzelpunkt: Zugriffsschutz: Das Handbuch ist produktiv intern (Login-Pflicht), öffentlich zugängliche Demo-Inhalte sind erkennbar fiktiv. Records Management (Aufbewahrung, Kassation) betrifft Protokolle und Mitgliederdaten; das ist Sache der jeweiligen Tools und Prozesse, nicht des Handbuchs. Das Handbuch dokumentiert höchstens, **wo** solche Nachweise liegen.

### [BPMN 2.0 (ISO/IEC 19510)](https://www.omg.org/spec/BPMN/2.0/) und [eCH-Standards](https://www.ech.ch/)

**Fordert u.a.:** grafische Prozessnotation mit definierter Semantik.

**Abweichung, begründet:** **Prozessbeschreibungen sind bei uns text-basiert mit ergänzenden Mermaid-Diagrammen**, ohne BPMN-Semantik. Der Aufbau: Auslöser, Rollen, nummerierter Ablauf, Ergebnis; dazu ein Mermaid-Ablaufdiagramm, wo es den Text verdeutlicht und kürzt ([Schreibregeln und Markdown-Konventionen](schreibregeln-und-markdown.md)). Mermaid ist textbasiert und versionierbar und veraltet damit nicht unbemerkt wie eingebettete Bilder; die volle BPMN-Notation wäre für Prozesse mit drei bis sieben Schritten Überformalisierung. Die eCH-Verwaltungsstandards richten sich an Behörden; ihre konkrete Anwendbarkeit wurde nicht weiter geprüft, weil BPMN bei uns nicht eingesetzt wird.

## Zusammenfassung der übernommenen Prüfregeln

Aus dem Abgleich sind konkret in den Skill eingeflossen:

1. **82079-Minimalismus-Prüffrage** (Schreibregeln, Review-Checkliste): Jeder Absatz unterstützt eine Handlung oder Entscheidung.
2. **ISO-10013-Ebenenfrage** (Inhaltstypen): Grundsatz/Prozess/Arbeitsanweisung/Nachweis; Nachweise gehören nicht ins Handbuch.
3. **STE-Anleihe** (Schreibregeln): harte Satzlängenprüfung, Standardsatzmuster für Schritte.
4. **tekom/VDI-Terminologie-Disziplin** (Schreibregeln): Seiten-Glossar als verbindliche Termliste.

## Verwandte Seiten

* [Regelwerk-Übersicht](README.md)
* [Leitprinzipien](leitprinzipien.md)
* [Schreibregeln und Markdown-Konventionen](schreibregeln-und-markdown.md)

## Transport-Metadaten (beim Erfassen in Felder übertragen, dann diesen Block löschen)

* Seitentyp: Hintergrund / Konzept
* Verantwortliche Rolle: GitHub-Spezialist
* Thema: Organisation
* Zielgruppe: Inhalts-Ersteller:innen
* Eltern-Seite: Handbuch-Erstellung
* Reihenfolge: 60
* Textauszug: Diese Seite zeigt, wo unser Regelwerk anerkannten Normen und Leitlinien folgt und wo wir bewusst von ihnen abweichen.
* Letzte Aktualisierung: 2026-07-28
* Letzte Prüfung: 2026-07-12
* Prüfintervall: 365
