# imports
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import allure

# global vars

yahoo_xpath = '//*[@id="ybar-logo"]/img[1]'

@pytest.fixture()
def test_setup():
    global chrome
    chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield
    chrome.quit()



@allure.description("This test checks if Yahoo logo is loaded and should pass")
@allure.severity(severity_level="CRITICAL")
def test_yahoo_logo(test_setup):
    chrome.get("https://www.yahoo.com/")
    assert chrome.find_element(By.XPATH, yahoo_xpath), "Yahoo logo not loaded"
    chrome.close()







