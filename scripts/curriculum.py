"""Authoritative workshop storyboard. Regenerates web data and downloadable learning plan."""
import json, zipfile
from pathlib import Path
lessons=[]
chapters={}
stepApps={}
stepFiles={}
stepPlaces={}
def D(title, action, prompt, see, app='chatgpt', visual=None, asset=''):
 return dict(title=title,action=action,prompt=prompt,see=see,app=app,visual=visual or [],asset=asset)
def L(id,title,intro,before,after,flow,demos,checks):
 chapters[id]=dict(title=title,intro=intro,before=before,after=after,flow=flow)
 stepApps[id]=[d['app'] for d in demos]
 tools=list(dict.fromkeys(['chatgpt']+[d['app'] for d in demos]))
 lessons.append(dict(id=id,number=len(lessons)+1,title=title,short=intro,tools=tools,why=intro,story=intro,principle=title,outcome=after,skills=[d['title'] for d in demos],demos=demos,mission=intro,steps=[d['title'] for d in demos],checks=checks,hints=['Wenn etwas nicht klappt: Zeige den aktuellen Stand und beauftrage nur den nächsten Schritt. Fehlen Plugin oder Rechte, helfen Kerim und ITP Consultants.'],files=[],bonus='',carry=after,question=dict(ask='Ist dein Ergebnis geprüft?',options=['Ja, im echten Programm geöffnet.','Ich habe nur die Chatantwort gelesen.'],correct=0,explain='Öffne das Ergebnis im jeweiligen Programm.')))
L('antwort','Kerim eine Mail schreiben',
 'Wir finden Kerim in Outlook und schreiben ihm: Unser Schrankprojekt startet.',
 'Öffne ChatGPT. Das Outlook-Plugin ist verbunden.',
 'Kerim hat deine erste Mail. Jetzt finden wir heraus, wer Hadi Teherani ist.',
 [['outlook','Kerim finden'],['chatgpt','Mail schreiben'],['outlook','Mail senden']], [
 D('Finde Kerim.','Prüfe den vollständigen Namen und die gefundene Adresse.',
 'Nutze das Outlook-Plugin. Suche Kerim Seehafer in meinen Kontakten. Zeige Name und E-Mail-Adresse. Wenn du keinen eindeutigen Treffer findest, frage mich. Erfinde keine Adresse.',
 'Du hast Kerim Seehafers richtige Adresse. Falls er fehlt, fragst du ihn im Raum.','outlook', ['Kontakte','Kerim Seehafer','Adresse prüfen']),
 D('Schreib ihm kurz.','Lass einen Entwurf erstellen. Du kannst den Ton noch ändern.',
 'Nutze das Outlook-Plugin. Erstelle einen Mailentwurf an die geprüfte Adresse von Kerim Seehafer. Betreff: „Seminar – unser Schrankprojekt startet“. Schreibe locker: „Hallo Kerim, wir planen heute einen Schrank für Hadi Teherani. Ob er schon davon weiß? Noch nicht – aber wir legen los!“ Zeige mir den Entwurf vor dem Senden.',
 'Ein kurzer Entwurf an Kerim ist in Outlook gespeichert.','outlook',['Kerims Adresse','Kurze Mail','Entwurf']),
 D('Mach die Mail zu deiner.','Ändere einen Satz, öffne den Entwurf und prüfe den Empfänger.',
 'Nutze das Outlook-Plugin. Mach meinen Entwurf etwas kürzer und persönlicher. Behalte den Seminarbezug. Zeige mir Empfänger, Betreff und den neuen Text.',
 'Du hast Text und Empfänger geprüft.','outlook',['Entwurf','Deine Änderung','Prüfen']),
 D('Sende die erste Mail.','Die Mail geht wirklich an Kerim. Sende den gerade geprüften Entwurf.',
 'Nutze das Outlook-Plugin. Sende genau den von mir geprüften Seminarentwurf an Kerim Seehafer. Zeige mir danach die gesendete Mail.',
 'Die Mail steht unter „Gesendet“ und ist an Kerim adressiert.','outlook',['Geprüfter Entwurf','Senden','Gesendet'])],
 ['Kerims Adresse ist geprüft.','Meine erste Seminarmail steht unter Gesendet.'])
