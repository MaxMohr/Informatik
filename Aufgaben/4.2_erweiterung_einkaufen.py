einkaufsliste_gegenstaende = ['Klopapier','Einhornzauber','Coronamaske','Milch','Schokolade','Chinesiche Instantnudeln']
vorname = 'Max'
einkaufsliste_anzahl = [2, 1, 5, 1, 100, 10]
einkaufsliste = zip(einkaufsliste_anzahl, einkaufsliste_gegenstaende)


for einkaufsliste_anzahl, einkaufsliste_gegenstaende in zip:
    print(f'Ich soll heute {einkaufsliste_anzahl}x {einkaufsliste_gegenstaende} einkaufen gehen.')

#for anzahl in einkaufsliste:
#    print(f'Ich soll heute {anzahl}x einkaufen gehen.')