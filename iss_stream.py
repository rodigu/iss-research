# iss_mimic_value_only.py
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://demos.lightstreamer.com/ISSLive/"
SEARCH_TERM = "NODE3000005"
POLL_INTERVAL = 2.0  # segundos

def start_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # roda em background
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.set_page_load_timeout(30)
    return driver

def main():
    driver = start_driver()
    print("Abrindo página:", URL)
    driver.get(URL)
    time.sleep(5)  # espera carregar o JS

    last_value = None

    try:
        while True:
            rows = driver.find_elements(By.TAG_NAME, "tr")
            for r in rows:
                cells = r.find_elements(By.TAG_NAME, "td")
                texts = [c.text.strip() for c in cells]
                if SEARCH_TERM in texts:
                    # Valor atual do tanque geralmente está na coluna 5 (ajuste se mudar)
                    value = texts[4]
                    if value != last_value:
                        print(f"Valor atual do tanque de urina: {value}")
                        last_value = value
            time.sleep(POLL_INTERVAL)
    except KeyboardInterrupt:
        print("Parado pelo usuário")
    finally:
        try:
            driver.quit()
        except Exception:
            pass

if __name__ == "__main__":
    main()