L('recherche','Hadi Teherani kennenlernen',
 'Eine einfache Frage wird zum Steckbrief: Wer ist Hadi, wie erreichen wir sein Büro und woher wissen wir das?',
 'Starte mit einer Frage in ChatGPT.',
 'Hadi_Steckbrief.txt liegt auf deinem Laptop. Diese Datei nehmen wir ins Projekt mit.',
 [['chatgpt','Wer ist Hadi?'],['chatgpt','Büro-Mail + Quelle'],['word','Steckbrief als TXT']], [
 D('Wer ist Hadi Teherani?','Lies die kurze Antwort und öffne eine Quelle.',
 'Wer ist Hadi Teherani? Recherchiere im Internet und erkläre mir in drei einfachen Sätzen, was er macht. Zeige die offiziellen Quellen dazu.',
 'Du kannst erklären, wer Hadi ist, und eine Quelle öffnen.',visual=['Eine Frage','Internetrecherche','Drei Sätze']),
 D('Finde seine Büro-Mail.','Prüfe auf der offiziellen Kontaktseite, wem die Adresse gehört.',
 'Finde die öffentlich angegebene geschäftliche E-Mail-Adresse von Hadi Teheranis Büro auf einer offiziellen Website. Gib mir den Quellenlink und die genaue Firmenbezeichnung. Sage dazu, ob es eine Büro-Adresse oder eine persönliche Adresse ist. Keine Adresse erraten.',
 'Eine öffentliche Büro-Adresse mit überprüfbarem Quellenlink.',visual=['Offizielle Website','Büro-Adresse','Quellenlink']),
 D('Erstelle den Steckbrief.','Lade die fertige Textdatei herunter. Wir verwenden sie gleich weiter.',
 'Erstelle aus unserer Recherche Hadi_Steckbrief.txt: Wer ist Hadi Teherani, was macht sein Büro, öffentliche Büro-Mail und Quellenlinks mit Abrufdatum. Halte es kurz. Kennzeichne unsere Schrankidee als Seminaridee. Gib mir die TXT-Datei zum Herunterladen.',
 'Hadi_Steckbrief.txt lässt sich auf deinem Laptop öffnen.',visual=['Fakten + Quellen','Steckbrief','TXT herunterladen'])],
 ['Die Büro-Mail ist an einer offiziellen Quelle geprüft.','Der Steckbrief ist als TXT heruntergeladen.'])
L('projekt','Ein Projekt für Hadi anlegen',
 'Wir legen eine gemeinsame Mappe in ChatGPT an und fügen unseren Steckbrief hinzu. Fertig.',
 'Halte Hadi_Steckbrief.txt aus dem letzten Kapitel bereit.',
 'Der Steckbrief liegt im Projekt „Schrank für Hadi“. Ab jetzt arbeiten wir dort weiter.',
 [['chatgpt','Neues Projekt'],['chatgpt','Schrank für Hadi'],['word','Steckbrief hinzufügen']], [
 D('Lege das Projekt an.','Öffne die Seitenleiste in ChatGPT. Wähle „Neues Projekt“ und nenne es „Schrank für Hadi“.','',
 'Du siehst „Schrank für Hadi“ in der Seitenleiste.',visual=['Seitenleiste','Neues Projekt','Namen eingeben'],asset='projects-sidebar.webp'),
 D('Füge deinen Steckbrief hinzu.','Öffne das Projekt. Wähle „Dateien hinzufügen“ und dann Hadi_Steckbrief.txt aus deinem Downloadordner.','',
 'Hadi_Steckbrief.txt ist als Projektdatei sichtbar.',visual=['Downloads','Hadi_Steckbrief.txt','Projekt'],asset='project-overview.webp')],
 ['Mein Projekt heißt „Schrank für Hadi“.','Mein recherchierter Steckbrief ist darin gespeichert.'])
