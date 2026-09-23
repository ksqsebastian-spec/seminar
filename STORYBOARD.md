> Historischer Entwurf. Die aktuelle vereinfachte Fassung mit 34 Folien wird in `scripts/content.py` gepflegt.

# KI, die mitarbeitet.

## Verbindlicher Rahmen

Deutschsprachiger Workshop für vollständige Anfänger aus Handwerk und Bau. Neutrales Branding, Ansprache mit „du“. Alle arbeiten in der Work-Oberfläche aus dem bereitgestellten Screenshot mit eigenen Lizenzen und verbundenen Microsoft-365-Konten. Kein technischer Codex-Unterricht. Browseraufgaben werden aus Work heraus angestoßen. Excel wird sowohl direkt in Excel als auch über Dateien in Work behandelt.

Präsenzformat mit eigenen Laptops. Modular für einen intensiven Tag oder mehrere Termine. Keine Moderationsnotizen. Präsentationswebsite mit zusätzlicher frei navigierbarer Lernansicht. Veröffentlichung später im Repository `seminar` über einen neuen Cloudflare Worker mit serverseitigem Passwortschutz. Das vereinbarte Passwort gehört ausschließlich in die Deployment-Secrets, nicht in dieses Repository.

**Lernziel:** Du kannst eine alltägliche Büroaufgabe mit KI selbstständig vorbereiten, bearbeiten, verbessern und prüfen. Du kannst erkennen, welche Informationen fehlen und welche Handlungen deine Entscheidung benötigen.

**Stand:** Ausgearbeitetes Inhaltsstoryboard. Animationen sind hier beschrieben, noch nicht implementiert. Produktfunktionen, Kontozugänge und konkrete Plugin-Aktionen müssen vor Aufnahme der Demos in der tatsächlichen Work-Umgebung verifiziert werden. Die Beispiele sind didaktische Szenarien und keine Behauptung, dass jede Verbindung jede Aktion unterstützt.

## Dramaturgie und Interaktion

Jedes Modul folgt demselben Rhythmus: Alltagssituation → ein schrittweise animiertes Beispiel → offene Herausforderung → Ergebnischeck. Auf den Präsentationsfolien steht wenig Text; ergänzende Aufgabeninformationen erscheinen in der Lernansicht und in aufklappbaren Hilfen.

- Beispielanimation: drei bis vier Zustände, jeweils per „Weiter“ ausgelöst; „Zurück“ und „Neu starten“ jederzeit verfügbar.
- Keine automatisch durchlaufenden Texte, keine dekorativen Tippanimationen, keine Simulation als echte Live-Aktion ausgeben.
- Demonstrationen sichtbar als „Beispiel mit fiktiven Daten“ kennzeichnen. Live-Übungen getrennt davon.
- Jede Aufgabe hat ein Ziel, Ausgangsmaterial und drei überprüfbare Kriterien. Der Lösungsweg bleibt offen.
- Hilfen in drei Stufen: Denkanstoß → Vorgehensidee → kopierbarer Beispielauftrag.
- Optionaler „Schon fertig?“-Impuls für schnellere Teilnehmende.
- Selbstcheck statt Punktewertung oder Wettbewerb. Fortschritt bedeutet „angesehen“ oder „selbst ausprobiert“, nicht nachgewiesene Kompetenz.
- Tastaturbedienung, sichtbarer Fokus, ausreichend Kontrast und reduzierte Bewegung berücksichtigen.

## Gemeinsame Übungswelt

**Werkraum Ausbau – fiktiver Handwerksbetrieb.** Innenausbau, Montage und kleinere Umbauten. Alle Personen, Vorgänge, Angebote und Geschäftsdaten sind erfunden. E-Mail-Beispiele verwenden ausschließlich `.example`-Adressen.

Drei unabhängige Vorgänge verhindern, dass eine gescheiterte Aufgabe den weiteren Workshop blockiert:

1. **Bauvorhaben Lindenhof:** Büroräume modernisieren; Anfrage verstehen, Unterlagen finden, Rückfragen und Besprechung vorbereiten.
2. **Materialeinkauf:** drei Angebote für dieselbe Materialmenge vergleichen, Gesamtkosten und Lieferbedingungen prüfen.
3. **Neuer Standort:** Büro mit Lagerfläche suchen, Kriterien und belegbare Fundstellen vergleichen.

Fiktive Inhalte werden in echten verbundenen Konten in einem klar benannten Übungsbereich verwendet. Vorbereitete Mailtexte können als Dateien bearbeitet werden, wenn keine fiktiven Nachrichten im Konto vorliegen. Der Workshop hängt nicht davon ab, echte geschäftliche Korrespondenz zu verwenden.

## Auftakt · Folien 01–04

### 01 · KI, die mitarbeitet.

**Auf der Folie:** „Weniger suchen. Klarer entscheiden. Arbeit fertig bekommen.“

