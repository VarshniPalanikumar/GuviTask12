import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def start_browser():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    driver.set_page_load_timeout(300)
    driver.get("https://www.guvi.in/")

    yield driver
    driver.quit()