L('dateien','Den Steckbrief in OneDrive ablegen',
 'ChatGPT legt einen Ordner an, speichert den Steckbrief, macht eine PDF daraus und ergänzt Informationen über die Firma.',
 'Öffne eine Aufgabe in deinem Projekt. Das OneDrive-Plugin ist verbunden.',
 'In „Seminar Schrank“ liegen die ursprüngliche TXT und der ergänzte Firmensteckbrief als PDF.',
 [['onedrive','Ordner + TXT'],['word','TXT → PDF'],['onedrive','Firmeninfos ergänzen']], [
 D('Lass den Ordner anlegen.','Öffne den Ordnerlink, den ChatGPT dir zeigt.',
 'Nutze das OneDrive-Plugin. Lege in meinem OneDrive den Ordner „Seminar Schrank“ an. Falls der Name schon existiert, frage mich. Zeige mir den Ordnerlink.',
 'Dein Ordner ist in OneDrive sichtbar.','onedrive',['OneDrive','Neuer Ordner','Seminar Schrank']),
 D('Speichere den Steckbrief.','Verwende die TXT aus dem Projekt. Falls ChatGPT sie nicht lesen kann, hänge sie an die Aufgabe an.',
 'Nutze das OneDrive-Plugin. Lade Hadi_Steckbrief.txt aus unserem Projekt unverändert in den gerade angelegten Ordner „Seminar Schrank“ hoch. Zeige mir die gespeicherte Datei.',
 'Die TXT liegt im richtigen OneDrive-Ordner.','onedrive',['Projekt-TXT','OneDrive-Plugin','TXT im Ordner']),
 D('Mach eine PDF daraus.','Öffne die PDF nach dem Speichern. Die TXT bleibt erhalten.',
 'Wandle Hadi_Steckbrief.txt in eine gut lesbare PDF namens Hadi_Steckbrief.pdf um. Nutze das OneDrive-Plugin, um sie in „Seminar Schrank“ zu speichern. Behalte die TXT und zeige mir den PDF-Link.',
 'Eine echte PDF lässt sich öffnen.','onedrive',['TXT','Format umwandeln','PDF']),
 D('Ergänze seine Firma.','Lass neue Fakten recherchieren und die PDF ergänzen.',
 'Recherchiere auf offiziellen Quellen mehr über die im Steckbrief genannte Firma: Tätigkeitsbereiche, Standort und zwei Beispielprojekte. Ergänze diese Angaben mit Quellen in unserem Steckbrief. Erstelle Hadi_Steckbrief_Firma.pdf. Nutze das OneDrive-Plugin zum Speichern in „Seminar Schrank“. Bestehende Dateien erhalten.',
 'Die neue PDF enthält einen kurzen Abschnitt zur Firma mit Quellen.','onedrive',['Neue Recherche','Firmenabschnitt','Ergänzte PDF'])],
 ['Der Ordner wurde von ChatGPT angelegt.','TXT und PDFs liegen in OneDrive.','Die ergänzten Firmeninfos haben Quellen.'])
L('browser','Material im Browser suchen',
 'ChatGPT sucht in einem echten Baumarkt. Aus den gefundenen Produkten entsteht unsere erste Excel-Datei.',
 'Unser Übungsentwurf: Büroschrank in Eiche-Optik, 120 × 180 × 45 cm. Noch kein fertiger Bauplan.',
 'Materialrecherche.xlsx liegt in OneDrive. Im nächsten Kapitel wird daraus unsere Kalkulation.',
 [['chatgpt','Baumarkt öffnen'],['chatgpt','Suchen + filtern'],['excel','Excel in OneDrive']], [
 D('Öffne den Baumarkt.','Beobachte, wie sich die Website im In-App-Browser öffnet.',
 'Öffne hornbach.de im In-App-Browser. Wir suchen Material für einen Büroschrank in Eiche-Optik.',
 'Du siehst die echte Baumarktseite.',visual=['ChatGPT','In-App-Browser','hornbach.de']),
 D('Suche und filtere.','ChatGPT soll die Website bedienen. Prüfe den sichtbaren Filter.',
 'Nutze das Suchfeld auf dieser Website: Suche Möbelbauplatte Eiche. Zeige die verfügbaren Filter und wende einen passenden sichtbaren Filter an. Fehlt er, frage mich.',
 'Die Suche und ein verfügbarer Filter sind auf der Website angewendet.',visual=['Suchfeld','Möbelbauplatte Eiche','Filter']),
 D('Prüfe zwei Produkte.','Öffne die Produktseiten. Vergleiche auch Maße und Preisbasis.',
 'Öffne zwei passende Produktseiten. Vergleiche Material, Maße, Preis, Einheit, Brutto oder Netto und Lieferkosten. Sichere Produktlinks und Abrufdatum. Fehlende Angaben offenlassen. Nichts bestellen.',
 'Zwei nachvollziehbare Produkte mit Quellen; Unterschiede bleiben sichtbar.',visual=['Produkt A','Vergleichen','Produkt B']),
 D('Erstelle die erste Excel.','Lass die Recherche als echte XLSX speichern.',
 'Erstelle Materialrecherche.xlsx mit den zwei Produkten: Name, Maße, Einheit, Preis, Brutto/Netto, Lieferkosten, Quellenlink und Abrufdatum. Nutze das OneDrive-Plugin und speichere die Excel-Datei in „Seminar Schrank“. Zeige mir den Link.',
 'Materialrecherche.xlsx liegt in OneDrive und lässt sich öffnen.','onedrive',['Produktdaten','Materialrecherche.xlsx','OneDrive'])],
 ['ChatGPT hat den In-App-Browser bedient.','Produktpreise, Einheiten und Quellen sind geprüft.','Die Excel-Datei liegt in OneDrive.'])