Keynote-artiger Auftakt: eine übergroße, präzise gesetzte Überschrift auf großzügiger weißer Fläche. Die Verben „finden“, „verstehen“, „erledigen“ erscheinen nacheinander als einzelne, farbige typografische Momente. Keine Produktversprechen oder erfundenen Zeitersparnisse.

### 02 · Was würdest du heute gern abgeben?

**Auf der Folie:** „Eine nervige Aufgabe reicht.“

Drei alltagsnahe Anstöße: Informationen zusammensuchen; Tabellen aufräumen; dieselben Dinge immer wieder schreiben. Kurzer Austausch im Raum. Keine Eingabe persönlicher Daten erforderlich.

### 03 · Unsere Werkstatt für heute

**Auf der Folie:** „Ein fiktiver Betrieb. Echte Aufgaben. Deine Entscheidungen.“

Werkraum Ausbau und die drei Vorgänge vorstellen. Zeigen, wo Übungsdateien, Kapitel und Hilfen liegen. Verbundene Konten einmal praktisch prüfen. Vorbereitete Dateien als Alternative bereithalten.

### 04 · Drei Gewohnheiten, die bleiben

**Auf der Folie:** „Klar beauftragen. Gemeinsam verbessern. Ergebnis prüfen.“

Animation: Auftrag → erste Fassung → Rückfrage → überarbeitete Fassung → Prüfung. Die erste Ausgabe ist ein Arbeitsstand.

## Modul 1 · In Work ankommen · Folien 05–08

### 05 · Aus einem Gedanken wird eine Aufgabe

**Auf der Folie:** „Beschreib, was am Ende fertig sein soll.“

An der echten Oberfläche zeigen: Aufgabe beginnen, Material hinzufügen, Ergebnis ansehen und weiterarbeiten. Nur verifizierte Bedienelemente benennen. Modellnamen und wechselnde Produktdetails nicht als Lernziel behandeln.

### 06 · Beispiel: Montag, 08:12 Uhr

**Auf der Folie:** „Fünf Notizen. Ein brauchbarer Start.“

**Animation:**
1. Notizzettel: „Lieferung unklar; Lindenhof fragt nach Termin; Angebot prüfen; Team informieren; Formular fehlt.“
2. Auftrag: „Ordne diese Notizen in nächste Schritte. Markiere fehlende Informationen. Erfinde keine Termine.“
3. Ergebnis: Aufgabe / nächster Schritt / benötigte Information.
4. „Lieferung unklar“ erhält die Rückfrage „Welcher Lieferant und welcher Vorgang?“.

### 07 · Du bist dran: Bring Ordnung rein

**Ziel:** Erstelle aus `01-tagesnotizen.txt` einen Arbeitsplan, mit dem eine andere Person weiterarbeiten könnte.

**Erfolgskriterien:** Alle fünf Themen sind enthalten; die nächsten Schritte sind konkret; unbekannte Zuständigkeiten und Zeiten sind als offen markiert.

**Hilfen:** Was ist Information, was ist Aufgabe? / Lass eine erste Struktur erstellen und überarbeite sie. / „Mach aus diesen Notizen eine übersichtliche Aufgabenliste. Trenne bekannte Fakten von offenen Fragen. Schlage eine Reihenfolge vor und begründe sie kurz.“

**Schon fertig?** Lass dir eine kompakte Version für eine kurze Teambesprechung erstellen.

### 08 · Woran erkennst du ein brauchbares Ergebnis?

**Auf der Folie:** „Kann jemand damit weiterarbeiten?“

Check: vollständig, konkret, ohne erfundene Zusagen. Zwei unterschiedliche Lösungen können beide gut sein.

## Modul 2 · Gute Arbeitsaufträge und Fehlerbehebung · Folien 09–12

### 09 · Sag mehr als „Mach mal“

**Auf der Folie:** „Ziel. Kontext. Material. Grenzen. Ergebnis.“

Kein auswendig zu lernender Spezialprompt. Fünf einfache Fragen: Was soll fertig sein? Für wen? Auf welcher Grundlage? Was darf nicht passieren? In welcher Form brauche ich es?

### 10 · Beispiel: Die viel zu freundliche Zusage

**Animation:**
1. Auftrag: „Beantworte die Kundenanfrage.“
2. Absichtlich mangelhafter Entwurf: „Wir garantieren die Fertigstellung bis Freitag.“
3. Korrektur: „Ein Termin ist noch nicht bestätigt. Entferne die Zusage und frage nach dem gewünschten Zeitfenster. Maximal 120 Wörter.“
4. Überarbeiteter Entwurf mit klarer Rückfrage statt Zusage.

### 11 · Du bist dran: Rettet diesen Entwurf

**Ziel:** Verbessere `02-fehlerhafter-entwurf.txt` anhand der Kundenanfrage.

