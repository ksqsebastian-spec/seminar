// Verified exposed plugin actions, phrased as user tasks rather than API names.
export const toolkit=[
{name:'ChatGPT & Projekte',app:'chatgpt',intro:'Hier organisierst du den Auftrag, gibst Kontext mit und steuerst nach. Prüfe Funktionen und Bezeichnungen in deiner eigenen Oberfläche.',items:[
['Auftrag starten','Nenne Ziel, Quelle, Ausgabe und Kontrollpunkt.','Fasse diese Anfrage in drei einfachen Sätzen zusammen. Nenne offene Angaben.','Die Antwort passt zur ausgewählten Quelle.'],
['Im Gespräch nachsteuern','Ändere die vorhandene Antwort mit einer Folgefrage.','Bitte kürzer und ohne Fachwörter. Ändere die bestätigten Fakten nicht.','Inhalt bleibt richtig, Sprache passt.'],
['Projekt anlegen','Ein Projekt pro zusammengehörigem Auftrag.','Lege selbst „Schrank für Hadi“ über Neues Projekt an.','Projekt ist in der Seitenleiste sichtbar.'],
['Quellen und Vorgaben wiederverwenden','Dateien gehören in die Projektquellen, dauerhafte Regeln in die Projekthinweise.','Keine erfundenen Maße, Preise oder Termine. Fehlende Angaben als offen markieren.','Quelle und Vorgabe sind im richtigen Projekt gespeichert.'],
['Fehler beheben','Benenne die konkrete falsche Stelle. Lass den Rest erhalten.','Auf Seite 1 steht drei Türen. Die aktuelle Anfrage nennt zwei. Korrigiere das und benenne den Quellenkonflikt.','Geänderte Stelle an der Quelle prüfen.'],
['Browser steuern','Kleine, überprüfbare Schritte; Handlungen explizit benennen.','Öffne die Maßtabelle auf dieser Seite und erkläre sie. Nichts bestellen.','Die sichtbare Seite zeigt die gesuchte Information.'],
['Erinnerung und Wiederholung','Zeit, Zeitzone, Quelle, Ergebnis und Endpunkt nennen. Verfügbarkeit ist kontoabhängig.','Zeige die Einrichtung einer Montagszusammenfassung um 08:30 Uhr für vier Wochen, Europe/Berlin.','Gespeicherte Aufgabe öffnen und nach der Übung deaktivieren.']
]},
{name:'Outlook Mail',app:'outlook',intro:'Die Grundübung endet mit einem ungesendeten Entwurf an Kerims zuvor geprüfte Adresse. Funktionen hängen von Konto, Plugin und Freigaben ab.',items:[
['Finden und auswählen','Suche nach Datum, Absender, Betreff oder Anhang. Wähle bei mehreren Treffern erst die richtige Mail.','Zeige meine heutigen Mails mit Absender und Betreff.','Richtige Mail und richtiges Konto.'],
['Lesen und erklären','Lass Inhalt, gewünschte Handlung und offene Fragen trennen.','Was möchte der Absender von mir, und welche Angaben fehlen?','Mit Originalmail vergleichen.'],
['Anhänge lesen','Benenne die konkrete Datei, statt pauschal alle Anhänge zu verwenden.','Erkläre mir den Anhang Projektbrief.pdf aus dieser Mail.','Dateiname, Inhalt und Bezug zur Mail stimmen.'],
['Antworttext verbessern','Erst in ChatGPT formulieren und überarbeiten.','Kürzer, freundlich und mit Sie. Keine neuen Zusagen.','Fakten und Ton prüfen.'],
['Entwurf speichern','Neuer Entwurf oder Antwortentwurf auf eine konkrete Mail. Ein Chattext ist noch kein Outlook-Entwurf.','Speichere den geprüften Text als Übungsentwurf an Kerims zuvor geprüfte Adresse. Noch nicht senden.','Im Outlook-Ordner Entwürfe öffnen.'],
['Datei anhängen','Direkte Plugin-Anhänge unter 3 MB. Bei fehlender Funktion selbst in Outlook anhängen.','Hänge diese geprüfte PDF an genau diesen Entwurf an.','Richtigen Anhang im Entwurf öffnen.'],
['Antwort-an-alle und Weiterleiten','Prüfe alle Empfänger. Weiterleiten kann Inhalte und Anhänge an neue Personen geben.','Zeige zuerst, wer die Antwort erhalten würde. Noch nicht versenden.','An und CC sind passend; kein ungewollter Empfänger.','Vertiefung'],
['Senden und später senden','Beides sind echte Handlungen. Eine geplante Mail kann ohne weiteres Zutun versendet werden.','Zeige Empfänger, Text, Anhang und Versandzeit zur Kontrolle.','Erst nach explizitem Auftrag ausführen; Übung höchstens an eigene Adresse.','Vertiefung'],
['Ordnen','Gelesen/ungelesen markieren, Kategorie setzen oder in einen eigenen Übungsordner verschieben.','Verschiebe nur meine ausgewählte Übungsmail in den Ordner Seminar.','Im Zielordner prüfen.','Vertiefung']
]},
{name:'OneDrive',app:'onedrive',intro:'Die Verbindung kann als OneDrive oder über SharePoint angeboten werden. Ein Plugin sucht und speichert Dateien; ChatGPT bearbeitet den Inhalt. Der verfügbare Zugriff muss zum Zielordner passen.',items:[
['Ordner anlegen','Eigener Übungsordner, eindeutig benannt.','Lege in meinem OneDrive einen Ordner Seminar Schrank an.','Ordner im richtigen Konto öffnen.'],
['Suchen und öffnen','Dateiname plus Ordner schränkt die Suche sinnvoll ein.','Finde 03-lindenhof.txt in meinem Übungsordner.','Datei öffnen, Datum und Inhalt vergleichen.'],
['Hochladen und speichern','Eine lokale oder von ChatGPT erzeugte Datei gezielt ablegen.','Speichere die geprüfte PDF in Seminar Schrank. Nichts überschreiben.','Gespeicherte Datei in OneDrive öffnen.'],
['Umbenennen und verschieben','Eindeutigen Quellnamen und Zielordner nennen.','Benenne nur die neue Kopie in Schrank_Projektbrief_v2.docx um.','Neuer Name, richtiger Ordner, Original erhalten.'],
['Kopieren und Versionen','Vor größeren Änderungen eine Kopie verwenden. Ersetzen kann den vollständigen Dateiinhalt überschreiben.','Erstelle zuerst eine Kopie. Bearbeite nur diese Kopie.','Original und neue Fassung sind unterscheidbar.'],
['Freigaben prüfen','Zugriff für benannte Personen und öffentliche Links sind nicht dasselbe.','Zeige die vorhandenen Freigaben dieser Übungsdatei. Ändere noch nichts.','Keine unbeabsichtigte öffentliche Freigabe.','Vertiefung'],
['Aufräumen oder Version zurückholen','Nur eindeutig benannte eigene Übungsdateien löschen oder eine gezielt geprüfte Version wiederherstellen.','Zeige zuerst die Versionshistorie, bevor eine Fassung wiederhergestellt wird.','Richtige Datei und Version prüfen.','Vertiefung']
]},
{name:'Outlook Kalender',app:'outlook',intro:'Die Grundübung verwendet einen Einzeltermin im eigenen Kalender ohne Gäste. Bei echten Einladungen können Änderungen und Absagen Nachrichten auslösen.',items:[
['Kalender und Termine lesen','Kalender, Datum und Zeitzone klären.','Zeige meine Termine am gewählten Tag in Europe/Berlin.','Der richtige Kalender und konkrete Daten.'],
['Freie Zeit finden','Dauer und Zeitfenster nennen; unbekannte Kalender nicht als frei annehmen.','Finde 45 freie Minuten zwischen 09:00 und 15:00 Uhr.','Konflikte und Fahrtzeit selbst prüfen.'],
['Termin anlegen','Titel, Anfang, Ende, Ort, Agenda und Teilnehmer bewusst festlegen.','Lege nach meiner Prüfung einen Übungstermin ohne weitere Teilnehmer an.','Im eigenen Outlook-Kalender öffnen.'],
['Verschieben und bearbeiten','Den bestehenden Termin eindeutig identifizieren.','Verschiebe genau ÜBUNG Schrank auf das neue freie Fenster. Dauer beibehalten.','Ein geänderter Termin, kein Duplikat.'],
['Entfernen oder absagen','Löschen im eigenen Kalender und Absage an Gäste unterscheiden.','Entferne nur meinen Übungstermin ohne Teilnehmer.','Nur die Übung wurde entfernt.'],
['Wiederholung','Bei Änderungen immer einzelne Instanz oder gesamte Serie klären.','Zeige zuerst die geplante Serie mit Ende und Ausnahmen.','Umfang der Änderung prüfen.','Vertiefung'],
['Einladungen beantworten','Zusagen, vorläufig oder ablehnen können eine Rückmeldung senden.','Zeige die Einladung und mögliche Antwortoptionen. Noch keine Rückmeldung senden.','Beteiligte und Rückmeldung bewusst prüfen.','Vertiefung'],
['Datei zum Termin','Nur die relevante kleine Datei an einen eigenen Termin hängen.','Hänge den geprüften Besichtigungsbrief an diesen eigenen Übungstermin an.','Anhang am richtigen Termin öffnen.','Vertiefung']
]},
{name:'Dateien & Excel',app:'excel',intro:'Dateiformat, Inhalt und Speicherort getrennt betrachten. Manche PDF-Layouts oder Formatkonvertierungen brauchen einen zweiten Versuch. Du öffnest die Ausgabe immer selbst.',items:[
['Datei hochladen','Plus am Eingabefeld, Datei auswählen, Dateinamen prüfen.','Verwende genau diese hochgeladene Datei.','Die richtige Datei ist zugeordnet.'],
['Vorlage ausfüllen','Vorlage und Quellen gemeinsam übergeben.','Fülle nur belegte Felder. Behalte die Struktur.','Keine erfundenen Angaben.'],
['Inhalt ändern','Abschnitt, gewünschte Änderung und unveränderte Teile benennen.','Ändere nur den Abschnitt Offene Fragen.','Original erhalten und neue Version prüfen.'],
['DOCX und PDF','Bearbeitbare Word-Datei plus lesbare Weitergabefassung.','Erzeuge zusätzlich eine PDF. Behalte die DOCX.','Beide öffnen; Layout und Inhalt vergleichen.'],
['Tabelle erklären und bereinigen','Blatt, Spalten und Datentypen klären.','Bereinige Schreibweisen und Zahlen in einer Kopie.','Summe und Originaldaten prüfen.'],
['Formeln und Szenarien','Rechenregel und Annahmen benennen.','Menge mal Stückpreis plus Lieferung. Vergleiche 8 und 10 Arbeitsstunden.','Eine Zeile nachrechnen; Ergebniswechsel verstehen.'],
['Direkt in Excel arbeiten','Die eingerichtete ChatGPT-Erweiterung nutzt die geöffnete Arbeitsmappe.','Erkläre zuerst die geplante Änderung der ausgewählten Tabelle.','Geänderte Zellen und Speicherung prüfen.'],
['XLSX und CSV','CSV ist eine einfache Tabelle; mehrere Blätter, Gestaltung und Formeln werden nicht wie in XLSX erhalten.','Exportiere nur die Ergebnistabelle als CSV und behalte die XLSX.','Richtige Tabelle, Trennzeichen und Zahlen prüfen.','Vertiefung']
]}];

// Reinforce naming the connected service in every plugin example.
for (const tool of toolkit) {
 const plugin = {outlook: "Outlook", onedrive: "OneDrive"}[tool.app];
 if (plugin) for (const item of tool.items) item[2] = `Nutze dafür das ${plugin}-Plugin. ${item[2]}`;
}
