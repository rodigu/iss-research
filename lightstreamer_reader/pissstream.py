# iss_mimic_value_only.py
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://demos.lightstreamer.com/ISSLive/"
SEARCH_TERM = "NODE3000005"
POLL_INTERVAL = 2.0  # segundos


def start_driver():
    """starts chromium web driver with selenium

    :return _type_: _description_
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # roda em background
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver: WebDriver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    driver.set_page_load_timeout(30)
    return driver


def _parse_urine_capacity(rows: WebElement) -> str:
    for r in rows:
        cells = r.find_elements(By.TAG_NAME, "td")
        texts = [c.text.strip() for c in cells]
        if SEARCH_TERM in texts:
            value = texts[4]
            return value


def fetch_current_capacity(
    driver: WebDriver = start_driver(), wait_time=0.1, do_fetch_page=True
) -> int:
    """returns urine tank capacity from iss stream

    :param WebDriver driver: chromium webdriver, defaults to start_driver()
    :return int: urine tank current capacity (%)
    """
    if do_fetch_page:
        driver.get(URL)

    rows = driver.find_elements(By.TAG_NAME, "tr")
    while (capacity := _parse_urine_capacity(rows=rows)) == "-":
        time.sleep(wait_time)
    return int(capacity)


def generate_continuous_fetcher():
    driver = start_driver()
    fetch_current_capacity(driver=driver)

    def f():
        return fetch_current_capacity(driver=driver, do_fetch_page=False)

    return f
