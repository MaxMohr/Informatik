mein_name = 'Max'
alter = 15
party_freunde_anzahl = 12
klasse_mitglieder_dieses_jahr = 28
klasse_mitglieder_letztes_jahr = 30
anzahl_schuljahre = 9
geschlecht = 'm'
ort = 'Leopoldsdorf'
betriebssystem = 'Mac'
tage_seit_letzter_aktivitaet = 2
lieblings_hobby = 'Tennis'

# Alter
if alter < 14:
    print('Ich darf in Wien zwischen 5 und 23h unterwegs sein.')
elif alter >= 14 and alter <= 16:
    print('Ich darf in Wien schon bis 1h Nachts unterwegs sein.')
else:
    print('Ich darf in Wien so lange ich will unterwegs sein.')

# Name length
if len(mein_name) >= 8:
    print(f'Mein Name {mein_name} hat mehr als/genau 8 Zeichen.')
else:
    print(f'Mein Name {mein_name} hat weniger als 8 Zeichen.')

# Party
if party_freunde_anzahl < 5:
    print(f'Wird eine überschaubare Party. Es kommen {party_freunde_anzahl} Freunde von mir.')
elif 5 <= party_freunde_anzahl:
    print('Die Party ist schon größer.')
elif party_freunde_anzahl > 20:
    print('Wird eine mächtige Party.')


# KLassenmitglieder
if klasse_mitglieder_letztes_jahr > klasse_mitglieder_dieses_jahr:
    print(f'Dieses Schuljahr haben {klasse_mitglieder_letztes_jahr - klasse_mitglieder_dieses_jahr} Freunde die Klasse verlassen...')
else:
    print('Wir sind noch immer gleich viele SchülerInnen in der Klasse.')


# Schuljahre
if 9 - anzahl_schuljahre <= 0:
    print('Ich habe meine Schulpflicht bereits erledigt.')
else:
    print(f'Ich habe noch {9 - anzahl_schuljahre} bis ich die Schulpflicht erreicht habe.')


# Geschlecht
if geschlecht=='m':
    print(f'Ich bin {mein_name} und bin männlich.')
elif geschlecht=='f':
    print(f'Ich bin {mein_name} und bin weiblich.')
else:
    print(f'Ich bin {mein_name} und bin weder männlich noch weiblich.')


# Ort
if ort=='Wien':
    print('Ich wohne in der Bundeshauptstadt!')
else:
    print(f'Ich wohne nicht in Wien aber in, {ort}.')


# OS
if betriebssystem=='Windows'=='Mac':
    print(f'Ich benutze {betriebssystem}.')
else:
    print(f'Ich benutze wahrscheinlich Linux, oder kann nicht schreiben. ({betriebssystem})')


# Hobby
if tage_seit_letzter_aktivitaet >= 3:
    print(f'Heute werde ich wieder {lieblings_hobby} machen :).')