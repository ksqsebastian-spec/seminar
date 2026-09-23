"""One seminar case: a cabinet proposal for Hadi Teherani, never a real customer order."""
import json, zipfile
from pathlib import Path

def demo(title,action,prompt='',see='',asset=''):
 return dict(title=title,action=action,prompt=prompt,see=see,asset=asset)
def lesson(id,title,short,tools,minutes,principle,story,outcome,skills,demos,mission,steps,checks,hints,question,files,bonus,carry):
 return dict(id=id,title=title,short=short,tools=tools,minutes=minutes,why=story,principle=principle,story=story,outcome=outcome,skills=skills,demos=demos,mission=mission,steps=steps,checks=checks,hints=hints,question=question,files=files,bonus=bonus,carry=carry)
def q(ask,a,b,correct,explain):return dict(ask=ask,options=[a,b],correct=correct,explain=explain)
brief='03-schrankbrief.txt';sheet='04-schrankkalkulation.xlsx';template='05-angebotsvorlage.docx';browserfile='09-recherche-und-browser.txt';change='10-aenderung-und-uebergabe.txt';term='07-weihnachtstermin.txt'
lessons=[
lesson('antwort','Kerim, wir haben Großes vor!', 'Korrespondenz suchen, Kontakt finden, Entwurf mit Anhang.',['chatgpt','outlook'],55,
 'Erst suchen. Dann Kerim einweihen.',
 'Wir prüfen, ob es im eigenen Postfach schon Korrespondenz mit Hadi Teherani oder seinem Büro gibt. Danach finden wir Kerims Kontakt und bereiten eine lockere interne Mail mit Mission_Hadi.pdf vor. Die angekündigte Zusammenarbeit ist unser Seminar-Rollenspiel, keine bestätigte Zusage.',
 'Ein ungesendeter Outlook-Entwurf an den geprüften Kontakt Kerim mit Mission_Hadi.pdf.',
 ['Posteingang und gesendete Mails durchsuchen','Treffer lesen und keinen Treffer ehrlich benennen','Kerims Kontakt finden und E-Mail-Adresse prüfen','Eine einseitige PDF aus Projektangaben erstellen','Humorvollen Mailtext überarbeiten','Entwurf mit tatsächlichem Dateianhang in Outlook prüfen'],
 [demo('Gab es schon Kontakt?','Suche im eigenen Postfach, auch in gesendeten Nachrichten. Lies passende Treffer; eine Namensnennung allein ist noch keine Korrespondenz mit seinem Büro.','Suche in meinen empfangenen und gesendeten Mails nach Hadi Teherani oder Hadi Tehrani. Zeige passende Nachrichten und fasse sie kurz zusammen. Wenn du nichts findest, sage mir, wo du gesucht hast. Erfinde keine Korrespondenz.','Passende Korrespondenz oder ein klarer Hinweis: Im durchsuchten Bereich nichts gefunden.'),
 demo('Finde Kerims Kontakt.','Lass gespeicherte Kontakte durchsuchen. Falls der Zugriff fehlt, kann eine frühere Mail helfen. Bei mehreren Treffern wählst du die richtige Person.','Suche Kerim in meinen Outlook-Kontakten. Zeige Name und E-Mail-Adresse. Frage mich bei mehreren Treffern. Wenn du keinen Kontakt findest, sage das. Erfinde keine Adresse.','Der richtige Kerim und seine Adresse sind geprüft. Fehlt der Kontakt, fragst du Kerim im Raum.'),
 demo('Mach eine Mission-PDF.','Lade zuerst 03-schrankbrief.txt aus den Übungsdateien in ChatGPT hoch. Erstelle daraus eine Seite und lade die PDF auf deinen Laptop herunter. Öffne sie vor dem Anhängen.','Erstelle aus dem hochgeladenen Schrankbrief eine Seite als Mission_Hadi.pdf: unsere Schrankidee, angenommene Maße und drei offene Fragen. Ohne Preise. Schreibe dazu: „Seminar-Rollenspiel, keine bestätigte Zusammenarbeit“. Gib mir die PDF zum Herunterladen.','Die heruntergeladene PDF lässt sich auf deinem Laptop öffnen.'),
 demo('Weihe Kerim ein.','Lass einen lockeren, kurzen Text schreiben und verbessere ihn. Echte Suchergebnisse und unser Rollenspiel bleiben unterscheidbar.','Entwirf eine kurze, lustige Mail an Kerim: „Wir arbeiten jetzt mit Hadi Teherani! Zumindest im Seminar – seine Zusage fehlt noch.“ Ergänze das echte Ergebnis unserer Mailsuche und erwähne Mission_Hadi.pdf. Betreff: „ÜBUNG – Wir haben Großes vor!“. Noch nicht senden.','Ein humorvoller Text, den du kürzen oder persönlicher machen lassen kannst.'),
 demo('Speichere den Entwurf mit Anhang.','Verwende den geprüften Kontakt Kerim. Wenn der Kontakt noch offen ist, kläre ihn zuerst. Anhangsfunktion prüfen; falls nötig die PDF direkt in Outlook anhängen.','Speichere den überarbeiteten Text als Outlook-Entwurf an die zuvor geprüfte E-Mail-Adresse von Kerim. Hänge die in dieser Aufgabe erstellte und geprüfte Datei Mission_Hadi.pdf an. Keine anderen Empfänger. Nicht senden.','Der Entwurf ist in Outlook sichtbar, an Kerim adressiert und enthält die PDF.'),
 demo('Öffne und prüfe alles.','Öffne den Entwurf in Outlook. Prüfe Kerims Adresse, den Rollenspiel-Hinweis und öffne den tatsächlichen Anhang.',see='Richtiger Empfänger, richtige PDF und weiterhin ungesendet.')],
 'Suche nach Hadi-Korrespondenz, finde Kerim und entwirf ihm eine lockere Projektmail mit Mission_Hadi.pdf.',
 ['Korrespondenz suchen und Kerims Kontakt prüfen.','Schrankbrief hochladen, Mission_Hadi.pdf erstellen und öffnen.','Mailtext verbessern, als Entwurf an Kerim speichern und PDF anhängen.'],
 ['Die Korrespondenzsuche ist belegt oder als erfolglos im durchsuchten Bereich benannt.','Kerims Name und E-Mail-Adresse sind geprüft.','Die Zusammenarbeit ist als Seminar-Rollenspiel erkennbar.','Mission_Hadi.pdf hängt tatsächlich an und lässt sich öffnen.','Die Mail bleibt ungesendet.'],
 ['Kein Suchtreffer ist ein gültiges Ergebnis. Nicht behaupten, es habe niemals Kontakt gegeben.','Mehrere Kerims? Vollständigen Namen und Adresse vergleichen. Kein Kontakt? Kerim im Raum fragen.','Bei fehlender Anhangsfunktion die geprüfte PDF direkt in Outlook ergänzen.'],
 q('ChatGPT findet keine passende Mail. Was schreiben wir?','Im durchsuchten Bereich wurde keine Korrespondenz gefunden.','Hadi hat uns mündlich zugesagt.',0,'Suchlücken sind keine Einladung, eine Vorgeschichte zu erfinden.'),[brief],'Lass zwei Betreffzeilen schreiben: eine sachliche und eine augenzwinkernde. Wähle selbst.','Jetzt recherchieren wir genauer, wem wir unseren Schrank anbieten möchten.'),
lesson('recherche','Wem bieten wir den Schrank an?','Echte Internetrecherche.',['chatgpt'],45,
 'Drei Fakten. Eine öffentliche Kontaktadresse.',
 'Wir recherchieren den Architekten und Designer Hadi Teherani auf offiziellen Quellen. Die öffentlich genannte Büro-E-Mail ist ein Geschäftskontakt, keine bestätigte persönliche Adresse. Ob er einen Schrank braucht, wissen wir nicht.',
 'Ein kurzer Steckbrief mit Quellen und öffentlichem Bürokontakt.',
 ['Recherchefrage eingrenzen','Offizielle Quellen finden','Drei relevante Fakten mit Links belegen','Öffentliche Büro-E-Mail von persönlicher Adresse unterscheiden','Fakten und eigene Verkaufsidee trennen'],
 [demo('Stelle eine einfache Frage.','Lass drei kurze Fakten recherchieren. Öffne mindestens eine Quelle.','Wer ist Hadi Teherani? Nenne drei kurze Fakten aus offiziellen Quellen mit Links.','Ein kurzer, belegbarer Steckbrief.'),
 demo('Finde den Bürokontakt.','Prüfe Kontaktseite oder offizielles Impressum. Keine persönliche Mailadresse erraten.','Finde auf einer offiziellen Website die öffentliche geschäftliche E-Mail-Adresse seines Designbüros. Zeige die Quelle und wessen Adresse es ist.','Die Gruppe erkennt eine veröffentlichte Büro-Adresse.'),
 demo('Entwickle unsere Idee.','Eine passende Idee ist eine Hypothese, kein bekannter Kundenwunsch.','Wir sind eine fiktive Tischlerei und möchten einen maßgefertigten Büroschrank anbieten. Formuliere eine mögliche Idee in zwei Sätzen. Trenne Fakten von Vermutungen.','Die Idee ist ausdrücklich unser Vorschlag.'),
 demo('Sichere den Steckbrief.','Speichere Fakten, Bürokontakt, Quellen und Abrufdatum.','Erstelle einen kurzen Steckbrief als TXT: drei Fakten, öffentlicher Bürokontakt mit Quelle, unsere Schrankidee und offene Fragen.','Eine Datei zum Mitnehmen ins Projekt.')],
 'Recherchiere Hadi Teherani und finde eine öffentliche geschäftliche Kontaktadresse.',
 ['Drei Fakten suchen.','Büro-E-Mail an einer offiziellen Quelle prüfen.','Steckbrief mit Links als TXT sichern.'],
 ['Ich kann die Quellen öffnen.','Ich kenne den Unterschied zwischen Büro-Adresse und persönlicher Mail.','Unsere Schrankidee ist als Vorschlag erkennbar.'],
 ['Nutze haditeherani.com als Ausgangspunkt.','Bei einer blockierten Seite eine andere zugängliche offizielle Veröffentlichung suchen; die Lücke benennen.','Keine Adresse aus einem vermuteten Namensschema erzeugen.'],
 q('Die Website nennt eine Büro-E-Mail. Ist das automatisch Hadis persönliche Mail?','Nein.','Ja.',0,'Wir verwenden die Bezeichnung der Quelle und erfinden keinen persönlichen Kontakt.'),[browserfile,brief],'Finde ein öffentlich dokumentiertes Designprojekt und erkläre, warum es dich zu deiner Schrankidee inspiriert.','Steckbrief und Schrankbrief gehören in unser neues Projekt.'),
lesson('projekt','Ein Projekt für den Schrank.','Kontext wiederverwenden.',['chatgpt'],40,
 'Ein Vorhaben. Eine gemeinsame Mappe.',
 'Das Projekt hält Recherche, Vorgaben und Aufgaben zusammen. Wir nennen es „Schrank für Hadi“. Es ist unser Seminarprojekt, kein bestehender Auftrag von Hadi Teherani.',
 'Dein Projekt mit Schrankbrief, Recherche und Vorgabe.',
 ['Projekt erstellen und benennen','Quellen hinzufügen','Gemeinsame Vorgaben speichern','Aufgabe im Projekt starten','Projekt wiederfinden'],
 [demo('Lege das Projekt an.','Öffne die Seitenleiste und Neues Projekt. Nenne es „Schrank für Hadi“. Die Originalabbildung kann anders beschriftet sein.',see='Das Projekt ist in der Seitenleiste sichtbar.',asset='projects-sidebar.webp'),
 demo('Füge Unterlagen hinzu.','Öffne das neue Projekt. Klicke auf Dateien hinzufügen und wähle 03-schrankbrief.txt und deinen heruntergeladenen Recherche-Steckbrief.',see='Beide Dateien gehören zum Projekt.',asset='project-overview.webp'),
 demo('Speichere eine Vorgabe.','Öffne im Projektmenü die Projekteinstellungen und dort die Hinweise. Füge den folgenden Text als Vorgabe ein und speichere ihn.','Für dieses Seminarprojekt: kurz und freundlich mit Sie schreiben. Annahmen kennzeichnen. Keine Anfrage oder Zusage von Hadi Teherani erfinden.','Die Regel steht in den gespeicherten Projekthinweisen.',asset='project-settings.webp'),
 demo('Starte eine Aufgabe darin.','Öffne eine neue Aufgabe im Projekt und nutze die Quellen.','Fasse unsere Schrankidee und die offenen Fragen kurz zusammen.','ChatGPT verwendet den gemeinsamen Kontext.')],
 'Erstelle „Schrank für Hadi“ und füge deine Unterlagen hinzu.',
 ['Projekt anlegen.','Schrankbrief und Recherche hinzufügen.','Vorgabe speichern und eine Zusammenfassung starten.'],
 ['Ich finde mein Projekt wieder.','Meine Quellen sind hinzugefügt.','Die Zusammenfassung erfindet keinen Kundenauftrag.'],
 ['Suche in der Seitenleiste nach Neues Projekt.','Eine Vorgabe kann ein einfacher Satz sein.','Wenn eine Angabe falsch ist, nenne die richtige Quelle und lasse die Zusammenfassung berichtigen.'],
 q('Wohin gehört morgen ein völlig anderer Kunde?','In ein eigenes Projekt.','In dieses Projekt.',0,'So vermischen sich Unterlagen und Vorgaben nicht.'),[brief],'Verlasse die Ansicht und finde Projekt, Datei und Aufgabe selbst wieder.','Als Nächstes richten wir die Dateiablage ein.'),
lesson('dateien','ChatGPT legt die Dateien ab.','OneDrive und Dateiformate.',['chatgpt','onedrive','word'],60,
 'Ordner anlegen. Hochladen. Format ändern.',
 'ChatGPT legt den eigenen OneDrive-Ordner an. Du gibst die Ausgangsdatei in ChatGPT und lässt sie dort speichern. Anschließend entsteht eine bearbeitbare Word-Datei und zusätzlich eine PDF. Eine neue Dateiendung allein ändert das Format nicht.',
 'Ein eigener OneDrive-Ordner mit Quelle, DOCX und PDF.',
 ['ChatGPT einen OneDrive-Ordner anlegen lassen','Lokale Datei in ChatGPT hochladen','ChatGPT die Datei in OneDrive speichern lassen','TXT in eine bearbeitbare DOCX umwandeln','Inhalt ändern und zusätzlich eine PDF erstellen','Dateien am Speicherort öffnen'],
 [demo('Lass den Ordner anlegen.','ChatGPT führt die Ordneranlage über das eingerichtete Plugin aus. Öffne danach den Link.','Lege in meinem OneDrive einen neuen Ordner „Seminar Schrank“ an. Falls der Name schon existiert, frage nach einem anderen Namen. Zeige den Ordnerlink.','Dein eigener Ordner ist tatsächlich vorhanden.'),
 demo('Lade die Quelle hoch.','Lade 03-schrankbrief.txt in ChatGPT hoch. Lass ChatGPT die Datei im neuen Ordner ablegen.','Speichere die hochgeladene Datei 03-schrankbrief.txt unverändert im gerade angelegten OneDrive-Ordner. Zeige mir die gespeicherte Datei.','Die Quelle liegt in OneDrive und lässt sich öffnen.'),
 demo('Mach eine Word-Datei daraus.','Bitte um eine echte Formatumwandlung, keine bloße Umbenennung.','Erstelle aus dem Schrankbrief eine übersichtliche, bearbeitbare Word-Datei namens Schrankbrief_v1.docx. Erhalte das Original.','Eine DOCX-Datei lässt sich in Word öffnen.'),
 demo('Ändere einen Inhalt.','Passe den Entwurf an, ohne die bisherigen Dateien zu überschreiben.','Ergänze unter offene Fragen: Welche Oberfläche und welche Innenaufteilung wären gewünscht? Speichere als Schrankbrief_v2.docx.','Eine neue Version enthält die Ergänzung.'),
 demo('Erzeuge zusätzlich eine PDF.','Öffne beide Formate und vergleiche die Inhalte.','Erzeuge zusätzlich Schrankbrief_v2.pdf. Behalte die Word-Datei.','DOCX und PDF enthalten denselben geprüften Inhalt.'),
 demo('Lass beide Dateien ablegen.','ChatGPT speichert die Ergebnisse im eigenen OneDrive-Ordner.','Speichere die geprüfte Word-Datei und PDF im Ordner „Seminar Schrank“. Nichts überschreiben. Zeige beide Dateien.','Du kannst beide Dateien direkt in OneDrive öffnen.')],
 'Lass ChatGPT deinen Ordner anlegen und den Schrankbrief als TXT, Word und PDF darin speichern.',
 ['Ordner direkt von ChatGPT anlegen lassen.','TXT hochladen und in OneDrive speichern lassen.','DOCX erstellen, ändern, PDF erzeugen und beide ablegen.'],
 ['ChatGPT hat meinen eigenen Ordner angelegt.','Die Ausgangsdatei ist dort gespeichert.','DOCX und PDF lassen sich öffnen.','Meine Originaldatei bleibt erhalten.'],
 ['Sage ausdrücklich „in meinem OneDrive“.','Sage „als bearbeitbare Word-Datei“, nicht nur „Dateiendung ändern“.','Wenn Schreibrechte fehlen, mit ITP Consultants klären. Den manuellen Upload nur als Ersatzweg zeigen.'],
 q('Du benennst brief.txt in brief.pdf um. Ist das eine PDF?','Ja.','Nein, der Inhalt muss umgewandelt werden.',1,'Das Format entsteht beim Erstellen oder Exportieren der Datei.'),[brief],'Lass eine Kopie umbenennen und in einen eigenen Unterordner „Angebot“ verschieben.','Jetzt recherchieren wir echte Produkte im Baumarkt.'),
lesson('browser','ChatGPT bedient den Browser.','Suchen und filtern lassen.',['chatgpt'],55,
 'Du gibst den Auftrag. ChatGPT klickt.',
 'Jetzt liest ChatGPT nicht nur Suchergebnisse. Es öffnet eine echte Baumarktseite im In-App-Browser, tippt in die Suche, bedient einen passenden Filter und öffnet ein Produkt. Du siehst die Schritte und prüfst das Ergebnis. Unser Schrankentwurf ist keine fertige technische Konstruktion.',
 'Zwei echte Produktlinks mit Preisangabe, Maßen und Abrufdatum.',
 ['Echte Website im In-App-Browser öffnen lassen','ChatGPT die Website-Suche bedienen lassen','Einen sichtbaren Filter anwenden lassen','Produkt öffnen und Angaben prüfen','Brutto und netto sowie Lieferung unterscheiden','Bei Hängern stoppen und einen einzelnen Schritt neu beauftragen'],
 [demo('Öffne einen echten Baumarkt.','Zeige den In-App-Browser und die Website neben der Aufgabe.','Öffne hornbach.de im In-App-Browser. Wir suchen Material für unseren Büroschrank.','Eine echte Baumarktseite ist sichtbar.'),
 demo('Lass ChatGPT suchen.','Der Auftrag betrifft das Suchfeld auf der Website.','Nutze das Suchfeld auf dieser Website und suche nach Möbelbauplatte Eiche.','ChatGPT bedient die Suche auf der geöffneten Seite.'),
 demo('Lass einen Filter bedienen.','Wähle einen tatsächlich sichtbaren Filter. Keine nicht vorhandene Option behaupten.','Zeige mir die verfügbaren Filter. Wende den Filter für Eiche an, falls vorhanden; sonst frage mich, welchen sichtbaren Filter wir nehmen.','Die Ergebnisliste reagiert auf einen Filter.'),
 demo('Öffne ein Produkt.','Prüfe Preis, Einheit und Maße direkt an der Produktseite.','Öffne eine passende Platte. Zeige Preis, Maße, Preisbasis und Quellenlink. Nichts in den Warenkorb legen.','Die Werte lassen sich auf der Website nachlesen.'),
 demo('Vergleiche eine Alternative.','Sichere zwei Quellen für unsere Kalkulationsübung. Nicht automatisch gleiche Qualität annehmen.','Finde eine zweite Platte. Vergleiche Maße, Material, Preis und Lieferkosten. Markiere Unterschiede und fehlende Angaben. Sichere die Links mit Abrufdatum.','Zwei nachvollziehbare Produktkandidaten, keine Bestellung.')],
 'Lass ChatGPT in einem echten Baumarkt suchen, filtern und zwei Produktseiten öffnen.',
 ['Website im In-App-Browser öffnen.','ChatGPT Suche und einen sichtbaren Filter bedienen lassen.','Zwei Produkte prüfen und Quellen sichern.'],
 ['Ich habe ChatGPT eine Website bedienen sehen.','Ein sichtbarer Filter wurde angewendet oder sein Fehlen benannt.','Ich habe Maße und Preisbasis selbst auf den Produktseiten geprüft.','Es wurde nichts bestellt.'],
 ['Beginne mit einem einzelnen Auftrag: „Öffne hornbach.de.“','Wenn die Seite blockiert, wähle einen anderen zugänglichen Baumarkt.','Bei einem Hänger: „Stopp. Zeige den aktuellen Stand. Führe nur den nächsten Schritt aus.“'],
 q('Was ist hier die neue Fähigkeit?','Nur eine Antwort lesen.','ChatGPT bedient die geöffnete Website.',1,'Suche eingeben, Filter anwenden und Produkt öffnen sind Browseraktionen.'),[browserfile],'Lass auf derselben Seite einen Zuschnittservice finden und die Bedingungen zeigen. Nichts buchen.','Die geprüften Preise gehen in die Excel-Kalkulation.'),
lesson('excel','Was kostet unser Schrank?','Mit echten Quellen kalkulieren.',['chatgpt','excel'],45,
 'Menge mal Preis. Dann die übrigen Kosten.',
 'Die Arbeitsmappe enthält klar bezeichnete Übungswerte. Ersetze Materialpreise durch deine recherchierten Werte, sofern sie zur angenommenen Einheit passen. Übernimm Brutto-Preise nicht ungeprüft als Netto-Preise. Arbeitszeit, Aufschlag und Maße sind unsere Annahmen, kein Kundenwunsch.',
 'Eine nachvollziehbare Angebotskalkulation mit Formeln.',
 ['Arbeitsmappe in ChatGPT hochladen','Recherchepreise mit Quelle und Datum eintragen','Brutto und netto unterscheiden','Formeln für Positionen und Gesamtsumme erklären lassen','Eine Zeile selbst nachrechnen','Dieselbe Datei mit ChatGPT direkt in Excel bearbeiten'],
 [demo('Öffne die Kalkulation.','Zeige die Eingaben und welche Werte nur Annahmen sind.','Erkläre mir die hochgeladene Schrankkalkulation. Welche Werte sind Übungsannahmen?','Mengen, Preise, Arbeitszeit und Aufschlag sind verständlich.'),
 demo('Trage einen echten Preis ein.','Verwende nur passende Einheiten. Quelle, Datum und Preisbasis festhalten.','Übernimm den geprüften Materialpreis aus unserer Recherche. Halte Quelle, Abrufdatum und Brutto/Netto fest. Frage nach, wenn Maße oder Einheiten nicht zusammenpassen.','Ein recherchierter Wert ist sauber belegt.'),
 demo('Lass Formeln erklären.','Prüfe eine Position mit der Gruppe.','Erkläre die Formel für Menge mal Einzelpreis und rechne eine Zeile vor. Zeige anschließend den Angebotspreis mit dem Übungsaufschlag.','Die Summe ist nachvollziehbar.'),
 demo('Ändere die Arbeitszeit.','Zeige, dass die Summe über die Formel reagiert.','Ändere unsere angenommene Arbeitszeit von 8 auf 10 Stunden. Erhalte die Formeln und speichere eine neue Version.','Die Kalkulation aktualisiert sich.'),
 demo('Arbeite direkt in Excel.','Öffne deine neue Datei in Excel und dort die eingerichtete ChatGPT-Seitenleiste. Füge den Text dort ein.','Hebe die Zeile mit dem Angebotspreis farbig hervor. Verändere keine Werte oder Formeln.','Die Angebotszeile ist in Excel farbig markiert. Die Zahlen sind unverändert.')],
 'Ergänze einen recherchierten Materialpreis und prüfe die Schrankkalkulation.',
 ['Arbeitsmappe öffnen.','Preis mit Quelle eintragen lassen.','Eine Formel nachrechnen und Arbeitszeit ändern.'],
 ['Quelle und Preisbasis sind erkennbar.','Eine Position ist nachgerechnet.','Die Gesamtsumme reagiert auf Änderungen.','Ich finde die gespeicherte Excel-Datei.'],
 ['Beginne mit den markierten Eingabezellen.','Unbekannte Lieferkosten bleiben offen.','Falls eine Formel falsch ist, nenne die betroffene Zelle und das gewünschte Rechenprinzip.'],
 q('Ein Baumarkt zeigt einen Bruttopreis. Darfst du ihn als Nettopreis übernehmen?','Nein, die Preisbasis muss stimmen.','Ja, die Zahl sieht passend aus.',0,'Vergleiche dieselbe Einheit und dieselbe Preisbasis.'),[sheet],'Vergleiche zwei Materialvarianten. Erkläre den Preisunterschied mit eigenen Worten.','Die geprüfte Summe füllt unser Angebot.'),
lesson('dokument','ChatGPT füllt das Angebot aus.','Eine echte Vorlage bearbeiten.',['chatgpt','word'],60,
 'Vorlage plus geprüfte Angaben.',
 'ChatGPT erhält unsere leere Angebotsvorlage, den Schrankbrief und die Kalkulation. Es füllt das Dokument, erhält die Struktur und lässt Unbekanntes offen. Das Ergebnis ist ein unverbindlicher Seminarentwurf.',
 'Eine ausgefüllte Angebotsvorlage als DOCX und PDF.',
 ['DOCX-Vorlage hochladen','Mehrere Quellen zuordnen','Felder und Positionen ausfüllen lassen','Unbekannte Angaben offenlassen','Formulierungen gezielt ändern','DOCX und PDF in OneDrive speichern'],
 [demo('Gib die Vorlage dazu.','Lade Vorlage, Schrankbrief und geprüfte Kalkulation in dieselbe Projektaufgabe.',see='ChatGPT hat Vorlage und Daten.'),
 demo('Lass die Felder ausfüllen.','Die Vorlage gibt die Form vor. Die Dateien liefern die Angaben.','Fülle 05-angebotsvorlage.docx mit unserem Schrankbrief und der geprüften Kalkulation aus. Adressiere den Vorschlag an das recherchierte Büro von Hadi Teherani. Erhalte die Vorlage. Unbekannte Daten als offen markieren. Als unverbindlichen Seminarentwurf kennzeichnen.','Eine ausgefüllte DOCX liegt vor.'),
 demo('Verbessere den Text.','Ändere nur den gewünschten Abschnitt.','Formuliere die Leistungsbeschreibung kürzer. Beschreibe unseren maßgefertigten Büroschrank als Vorschlag. Keine Bestellung, Kundenwünsche oder Lieferzusage erfinden.','Eine klare Angebotsbeschreibung.'),
 demo('Prüfe und exportiere.','Öffne das Dokument und kontrolliere Zahlen und Layout.','Erzeuge zusätzlich eine PDF. Speichere Word und PDF in meinem OneDrive-Ordner „Seminar Schrank“. Zeige mir beide Dateien.','Beide Formate sind gespeichert und lesbar.')],
 'Lass die Angebotsvorlage ausfüllen und speichere Word und PDF.',
 ['Vorlage und Quellen hochladen.','Felder ausfüllen lassen.','Zahlen prüfen und beide Formate öffnen.'],
 ['Die Vorlage ist ausgefüllt und bleibt bearbeitbar.','Der Preis entspricht meiner Kalkulation.','Annahmen und offene Angaben sind erkennbar.','DOCX und PDF liegen in meinem OneDrive.'],
 ['Nenne die Vorlage beim Dateinamen.','Sage „Struktur erhalten, nur Felder ausfüllen“.','Bei einem Layoutfehler die konkrete Stelle nennen und eine neue Version erstellen lassen.'],
 q('Die Vorlage fragt nach einer bestätigten Lieferzeit. Wir haben keine.','Eine plausible Woche einsetzen.','Offenlassen oder als Vorschlag kennzeichnen.',1,'Die KI darf aus unserer Idee keine Zusage machen.'),[template,brief,sheet],'Lass die Einleitung für einen sachlichen und einen etwas mutigeren Stil formulieren.','Aktualisiere später Mission_Hadi.pdf und den vorhandenen Entwurf an Kerim mit dem geprüften Angebotspreis.'),
lesson('kalender','Schrankbesprechung an Weihnachten.', 'Ein bewusst absurder Übungstermin.',['chatgpt','outlook'],60,
 '25. Dezember. Nur in deinem Kalender.',
 'Unser Rollenspiel bekommt einen Weihnachtstermin: 25.12.2026 um 10:00 Uhr, Europe/Berlin, 30 Minuten. Es ist kein vereinbarter Termin mit Hadi Teherani. Wir legen ihn ohne Gäste im eigenen Kalender an, verschieben ihn und entfernen ihn wieder.',
 'Ein selbst geprüfter, verschobener und wieder gelöschter Übungstermin.',
 ['Kalender und Zeitzone prüfen','Konkretes Datum und Dauer nennen','Termin ohne externe Gäste anlegen','Denselben Termin verschieben','Nur den eigenen Übungstermin löschen'],
 [demo('Zeige den Weihnachtstag.','Lass den 25. Dezember im eigenen Kalender anzeigen.','Zeige meinen Kalender für den 25.12.2026 in Europe/Berlin.','Du siehst den richtigen Tag und das richtige Konto.'),
 demo('Lege unseren Testtermin an.','Der Titel macht die Übung erkennbar. Es werden keine Gäste eingeladen.','Lege am 25.12.2026 von 10:00 bis 10:30 Uhr, Europe/Berlin, in meinem eigenen Kalender „ÜBUNG – Schrank für Hadi“ an. Keine Gäste und keine Einladungen. Beschreibung: Unser fiktives Seminarprojekt.','Der Testtermin ist im eigenen Kalender sichtbar.'),
 demo('Verschiebe ihn.','Ändere denselben Termin statt einen zweiten zu erstellen.','Verschiebe genau diesen Übungstermin auf 11:00 bis 11:30 Uhr am selben Tag.','Ein Termin, neue Uhrzeit.'),
 demo('Räume wieder auf.','Lass nur diesen Übungstermin entfernen und kontrolliere den Kalender.','Entferne nur den eben angelegten Termin „ÜBUNG – Schrank für Hadi“ am 25.12.2026.','Der Übungstermin ist weg. Andere Termine bleiben erhalten.')],
 'Lege den Weihnachtstermin ohne Gäste an, verschiebe ihn und lösche ihn wieder.',
 ['25.12.2026 prüfen','Testtermin anlegen und verschieben','Nur den Testtermin entfernen'],
 ['Datum und Zeitzone stimmen.','Es wurden keine Gäste eingeladen.','Ich habe denselben Termin verschoben.','Der Übungstermin ist wieder entfernt.'],
 ['Sage ein vollständiges Datum mit Jahr.','Prüfe vor dem Anlegen den Kalender.','Bei mehreren Treffern zuerst den richtigen Übungstermin auswählen.'],
 q('Der Termin heißt „Schrank für Hadi“. Weiß sein Büro davon?','Nein, es ist unser eigener Übungstermin.','Ja, der Titel genügt.',0,'Ein Titel ist keine Einladung oder Zusage.'),[term],'Lass eine Vorbereitungserinnerung erklären und unterscheide sie von einer Aufgabe, die später Arbeit erledigt.','Jetzt planen wir eine spätere Entwurfserstellung.'),
lesson('spaeter','Den Entwurf später erstellen lassen.', 'Eine Aufgabe für ChatGPT planen.',['chatgpt','outlook'],45,
 'Später erstellen. Nicht versenden.',
 'Wir planen, dass ChatGPT zu einem späteren Zeitpunkt einen Mailentwurf vorbereitet. Das ist kein zeitversetzter Versand. Ob eine geplante Aufgabe auf Projektdateien und Outlook zugreifen kann, wird im Konto geprüft. Wenn nicht, soll sie die fehlende Verbindung melden oder den Entwurf als Text bereitstellen.',
 'Eine geprüfte geplante Aufgabe ohne Sendeauftrag.',
 ['Projektstand wiederverwenden','Geplante Aufgabe von Kalender und Mailversand unterscheiden','Zeitpunkt und Zeitzone setzen','Zugriff auf Dateien und Outlook prüfen','Aufgabe wiederfinden und deaktivieren'],
 [demo('Sichere den aktuellen Stand.','Lass Angebot, Quellen und offene Punkte kurz zusammenfassen.','Fasse den Stand unseres Schrankprojekts zusammen. Welche Datei ist die aktuelle Angebots-PDF? Was ist noch offen?','Der spätere Auftrag hat klaren Kontext.'),
 demo('Plane die Entwurfserstellung.','Nimm zum Test einen Zeitpunkt einige Minuten später. Die Aufgabe darf nichts senden.','Plane für einen von mir bestätigten Zeitpunkt in Europe/Berlin: Erstelle einen kurzen Folgeentwurf an Kerim zu unserem Schrankprojekt. Nutze nur den zuvor geprüften Kontakt und den gesicherten Projektstand. Kennzeichne das Seminar-Rollenspiel. Speichere ihn, wenn Outlook verfügbar ist, als ÜBUNG-Entwurf an Kerim. Ist seine geprüfte Adresse nicht verfügbar, frage nach und erfinde keine. Nichts versenden. Fehlen Dateien oder Berechtigungen, melde das.','Die geplante Aufgabe enthält Uhrzeit, Kontext und die Grenze „nicht senden“.'),
 demo('Prüfe den gespeicherten Auftrag.','Öffne die geplante Aufgabe. Kontrolliere Zeitpunkt, Zeitzone und erlaubte Aktion.','Zeige mir die gespeicherte Aufgabe und ihren genauen Auftrag.','Entwurfserstellung ist geplant, kein Mailversand.'),
 demo('Prüfe das Ergebnis und räume auf.','Wenn die Testzeit erreicht ist, öffne den Entwurf oder die Rückmeldung. Deaktiviere die Übungsaufgabe danach.','Zeige mir das Ergebnis der Übungsaufgabe. Deaktiviere anschließend nur diese Übungsaufgabe.','Der Entwurf oder die klar benannte Zugriffslücke ist geprüft.')],
 'Plane einen späteren Mailentwurf. Prüfe den Auftrag und deaktiviere die Übung danach.',
 ['Späteren Zeitpunkt wählen','Entwurfserstellung ohne Versand planen','Aufgabe und Ergebnis prüfen'],
 ['Die Aufgabe enthält keinen Sendeauftrag.','Zeitpunkt und Zeitzone sind richtig.','Ich weiß, was ohne Outlook-Zugriff passiert.','Die Übungsaufgabe ist danach deaktiviert.'],
 ['Plane zuerst nur eine einmalige Aufgabe.','Fehlt die Funktion, zeigt Kerim den Ablauf; ITP Consultants prüft die Einrichtung.','Ein Kalendertermin allein führt keinen ChatGPT-Auftrag aus.'],
 q('Wir planen die Erstellung eines Mailentwurfs. Wird die Mail dann gesendet?','Nein.','Ja, automatisch.',0,'Erstellen und Senden sind unterschiedliche Handlungen. Unser Auftrag endet beim Entwurf.'),[term],'Formuliere zusätzlich eine wiederkehrende Zusammenfassung offener Projektpunkte. Nur als Text, nicht aktivieren.','Zum Schluss verbindest du alle Schritte selbst.'),
lesson('abschluss','Dein Angebot steht.', 'Alles selbst verbinden.',['chatgpt','onedrive','excel','word','outlook'],65,
 'Ein nachvollziehbares Angebotspaket.',
 'Unser fiktiver Betrieb ändert die Annahme: zehn statt acht Arbeitsstunden. Aktualisiere die Kalkulation und das Angebot. Eine andere Person soll Quellen, Annahmen, Dateien und Entwurf wiederfinden können.',
 'Recherche, Kalkulation, Word, PDF und ein ungesendeter Entwurf.',
 ['Änderung durch alle Dateien verfolgen','Originale erhalten','Ergebnisse in OneDrive ablegen','Mailanhang aktualisieren','Quellen und offene Fragen übergeben'],
 [demo('Prüfe die zehn Arbeitsstunden.','Öffne deine aktuelle Kalkulation in ChatGPT. Wenn bereits zehn Stunden eingetragen sind, lass den Wert stehen.','Prüfe meine Kalkulation: Wir planen zehn Arbeitsstunden. Falls noch acht eingetragen sind, ändere sie auf zehn. Erhalte die Formeln und speichere eine neue Version. Zeige den aktuellen Angebotspreis.','Die Kalkulation enthält zehn Arbeitsstunden und einen geprüften Angebotspreis.'),
 demo('Aktualisiere dein Paket.','Bleibe im Projekt. Gib ChatGPT deine aktuelle Kalkulation und die zu aktualisierenden Dateien. Öffne die Ergebnisse danach selbst.','Aktualisiere mit meiner geprüften Kalkulation das Angebot als Word und PDF sowie Mission_Hadi.pdf in Seminar Schrank. Aktualisiere auch den bestehenden Entwurf an Kerim und seinen PDF-Anhang. Nicht senden. Zeige die aktuellen Dateien und offene Fragen.','Kalkulation, Angebot, Mission_Hadi.pdf und Kerims Entwurf enthalten denselben Stand.')],
 'Aktualisiere dein Angebot für zehn Arbeitsstunden und zeige das fertige Paket.',
 ['Kalkulation ändern','Word und PDF aktualisieren','Entwurf und Ablage prüfen'],
 ['Die Dateien verwenden denselben geprüften Preis.','Quellen und Annahmen sind unterscheidbar.','Der Entwurf enthält die aktuelle PDF und ist ungesendet.','Übungstermin und geplante Aufgabe sind aufgeräumt.'],
 ['Beginne mit der Kalkulation als Preisquelle.','Erstelle neue Versionen statt Originale zu überschreiben.','Lass eine andere Person deine Dateien öffnen und den nächsten Schritt erklären.'],
 q('Was macht dein Paket brauchbar?','Es sieht überzeugend aus.','Quellen, Preis und Dateien sind nachvollziehbar.',1,'Ein gutes Ergebnis lässt sich prüfen und übernehmen.'),[change],'Wähle eine Aufgabe aus deinem echten Arbeitsalltag, die du morgen so bearbeiten möchtest.','Deine Ergebnisse bleiben in deinen eigenen Konten.')
]
# Two realistic seminar days. Clock values are generated, not fictional workday times.
day_specs=[ [('Ankommen und Modell wählen',15),('antwort',55),('recherche',45),('projekt',40),('Pause',15),('dateien',60),('Mittagspause',60),('browser',55),('Pause',15),('excel',45),('Ergebnisse sichern',15)], [('Wieder ankommen',15),('dokument',60),('Eigene Fragen und Vertiefung',55),('Pause',15),('kalender',60),('Mittagspause',60),('spaeter',45),('Pause',15),('abschluss',65),('Ergebnisse zeigen und Transfer',30)]]
lookup={l['id']:l for l in lessons};schedule=[]
for day,spec in enumerate(day_specs,1):
 t=540;items=[]
 for key,n in spec:
  clock=f'{t//60:02d}:{t%60:02d}';items.append([clock,lookup[key]['title'] if key in lookup else key,f'{n} min'])
  if key in lookup:lookup[key].update(day=day,time=clock)
  t+=n
 assert t==960
 schedule.append(dict(day=day,title='Recherchieren und vorbereiten' if day==1 else 'Anbieten und planen',items=items))