L('excel','Mehrere Schränke kalkulieren',
 'Aus unserer Recherche wird eine Kalkulation für 1, 5 und 10 Schränke – mit Material, Arbeitszeit, Transport und Angebotspreis.',
 'Materialrecherche.xlsx liegt in OneDrive. ChatGPT in Excel ist eingerichtet.',
 'Schrankkalkulation.xlsx enthält geprüfte Formeln und eine übersichtliche Gestaltung.',
 [['excel','Kalkulation erstellen'],['excel','1 · 5 · 10 Schränke'],['excel','Prüfen + gestalten']], [
 D('Erstelle die Kalkulation.','ChatGPT erstellt die Datei zuerst. Im nächsten Schritt öffnest du sie in Excel.',
 'Nutze das OneDrive-Plugin und lies Materialrecherche.xlsx aus „Seminar Schrank“. Erstelle Schrankkalkulation.xlsx mit einem Blatt Quellen und einem Blatt Kalkulation. Übernimm die recherchierten Produkte und kennzeichne offene Preise. Lege Eingabefelder für Schrankanzahl, Materialbedarf, Beschläge, Arbeitsstunden, Stundensatz, Transport, Aufschlag und Umsatzsteuer an. Speichere die XLSX im selben Ordner.',
 'Die neue Schrankkalkulation.xlsx ist in OneDrive gespeichert.','onedrive',['Materialrecherche','Kalkulation anlegen','Schrankkalkulation.xlsx']),
 D('Öffne Excel und ChatGPT.','Öffne Schrankkalkulation.xlsx in Excel. Öffne dort die eingerichtete ChatGPT-Erweiterung. Die nächsten Prompts kommen in diese Seitenleiste.','',
 'Du siehst die Tabelle und daneben ChatGPT in Excel.','excel',['OneDrive-Datei','In Excel öffnen','ChatGPT-Seitenleiste']),
 D('Rechne 1, 5 und 10 Schränke.','Diese Werte sind Übungsannahmen. Wähle zuvor eine passende Materialposition und prüfe deren Einheit.',
 'Arbeite in dieser geöffneten Excel-Datei. Nutze die geprüfte Netto-Materialposition aus dem Blatt Quellen. Rechne Szenarien für 1, 5 und 10 Schränke mit Formeln. Annahmen je Schrank: 8 Materialeinheiten, Beschläge 120 € netto, 8 Arbeitsstunden zu 65 € netto. Je Auftrag zusätzlich: 2 Stunden Einrichtung zu 65 € und 80 € Transport netto. Auf alle Kosten 20 % Aufschlag, danach 19 % Umsatzsteuer. Zeige Gesamtstunden, Kosten, Netto-/Brutto-Angebot und Stückpreis. Unbekannte Materialpreise nicht erfinden. Alle Eingaben veränderbar machen.',
 'Alle drei Szenarien rechnen mit Formeln. Einrichtung und Transport fallen je Auftrag nur einmal an.','excel',['1 Schrank','5 Schränke','10 Schränke']),
 D('Ändere und prüfe die Arbeitszeit.','Ändere einen Eingabewert und beobachte alle drei Szenarien.',
 'Ändere die Arbeitszeit je Schrank von 8 auf 10 Stunden. Prüfe alle Formeln für 1, 5 und 10 Schränke. Erkläre an einer Zeile die Rechnung. Einrichtung und Transport dürfen nicht pro Schrank vervielfacht werden. Wir wählen für unser Angebot das Szenario mit 5 Schränken.',
 'Die Szenarien reagieren auf die Änderung. Das Angebot verwendet 5 Schränke.','excel',['8 → 10 Stunden','Formeln rechnen neu','5 Schränke fürs Angebot']),
 D('Mach die Tabelle übersichtlich.','Lass Farben und Formate ändern, ohne die Berechnung anzutasten.',
 'Gestalte diese Arbeitsmappe übersichtlich: Eingabefelder helllila, Formelergebnisse hellgrün, Überschriften dunkel. Geldbeträge mit zwei Nachkommastellen und Eurozeichen. Hebe das Angebot für 5 Schränke hervor. Erhalte alle Werte und Formeln. Speichere die Datei am bestehenden OneDrive-Speicherort.',
 'Die farbige XLSX ist in OneDrive gespeichert. Formeln und Zahlen sind unverändert.','excel',['Lila: Eingaben','Grün: Ergebnisse','OneDrive speichern'])],
 ['1, 5 und 10 Schränke werden mit Formeln berechnet.','Einrichtung und Transport fallen einmal pro Auftrag an.','Für das Angebot sind 5 Schränke und 10 Stunden je Schrank gewählt.','Die gestaltete Datei ist in OneDrive gespeichert.'])