**Erfolgskriterien:** Keine unbelegte Termin- oder Preiszusage; die zwei fehlenden Angaben werden erfragt; Ton und Länge passen zu einer Kundenmail.

**Hilfen:** Welche Behauptung steht nicht in der Quelle? / Benenne den Fehler und das gewünschte Verhalten. / „Vergleiche Entwurf und Anfrage. Markiere unbelegte Aussagen und schreibe eine sachliche Antwort. Frage fehlende Angaben ab, statt sie zu ergänzen.“

**Schon fertig?** Lass erklären, welche Änderungen nötig waren und welche Quelle sie begründet.

### 12 · Wenn es hakt: kleiner, klarer, überprüfbar

**Auf der Folie:** „Fehler benennen. Grundlage zeigen. Einen Schritt erneut versuchen.“

Drei Fälle: falscher Inhalt → Fundstelle zeigen; falsch gelesene Datei → betroffene Seite oder Zeile prüfen; festhängender Browser → letzten sichtbaren Zustand beschreiben und nächsten Schritt eingrenzen. Vor Wiederholungen prüfen, ob eine Handlung bereits ausgeführt wurde, besonders bei Versand oder Terminen.

## Modul 3 · Projekte und wiederverwendbarer Kontext · Folien 13–16

### 13 · Nicht jeden Morgen von vorn

**Auf der Folie:** „Ein Vorgang. Ein gemeinsamer Arbeitskontext.“

Ein Projekt als organisatorischen Ort für zusammengehörige Arbeit erklären. Welche Dateien, Hinweise und Aufgaben die konkrete Work-Version darin tatsächlich gemeinsam nutzt, wird live verifiziert. Unterschied zwischen einer einzelnen Aufgabe und dauerhaft nützlichen Projektvorgaben zeigen.

### 14 · Beispiel: Bauvorhaben Lindenhof

**Animation:**
1. Verstreute Informationen: Kundenanfrage, Projektbogen, Kommunikationsregeln.
2. Projekt „Lindenhof – Büroausbau“ entsteht als schematische Darstellung.
3. Vorgabe: „Kundenfreundlich und sachlich. Keine Preise oder Termine verbindlich zusagen. Fehlende Angaben markieren.“
4. Neuer Auftrag greift die Vorgaben auf; Ergebnis wird dennoch geprüft.

### 15 · Du bist dran: Richte deinen Arbeitskontext ein

**Ziel:** Organisiere die vorbereiteten Lindenhof-Unterlagen so, dass du im nächsten Schritt eine Kundenantwort erarbeiten kannst.

**Erfolgskriterien:** Der Vorgang ist eindeutig benannt; relevante Quellen sind auffindbar; drei sinnvolle Arbeitsregeln sind formuliert.

**Hilfen:** Was gilt für jede Aufgabe dieses Vorgangs? / Trenne Vorgaben von veränderlichen Fakten. / „Formuliere aus diesem Projektbrief drei kurze Arbeitsregeln und eine Übersicht der offenen Angaben. Kennzeichne Vorschläge als Vorschläge.“

**Schon fertig?** Starte eine neue Aufgabe im Projekt und prüfe ausdrücklich, welcher Kontext verfügbar ist.

### 16 · Kontext pflegen gehört dazu

**Auf der Folie:** „Aktuell schlägt ausführlich.“

Veraltete Stände erkennen, widersprüchliche Vorgaben korrigieren, gültige Quellen kennzeichnen. Nicht davon ausgehen, dass jede frühere Unterhaltung automatisch verfügbar ist.

## Modul 4 · Plugins und Microsoft 365 · Folien 17–20

### 17 · Verbinden, damit Informationen erreichbar werden

**Auf der Folie:** „Welche Quelle braucht diese Aufgabe?“

Mail für Nachrichten, OneDrive für Unterlagen, Kalender für Termine. Plugin-Namen, Einrichtung und mögliche Aktionen anhand der tatsächlich verfügbaren Verbindungen zeigen. Zugriff auf eine Quelle ist nicht automatisch eine Freigabe für jede weitere Handlung.

### 18 · Beispiel: Welche Unterlage gilt?

**Animation:**
1. Frage: „Welche Unterlagen fehlen für Lindenhof?“
2. Quellen: Kundenanfrage und Projektbogen aus dem Übungsbereich.
3. Gegenüberstellung: vorhanden / fehlt / widersprüchlich.
4. Quellverweise werden hervorgehoben; die veraltete Notiz bleibt als veraltet markiert.

### 19 · Du bist dran: Finde die Grundlage

**Ziel:** Finde die passenden Lindenhof-Unterlagen im verbundenen Übungsbereich und erstelle eine kurze Quellenübersicht.

**Erfolgskriterien:** Die richtigen Dateien sind identifiziert; Herkunft und Stand sind nachvollziehbar; fehlende Zugriffe werden offengelegt.

