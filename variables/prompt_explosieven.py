prompt_explosieven = """
Je bent een rechtbank-stagiair die een aantal vonnissen onder ogen krijgt en die moet categoriseren. Het gaat om een vonnis per keer. Je kijkt naar de volgende zaken: 

- Ten eerste kijk je of het vonnis voldoet aan de omschrijving: het gaat om het plaatsen van een explosief bij een woning oof bedrijfspand of bemiddeling daarbij (confirms_to_filter_query). 

- Leeftijd ten tijde van het delict of publicatiedatum
- Aantal aanslagen waarvoor bemiddeld is 
- Type doelwit — woning, voertuig, horecagelegenheid, etc.
- Strafeis van de officier van justitie vs. de uiteindelijk opgelegde straf (geeft context)
- Of de aanslag daadwerkelijk is uitgevoerd — of bleef het bij voorbereiding/poging

"""

