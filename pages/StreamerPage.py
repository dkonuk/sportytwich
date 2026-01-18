from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage

class StreamerPage(BasePage):
    CONTENT_GATE_START = (By.CSS_SELECTOR,"button[data-a-target='content-classification-gate-overlay-start-watching-button']")
    VIDEO_PLAYER = (By.CSS_SELECTOR,"[data-a-target='video-player']")

    def pass_content_classification_gate_if_present(self):
        buttons = self.driver.find_elements(*self.CONTENT_GATE_START)
        if buttons:
            buttons[0].click()

    def wait_for_video_player(self, timeout=10):
        wait = WebDriverWait(self.driver, timeout)

        wait.until(lambda d: d.execute_script("""
                    const video = document.querySelector('video');
                    return video && video.readyState >= 2;
                    """))

    def wait_until_page_is_ready(self):
        self.pass_content_classification_gate_if_present()
        self.wait_for_video_player()

    # Assertion methods

    def is_video_player_visible(self, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.VIDEO_PLAYER))
        return element.is_displayed()
