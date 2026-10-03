# WordPress-Erfassung (Workflow W5)

WordPress ist die Single Source of Truth. Seit Prototyp 0.10.0 ist der Standardweg der **Markdown-Import**; das manuelle Einfügen ist nur noch Notbehelf. Führe den Menschen hindurch; frage nach fehlenden Werten, statt zu raten.

## Standardweg: Markdown-Import

1. **Reihenfolge planen:** Zuerst die Eltern-Seite des Bereichs importieren, dann die Kinder (sonst kann der Import die Eltern-Seite nicht zuordnen; er warnt dann und lässt sie weg).
2. **wp-admin → Handbuch → Markdown-Import** öffnen.
3. **Dateiname (ohne .md)** eintragen; er wird der Slug und muss dem Dateinamen im Repo entsprechen (Konvention Dateiname = Slug, Grundlage der Link-Konvertierung).
4. **Kompletten Entwurf einfügen**, inklusive `# Titel` und Transport-Block, unverändert aus dem Repo.
5. **Importieren.** Es entsteht ein **Entwurf** mit fertigem Block-Markup (Überschriften, Listen, Tabellen, Aufklappbereiche als echte Details-Blöcke) und gesetzten Feldern: Eltern-Seite, Reihenfolge, Seitentyp, Thema, Verantwortliche Rolle, Zielgruppe, Textauszug, Prüfdatum, Prüfintervall. Der Transport-Block landet nicht im Inhalt.
6. **Warnhinweise lesen** (z.B. Eltern-Seite nicht gefunden), Entwurf im Editor prüfen, **veröffentlichen**. Menü, Übersicht und Filter ziehen automatisch nach.
7. **Nach dem letzten Import des Bereichs:** Dashboard → Widget «Handbuch: Prüfung überfällig» → **«.md-Links jetzt automatisch konvertieren»**. Danach dürfen keine Markierungen «⚠ n .md-Links» mehr stehen; bleibt eine, fehlt die Zielseite oder ihr Slug weicht vom Dateinamen ab.
8. **Sichtprüfung im Frontend:** Menüplatz, Aufklappbereiche, Metadaten-Fußzeile, Karte mit Auszug, interne Links.


**Startseite eines Bereichs (README.md):** Sie wird immer zuerst importiert. Im Import-Formular gilt nicht der Dateiname (`README`), sondern der Slug aus der Transport-Block-Zeile `Slug:` (Bereichsname in Slug-Form). Alle übrigen Seiten des Bereichs tragen die Startseite als Eltern-Seite.

## Notbehelf: manuelles Einfügen (nur wenn der Import nicht verfügbar ist)

Markdown direkt einzufügen ist unzuverlässig (insbesondere werden `<details>` nie zu Details-Blöcken). Falls es doch sein muss: Inhalt ohne Transport-Block in den visuellen Editor einfügen, jedes `<details>` von Hand als Details-Block nachbauen, alle Felder gemäß Transport-Block setzen (Seiten-Attribute, vier Schlagwort-Gruppen, Textauszug wortgleich zum ersten Satz der Kurzbeschreibung, Meta-Box Aktualität), Slug angleichen, veröffentlichen, `.md`-Links über den Dashboard-Knopf konvertieren.

## Häufige Fehler

* Kinder vor der Eltern-Seite importiert → Warnung; Eltern-Seite später unter Seiten-Attribute nachtragen.
* Dateiname im Import-Formular weicht vom Repo-Dateinamen ab → Link-Konvertierung findet die Seite nicht; Slug angleichen.
* `.md` von Hand aus Links gelöscht → ergibt relative, kaputte Pfade, die der Checker nicht mehr erkennt. Links unverändert lassen; die Konvertierung braucht das `.md`.
* Transport-Block vor dem Import entfernt → Felder bleiben leer; kompletten Entwurf einfügen.
* Entwurf vergessen zu veröffentlichen → Seite erscheint weder im Menü noch in der Übersicht.
