from pathlib import Path
from docx import Document
from docx.shared import Cm,Pt,RGBColor
out=Path('public/material');out.mkdir(exist_ok=True)
files={
'01-tagesnotizen.txt':'''WERKRAUM AUSBAU – FIKTIVE ÜBUNGSDATEN
Montag, 08:12 Uhr
- Lieferung unklar. Jemand sollte nachfragen.
- Lindenhof fragt nach einem Ausführungstermin. Bisher nichts bestätigt.
- Drei Angebote für 100 Montageeinheiten liegen vor. Preise vergleichen.
- Team muss wissen, welche Unterlagen für Lindenhof fehlen.
- Der Projektbogen ist noch leer.
Auftrag: Erstelle einen brauchbaren Arbeitsplan. Ergänze keine erfundenen Zuständigkeiten oder Termine.
''',
'02-fehlerhafter-entwurf.txt':'''FIKTIVE ÜBUNGSDATEN
Kundenanfrage von Mara Sommer <mara.sommer@lindenhof.example>
Betreff: Büroräume Lindenhof modernisieren
Hallo, wir möchten zwei Büroräume modernisieren. Können Sie ein Angebot für neue Trennwände und die Montage von zwei Innentüren erstellen? Der genaue Umfang ist noch offen. Wir würden gern zeitnah beginnen. Ein Termin wurde noch nicht vereinbart. Viele Grüße, Mara Sommer

FEHLERHAFTER ENTWURF ZUM ÜBERARBEITEN
Hallo Frau Sommer, wir garantieren die Fertigstellung bis Freitag. Alle Arbeiten kosten zusammen 4.500 Euro. Die Handwerker kommen um 7 Uhr. Das Angebot finden Sie im Anhang.

AUFGABE
Prüfe den Entwurf gegen die Anfrage. Preise, Termine und Anhänge sind nicht belegt. Erfrage insbesondere den genauen Leistungsumfang und das gewünschte Zeitfenster. Maximal 120 Wörter.
''',
'03-lindenhof.txt':'''BAUVORHABEN LINDENHOF – FIKTIVE ÜBUNGSDATEN
Alle Namen, Adressen und Vorgänge in diesem Dokument sind erfunden.

AKTUELLE KUNDENANFRAGE – Stand 23.09.2026
Von: Mara Sommer <mara.sommer@lindenhof.example>
An: Werkraum Ausbau <buero@werkraum.example>
Wir möchten zwei Büroräume modernisieren: Trennwände prüfen und zwei neue Innentüren montieren. Bitte sagen Sie uns, welche Informationen Sie für ein Angebot benötigen. Wir wünschen eine Besichtigung vor der Kalkulation. Zugang zum Gebäude müssen wir noch mit der Hausverwaltung klären. Ein Ausführungstermin ist noch nicht bestätigt.

PROJEKTBRIEF – Stand 23.09.2026
Vorgang: LH-026
Kunde: Lindenhof Büroservice, fiktiv
Ansprechpartnerin: Mara Sommer
Objekt: Musterweg 12, 20000 Musterstadt, fiktive Adresse
Anfrage: zwei Büroräume, Trennwände und zwei Innentüren
Türmaße: nicht mitgeteilt
Wandaufbau und Schallschutzanforderungen: nicht mitgeteilt
Zugang und Ansprechpartner vor Ort: zu klären
Budget: nicht mitgeteilt
Termine: Besichtigung gewünscht, Ausführung nicht bestätigt

ÄLTERE INTERNE NOTIZ – Stand 18.09.2026
Telefonisch wurde zunächst von drei Türen gesprochen. Eine Ausführung im Oktober wäre eventuell wünschenswert. Keine Zusage.
Die aktuelle Kundenanfrage vom 23.09.2026 nennt zwei Türen. Abweichung vor verbindlicher Kalkulation klären.

KOMMUNIKATIONSREGELN
Sachlich und kundenfreundlich schreiben. Kunden in E-Mails siezen.
Keine Preise, Kapazitäten oder Termine verbindlich zusagen, die nicht bestätigt sind.
Fehlende Angaben markieren. Vorschläge ausdrücklich als Vorschlag kennzeichnen.

AUFGABEN
Organisiere ein Projekt, finde relevante Quellen und erstelle eine Zusammenfassung mit offenen Fragen. Entwirf eine Antwort, ohne sie zu versenden. Nutze bei Bedarf einen eigenen Übungsordner in OneDrive. Dieses Paket kann als Datei verwendet werden, ohne fiktive Nachrichten an reale Empfänger zu schicken.
''',
'06-standortsuche.txt':'''STANDORTSUCHE – ÜBUNGSKRITERIEN
Fiktiver Betrieb Werkraum Ausbau sucht ein Büro mit Lager.
Muss: Hamburg und bis zu 30 km Umgebung; 80–180 m² Gesamtfläche; Büro und nutzbare Lagerfläche; maximal 2.000 Euro monatliche Nettokaltmiete; geeignete Anlieferung.
Wünsche: Stellplätze, kurzfristige Verfügbarkeit, öffentliche Verkehrsmittel.
Recherchiere über Work im Browser auf ImmoScout. Notiere Links, Abrufdatum, belegbare Angaben und offene Fragen. Keine Anbieter kontaktieren. Fehlende passende Treffer sind ein gültiges Rechercheergebnis.

ERSATZOBJEKTE – VOLLSTÄNDIG FIKTIV, KEINE REALEN INSERATE
A: Hamburg-Ost; 120 m², davon 40 m² Büro und 80 m² Lager; 1.650 Euro Nettokaltmiete; 250 Euro Nebenkosten pro Monat; ebenerdige Anlieferung; zwei Stellplätze je 50 Euro monatlich; Nutzung als Lager laut Beispieldaten erlaubt. Verfügbarkeit offen.
B: Hamburg-West; 95 m² Büro; 1.400 Euro Nettokaltmiete; 200 Euro Nebenkosten; Obergeschoss ohne Lastenaufzug; Lagerfläche nicht ausgewiesen. Nutzung und Anlieferung ungeklärt.
C: Musterstandort südlich Hamburgs, Entfernung nur ungefähr 25 km angegeben; 170 m², davon 50 m² Büro und 120 m² Lager; 1.950 Euro Nettokaltmiete; Nebenkosten nicht angegeben; Rolltor vorhanden; zwei Stellplätze enthalten; Verfügbarkeit und genehmigte Nutzung offen.
Vergleiche die Ersatzobjekte nur als fiktive Fallstudie. Erfinde keine URLs, tatsächlichen Fahrtstrecken oder fehlenden Kosten.
''',
'07-terminbrief.txt':'''TERMINBRIEF – FIKTIVE ÜBUNGSDATEN
Vorgang: Lindenhof LH-026
Anlass: Besichtigung und Klärung des Leistungsumfangs
Dauer: 45 Minuten, zusätzlich Fahrtzeit nach eigener Einschätzung
Ort: Musterweg 12, 20000 Musterstadt, fiktive Adresse – nicht als reale Navigation verwenden
Beteiligte: eigene Projektleitung und Mara Sommer. Ihre Verfügbarkeit ist nicht bekannt.
Zeitfenster: Dienstag bis Donnerstag der kommenden Woche, zwischen 09:00 und 15:00 Uhr, Europe/Berlin. Ersetze relative Angaben vor Einrichtung durch konkrete Daten.
Agenda: Zugang; Türmaße; Trennwandaufbau; gewünschtes Ausführungsfenster.
Erinnerung: Am Vortag um 15:00 Uhr die Unterlagen prüfen.
Wiederkehrende Aufgabe: Jeden Montag um 08:30 Uhr, Europe/Berlin, vier Wochen lang die offenen Punkte im Übungsprojekt zusammenfassen. Nur bei neuen offenen Punkten oder nötiger Entscheidung benachrichtigen, falls die eingesetzte Funktion dies unterstützt.
Übung: Zeige Vorschlag und offene Punkte zuerst. Keine Einladung an fiktive E-Mail-Adressen versenden. Ein optionaler Testtermin bleibt im eigenen Kalender und trägt den Titel ÜBUNG Lindenhof. Kontrolliere anschließend die Speicherung. Deaktiviere Wiederholungen nach dem Workshop.
''',
'08-parkblick.txt':'''PRAXISUMBAU PARKBLICK – FIKTIVE ABSCHLUSS-CHALLENGE
Alle Angaben sind erfunden.

ANFRAGE – Stand 23.09.2026
Nils Berger <nils.berger@parkblick.example> bittet Werkraum Ausbau um die Vorbereitung eines Praxisumbaus. Vier Innentüren sollen ausgetauscht werden. Ein verbindliches Angebot ist erst nach Aufmaß möglich. Gewünschtes Zeitfenster: November 2026, noch nicht bestätigt. Budget wurde nicht genannt. Praxisbetrieb soll nach Möglichkeit weiterlaufen.
Objekt: Beispielallee 8, 20000 Musterstadt, fiktiv.
Vorgangsnummer PB-026. Besichtigung 60 Minuten. Kundenverfügbarkeit und Zugang sind offen.

MATERIALANGEBOTE – Alle netto, gleiche technische Spezifikation vorerst nur angenommen
Anbieter Nord: 4 Türsets zu je 240 Euro, Lieferung pauschal 70 Euro, Lieferzeit 12 Werktage ab Bestellung.
Anbieter Mitte: 4 Türsets zu je 255 Euro, Lieferung enthalten, Lieferzeit 8 Werktage ab Bestellung.
Anbieter Süd: 4 Türsets zu je 230 Euro, Lieferung pauschal 130 Euro, Lieferzeit nicht angegeben.
Montage, Entsorgung und Zusatzarbeiten sind in keinem Angebot enthalten.

UNTERLAGENLÜCKEN
Türmaße; Öffnungsrichtungen; Anforderungen an Brand- und Schallschutz; Zugang; Umgang mit Praxisbetrieb; Kundenverfügbarkeit; verbindlicher Ausführungstermin.

DEIN AUFTRAG
Erstelle eine kurze Zusammenfassung, offene Fragen, einen nachvollziehbaren Materialkostenvergleich, einen ausgefüllten Projektbogen und einen Kundenantwortentwurf mit Besichtigungsvorschlag. Nutze mindestens drei Workshop-Fähigkeiten. Verbindliche Zusagen und Versand gehören nicht zur Aufgabe. Verwende die leere DOCX-Vorlage aus dem Materialpaket. Prüfe die Ergebnisse auf Widersprüche.
'''
}
for name,text in files.items():(out/name).write_text(text)
d=Document();sec=d.sections[0];sec.top_margin=Cm(2);sec.bottom_margin=Cm(2);sec.left_margin=Cm(2.2);sec.right_margin=Cm(2.2)
style=d.styles['Normal'];style.font.name='Arial';style.font.size=Pt(10);style.paragraph_format.space_after=Pt(7)
d.styles['Title'].font.color.rgb=RGBColor(0,0,0)
for st in d.styles:
 for element in list(st.element.iter()):
  if element.tag.endswith('}pBdr') and element.getparent() is not None: element.getparent().remove(element)