**Hilfen:** Suche nach eindeutigem Vorgangsnamen. / Grenze Quelle und Ordner ein. / „Suche im Übungsbereich nach Lindenhof. Nenne passende Dateien mit Fundstelle und Stand, soweit sichtbar. Sage ausdrücklich, wenn du eine Quelle nicht lesen kannst.“

**Schon fertig?** Vergleiche zwei Fassungen und begründe, welche Information aktuell ist.

### 20 · Lesen, Entwerfen, Ausführen

**Auf der Folie:** „Was darf die KI jetzt tatsächlich tun?“

Die drei Handlungstypen unterscheiden. Vor Ausführung Ziel, Empfänger, Inhalt und Umfang prüfen. Freigabeoptionen in Work nur anhand ihrer verifizierten aktuellen Bedeutung erklären; keine pauschale Empfehlung für automatische Freigaben.

## Modul 5 · Mail und OneDrive · Folien 21–24

### 21 · Vom Posteingang zum nächsten Schritt

**Auf der Folie:** „Verstehen. Unterlagen finden. Antwort vorbereiten.“

Ein Kunde möchte ein Angebot, nennt aber weder einen vollständigen Leistungsumfang noch ein bestätigtes Ausführungsfenster.

### 22 · Beispiel: Die Antwort mit den richtigen Rückfragen

**Animation:**
1. Auszug aus der fiktiven Anfrage.
2. Zugehöriger Projektbogen ergänzt gesicherte Fakten.
3. Drei Rückfragen werden sichtbar: Umfang, Zugang zum Gebäude, gewünschtes Zeitfenster.
4. Antwortentwurf mit Quellencheck; kein Versand in der Animation.

### 23 · Du bist dran: Mach den Vorgang bearbeitbar

**Ziel:** Erstelle eine kurze Vorgangszusammenfassung und einen passenden Antwortentwurf aus den bereitgestellten Unterlagen.

**Erfolgskriterien:** Anliegen korrekt wiedergegeben; Rückfragen auf tatsächliche Lücken begrenzt; keine erfundenen Preise, Termine oder Anlagen.

**Hilfen:** Welche Antwort braucht ihr, bevor ihr anbieten könnt? / Lass Fakten und Fragen zunächst getrennt sammeln. / „Fasse die Anfrage zusammen, nutze die zugehörigen Unterlagen und entwirf eine kurze Antwort. Stelle nur notwendige Rückfragen. Noch nicht versenden.“

**Schon fertig?** Erstelle eine interne Übergabe mit nächstem Schritt und offener Zuständigkeit.

### 24 · Bereit zum Versenden?

**Auf der Folie:** „Empfänger. Aussagen. Anhänge. Zusagen.“

Den Entwurf gegen die Quelle prüfen. Ein Übungsentwurf muss nicht versendet werden, um das Lernziel zu erreichen. Ein absichtlich gewünschter Testversand braucht ein festgelegtes Testziel.

## Modul 6 · Internetrecherche und Browser · Folien 25–28

### 25 · Gesucht: Platz für den nächsten Schritt

**Auf der Folie:** „Büro plus Lager. Mit nachvollziehbarer Auswahl.“

Suchauftrag: Hamburg und bis zu 30 km Umgebung; 80–180 m² Gesamtfläche; Büro und nutzbare Lagerfläche; maximal 2.000 Euro monatliche Nettokaltmiete; geeignete Anlieferung. Das sind Übungskriterien, keine Marktbehauptung.

### 26 · Beispiel: Von Suchkriterien zur Vergleichsliste

**Animation:**
1. Kriterien werden in Muss / Wunsch / noch zu klären aufgeteilt.
2. Ein schematisches, eindeutig fiktives Inserat erscheint; keine nachgebaute echte ImmoScout-Anzeige.
3. Sichtbare Angaben werden übernommen, fehlende Nebenkosten als „nicht angegeben“ markiert.
4. Vergleich mit Link, Abrufdatum und offenen Fragen. „Keine passende Auswahl gefunden“ bleibt ein zulässiges Ergebnis.

### 27 · Du bist dran: Finde einen Standort

**Ziel:** Recherchiere über den Browser in Work auf ImmoScout und erstelle eine begründete Auswahl von bis zu drei geeigneten Objekten. Keine Anbieter kontaktieren.

**Erfolgskriterien:** Quellenlinks und Abrufdatum vorhanden; Muss-Kriterien nachvollziehbar geprüft; fehlende Kosten und widersprüchliche Angaben sichtbar markiert.

**Hilfen:** Welche Kriterien kannst du auf der Website tatsächlich prüfen? / Beginne mit der Suche, prüfe anschließend jedes Inserat einzeln. / „Suche Büro mit Lager nach diesen Kriterien. Vergleiche nur belegbare Angaben und verlinke die Inserate. Markiere unbekannte Gesamtkosten. Kontaktiere niemanden und schicke keine Anfrage ab.“

