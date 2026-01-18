from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage
from pages.StreamerPage import StreamerPage


class SearchResultsPage(BasePage):
    SEARCH_RESULTS_READY = (By.XPATH,"//section[.//h2[normalize-space()='Channels']]//button")
    CHANNEL_CARDS = (By.XPATH,"//section[.//h2[normalize-space()='Channels']]//button")
    STREAMERS = (By.CSS_SELECTOR, "a.tw-link")
    MAX_SCROLL_ATTEMPTS = 2

    def wait_for_page_to_load(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.SEARCH_RESULTS_READY))

    def scroll_for_specified_time(self):
        previous_height = self.driver.execute_script("return document.body.scrollHeight")

        for attempt in range(self.MAX_SCROLL_ATTEMPTS):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            WebDriverWait(self.driver, 5).until(
                lambda d: d.execute_script("return document.body.scrollHeight") >= previous_height
            )
            new_height = self.driver.execute_script("return document.body.scrollHeight")

            if previous_height == new_height:
                break

            previous_height = new_height
    def select_first_streamer(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.CHANNEL_CARDS))
        channels = self.find_elements(self.CHANNEL_CARDS)

        if not channels:
            raise AssertionError("No channels found")

        channel = channels[0]
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", channel)

        channel.click()
        return StreamerPage(self.driver)

    # Assertion methods

    def is_loaded(self, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.SEARCH_RESULTS_READY)
        )
        return element.is_displayed()

    def results_contain_text(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(self.CHANNEL_CARDS))
        cards = self.find_elements(self.CHANNEL_CARDS)
        combined = " ".join([c.text for c in cards if c.text])
        return text.lower() in combined.lower()

    def has_streamer_results(self, timeout=10):
        elements = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(self.CHANNEL_CARDS)
        )
        return len(elements) > 0
