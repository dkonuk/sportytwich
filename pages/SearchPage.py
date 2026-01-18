from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.BasePage import BasePage
from pages.SearchResultsPage import SearchResultsPage
from selenium.webdriver.support import expected_conditions as EC

class SearchPage(BasePage):
    SEARCH_BOX = (By.CSS_SELECTOR, "input[placeholder='Search']")

    def search_for_query(self, query):
        self.send_keys(self.SEARCH_BOX, query + Keys.ENTER)
        return SearchResultsPage(self.driver)

    # Assertion Functions

    def is_search_input_visible(self, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.SEARCH_BOX)
        )
        return element.is_displayed()




