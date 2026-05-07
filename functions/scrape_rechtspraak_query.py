import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pydantic import BaseModel
from tqdm import tqdm

from classes.Uitspraak import Uitspraak

LOAD_MORE_BTN_ID = "lib-rnl-lib-rnl-laadMeerBtn"
RESULT_CONTAINER_SELECTOR = ".rnl-listresults-item-container"
DETAIL_CONTENT_SELECTOR = ".rnl-detail-uitspraaktekst"
DETAIL_TITLE_SELECTOR = ".rs-panel-title"
LOAD_MORE_WAIT_SECONDS = 3
PAGE_LOAD_WAIT_SECONDS = 4


def scrape_rechtspraak_query(driver: webdriver.Firefox, uitspraak_class: type[BaseModel] = Uitspraak, limit: int | None = None) -> list[BaseModel]:
    driver.get(uitspraak_class.search_url)
    time.sleep(PAGE_LOAD_WAIT_SECONDS)
    _load_all_results(driver)
    links = _collect_result_links(driver)
    if limit is not None:
        links = links[:limit]
    results = []
    with tqdm(links, desc="Scraping uitspraken", unit="uitspraak") as progress:
        for link in progress:
            progress.set_postfix(url=link[-40:])
            results.append(_scrape_detail(driver, link, uitspraak_class))
    return results


def _load_all_results(driver: webdriver.Firefox) -> None:
    while True:
        buttons = driver.find_elements(By.ID, LOAD_MORE_BTN_ID)
        if not buttons or not buttons[0].is_displayed():
            break
        buttons[0].click()
        time.sleep(LOAD_MORE_WAIT_SECONDS)


def _collect_result_links(driver: webdriver.Firefox) -> list[str]:
    containers = driver.find_elements(By.CSS_SELECTOR, RESULT_CONTAINER_SELECTOR)
    links = []
    for container in containers:
        anchors = container.find_elements(By.TAG_NAME, "a")
        if anchors:
            links.append(anchors[0].get_attribute("href"))
    return links


def _scrape_detail(driver: webdriver.Firefox, url: str, uitspraak_class: type[BaseModel]) -> BaseModel:
    driver.get(url)
    time.sleep(PAGE_LOAD_WAIT_SECONDS)
    uitspraak = uitspraak_class()
    title_elements = driver.find_elements(By.CSS_SELECTOR, DETAIL_TITLE_SELECTOR)
    if title_elements:
        uitspraak.zaak_nr = title_elements[0].text

    content_elements = driver.find_elements(By.CSS_SELECTOR, DETAIL_CONTENT_SELECTOR)
    if content_elements:
        uitspraak.inhoud = content_elements[0].text

    return uitspraak
