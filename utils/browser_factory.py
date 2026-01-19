from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_mobile_chrome_driver():
    mobile_emulation = {"deviceName": "Pixel 7"}

    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(412, 915)
    return driver