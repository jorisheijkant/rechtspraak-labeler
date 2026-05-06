from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def setup_selenium(headless: bool = True) -> webdriver.Firefox:
    options = Options()
    if headless:
        options.add_argument("--headless")
    return webdriver.Firefox(options=options)