L('dokument','Die Angebotsvorlage ausfüllen',
 'ChatGPT lädt die Vorlage im Browser herunter und legt sie in OneDrive ab. Die Excel-Kalkulation liefert die Zahlen fürs Angebot.',
 'Schrankkalkulation.xlsx ist geprüft. Wir verwenden das Szenario mit 5 Schränken.',
 'Angebot_Hadi.docx und Angebot_Hadi.pdf liegen in OneDrive. Jetzt kommt ein kleines Extra dazu.',
 [['chatgpt','Vorlage herunterladen'],['excel','Mit Excel ausfüllen'],['onedrive','Word + PDF speichern']], [
 D('Lade die Vorlage im Browser herunter.','Lass ChatGPT die Materialseite dieser Seminarwebsite öffnen. Melde dich dort bei Bedarf selbst an.',
 'Öffne https://seminar.ksqsebastian.workers.dev/ im In-App-Browser. Öffne „Material“ und lade „Angebotsvorlage“ herunter. Wenn eine Anmeldung nötig ist, warte auf mich. Zeige mir die heruntergeladene DOCX-Datei.',
 '05-angebotsvorlage.docx ist heruntergeladen.',visual=['Seminarwebsite','Material','DOCX herunterladen']),
 D('Lade die Vorlage nach OneDrive.','Falls die heruntergeladene Datei für ChatGPT nicht erreichbar ist, hänge sie an die Aufgabe an.',
 'Nutze das OneDrive-Plugin. Lade die gerade heruntergeladene 05-angebotsvorlage.docx unverändert in „Seminar Schrank“ hoch. Zeige mir die Datei.',
 'Die leere Vorlage liegt in OneDrive.','onedrive',['Download','OneDrive-Plugin','Vorlage im Ordner']),
 D('Fülle sie anhand der Excel aus.','Verwende die tatsächliche Tabelle als Zahlenquelle.',
 'Nutze das OneDrive-Plugin. Lies Schrankkalkulation.xlsx, Hadi_Steckbrief_Firma.pdf und 05-angebotsvorlage.docx aus „Seminar Schrank“. Fülle die Vorlage für 5 Büroschränke anhand des gewählten Excel-Szenarios aus. Übernimm Mengen, Arbeitszeit und Netto-/Brutto-Summen exakt. Behalte die Vorlagenstruktur. Kennzeichne es als unverbindlichen Seminarentwurf, lasse unbekannte Angaben offen. Speichere als Angebot_Hadi.docx.',
 'Das Word-Angebot stimmt mit dem Szenario für 5 Schränke überein.','onedrive',['Excel + Steckbrief','Vorlage ausfüllen','Angebot_Hadi.docx']),
 D('Verbessere die Beschreibung.','Lass nur den Text kürzer und verständlicher machen.',
 'Kürze die Leistungsbeschreibung im Angebot. Beschreibe unsere 5 maßgefertigten Büroschränke freundlich und verständlich. Keine Zusagen erfinden. Mengen, Preise und Formeln nicht ändern. Nutze das OneDrive-Plugin zum Speichern von Angebot_Hadi.docx.',
 'Der Text ist klarer. Die geprüften Zahlen bleiben gleich.','onedrive',['Langer Text','Kürzer + klarer','Gleiche Zahlen']),
 D('Erzeuge die PDF.','Öffne Word und PDF und vergleiche Preis und Layout.',
 'Erzeuge aus der geprüften Angebot_Hadi.docx eine PDF. Nutze das OneDrive-Plugin und speichere Angebot_Hadi.pdf in „Seminar Schrank“. Behalte die Word-Datei und zeige beide Links.',
 'Word und PDF liegen in OneDrive und lassen sich öffnen.','onedrive',['Angebot.docx','PDF erzeugen','OneDrive'])],
 ['Die Vorlage wurde im In-App-Browser heruntergeladen.','Das Angebot übernimmt die geprüfte Excel-Kalkulation.','Word und PDF sind lesbar und in OneDrive gespeichert.'])
