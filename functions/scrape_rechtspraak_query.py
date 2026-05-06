import pandas as pd 
from classes.Uitspraak import Uitspraak

def scrape_rechtspraak_query(driver):
    # Take the uitspraak_type, get the standard url from the class and scrape the links to uitspraken from there. Go through all of these links and get the textual content of the uitspraken. Put these in an array of the provided class type, which you then convert ot a pandas dataframe

    uitspraak_type = Uitspraak()
    uitspraak_query_url = uitspraak_type.search_url 
