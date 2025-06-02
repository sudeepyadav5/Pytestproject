import time
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browserSetup():
    googleOption = Options()
    googleOption.add_argument('--incognito')
    driver = webdriver.Chrome(googleOption)
    driver.get("https://www.google.com/")
    driver.maximize_window()
    yield driver
    time.sleep(5)
    driver.quit()


@pytest.mark.parametrize("name", ["python program","QA Automation", "SDET List"])
def test_googleSearch(browserSetup, name):
    driver = browserSetup

    searchBox = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
    searchBox.send_keys(name)
    searchBox.send_keys(Keys.ENTER)