L('teppich','Ein Teppich als kleines Extra',
 'Wir finden einen Teppich auf Kleinanzeigen. Ein Screenshot unseres Favoriten kommt als Geschenkidee ins Angebot.',
 'Angebot_Hadi.pdf liegt in OneDrive. Wir suchen in Hamburg bis 200 € und ungefähr 200 × 300 cm.',
 'Angebot_Hadi_mit_Extra.pdf zeigt das Angebot und die Teppich-Geschenkidee mit Bild und Quelle.',
 [['kleinanzeigen','Teppich suchen'],['chatgpt','Screenshot machen'],['onedrive','Im Angebot ergänzen']], [
 D('Füge Kleinanzeigen hinzu.','Öffne in ChatGPT „Plugins“, suche „Kleinanzeigen“ und füge es hinzu. Ist es bereits eingerichtet, gehe weiter.','',
 'Kleinanzeigen ist in deinem Konto verfügbar.','kleinanzeigen',['Plugins','Kleinanzeigen','Hinzufügen']),
 D('Suche und verfeinere.','Wähle einen Favoriten. Du kannst Farbe oder Budget mit einer Folgefrage ändern.',
 'Nutze das Kleinanzeigen-Plugin. Suche drei schlichte Teppiche in Hamburg, maximal 200 € und ungefähr 200 × 300 cm. Zeige Preis, Maße, Zustand und Link. Bevorzuge helle, einfarbige Teppiche. Fehlende Angaben offenlassen. Nichts kaufen und niemanden anschreiben.',
 'Du hast einen Favoriten aus echten Anzeigen gewählt.','kleinanzeigen',['Drei Anzeigen','Farbe + Maße prüfen','Ein Favorit']),
 D('Lass Astra einen Screenshot machen.','Wechsle für diesen Schritt im Modellmenü auf GPT-6 Astra. Füge den Link deines Favoriten ein.',
 'Öffne diese Anzeige im In-App-Browser: [ANZEIGENLINK EINFÜGEN]. Prüfe Preis, Maße und Zustand. Erstelle einen Screenshot des Teppichbildes ohne private Verkäuferdaten. Nutze das OneDrive-Plugin und speichere ihn als Teppich_Favorit.png in „Seminar Schrank“. Bewahre den Anzeigenlink als Quelle. Nichts kaufen und niemanden anschreiben.',
 'Der Screenshot zeigt den gewählten Teppich und liegt in OneDrive.',visual=['Astra + Browser','Teppichbild','Screenshot.png']),
 D('Baue das Geschenk ins Angebot ein.','Lass eine kleine Zusatzseite ergänzen. Prüfe, dass die Kalkulation gleich bleibt.',
 'Nutze das OneDrive-Plugin. Ergänze Angebot_Hadi.docx um eine kleine Seite „Ein Extra fürs Büro“ mit Teppich_Favorit.png, Anzeigenlink und Abrufdatum. Text: „Unsere Geschenkidee zum Schrank – vorbehaltlich Verfügbarkeit. Seminarvorschlag, noch nicht gekauft.“ Weise das Extra mit 0 € für den Empfänger aus; ändere die bisherigen Angebotssummen nicht. Speichere Angebot_Hadi_mit_Extra.docx und Angebot_Hadi_mit_Extra.pdf in „Seminar Schrank“. Behalte die bisherigen Versionen.',
 'Die neue PDF enthält das Teppichbild, die Quelle und den Geschenkhinweis.','onedrive',['Screenshot','Geschenkseite','Angebot mit Extra'])],
 ['Der Screenshot zeigt den richtigen Teppich.','Die PDF enthält Bild und Quellenlink.','Das Extra ist als Geschenkidee gekennzeichnet; nichts wurde gekauft.'])
