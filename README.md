# Rechtspraak-labeler
De code in deze _repository_ haalt voor een zoekopdracht op [rechtspraak.nl](https://rechtspraak.nl/) alle zoekresultaten binnen, en labelt deze met behulp van een taalmodel. Hiermee kun je dus uitspraken ophalen en labelen, zodat je snel onderzoek kunt doen naar grote hoeveelheden gerechtelijke uitspraken. Enkele voorbeelden van vragen die je hiermee kunt proberen te beantwoorden: 

- Wat is de gemiddelde leeftijd van iemand die opgepakt voor de handel in illegaal vuurwerk? 
- In hoeveel gevallen is een fietsendief al eerder veroordeeld? 
- Hoe vaak wordt iemand verminderd toerekeningsvatbaar verklaard bij het plegen van delict X? 

Deze code is geschreven in het kader van een AI-cursus voor journalisten van het [Fonds Bijzondere Journalistieke Projecten](https://fondsbjp.nl/).

## Benodigdheden 
De code is geschreven in Python, gebruik het liefst een moderne versie. Omdat we zowel scrapen als LLM's aanroepen, komen er relatief veel libraries bij kijken, zie `requirements.txt`. Installeer deze het liefst in een _virtual environment_ als `venv` of `conda`. 

Voor het scrapen dien je [Selenium](https://selenium-python.readthedocs.io/) te installeren, inclusief een bijbehorende _webdriver_ (bijv. geckodriver voor Firefox). 

## Het opzetten van je scraper
Met deze code kun je uitspraken op rechtspraak.nl binnenhalen en labelen. Hiervoor moet je de zoek-url hebben van de uitspraken waar je naar op zoek bent. Dat werkt vrij simpel. Zoek op de website naar je term/onderwerp, en kopieer de url daarvan. Maak ook een omschrijving van één of twee zinnen waarin je omschrijft waaraan de uitspraak precies moet voldoen om in de dataset terecht te komen. Die gebruiken we om eventuele niet-relevante resultaten van je zoekslag er alsnog uit te filteren. 

Het opzetten van je scraper doe je door een klasse aan te maken in de `classes/` map. Zie ook het voorbeeld `Uitspraak.py` daar (deze kun je kopiëren als basis). Wat je klasse in ieder geval nodig heeft: 
- Een naam, `class_name`
- Een zoek-url (zie hierboven), `search_url`
- Een omschrijving van je type uitspraak (zie hierboven), `filter_query`

Pas de prompt in de `variables/prompt.py` ook aan op basis van je schema.

Importeer je klasse en je prompt in het hoofdscript, `fetch_and_label.py` en draai dat script. 


