import pytest
from utils.browser_factory import create_mobile_chrome_driver

@pytest.fixture
def driver():
    driver= create_mobile_chrome_driver()
    yield driver
    driver.quit()