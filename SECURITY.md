# Sicherheitsrichtlinie

## Unterstützte Versionen

Dieses Repository enthält keine Software-Releases. Die Sicherheitsrichtlinie bezieht sich auf die GitHub Actions Workflows und die Repository-Konfiguration.

## Sicherheitsprobleme melden

Falls du ein Sicherheitsproblem in einem der Workflows oder in der Repository-Konfiguration entdeckst (z.B. unsichere Verwendung von Secrets, Command-Injection-Risiken), erstelle ein [neues Issue](https://github.com/learn-wp-dach/learn-wp-dach-team/issues/new) mit dem Titel `[SECURITY] Kurze Beschreibung` und benachrichtige anschliessend ein Team-Mitglied direkt per Nachricht oder Kommentar.

Wir werden das Problem so schnell wie möglich prüfen und beheben.

## Sicherheitshinweise für Admins

- Personal Access Tokens (PAT) **nie** in den Code, in Issues oder in Chats einfügen – immer als [Repository-Secret](../../settings/secrets/actions) speichern.
- Den PAT regelmässig erneuern (Empfehlung: alle 12 Monate).
- Nur die minimal notwendigen Scopes für den PAT aktivieren (`repo` und `project`).
- Secrets verwalten: Repository → **Settings** → **Secrets and variables** → **Actions**.