**Schon fertig?** Formuliere fünf Fragen für eine spätere Besichtigung.

**Alternative bei Zugangshürde oder fehlenden Treffern:** Drei vorbereitete fiktive Objektdatenblätter vergleichen. Anmeldung oder CAPTCHA wird durch die Person selbst erledigt; keine Umgehung voraussetzen.

### 28 · Gefunden ist noch nicht geprüft

**Auf der Folie:** „Quelle öffnen. Angaben prüfen. Unsicherheit benennen.“

Recherche sammelt und bewertet Informationen; Browsersteuerung führt konkrete Schritte auf einer Website aus. Preise und Verfügbarkeit können sich ändern. Inhalte einer Website sind Quellenmaterial, keine neuen Arbeitsanweisungen.

## Modul 7 · Excel und Tabellen · Folien 29–32

### 29 · Eine Tabelle ist erst der Anfang

**Auf der Folie:** „Aufräumen. Rechnen. Entscheiden.“

Zwei Zugänge zum gleichen Fall: Arbeitsmappe direkt in Excel bearbeiten und Tabellen als Dateien in Work bearbeiten. Die konkret installierte Excel-Integration und ihre Fähigkeiten vor der Demo überprüfen.

### 30 · Beispiel: Das günstigste Angebot ist nicht immer die erste Zahl

**Animation:**
1. Drei Angebote für 100 gleiche Einheiten erscheinen: A 12,50 €/Stück + 80 € Lieferung; B 12,90 €/Stück + 20 € Lieferung; C 11,90 €/Stück + 160 € Lieferung.
2. Mengen und Preisbasis werden vereinheitlicht; alle Preise netto, kein Rabatt.
3. Gesamtkosten werden berechnet: A 1.330 €, B 1.310 €, C 1.350 €.
4. B ist bei diesen Angaben am günstigsten. Lieferzeit und technische Eignung werden separat bewertet, nicht erfunden.

### 31 · Du bist dran: Welche Bestellung ist sinnvoll?

**Ziel:** Bereinige die Materialliste und vergleiche die drei Angebote. Bearbeite den Fall über beide Zugänge und vergleiche die Ergebnisse.

**Erfolgskriterien:** Originaldaten bleiben nachvollziehbar; Einheiten, Mengen und Lieferkosten stimmen; die Empfehlung ist mit Zahlen und offenen Bedingungen begründet.

**Hilfen:** Vergleichen alle Angebote dieselbe Menge? / Trenne Quelldaten, Berechnung und Empfehlung. / „Prüfe diese Angebote auf gleiche Mengen und Preisbasis. Berechne nachvollziehbare Gesamtpreise inklusive angegebener Lieferkosten. Markiere fehlende Angaben und prüfe die Rechnung mit einer zweiten Berechnung.“

**Schon fertig?** Berechne, ob sich die Reihenfolge bei 200 Einheiten ändert, sofern Lieferkosten unverändert bleiben. Kennzeichne diese Annahme.

### 32 · Gute Tabelle, richtige Rechnung?

**Auf der Folie:** „Stichprobe statt blindem Vertrauen.“

Eine Zeile manuell nachrechnen. Formeln, Datentypen, Filter und Summen prüfen. Darstellungsqualität ist kein Beleg für korrekte Zahlen.

## Modul 8 · Dateien bearbeiten und Formulare ausfüllen · Folien 33–36

### 33 · Aus Unterlagen wird ein fertiges Dokument

**Auf der Folie:** „Übernehmen, was belegt ist. Offen lassen, was fehlt.“

Projektbogen, Übergabeprotokoll und Kundeninformation als Beispiele. DOCX und PDF unterscheiden: Ein bearbeitbares Ergebnis und eine gut lesbare Ausgabe können unterschiedliche Formate brauchen.

### 34 · Beispiel: Ein Formular mit einer ehrlichen Lücke

**Animation:**
1. Leerer Projektbogen mit Feldern für Vorgang, Ansprechpartner, Leistung und Ausführungstermin.
2. Passende Informationen aus der Anfrage werden zugeordnet.
3. Ausführungstermin bleibt „noch nicht bestätigt“.
4. Fertige Fassung plus kurze Liste offener Angaben; keine erfundene Unterschrift oder Freigabe.

### 35 · Du bist dran: Mach das Dokument fertig

**Ziel:** Fülle den Projektbogen aus dem Lindenhof-Informationspaket und erstelle eine überarbeitbare Fassung. Prüfe anschließend die Darstellung.

**Erfolgskriterien:** Angaben lassen sich Quellen zuordnen; fehlende Informationen bleiben sichtbar; Datei öffnet korrekt und ist lesbar.

