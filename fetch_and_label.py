import pandas as pd

from functions.setup_selenium import setup_selenium
from functions.scrape_rechtspraak_query import scrape_rechtspraak_query
from functions.label_with_llm import label_with_llm

SCRAPE_LIMIT = 2
LLM_PROVIDER = "ollama"

selenium_driver = setup_selenium(headless=False)

try:
    scraped_uitspraken = scrape_rechtspraak_query(selenium_driver, limit=SCRAPE_LIMIT)
    labeled_uitspraken = [label_with_llm(uitspraak, provider=LLM_PROVIDER) for uitspraak in scraped_uitspraken]

    print(labeled_uitspraken)

    if labeled_uitspraken:
        records = [{"inhoud": u.inhoud, **u.model_dump()} for u in labeled_uitspraken]
        pd.DataFrame(records).to_csv("uitspraken.csv", index=False)
finally:
    selenium_driver.quit()