L('kalender','Kerim zu Weihnachten einladen',
 'Wir planen eine Schrankbesprechung am 25. Dezember und laden Kerim Seehafer dazu ein.',
 'Kerims Adresse ist aus der ersten Mail bekannt. Die Einladung geht wirklich an ihn.',
 'Der Termin steht in deinem Kalender und Kerim ist eingeladen.',
 [['outlook','Kalender prüfen'],['outlook','Kerim hinzufügen'],['outlook','Einladung senden']], [
 D('Prüfe den Weihnachtstag.','Prüfe Datum, Uhrzeit und das verwendete Konto.',
 'Nutze das Outlook-Plugin. Zeige meinen Kalender am 25.12.2026 in Europe/Berlin. Wir planen 10:00–10:30 Uhr. Zeige mögliche Konflikte.',
 'Du siehst den richtigen Tag und mögliche Überschneidungen.','outlook',['25. Dezember','10:00–10:30','Kalender prüfen']),
 D('Bereite Kerims Einladung vor.','Prüfe Kerims Adresse nochmals, bevor die Einladung rausgeht.',
 'Nutze das Outlook-Plugin. Bereite einen Termin am 25.12.2026 von 10:00 bis 10:30 Uhr, Europe/Berlin, vor. Titel: „Seminar – Schrankbesprechung an Weihnachten“. Lade ausschließlich Kerim Seehafer über die bereits geprüfte Adresse ein. Beschreibung: „Unser Seminarprojekt: Schränke und ein Teppich-Extra.“ Zeige mir Datum, Empfänger und Text, bevor du die Einladung sendest.',
 'Der Termin und Kerims Adresse sind zur Prüfung sichtbar.','outlook',['Datum + Titel','Kerims Adresse','Vor Versand prüfen']),
 D('Sende die Einladung.','Die echte Einladung geht nur an Kerim.',
 'Nutze das Outlook-Plugin. Erstelle den gerade geprüften Termin und sende die Einladung an Kerim Seehafer. Zeige mir anschließend den Kalendereintrag mit Teilnehmern.',
 'Der Termin ist vorhanden und Kerim steht als eingeladener Teilnehmer darin.','outlook',['Geprüfter Termin','Einladen','Kalendereintrag'])],
 ['Datum, Zeitzone und Kerims Adresse stimmen.','Kerim ist als Teilnehmer eingeladen.'])
L('spaeter','Alles fertig, Kerim!',
 'Zum Abschluss bekommt Kerim unser fertiges Paket per Mail – mit allen im Seminar erstellten Dateien als Anhang.',
 'Alle Ergebnisse liegen im Ordner „Seminar Schrank“. Keine Dateien aus anderen Ordnern verwenden.',
 'Kerim hat deine Abschlussmail mit den geprüften Dateien. Dein Projekt ist vollständig übergeben.',
 [['onedrive','Dateien sammeln'],['outlook','Anhängen + prüfen'],['outlook','An Kerim senden']], [
 D('Sammle unser Paket.','Prüfe die Liste. Dazu gehören Steckbrief, Excel-Dateien, Angebote und Teppichbild.',
 'Nutze das OneDrive-Plugin. Liste alle von uns in diesem Seminar erstellten Dateien aus „Seminar Schrank“ mit Name, Dateityp und Größe auf. Dazu gehören Steckbrief-TXT und PDFs, Materialrecherche.xlsx, Schrankkalkulation.xlsx, unsere erstellten Angebots-DOCX und PDFs sowie Teppich_Favorit.png. Keine fremden Dateien und keine unveränderte leere Vorlage. Zeige mir die Liste vor dem Anhängen.',
 'Du hast eine vollständige Dateiliste geprüft.','onedrive',['Seminar Schrank','Erstellte Dateien','Liste prüfen']),
 D('Erstelle die Abschlussmail.','Lass alle geprüften Dateien tatsächlich anhängen. Öffne den Entwurf in Outlook.',
 'Nutze das OneDrive-Plugin zum Laden der gerade geprüften Dateien und das Outlook-Plugin für die Mail. Erstelle einen Entwurf an Kerim Seehafers geprüfte Adresse. Betreff: „Alles fertig, Kerim – Schränke und Teppich inklusive“. Schreibe locker: „Hallo Kerim, alles fertig! Recherche, Kalkulation und Angebot sind im Anhang. Sogar eine Teppich-Geschenkidee ist dabei. Unser Seminarprojekt kann sich sehen lassen!“ Hänge alle Dateien aus der bestätigten Liste als echte Dateianhänge an. Zeige Empfänger, Text und Anhangsliste. Noch nicht senden.',
 'Der Outlook-Entwurf enthält die richtigen Dateien als Anhänge.','outlook',['Geprüfte Dateien','Mailentwurf','Echte Anhänge']),
 D('Sende das fertige Paket.','Vergleiche Anhänge und Dateiliste. Öffne mindestens die finale PDF und die Kalkulation. Dann sende.',
 'Nutze das Outlook-Plugin. Sende genau die von mir geprüfte Abschlussmail mit allen bestätigten Anhängen an Kerim Seehafer. Zeige mir die gesendete Nachricht mit Anhangsliste. Bei einer Fehlermeldung zuerst den Versandstatus prüfen, nicht blind erneut senden.',
 'Die Abschlussmail steht mit ihren Anhängen unter „Gesendet“.','outlook',['Empfänger + Anhänge prüfen','Senden','Alles fertig, Kerim!'])],
 ['Alle im Seminar erstellten Dateien sind angehängt.','Die finale Angebots-PDF und die Excel-Datei lassen sich öffnen.','Die Abschlussmail steht unter Gesendet.'])
