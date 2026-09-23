# Ein Arbeitstag mit KI

Deutschsprachiger Anfängerworkshop für Handwerk und Bau: elf zusammenhängende Stationen: ein maßgefertigter Büroschrank für Hadi Teherani als fiktive Angebotsidee unseres Handwerksbetriebs. Empfohlen sind zwei Seminartage, jeweils 09–16 Uhr einschließlich Pausen.

Die Seminarleitung erklärt und demonstriert live. Teilnehmende arbeiten anschließend in ihrer eigenen Work- und Microsoft-365-Umgebung. Die Website verbindet keine Konten und führt keine KI-Aufträge aus.

Jede Station hat vier Abschnitte: Verstehen, gemeinsam ansehen, selbst machen, Ergebnis prüfen. Elf steuerbare Animationen zeigen das Prinzip jeder Station. Details und Beispielaufträge sind aufklappbar; eigene Aufgaben beginnen mit drei Schritten. Internetrecherche zu Person und öffentlichem Bürokontakt ist eine eigene Station. Die Browserübung zeigt echte Websiteaktionen: Baumarkt öffnen, Suche eingeben, Filter bedienen und Produkte prüfen. Verständnisfragen, ein Angebotsvergleich, eine Auftragshilfe und lokale Ergebnischecklisten bleiben verfügbar. Die Beameransicht vergrößert die Darstellung. Einrichtungspartner: ITP Consultants; Desktop-Installation: Kerim.

## Entwicklung

Node.js 20 oder neuer, keine Frontend-Abhängigkeiten erforderlich.

1. Eine lokale, nicht versionierte Datei `.dev.vars` mit `WORKSHOP_PASSWORD` und einem zufälligen `SESSION_SECRET` anlegen.
2. `npm run build`
3. `npm test`
4. `npm run dev` startet die Vorschau auf `http://localhost:4173`.

Die Vorschau entfernt nur lokal das Secure-Cookie-Attribut für HTTP. Der Produktions-Worker setzt Secure, HttpOnly und SameSite=Strict. Nach Quelländerungen neu bauen und den Browser neu laden.

## Inhalte und Dateien

- `CURRICULUM.md`: vollständiger Lernplan mit Lernzielen, Live-Vorführung, Übungen und Ergebniskriterien.
- `scripts/curriculum.py`: erzeugt `public/curriculum.json`, Lernplan und Material-ZIP. Nach Inhaltsänderungen ausführen.
- `public/day.js`, `public/day.css`: aktuelle Seminaroberfläche.
- `public/visuals.js`, `public/visual.css`: visuelle Lernschicht und steuerbare Animationen. Illustrationen sind als schematische Beispiele gekennzeichnet; echte Aufgaben bleiben in den eigenen Konten.
- `public/toolkit.js`: nach Funktionen gegliedertes Werkzeugwissen.
- `public/vorbereitung.html`: druckbare Vorbereitungsliste.
- `public/material/`: fiktive Übungsdateien einschließlich XLSX, DOCX und ZIP.
- `public/screens/SOURCES.md`: Quellen der Originalabbildungen.
- `public/referenz.html`: frühere Folienfassung; die aktuelle Hauptseite ersetzt sie. Alte Folienlinks werden auf passende Stationen umgeleitet.
- `scripts/build.mjs`: bündelt geschützte Assets in den Worker.
- `src/worker.js`: Passwortschutz und Sitzungen.

Frühere Generatoren `content.py`, `materials.py`, `spreadsheet.mjs` und `walkthroughs.py` bleiben für vorhandene Ausgangsmaterialien erhalten. Nach deren Verwendung den aktuellen Lernplan und die Vorbereitung redaktionell prüfen.

## Veröffentlichung

`npm run build`, anschließend mit Cloudflare Wrangler oder dem Cloudflare-Connector deployen. Die Konfiguration steht in `wrangler.jsonc`.

Erforderliche Secret-Bindings: `WORKSHOP_PASSWORD`, `SESSION_SECRET`. Beide niemals in Git aufnehmen. Login-Limit: 60 Versuche pro Minute und IP, damit eine Gruppe hinter einer gemeinsamen Internetverbindung teilnehmen kann. Cloudflare erzwingt dieses Limit standortbezogen, nicht als globalen Zähler.

Passwortschutz gilt für die ausgelieferte Website und direkte Download-URLs. Dieses Repository ist öffentlich; seine fiktiven Lehrinhalte und Übungsdateien sind dadurch öffentlich lesbar. Geheimnisse gehören ausschließlich in Secret-Bindings.

Die automatisierten Tests prüfen geschützte Assets, Login, Cookies, abgelaufene/manipulierte Sitzungen, Cross-Origin-Schutz, Download-Dateien und die Inhaltsstruktur. Die tatsächlichen Work-Aktionen sind keine automatisierte Integration dieser Website.