for i,l in enumerate(lessons):
 l['number']=i+1;l['rhythm']=dict(explain=5,show=10,do=l['minutes']-20,check=5)
plan=dict(title='Ein Schrank für Hadi.',subtitle='Echte Recherche. Unser fiktives Angebot. Dein ChatGPT.',case='Schrank für Hadi',promise='Du recherchierst, bedienst Websites, bearbeitest Dateien und bereitest ein vollständiges Angebot vor.',environment='Du arbeitest in deinem eigenen ChatGPT und Microsoft 365. Unser Angebot ist ein Seminar-Rollenspiel. Es gibt keine Anfrage oder Zusage von Hadi Teherani.',lessons=lessons,schedule=schedule,glossary={'Projekt':'Die gemeinsame Mappe für Dateien, Aufgaben und Vorgaben.','Plugin':'Die Verbindung von ChatGPT zu einem anderen Programm.','Recherche':'Informationen suchen und an Quellen prüfen.','Browseraktion':'ChatGPT öffnet eine Website, tippt, klickt oder wendet einen Filter an.','Entwurf':'Eine vorbereitete, noch nicht versendete Mail.','Geplante Aufgabe':'Ein ChatGPT-Auftrag, der später ausgeführt werden soll.','Hochladen':'Eine Datei von deinem Computer in eine Anwendung geben.','DOCX':'Eine bearbeitbare Word-Datei.','PDF':'Eine Datei zum Lesen und Weitergeben.','XLSX':'Eine Excel-Arbeitsmappe mit Tabellen und Formeln.','Annahme':'Eine Vorgabe für unsere Übung, keine bestätigte Kundenangabe.','Freigabe':'Deine bewusste Entscheidung für eine bestimmte Handlung.'})
Path('public/curriculum.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2))
md=['# Ein Schrank für Hadi','',plan['subtitle'],'',plan['environment'],'','Hadi Teherani ist die reale Person. Schrank, Betrieb, Maße, Preise und Weihnachtstermin sind unser Seminar-Rollenspiel. Wir recherchieren öffentliche Geschäftskontakte; Übungsentwürfe gehen an den zuvor geprüften Kontakt Kerim und bleiben ungesendet.','', '## Lernziel',plan['promise'],'','## Ablauf pro Station','Prinzip ansehen, echte Vorführung durch Kerim, im eigenen Konto üben, Ergebnis prüfen.','']
for d in schedule:md+=['## Tag '+str(d['day'])]+['- '+' · '.join(r) for r in d['items']]+['']
for l in lessons:
 md+=['## '+str(l['number'])+'. '+l['title'],l['story'],'','**Das lernen wir:**']+['- '+x for x in l['skills']]+['','**Das zeigst du live:**']
 for i,d in enumerate(l['demos'],1):md+=[str(i)+'. '+d['title']+' '+d['action']]+(['   Auftrag: '+d['prompt']] if d['prompt'] else [])
 md+=['','**Eigene Aufgabe:** '+l['mission'],'','**Ergebnis prüfen:**']+['- '+x for x in l['checks']]+['','**Danach:** '+l['carry'],'']
md+=['## Quellen und Verfügbarkeit','- Offizielle Recherche zum Büro: https://www.haditeherani.com/','- Offizielle Vita als mögliche Quelle: https://www.haditeherani.com/sites/default/files/2025-02/211208_HT%20Vita%20dt.pdf','- Echte Browserübung: https://www.hornbach.de/','- ChatGPT und verbundene Programme: https://help.openai.com/en/articles/20001275/','- Modellwahl: https://help.openai.com/en/articles/20001516','Die konkreten Websites, Preise, Filter und Konto-Funktionen werden im Seminar geprüft. Blockierte Seiten oder fehlende Berechtigungen werden benannt. Öffentliche Kontaktdaten werden nicht als persönliche E-Mail ausgegeben. Die geplante Aufgabe erstellt nur einen Entwurf; externe Empfänger werden nicht angeschrieben.','']
Path('CURRICULUM.md').write_text('\n'.join(md));Path('public/material/11-lernplan.txt').write_text('\n'.join(md))
print('10 Stationen: Recherche und Browseraktionen getrennt; zwei Tage 09–16 Uhr.')
