# KI, die mitarbeitet

Deutschsprachiger Praxisworkshop für KI im Arbeitsalltag von Handwerk und Bau. Eine Keynote-artige Website mit 44 Folien, neun schrittweisen Beispielen, zehn offenen Herausforderungen und einem vollständigen fiktiven Übungspaket.

## Website

Cloudflare Worker: `seminar`. Präsentationsmodus mit Pfeiltasten und Vollbild, Entdecken-Modus, Kapitelsuche, lokale Checklisten, optionale Hilfen und kopierbare Arbeitsaufträge.

Die Seminarwebsite verbindet sich selbst nicht mit Microsoft 365. Die Teilnehmer bearbeiten Übungen in ihren eigenen Work- und Microsoft-365-Konten. Die Verfügbarkeit einzelner Plugins, Excel-Integration und geplanter Aktionen muss im jeweiligen Konto geprüft werden. Demos sind ausdrücklich fiktive Beispiele.

## Entwicklung

Node.js 20 oder neuer, keine Frontend-Abhängigkeiten erforderlich.

1. Eine lokale, nicht versionierte Datei `.dev.vars` mit `WORKSHOP_PASSWORD` und einem zufälligen `SESSION_SECRET` anlegen.
2. `npm run build`
3. `npm test`
4. `npm run dev` startet die Vorschau auf `http://localhost:4173`.

Die Vorschau entfernt nur lokal das Secure-Cookie-Attribut für HTTP. Der Produktions-Worker setzt Secure, HttpOnly und SameSite=Strict. Nach Quelländerungen neu bauen und den Browser neu laden.

## Inhalte und Dateien

- `STORYBOARD.md`: Inhaltskonzept und didaktische Planung.
- `public/content.json`: strukturierte Teilnehmerinhalte.
- `public/app.js`, `public/style.css`: Darstellung und Interaktion.
- `public/material/`: Übungsdateien einschließlich XLSX, DOCX und ZIP.
- `scripts/content.py`: erzeugt Teilnehmerinhalte aus dem Storyboard mit redaktionellen Anpassungen.
- `scripts/materials.py`: erzeugt die Textdateien und Word-Vorlage; benötigt python-docx.
- `scripts/spreadsheet.mjs`: erzeugt die Excel-Datei mit dem Codex-Artifact-Tool; `ARTIFACT_TOOL_MODULE` muss auf dessen ESM-Einstieg zeigen.
- `scripts/build.mjs`: bündelt die statischen Dateien in einen Worker. Kein öffentlicher Asset-Bypass.
- `src/worker.js`: Passwortprüfung, signierte 12-Stunden-Sitzung, Login-Limit und geschützte Auslieferung.

`public/content.json` ist ein Artefakt mit redaktionellen Anpassungen. Bei Änderungen am Storyboard den Generator ausführen und das Ergebnis prüfen. Die Beispielanimationen enthalten eigene Teilnehmertexte in `public/app.js`.

## Veröffentlichung

`npm run build`, anschließend mit Cloudflare Wrangler oder dem Cloudflare-Connector deployen. Die Konfiguration steht in `wrangler.jsonc`.

Erforderliche Secret-Bindings: `WORKSHOP_PASSWORD`, `SESSION_SECRET`. Beide niemals in Git aufnehmen. Login-Limit: 60 Versuche pro Minute und IP, damit eine Gruppe hinter einer gemeinsamen Internetverbindung teilnehmen kann. Cloudflare erzwingt dieses Limit standortbezogen, nicht als globalen Zähler.

Passwortschutz gilt für die ausgelieferte Website und direkte Download-URLs. Dieses Repository ist öffentlich; seine fiktiven Lehrinhalte und Übungsdateien sind dadurch öffentlich lesbar. Geheimnisse gehören ausschließlich in Secret-Bindings.

Die automatisierten Tests prüfen geschützte Assets, Login, Cookies, abgelaufene/manipulierte Sitzungen, Cross-Origin-Schutz, Download-Dateien und die Inhaltsstruktur. Die tatsächlichen Work-Aktionen sind keine automatisierte Integration dieser Website.