**Hilfen:** Welche Felder sind belegt? / Lass vor dem Ausfüllen eine Zuordnung erstellen. / „Fülle die Vorlage ausschließlich mit belegten Angaben aus den Unterlagen. Markiere fehlende oder widersprüchliche Informationen. Bewahre die Struktur und liefere eine bearbeitbare Fassung.“

**Schon fertig?** Erstelle eine kurze Kundeninformation aus demselben Material und prüfe beide Fassungen auf Widersprüche.

### 36 · Die Datei selbst ist Teil des Ergebnisses

**Auf der Folie:** „Öffnen. Lesen. Vergleichen.“

Tabellen, Seitenumbrüche, Sonderzeichen, Zahlen und Feldzuordnungen prüfen. Ein Downloadlink allein belegt noch kein brauchbares Dokument.

## Modul 9 · Kalender und Scheduling · Folien 37–40

### 37 · Ein Termin ist mehr als ein Datum

**Auf der Folie:** „Zeit, Beteiligte, Ort und Vorbereitung.“

Drei getrennte Fälle erklären: einen Kalendertermin organisieren; eine Erinnerung auslösen; wiederkehrende KI-Arbeit planen. Welche Funktionen verfügbar sind, hängt von den tatsächlich eingerichteten Werkzeugen ab.

### 38 · Beispiel: Baustellenbesprechung vorbereiten

**Animation:**
1. Auftrag: „45 Minuten, nächste Woche, vor Ort, mit Bauleitung.“
2. Unbekannte Verfügbarkeit der Bauleitung wird als offen markiert; eigener freier Kalenderplatz genügt nicht.
3. Terminvorschlag mit vollständigem Datum, Uhrzeit, Zeitzone, Ort und Agenda.
4. Separat: wöchentlicher Auftrag zur Prüfung offener Übungsaufgaben; Ausführungszeit, Quelle und Benachrichtigung werden explizit formuliert.

### 39 · Du bist dran: Termin plus Follow-up

**Ziel:** Bereite einen Baustellentermin aus dem Terminbrief vor und formuliere eine einmalige Erinnerung sowie eine wiederkehrende Aufgabe. Richte verfügbare Funktionen als klar gekennzeichnete Übung ein und prüfe sie.

**Erfolgskriterien:** Datum, Uhrzeit und Zeitzone eindeutig; Beteiligte und offene Verfügbarkeiten korrekt; wiederkehrende Aufgabe nennt Quelle, Rhythmus und gewünschte Benachrichtigung.

**Hilfen:** Was soll wann passieren? / Trenne Termin, Erinnerung und wiederkehrende Arbeit. / „Bereite aus diesen Angaben einen Terminvorschlag vor. Markiere unbekannte Verfügbarkeiten. Formuliere zusätzlich eine Erinnerung und einen wöchentlichen Prüfauftrag mit eindeutiger Zeitangabe. Zeige vor dem Einrichten die Details.“

**Schon fertig?** Lege fest, wann die Wiederholung endet und wann keine Nachricht nötig ist.

### 40 · Geplant heißt nicht überprüft

**Auf der Folie:** „Was läuft wann – und wie beendest du es?“

Gespeicherte Details am tatsächlichen Ort kontrollieren. Übungstermine und Wiederholungen nach Abschluss löschen oder deaktivieren. Eine behauptete Einrichtung im Chat ersetzt keine Bestätigung des tatsächlichen Systems.

## Modul 10 · Abschluss-Challenge · Folien 41–44

### 41 · Jetzt gehört der Ablauf dir

**Auf der Folie:** „Ein neuer Auftrag. Dein Weg zum Ergebnis.“

Neuer fiktiver Vorgang „Praxisumbau Parkblick“. Eigenständiges Datenpaket, damit kein Zwischenstand aus früheren Übungen vorausgesetzt wird.

### 42 · Der Auftrag

**Auf der Folie:** „Mach aus dieser Anfrage einen bearbeitbaren Vorgang.“

Erwartete Ergebnisse: kurze Zusammenfassung, Liste offener Fragen, nachvollziehbarer Kostenvergleich, bearbeitetes Projektdokument und Antwortentwurf mit Terminvorschlag. Verwende mindestens drei der geübten Fähigkeiten. Die Werkzeuge und Reihenfolge wählst du selbst.

### 43 · Zeig, was du geprüft hast

**Auf der Folie:** „Ergebnis. Quelle. Entscheidung.“

**Erfolgskriterien:** Ergebnisse passen zueinander; wichtige Aussagen und Zahlen sind belegt; offene Informationen und nötige Freigaben sind erkennbar.

**Optionale Hilfe:** „Zerlege diesen Vorgang in sinnvolle Arbeitsschritte. Sage, welche Unterlagen du für jeden Schritt brauchst. Beginne mit dem ersten Schritt und frage nach, wenn wesentliche Angaben fehlen.“

**Schon fertig?** Lass eine zweite Prüfung durchführen und entscheide selbst, welche Hinweise zutreffen.

