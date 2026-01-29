import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class YahooScraper:
    def __init__(self, url, timeout=10):
        self.url = url
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, timeout)

    def wait_for_page_to_load(self):
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        print("Page loaded")

    def go_to_stocks_page(self):
        action = ActionChains(self.driver)

        market_menu = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[contains(@data-ylk,'subsec:Markets')]")
            )
        )
        action.move_to_element(market_menu).perform()

        stocks = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@data-ylk,'slk:Stocks')]")
            )
        )
        stocks.click()

    def scrape_stocks(self):
        data = []

        while True:
            self.wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "table"))
            )

            rows = self.driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

            for row in rows:
                values = row.find_elements(By.TAG_NAME, "td")
                stock = {
                    "name": values[1].text,
                    "symbol": values[0].text,
                    "price": values[3].text,
                    "change": values[4].text,
                    "volume": values[6].text,
                    "market_cap": values[8].text,
                    "pe_ratio": values[9].text,
                }
                print(stock)
                data.append(stock)

            try:
                next_button = self.wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[@data-testid='next-page-button']")
                    )
                )

                if next_button.get_attribute("disabled"):
                    print("Last page reached")
                    break

                self.driver.execute_script("arguments[0].click();", next_button)
                time.sleep(1)

            except Exception as e:
                print("Next button issue:", e)
                break

        return data

    def close(self):
        self.driver.quit()

if __name__ == "__main__":

    URL = "https://finance.yahoo.com/markets/stocks/most-active/"

    scraper = YahooScraper(URL)
    scraper.wait_for_page_to_load()
    scraper.go_to_stocks_page()
    scraper.wait_for_page_to_load()

    data = scraper.scrape_stocks()

    df = pd.DataFrame(data)
    df.to_csv("yaho_fininces_stocks.csv", index=False)

    print("work is complete")
    scraper.close()





