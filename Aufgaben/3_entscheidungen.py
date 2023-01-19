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

if alter < 14:
    print('Ich darf in Wien zwischen 5 und 23h unterwegs sein.')
elif alter >= 14 and alter <= 16:
    print('Ich darf in Wien schon bis 1h Nachts unterwegs sein.')
else:
    print('Ich darf in Wien so lange ich will unterwegs sein.')

if len(mein_name) >= 8:
    print(f'Mein Name {mein_name} hat mehr als/genau 8 Zeichen.')
else:
    print(f'Mein Name {mein_name} hat weniger als 8 Zeichen.')