### 44 · Was machst du morgen anders?

**Auf der Folie:** „Eine Aufgabe. Ein erster Versuch. Ein klarer Check.“

Alle formulieren ihren eigenen nächsten Einsatz: „Bei … nutze ich KI für … und prüfe anschließend …“. Abschließend Übungsautomationen kontrollieren und bereinigen. Kapitelnavigation und Downloads bleiben zum Nachschlagen verfügbar.

## Übungsmaterialien für die Umsetzung

| Datei oder Paket | Inhalt | Absichtliche Schwierigkeit |
|---|---|---|
| `01-tagesnotizen.txt` | Fünf unsortierte Alltagsthemen | Fehlende Zuständigkeit und Termine |
| `02-fehlerhafter-entwurf.txt` | Kundenanfrage plus unbrauchbarer Antwortentwurf | Unbelegte Zusage |
| `03-lindenhof/` | Anfrage, Projektbrief, ältere Notiz, Kommunikationsregeln | Veraltete Information und fehlender Umfang |
| `04-materialvergleich.xlsx` | Quelldaten, Materialliste, Platz für Auswertung | Zahl als Text, unterschiedliche Schreibweisen, Lieferkosten |
| `05-projektbogen.docx` | Bearbeitbare Vorlage | Unbestätigter Ausführungstermin |
| `06-standortsuche/` | Kriterien und drei fiktive Ersatz-Objektdatenblätter | Unbekannte Nebenkosten und Nutzbarkeit |
| `07-terminbrief.txt` | Beteiligte, Dauer, Ort, Zeitbedingungen | Fremde Verfügbarkeit unbekannt |
| `08-parkblick/` | Eigenständiges Abschlussmaterial | Kombination der bekannten Herausforderungen |

Diese Dateien sind als Produktionsumfang definiert und werden in der Umsetzungsphase erstellt; die Tabelle ist keine Downloadliste bereits vorhandener Dateien.

## Zeitmodelle

**Kompakter Präsenztag:** 09:00–17:00 einschließlich 60 Minuten Mittagspause und zwei Pausen à 15 Minuten; 390 Minuten Lernzeit. Richtwerte: Auftakt 15, Module 1–10 jeweils 20 / 30 / 25 / 25 / 40 / 45 / 55 / 40 / 40 / 55 Minuten. Das ist für Anfänger ambitioniert und braucht vollständig eingerichtete Zugänge.

**Empfehlung für vollständige Anfänger:** Zwei Tage mit je 4,5 Stunden Lernzeit plus Pausen. Tag 1: Auftakt, Module 1–6 und Wiederholung. Tag 2: kurzer Wiedereinstieg, Module 7–10 und ausführliche Praxis. Zusätzliche Zeit dient Übungen und Unterstützung statt zusätzlicher Themen. Noch kein reales Datum oder Kalendereintrag festgelegt.

## Visuelles Konzept und Mobbin-Referenzen

**Festgelegte Designrichtung nach Nutzerfeedback: Apple-Keynote-Anmutung mit spielerischen Farben.** Ruhig, hochwertig, bildstark und auf eine Aussage pro Szene konzentriert. Die folgenden angesehenen Mobbin-Screens dienen ausschließlich als funktionale Referenzen für die Lernansicht, nicht als visuelle Vorlage für die Präsentation:

