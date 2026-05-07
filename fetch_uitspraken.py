import pandas as pd

from classes.Uitspraak import Uitspraak
from functions.setup_selenium import setup_selenium
from functions.scrape_rechtspraak_query import scrape_rechtspraak_query

selenium_driver = setup_selenium(headless=False)

try:
    scraped_uitspraken = scrape_rechtspraak_query(selenium_driver, uitspraak_class=Uitspraak)
    output_file = "data/uitspraken.csv"
    pd.DataFrame([u.model_dump() for u in scraped_uitspraken]).to_csv(output_file, index=False)
    print(f"Saved {len(scraped_uitspraken)} uitspraken to {output_file}")
finally:
    selenium_driver.quit()
