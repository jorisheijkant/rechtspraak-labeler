import pandas as pd

from functions.setup_selenium import setup_selenium
from functions.scrape_rechtspraak_query import scrape_rechtspraak_query

from variables.prompt import prompt 

selenium_driver = setup_selenium(headless=False)
scraped_uitspraken = scrape_rechtspraak_query(driver)

if scraped_uitspraken:
    print(scraped_uitspraken)
    scraped_uitspraken.to_csv("uitspraken.csv")