d.add_paragraph('Projektbogen',style='Title');d.add_paragraph('Werkraum Ausbau · Fiktive Workshopvorlage')
d.add_paragraph('Übertrage belegte Angaben aus dem Informationspaket. Markiere fehlende Informationen als offen und nenne bei widersprüchlichen Angaben beide Quellen.')
t=d.add_table(rows=1,cols=2);t.style='Light Shading Accent 1';t.rows[0].cells[0].text='Feld';t.rows[0].cells[1].text='Angabe und Quelle'
for field in ['Vorgangsnummer','Kunde','Ansprechpartner und E-Mail','Objekt','Leistungsumfang','Maße und technische Anforderungen','Gewünschtes Zeitfenster','Bestätigter Ausführungstermin','Zugang und Verfügbarkeit','Budget oder Preisgrundlage','Nächster Schritt']:
 c=t.add_row().cells;c[0].text=field;c[1].text='[hier ausfüllen]'
d.add_paragraph('Offene Fragen',style='Heading 2');d.add_paragraph('[Fehlende und widersprüchliche Angaben hier sammeln.]')
d.add_paragraph('Prüfung',style='Heading 2');d.add_paragraph('Sind alle Angaben belegt? Sind Vorschläge erkennbar? Wurden unbestätigte Preise und Termine als offen markiert?')
d.sections[0].footer.paragraphs[0].text='Fiktive Übungsdaten · Keine Auftragsbestätigung'
d.save(out/'05-projektbogen.docx')
print('7 Textdateien und DOCX-Vorlage erstellt')
