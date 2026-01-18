from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.SearchPage import SearchPage


class HomePage(BasePage):
    PATH = "/"
    SEARCH_PAGE = (By.CSS_SELECTOR, "a[href='/directory']")

    def open_page(self, base_url):
        self.driver.get(f"{base_url}{self.PATH}")

    def tap_search(self):
        self.click(self.SEARCH_PAGE)
        return SearchPage(self.driver)



