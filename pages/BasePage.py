from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from datetime import datetime

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def take_screenshot(self, name="end_of_test"):
        screenshots_dir = "screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(
            screenshots_dir,
            f"{name}_{timestamp}.png"
        )

        self.driver.save_screenshot(file_path)
        return file_path

    def find_elements(self, locator):
        """
        Finds multiple elements.
        Returns an empty list if none are found.
        """
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def demo_pause(self, seconds: float = 1.0):
        """Visual pause for demo/recording purposes only."""
        time.sleep(seconds)