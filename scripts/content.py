from pathlib import Path
import re,json
text=Path('STORYBOARD.md').read_text()
slides=[]
chapters=['Dein neuer Arbeitsalltag','In Work ankommen','Gute Arbeitsaufträge','Projekte & Kontext','Plugins & Verbindungen','Mail & OneDrive','Recherche & Browser','Excel & Tabellen','Dateien & Formulare','Kalender & Scheduling','Dein kompletter Workflow']
for match in re.finditer(r'^### (\d{2}) · ([^\n]+)\n(.*?)(?=^### |^## |\Z)',text,re.M|re.S):
 n=int(match[1]); body=match[3].strip(); chapter=0 if n<=4 else (n-5)//4+1
 def field(label):
  m=re.search(r'\*\*'+re.escape(label)+r':\*\* (.+)',body)
  return m[1].strip() if m else ''
 lead=field('Auf der Folie').strip('„“')
 steps=re.findall(r'^\d+\. (.+)$',body,re.M)
 goal=field('Ziel'); criteria=field('Erfolgskriterien')
 hints=field('Hilfen').split(' / ') if field('Hilfen') else []
 plain=[]
 for p in body.split('\n\n'):
  if p.startswith('**') or re.match(r'^\d+\.',p):continue
  plain.append(p)
 slides.append(dict(id=n,title=match[2],chapter=chapter,chapterName=chapters[chapter],lead=lead,steps=steps,goal=goal,criteria=criteria,hints=hints,bonus=(re.search(r'\*\*Schon fertig\?\*\* (.+)',body)[1] if re.search(r'\*\*Schon fertig\?\*\* (.+)',body) else ''),paragraphs=plain,type='challenge' if goal else 'demo' if steps else 'statement'))
# Public explanatory copy, independent of internal production directions.
overrides={
1:[],2:['Welche Aufgabe kostet dich regelmäßig Zeit? Denk an eine Sache, die du heute gern einfacher erledigen würdest.'],3:['Willkommen bei Werkraum Ausbau. Unser fiktiver Handwerksbetrieb modernisiert Büroräume, kauft Material ein und sucht einen neuen Standort.','Alle Übungsdaten sind erfunden. Du arbeitest mit vorbereiteten Unterlagen in deinen verbundenen Konten.'],4:['Die erste Antwort ist ein Arbeitsstand. Sag, was fehlt. Zeig die Quelle. Prüfe, ob das Ergebnis wirklich zur Aufgabe passt.'],
5:['Beginne mit dem gewünschten Ergebnis. Füge die passenden Dateien hinzu und arbeite im selben Vorgang weiter.','Probier es aus: Aufgabe starten, Material hinzufügen, Ergebnis ansehen und eine Verbesserung anfordern.'],
13:['Ein Projekt bündelt zusammengehörige Arbeit. Lege dort die Unterlagen und Vorgaben ab, die du für einen Vorgang wiederholt brauchst.','Prüfe bei einer neuen Aufgabe, welche Informationen Work tatsächlich zur Verfügung stehen. Kontext muss aktuell bleiben.'],
17:['Verbinde die Quelle, die deine Aufgabe braucht: Outlook Mail für Nachrichten, OneDrive für Dateien und Kalender für Termine.','Öffne Plugins in Work und prüfe die verfügbaren Microsoft-365-Verbindungen. Welche Aktionen möglich sind, siehst du an der eingerichteten Verbindung.'],
20:['Lesen: Informationen finden und verstehen. Entwerfen: ein Ergebnis zur Prüfung vorbereiten. Ausführen: etwas speichern, senden oder einrichten.','Sag ausdrücklich, was jetzt passieren soll. Prüfe bei einer Freigabe Empfänger, Inhalt und Umfang.'],
29:['Bearbeite dieselbe Aufgabe direkt in Excel und mit einer hochgeladenen Arbeitsmappe in Work. Vergleiche anschließend die Ergebnisse.','Öffne in Excel die eingerichtete ChatGPT-Integration. Ist sie in deinem Konto nicht verfügbar, nutze zunächst die Datei in Work.'],
37:['Ein Kalendertermin blockiert Zeit. Eine Erinnerung macht dich auf etwas aufmerksam. Eine wiederkehrende KI-Aufgabe bearbeitet einen Auftrag nach einem Rhythmus.','Prüfe jeweils, welche Funktion in deinem Konto verfügbar ist und wo du das gespeicherte Ergebnis wiederfindest.'],
41:['Ein neuer Vorgang: Praxisumbau Parkblick. Alle benötigten Informationen findest du im Abschlussmaterial. Du entscheidest, welche Werkzeuge dir helfen.'],
42:['Erstelle eine Zusammenfassung, offene Fragen, einen Kostenvergleich, einen Projektbogen und einen Antwortentwurf mit Terminvorschlag.','Nutze mindestens drei geübte Fähigkeiten. Reihenfolge und Lösungsweg bestimmst du.'],
43:['Passen deine Ergebnisse zueinander? Sind wichtige Aussagen und Zahlen belegt? Ist klar, was noch offen ist?','Vergleicht eure Ergebnisse zu zweit. Zeigt euch einen Fehler, den ihr entdeckt habt, und wie ihr ihn behoben habt.'],
44:['Vervollständige: Bei … nutze ich KI für … und prüfe anschließend …','Kontrolliere zum Abschluss deine Übungstermine und wiederkehrenden Aufgaben. Deaktiviere, was nicht weiterlaufen soll.']}
for s in slides:
 if s['id'] in overrides:s['paragraphs']=overrides[s['id']]
 if s['id']==42:
  s.update(type='challenge',goal=s['paragraphs'][0],criteria='Mindestens drei Fähigkeiten kombiniert; Aussagen und Zahlen belegt; offene Fragen und nötige Freigaben erkennbar.',hints=['Was braucht der nächste Bearbeiter?','Zerlege den Vorgang in überprüfbare Teilergebnisse.','Zerlege diesen Vorgang in sinnvolle Arbeitsschritte. Sage, welche Unterlagen du brauchst. Beginne mit dem ersten Schritt und frage nach, wenn wesentliche Angaben fehlen.'])
Path('public/content.json').write_text(json.dumps({'chapters':chapters,'slides':slides},ensure_ascii=False,indent=2))
print(len(slides),'slides exported')
