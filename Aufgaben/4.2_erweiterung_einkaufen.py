einkaufsliste_gegenstaende = ['Klopapier','Einhornzauber','Coronamaske','Milch','Schokolade','Chinesiche Instantnudeln']
vorname = 'Max'
einkaufsliste_anzahl = [2, 1, 5, 1, 100, 10]
einkaufsliste = zip(einkaufsliste_anzahl, einkaufsliste_gegenstaende)


for anzahl, gegenstand in einkaufsliste:
    print(f'Ich, {vorname}, soll heute {anzahl}x {gegenstand} einkaufen gehen.')
