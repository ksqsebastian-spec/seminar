# Ein Arbeitstag mit KI

Deutschsprachiger Anfängerworkshop für Handwerk und Bau: zehn zusammenhängende Kapitel: ein maßgefertigter Büroschrank für Hadi Teherani als fiktive Angebotsidee unseres Handwerksbetriebs. Ohne feste Tages- oder Zeitvorgaben.

Die Seminarleitung erklärt und demonstriert live. Teilnehmende arbeiten anschließend in ihrer eigenen ChatGPT- und Microsoft-365-Umgebung. Die Website verbindet keine Konten und führt keine KI-Aufträge aus.

Jedes Kapitel hat drei Abschnitte: Ziel und Ablauf, geführte Schritte, Ergebnis prüfen. Vorführung und eigenes Üben nutzen dieselben Anweisungen. Prompts sind direkt sichtbar und kopierbar. Logos und einfache Ablaufdiagramme verbinden die Werkzeuge. Die Beameransicht vergrößert die Darstellung. Einrichtungspartner: ITP Consultants; Desktop-Installation: Kerim.

## Entwicklung

Node.js 20 oder neuer, keine Frontend-Abhängigkeiten erforderlich.

1. Eine lokale, nicht versionierte Datei `.dev.vars` mit `WORKSHOP_PASSWORD` und einem zufälligen `SESSION_SECRET` anlegen.
2. `npm run build`
3. `npm test`
4. `npm run dev` startet die Vorschau auf `http://localhost:4173`.

Die Vorschau entfernt nur lokal das Secure-Cookie-Attribut für HTTP. Der Produktions-Worker setzt Secure, HttpOnly und SameSite=Strict. Nach Quelländerungen neu bauen und den Browser neu laden.

## Inhalte und Dateien

- `CURRICULUM.md`: vollständiger Lernplan mit Lernzielen, Live-Vorführung, Übungen und Ergebniskriterien.
- `scripts/curriculum.py`: erzeugt `public/curriculum.json`, `public/chapters.js`, Lernplan und Material-ZIP. Nach Inhaltsänderungen ausführen.
- `public/day.js`, `public/day.css`: aktuelle Seminaroberfläche.
- `public/storyboard.js`, `public/chapters.css`: animierbare Schaubilder, Ergebnisdateien und interaktive Beispielkalkulation. Echte Aufgaben bleiben in den eigenen Konten.
- `public/toolkit.js`: nach Funktionen gegliedertes Werkzeugwissen.
- `public/vorbereitung.html`: druckbare Vorbereitungsliste.
- `public/material/`: aktuelle Vorlage, Vorbereitung, Lernplan und ZIP; ältere Ausgangsmaterialien bleiben für bestehende Links erhalten.
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


## Aktuelles Storyboard
Kerim finden und eine Mail senden → Hadi recherchieren und Steckbrief erstellen → Projekt mit Steckbrief → OneDrive-Ordner, TXT und ergänzte Firmen-PDF → Browserrecherche als Excel → Kalkulation direkt in Excel für 1, 5 und 10 Schränke → Angebotsvorlage im Browser herunterladen und anhand der Kalkulation ausfüllen → Teppich-Screenshot mit Astra als Geschenkidee im Angebot → Kerim zu Weihnachten einladen → alle erstellten Dateien an Kerim senden.

Die Website führt keine Mail- oder Kalenderaktion selbst aus. Die Teilnehmer prüfen Empfänger und Dateien in ihren eigenen Konten. Hadi wird nicht kontaktiert. Reale Preise und Verfügbarkeit werden im Seminar recherchiert. Die interaktive Kalkulation zeigt ausdrücklich fiktive Beispielpreise.

Für das Angebot: fünf Schränke, zehn Arbeitsstunden je Schrank, zwei Stunden Einrichtung und Transport einmal je Auftrag. Quellenpreise müssen zur Materialeinheit passen. Keine technische Bauplanung.

Kapitelübersichten zeigen drei Stationen und das Ergebnis. Jeder Schritt hat ein animierbares Schaubild, eine konkrete Anweisung, einen kopierbaren Prompt oder eine Klickanleitung und eine Erfolgskontrolle. Bewegungen respektieren Reduced Motion. Der separate Übungsmodus bleibt entfernt.

Kleinanzeigen-Symbol: offizielles App-Icon von https://themen.kleinanzeigen.de/static/img/meta/apple-touch-icon.641bad4b6e0d.png
