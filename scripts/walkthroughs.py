"""Guided scenes: original product images and explicitly labeled simulations."""
def frame(title,body,view='work',**kw):return dict(title=title,body=body,view=view,**kw)
def walkthroughs(modules):
 result={}
 for i,m in enumerate(modules,1):
  result[i]=[
   frame('Hier beginnt deine Aufgabe.','Öffne Work. In das große Eingabefeld schreibst du gleich, was du erledigen möchtest. Du brauchst dafür keine besonderen Befehle.','work',focus='composer'),
   frame('Gib Work die passenden Unterlagen.','Lade die Übungsdatei über das Plus am Eingabefeld hoch. Warte, bis der Dateiname erscheint. So weißt du, dass Work die richtigen Unterlagen bekommen hat.','compose',file=m['file'],focus='upload'),
   frame('Beschreibe das gewünschte Ergebnis.','Sag nicht nur, worum es geht, sondern auch, was du am Ende erhalten möchtest. Diesen Auftrag könntest du in das Eingabefeld schreiben.','compose',prompt=m['prompt'],file=m['file'],focus='send'),
   frame('Jetzt siehst du ein mögliches Ergebnis.','Lies die Antwort und vergleiche sie mit deiner Ausgangsdatei. Work darf fehlende Angaben nicht einfach ergänzen.','result',prompt=m['prompt'],result=m['output'],kind=m['kind']),
   frame('Du prüfst und machst weiter.',m['check'],'result',result=m['output'],kind=m['kind'],check=True)
  ]
 result[1][3]['body']='Aus den unsortierten Notizen ist eine Aufgabenliste geworden. Zu jedem Eintrag steht jetzt, was als Nächstes zu tun ist. Du kannst die Liste so übernehmen oder weiter bearbeiten lassen.'
 result[2]=[
  frame('Du musst nicht von vorn anfangen.','Wenn eine Antwort nicht passt, bleibst du in derselben Aufgabe. Work kennt dort bereits deine Anfrage und den ersten Entwurf.','result',result=modules[1]['input'],kind='mail'),
  frame('Sag konkret, was sich ändern soll.','Schreibe unter die Antwort, was du anders brauchst. „Kürzer“ verändert die Länge; „ohne Zusagen“ verhindert, dass aus einer Anfrage schon eine verbindliche Antwort wird.','compose',prompt=modules[1]['prompt'],focus='send'),
  frame('Vergleiche die neue Fassung.','Die neue Antwort ist kürzer und fragt nach einer Besichtigung. Sie verspricht weder einen Preis noch einen festen Termin.','result',result=modules[1]['output'],kind='mail'),
  frame('Wenn Work hängen bleibt: einen Schritt zurück.','Hat Work die Datei falsch gelesen, nenne die konkrete Stelle und lade die richtige Datei erneut hoch. Bleibt eine Browseraktion hängen, lass dir den aktuellen Stand zeigen und gib nur den nächsten Schritt vor.','compose',prompt='Stopp. Zeige mir kurz, was bereits erledigt ist und wo es hängt. Noch nichts erneut absenden. Ich gebe dir dann den nächsten Schritt.',focus='composer')
 ]
 result[3]=[
  frame('Ein Projekt ist deine Arbeitsmappe.','Stell dir den Auftrag Lindenhof als eine Mappe vor: Darin liegen Unterlagen, passende Gespräche und deine Vorgaben. Ein einzelnes Gespräch bearbeitet eine Aufgabe; das Projekt hält mehrere Aufgaben zum selben Auftrag zusammen.','overview',focus='overview'),
  frame('So legst du eine neue Mappe an.','Öffne die Seitenleiste und wähle „Neues Projekt“. In dieser englischen Originalabbildung heißt der Eintrag „New project“. Klicke hier auf die markierte Stelle, um weiterzugehen.','sidebar',focus='new-project'),
  frame('Gib dem Projekt einen klaren Namen.','Trage zum Beispiel „Lindenhof · Umbau“ ein und bestätige die Erstellung. Der Name hilft dir später, den Auftrag in der Seitenleiste wiederzufinden.','new-project',focus='create'),
  frame('Lege die Unterlagen in das Projekt.','Öffne im Projekt den Bereich für Dateien beziehungsweise Quellen. Füge dort „03-lindenhof.txt“ hinzu. Eine Datei im Projekt steht als Hintergrund für weitere Aufgaben in diesem Projekt bereit.','overview',focus='files'),
  frame('Füge die erste Projektdatei hinzu.','Wähle im Dateibereich die Funktion zum Hinzufügen und öffne die heruntergeladene Datei „03-lindenhof.txt“. Warte, bis sie in den Projektquellen auftaucht. Erst dann startest du mit der Datei eine Aufgabe.','project-upload',file='03-lindenhof.txt'),
  frame('Speichere Vorgaben für diesen Auftrag.','Über das Menü mit den drei Punkten kommst du zu den Projekteinstellungen. Dort kannst du Hinweise hinterlegen, die für die Arbeit in diesem Projekt gelten sollen.','settings',focus='settings'),
  frame('So könnte deine Vorgabe aussehen.','Für Lindenhof soll Work kurze Kundenantworten schreiben und unbekannte Angaben offenlassen. Speichere diese Vorgabe im Projekt; sie ist kein neuer Arbeitsauftrag.','instructions',prompt='Wir bearbeiten den Kundenauftrag Lindenhof. Schreibe Kundenantworten freundlich und kurz. Erfinde keine Maße, Preise oder Termine. Kennzeichne fehlende Angaben als „noch offen“.',focus='save'),
  frame('Starte jetzt eine Aufgabe in Work.','Öffne dein Projekt und wähle Work. Prüfe, dass Lindenhof als Projekt zugeordnet ist. Dann fragst du nach einer Zusammenfassung der Unterlagen.','compose',project='Lindenhof · Umbau',file='03-lindenhof.txt',prompt=modules[2]['prompt'],focus='project'),
  frame('Morgen machst du hier weiter.','Öffne wieder Lindenhof in der Seitenleiste. Du findest die Unterlagen und die bisherigen Aufgaben dort wieder. Für ein anderes Bauvorhaben legst du ein eigenes Projekt an.','project-home',project='Lindenhof · Umbau')
 ]
 result[4]=[
  frame('Hier findest du die Verbindungen.','Unter dem Eingabefeld liegt „Plugins“. Darüber erreichst du die Erweiterungen für deine Programme. Für den Workshop sollten die benötigten Konten bereits mit ITP eingerichtet sein.','work',focus='plugins'),
  frame('Wähle das passende Programm.','Für eine gespeicherte Datei brauchst du OneDrive. Für E-Mails brauchst du Outlook Mail. Die Erweiterung bestimmt, in welchem verbundenen Programm Work nachsehen kann.','plugins',focus='onedrive'),
  frame('Nenne, was Work finden soll.','Beschreibe den Ordner und die gesuchte Datei möglichst genau. Du musst sie nicht erst selbst herunterladen und wieder hochladen.','compose',prompt=modules[3]['prompt'],focus='send'),
  frame('Öffne den Treffer und prüfe ihn.','Vergleiche den Dateinamen und den Inhalt mit der gesuchten Unterlage. Wird nichts gefunden, prüfe zuerst das verbundene Konto und die Zugriffsrechte.','result',result=modules[3]['output'],kind='connections')
 ]
 result[5]=[
  frame('Lass dir zuerst die heutigen Mails zeigen.','Öffne Work mit deiner Outlook-Verbindung. Bitte zunächst nur um Absender und Betreff. Danach entscheidest du, welche Mail du bearbeiten möchtest.','compose',prompt=modules[4]['mailStages'][0]['prompt'],focus='send'),
  frame('Wähle eine konkrete Mail aus.','Nenne den Absender und den Betreff der Mail. So ist klar, worauf sich deine nächste Frage bezieht. Hier verwenden wir die erfundene Nachricht von Mara Sommer.','inbox'),
  frame('Lass dir erklären, was gebraucht wird.','Work soll die Mail in einfachen Worten zusammenfassen. Frag zusätzlich, was du selbst als Nächstes tun musst.','result',prompt=modules[4]['mailStages'][1]['prompt'],result=modules[4]['mailStages'][1]['result'],kind='notes'),
  frame('Gib Work die Fakten für die Antwort.','Work kann nicht wissen, welche Unterlagen dein Betrieb benötigt. Hier gibst du vor, dass ein Grundriss und Fotos gebraucht werden. Daraus entsteht zunächst ein Vorschlag in Work.','result',prompt=modules[4]['mailStages'][2]['prompt'],result=modules[4]['mailStages'][2]['result'],kind='mail'),
  frame('Passe den Ton an und speichere den Entwurf.','Bitte in derselben Aufgabe um eine kürzere Fassung. Erst die überarbeitete Antwort wird als Entwurf in Outlook gespeichert.','result',prompt=modules[4]['mailStages'][3]['prompt'],result=modules[4]['mailStages'][3]['result'],kind='mail',saved=True),
  frame('Kontrolliere den Entwurf in Outlook.','Öffne Outlook und den Ordner Entwürfe. Lies Empfänger und Antwort durch. Als Zusatz kannst du Work eine Übungsdatei unter 3 MB an diesen Entwurf anhängen lassen; prüfe den Anhang danach ebenfalls.','outlook',result=modules[4]['output'])
 ]
 result[6]=[
  frame('Beginne mit einem klaren Suchauftrag.','Öffne Work und nenne Website, Ort, Budget und die Kriterien, die wirklich wichtig sind. Sag auch, ob Work nur recherchieren oder etwas auf der Website ausführen soll.','compose',prompt=modules[5]['prompt'],focus='send'),
  frame('Lass dir die geöffnete Website zeigen.','Wenn Work den Browser verwendet, kannst du dich auf die sichtbare Seite beziehen. Beschreibe das Ziel des nächsten Schritts statt eine lange Folge von Klicks vorzugeben.','browser'),
  frame('Steuere in kleinen Schritten nach.','Fehlt zum Beispiel die Lagerfläche, sag das direkt in derselben Aufgabe. Work soll den Treffer prüfen, statt eine fehlende Angabe zu erraten.','compose',prompt='Prüfe beim zweiten Objekt, ob eine Lagerfläche dazugehört. Zeige mir die Fundstelle. Wenn es dort nicht steht, kennzeichne die Angabe als unklar. Kontaktiere keinen Anbieter.',focus='send'),
  frame('Öffne die Quellen selbst.','Vergleiche den Vorschlag mit den Originalanzeigen. Die gezeigten Objekte sind fiktiv; bei deiner eigenen Suche brauchst du echte Quellen und aktuelle Preise.','result',result=modules[5]['output'],kind='browser')
 ]
 result[7][1]['body']='Für den ersten Weg öffnest du das Plus in Work und lädst „04-materialvergleich.xlsx“ hoch. Achte darauf, dass genau diese Datei als Anhang am Auftrag steht.'
 result[7][3]['body']='Work rechnet hier Menge mal Stückpreis und addiert die Lieferung. Dadurch ist Angebot B insgesamt günstiger, obwohl der Stückpreis höher ist als bei A.'
 result[7].append(frame('Der zweite Weg beginnt direkt in Excel.','Öffne dieselbe Arbeitsmappe in Excel und die vorab eingerichtete ChatGPT-Erweiterung. Gib dort denselben Auftrag ein. Kontrolliere die vorgeschlagenen Änderungen in der Tabelle, bevor du sie übernimmst.','excel',prompt=modules[6]['prompt']))
 result[8][1]['body']='Lade beide Dateien hoch: den leeren Projektbogen und die Lindenhof-Unterlagen. Die Vorlage sagt, wo etwas stehen soll; die Unterlagen liefern die Angaben.'
 result[8][1]['file']='05-projektbogen.docx + 03-lindenhof.txt'
 result[8][4]['view']='download';result[8][4]['file']='Projektbogen-Lindenhof.docx'
 result[9][1]=frame('Nenne Anlass, Dauer und Beteiligte.','Work braucht genug Angaben, um einen sinnvollen Vorschlag zu machen. Für unbekannte Daten soll es nachfragen. Ein freier Platz in deinem Kalender sagt nichts über die Kundin aus.','compose',prompt=modules[8]['prompt'],focus='send')
 result[9][4]['view']='calendar'
 result[10][1]=frame('Unterscheide Erinnerung und Arbeitsauftrag.','„Erinnere mich am Montag“ erzeugt einen Hinweis. „Fasse jeden Montag die offenen Aufgaben zusammen“ beschreibt Arbeit, die regelmäßig ausgeführt werden soll.','compose',prompt=modules[9]['prompt'],focus='send')
 result[10][4]['view']='schedule'
 return result
