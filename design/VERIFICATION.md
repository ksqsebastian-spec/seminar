# Prüfung der veröffentlichten Präsentation

Stand: 23.09.2026. Veröffentlichung: https://seminar.ksqsebastian.workers.dev

## Gestaltung

Die Titelszene wurde im In-App-Browser bei 1672 × 941 Pixeln aufgenommen und mit `title-concept.png` über die Bildansicht verglichen. Die Excel-Demo wurde mit `example-concept.png` verglichen. Die fertige Titelszene ist in `preview.png` festgehalten. Die Konzeptbilder und Vorschau bleiben lokale Designartefakte, keine Website-UI aus Rasterbildern.

Geprüfte Vergleichspunkte:

1. Komposition: große linke Typografie, drei versetzte Farbflächen rechts, großzügiger Weißraum.
2. Typografie: lesbare Groteskschrift; anfangs zu enge Laufweite korrigiert und Schriftgewicht vereinheitlicht.
3. Palette: weiße Grundlage, fast schwarzer Text, Blau–Violett–Koralle-Verlauf im Titel, blaue/limettengrüne/korallfarbene Wortflächen.
4. Navigation: reduzierte Kopfzeile, Folienzähler, feine Fortschrittslinie, Vor-/Zurück-Steuerung.
5. Beispiel: Material- und Lieferkosten getrennt, grüner Entscheidungszustand, explizite Schrittsteuerung und Wiederholung.
6. Responsive: Titel und Farbflächen auf 390 × 844 Pixeln untereinander; ein Überlauf bei „Baustellenbesprechung“ wurde durch Wortumbruch behoben.
7. Bewegung: dezente Übergänge, vom Nutzer ausgelöste Beispielschritte, Unterstützung reduzierter Bewegung im Stylesheet.

Bewusste Umsetzungsanpassungen: zusätzliche Vollbildfunktion; erläuternde Schrittüberschrift in Beispielen; Titel-Unterzeile bei begrenzter Breite zweizeilig; native Arial/Helvetica-Typografie statt der nicht exakt spezifizierten Bildschrift. Alle Titeltexte und Navigationsbegriffe der Titelszene sind erhalten. Die Umsetzung folgt der festgelegten Keynote-Komposition und Farbgebung; eine pixelidentische Reproduktion der generierten Bilder wird nicht behauptet.

## Browser und Funktion

- In-App-Browser, keine Playwright-Ausweichlösung erforderlich.
- Alle 44 veröffentlichten Folien bei Desktopbreite ohne horizontalen Überlauf und mit Überschrift.
- Alle 44 Folien mobil geprüft; der einzige gefundene Überlauf wurde behoben und erneut geprüft.
- Kapitelsuche nach Excel, Auswahl einer Folie, Beispiel bis zur Entscheidung, kopierbarer Auftrag, Checkliste und Entdecken-Modus geprüft.
- Keine Browser-Konsolenfehler im abschließenden Live-Test.
- Lokale Tabellenprüfungen ergeben 1.330 €, 1.310 € und 1.350 €; keine Formel-Fehler im geprüften Workbook. Alle drei Tabellenblätter visuell geprüft.
- Word-Vorlage gerendert und die vollständige Seite visuell geprüft; Titel in Schwarz, kein dekorativer Titelstrich.

## Passwortschutz und Veröffentlichung

Sieben automatisierte Tests erfolgreich: geschützte Assets, erfolgreicher Login mit sicheren Cookie-Attributen, falsches Passwort/Cross-Origin-POST, Rate-Limit/fehlende Konfiguration, ungültige oder abgelaufene Sitzung, tatsächliche Office-/ZIP-Dateien, Inhaltsstruktur mit zehn Aufgaben.

Live per HTTPS zusätzlich bestätigt:

- Loginseite erreichbar, unautorisierte Inhalts- und Downloadaufrufe liefern 401.
- Korrektes Passwort führt mit 303 zur Präsentation.
- Authentifizierte Aufrufe von Inhaltsdaten, XLSX, DOCX und ZIP liefern 200 mit Dateiinhalten.
- Antworten verwenden `Cache-Control: no-store`.
- Passwort und Sitzungsschlüssel sind Secret-Bindings und nicht im Repository.

## Grenze der Prüfung

Die Lehrbeispiele sind fiktiv. Die Website führt selbst keine Microsoft-365-, Work-Browser-, Excel-Plugin- oder Scheduling-Aktionen aus. Verfügbarkeit und genaue Bedienung dieser Funktionen sind vor einem realen Workshop in den Teilnehmerkonten zu prüfen. Der öffentliche Repository-Inhalt ist unabhängig vom Passwortschutz der ausgelieferten Website öffentlich lesbar.