- [Optimal Workshop – Lernansicht](https://mobbin.com/screens/5751af02-f5df-41ed-8daf-38f174e89bb9): linke Kapitelstruktur, große gelbe Medienfläche, deutliches Weiter-Element. Übernehmen: klare Trennung von Orientierung und Hauptinhalt.
- [Podia – Kursansicht](https://mobbin.com/screens/38cd9986-4d77-4342-97c9-96d5a1f0f0de): ruhige Inhaltsnavigation und kompakte Vor-/Zurück-Steuerung. Übernehmen: frei zugängliche Kapitel und zurückhaltende Navigation, ohne Kommentarbereich.
Die zuvor erwogene Duolingo-Richtung wurde verworfen und ist keine Designreferenz für die Umsetzung.

Eigene visuelle Richtung:

- **Komposition:** eine große Idee pro Szene, großzügiger Freiraum, übergroße Überschriften und wenige sorgfältig platzierte Elemente. Text darf bildfüllend wirken. Detailinformationen bleiben in der Lernansicht zugänglich.
- **Typografie:** klare, hochwertige Groteskschrift mit präzisen Abständen; starke Größenkontraste zwischen Überschrift, Beispiel und zurückhaltender Navigation.
- **Farben:** Weiß und nahezu Schwarz als ruhige Basis. Kobaltblau, Koralle, Limette und Violett als vorgeschlagene Akzentpalette; pro Szene eine dominante Akzentfarbe. Gelegentliche vollflächige Farbmomente und gezielte Farbverläufe schaffen Abwechslung.
- **Bildsprache:** große, scharf lesbare Dokumentausschnitte, Tabellen und ausgewählte Oberflächendetails. Ein relevantes Detail wird herangeholt, statt eine ganze Anwendung unleserlich klein abzubilden.
- **Bewegung:** bewusste Enthüllungen und fließende Übergänge zwischen Ausgangsmaterial und Ergebnis, vom Vortragenden per Klick gesteuert. Bewegungen erklären einen Arbeitsschritt; bei reduzierter Bewegung bleiben alle Zustände unmittelbar lesbar.
- **Rhythmus:** helle Erklärungen, dunkle dramaturgische Pausen und überraschende Farbflächen. Aufgaben erscheinen als klare, große Arbeitsaufträge. Kapitelnummern und Fortschritt bleiben dezent.
- **Produktcharakter:** Präsentation und digitales Nachschlagewerk. Keine spieltypischen Pfade, Belohnungen, Maskottchen oder bunten Lernkartenraster.

**Präsentieren:** volle Inhaltsfläche wie eine Keynote, ausgeblendete Kapitelnavigation und unaufdringliche Steuerung am unteren Rand. Große Schrift, Pfeiltasten, Vollbild und dezente Anzeige des Animationsschritts. Klicks innerhalb von Eingaben dürfen keine Folienwechsel auslösen.

**Entdecken:** links Kapitel, rechts Inhalt, darunter Aufgabe, Hilfen und Materialien. Direkte Kapitel-Links, Suchfunktion für Inhalte und wiederaufnehmbarer lokaler Fortschritt. Keine Teilnehmerkonten oder Cloud-Speicherung eigener Übungsergebnisse erforderlich.

**Mobiler Zugriff:** Inhalte untereinander, Navigation als aufklappbare Liste. Laptop ist das Übungsgerät; Nachschlagen soll auch auf dem Telefon funktionieren.

## Vor der technischen Umsetzung prüfen

1. Work-Projekte: Welche Inhalte sind projektweit verfügbar, welche nur innerhalb einer Aufgabe?
2. Microsoft-365-Verbindungen: tatsächliche Plugin-Namen, Autorisierung, verfügbare Lese- und Schreibaktionen; fehlende Funktionen in der Anleitung nicht versprechen.
3. Excel: installierte Integration, Berechtigungen, Bearbeitung und Dateiexport beider Wege.
4. Work-Browser: Einstieg und Interaktion in der Teilnehmeroberfläche; ImmoScout-Zugänglichkeit.
5. Scheduling: getrennte Prüfung von Kalenderaktion, Erinnerung und wiederkehrender KI-Aufgabe; Bestätigung und Deaktivierung zeigen.
6. Git-Ziel: lokaler Ordner enthält derzeit ein Git-Verzeichnis, aber keinen konfigurierten Remote. Repository `seminar` vor einem Push eindeutig zuordnen.
7. Cloudflare: Zielkonto und Authentifizierung ermitteln; neuen Worker erst in der Umsetzungsphase anlegen.

## Technischer Produktionsumfang

- Präsentationswebsite mit den 44 Inhaltsfolien, zehn schrittweisen Beispielen und zehn Herausforderungen.
- Inhalt strukturiert von Darstellung getrennt, damit Produktdetails aktualisiert werden können.
- Server prüft Zugang vor Auslieferung geschützter Inhalte und Übungsdownloads. Passwort als Secret; Session-Cookie mit geeigneten Sicherheitsattributen; Loginversuche begrenzen. Keine Passwortprüfung ausschließlich im Frontend.
- Login und Fehlermeldung knapp und verständlich. Keine Kontoregistrierung.
- Übungen speichern keine realen Kontoinhalte auf der Seminarwebsite.
- Deployment über Cloudflare Worker; Quellcode und Inhalte im zugeordneten `seminar`-Repository.
- Vor Veröffentlichung: Inhalte gegen Work prüfen, Rechenbeispiele verifizieren, Dateien öffnen und visuell prüfen, Navigation und Animationen testen, Passwortschutz einschließlich direkter Download-URLs prüfen, Desktop und mobile Darstellung kontrollieren.

## Fertig, wenn …

- Jede Herausforderung ohne Vorwissen aus einem vorherigen Übungsabschluss begonnen werden kann.
- Alle Beispielzustände sinnvoll vor- und zurückgespielt werden können.
- Dateien tatsächlich vorhanden, bearbeitbar und mit den Aufgaben konsistent sind.
- Fakten, Vorschläge und fehlende Angaben im Lehrmaterial klar unterscheidbar bleiben.
- Die Website authentifiziert erreichbar ist und ein unberechtigter Direktzugriff auf Inhalte oder Dateien scheitert.
- Keine unbelegten Work-Funktionen, erfundenen Live-Angebote oder echten personenbezogenen Übungsdaten veröffentlicht werden.
