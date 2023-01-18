mein_name = input('Wie heißt du? ')
alter = int(input('Gib dein Alter an: '))
party_freunde_anzahl = int(input('Wie viele Freunde sollen zu deiner Party kommen? '))
klasse_mitglieder_dieses_jahr = int(input('Wie viele sind in deiner Klasse? '))
klasse_mitglieder_letztes_jahr = int(input('Wie viele waren letztes Jahr in deiner Klasse? '))
anzahl_schuljahre = int(input('Wie lange bist du schon in der Schule (Jahre)? '))
geschlecht = input('Bist du Männlich oder Weiblich? (m/f) ')
ort = input('Wo wohnst du? ')
betriebssystem = input('Welches Betriebssystem nutzt du? ')
lieblingshobby = input('Was ist dein Lieblingshobby? ')
tage_seit_letzter_aktivitaet = int(input('Wann hast du zuletzt dein Lieblingshobby ausgelebt? In Tagen'))

# Namenslänge ausgabe
if len(mein_name) > 8:
    print('Was für ein langer Name!')
else:
    print('Dein Name hat unter 8 Zeichen.')

# Alter Ausgabe
if alter < 14:
    print('Ich darf in Wien zwischen 5 und 23h unterwegs sein.')
elif 14 < alter < 16:
    print('Ich darf laut Judengschutzgesetzt in Wien schon bis 1h Nachts unterwegs sein.')
elif alter > 16:
    print('Ich darf in Wien so lange ich will unterwegs sein.')

# Party Gäste
if party_freunde_anzahl < 5:
    print(f'Wird eine überschaubare Party. Es kommen {party_freunde_anzahl} Freunde von mir.')
elif 5 < party_freunde_anzahl:
    print('Die Party ist schon größer.')
elif party_freunde_anzahl > 20:
    print('Wird eine mächtige Party.')


# Klassenmitglieder - abgeändert damit es nicht heißt: Dieses Schuljahr haben -x Freunde....
if klasse_mitglieder_letztes_jahr > klasse_mitglieder_dieses_jahr:
    print(f'Dieses Schuljahr haben {klasse_mitglieder_letztes_jahr - klasse_mitglieder_dieses_jahr}  Freunde die Klasse verlassen.')
else:
    print('Wir sind noch immer gleich viele SchülerInnen in der Klasse.')


# Schuljahre
if 9 - anzahl_schuljahre <= 0:
    print('Ich habe meine Schulpflicht schon erfüllt.')
else:
    print(f'Ich habe noch {9 - anzahl_schuljahre} bis ich die Schulpflicht erreicht habe.')


# Geschlecht
if geschlecht=='f':
    print(f'Ich bin {mein_name} und bin weiblich.')
elif geschlecht=='m':
    print(f'Ich bin {mein_name} und bin männlich.')
else:
    print(f'Ich bin {mein_name} und bin weder männlich noch weiblich.')


# Ort
if ort=='Wien':
    print('Ich wohne in der Bundeshauptstadt von Österreich.')
else:
    print('Ich wohne nicht in Wien.')

if betriebssystem=='Mac'=='MacOS'=='Windows':
    print(f'Ich benutze {betriebssystem}.')
else:
    print(f'Ich benutze {betriebssystem}. Wahrscheinlich ist es Linux oder ich habe mich verschrieben.')


# Lieblingshobby
if tage_seit_letzter_aktivitaet >= 3:
    print(f'Heute werde ich wieder {lieblingshobby} machen/spielen :).')