while True:
     try:
         alter = int(input("Geben Sie Ihr Alter in Jahren ein!: "))
         print(
"""                                        _______      _______   
            |     |         /\         |       |    |       |    \     /
            |     |        /  \        |       |    |       |     \   /
            |-----|       /----\       |_______|    |_______|      \_/
            |     |      /      \      |            |               |
            |     |     /        \     |            |               |
            
             _____             _______       _______                    _____  
            |     |     |     |       |         |          |     |     |     \           /\      \     / 
            |     |     |     |       |         |          |     |     |      \         /  \      \   /
            |-----      |     |______/\         |          |-----|     |       |       /----\      \_/
            |     |     |     |        \        |          |     |     |      /       /      \      |
            |_____|     |     |         \       |          |     |     |_____/       /        \     |

"""
         )
         print(
"""         
Alles gute zu Ihrem 21. Geburtstag! ;)
Von Max und Valerie
"""
               )
         break
     except ValueError:
       print(
           """
Na das war aber keine Zahl!
Versuche wir das nochmal!
           """
       )