lessons[-1]['hints']=['Fehlt eine Datei, hole sie zuerst in den Seminarordner. Keine fremden Dateien ergänzen.','Kann das Plugin einen Anhang nicht laden oder ist er zu groß? Lade die bestätigten Dateien herunter und hänge sie selbst in Outlook an. Prüfe die vollständige Liste; nichts stillschweigend weglassen.','Bei einem Versandfehler zuerst Gesendet und den Entwurf prüfen. Nicht blind doppelt senden.']
stepPlaces['excel']={2:'In ChatGPT direkt in Excel eingeben',3:'In ChatGPT direkt in Excel eingeben',4:'In ChatGPT direkt in Excel eingeben'}
plan=dict(title='Ein Schrank für Hadi.',subtitle='Von der ersten Mail bis zum fertigen Angebot.',case='Schrank für Hadi',promise='Du recherchierst, bearbeitest Dateien, kalkulierst und übergibst dein Angebot.',environment='Du arbeitest in deinem eigenen ChatGPT und Microsoft 365. Das Schrankangebot ist ein Seminarprojekt. Mails und Termineinladung gehen wirklich an Kerim Seehafer; Hadi Teherani wird nicht kontaktiert.',lessons=lessons,schedule=[],glossary={'Projekt':'Deine Mappe in ChatGPT für dieses Vorhaben.','Plugin':'Verbindet ChatGPT mit einem Programm. Nenne es im Auftrag beim Namen.','Recherche':'Informationen suchen und an Quellen prüfen.','Browseraktion':'ChatGPT öffnet Websites, tippt und klickt.','Entwurf':'Eine Mail, die noch nicht gesendet wurde.','DOCX':'Eine bearbeitbare Word-Datei.','PDF':'Ein Dokument zum Lesen und Weitergeben.','XLSX':'Eine Excel-Datei mit Tabellen und Formeln.','Screenshot':'Ein Bild vom sichtbaren Bildschirminhalt.','Annahme':'Ein Übungswert, kein bestätigter Kundenwunsch.'})
Path('public/curriculum.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2))
Path('public/chapters.js').write_text('// Generated by scripts/curriculum.py.\n'+''.join('export const '+name+'='+json.dumps(value,ensure_ascii=False)+';\n' for name,value in [('chapters',chapters),('stepApps',stepApps),('stepFiles',stepFiles),('stepPlaces',stepPlaces)]))
md=['# Ein Schrank für Hadi','',plan['subtitle'],'',plan['environment'],'','## So arbeiten wir','Kerim zeigt den Schritt. Du führst ihn in deiner eigenen Umgebung aus und prüfst das Ergebnis. Nenne Plugins ausdrücklich beim Namen.','']
for l in lessons:
 md+=['## '+str(l['number'])+'. '+l['title'],l['story'],'']
 for i,d in enumerate(l['demos'],1):
  md += [str(i)+'. '+d['title'],d['action']]+(['Auftrag: '+d['prompt']] if d['prompt'] else [])+['Prüfen: '+d['see'],'']
 md+=['Danach: '+l['outcome'],'']
for f in ['CURRICULUM.md','public/material/11-lernplan.txt']:Path(f).write_text('\n'.join(md))
print('10 Kapitel mit durchgängigem Dateifluss erstellt.')

with zipfile.ZipFile('public/material/workshop-material.zip','w',zipfile.ZIP_DEFLATED) as z:
 for n in ['00-vorbereitung.txt','05-angebotsvorlage.docx','11-lernplan.txt']:z.write('public/material/'+n,n)
