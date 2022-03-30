# imports
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# global vars

yahoo_xpath = '//*[@id="ybar-logo"]/img[1]'


def check_yahoo_logo() -> bool:
    try:
        chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        chrome.get("https://www.yahoo.com/")
        chrome.find_element(By.XPATH, yahoo_xpath)
        print("Yahoo logo loaded successfully")
        return True
    except Exception as e:
        print(f"Something went wrong: {e}")
        return False


def test_yahoo_logo():
    result = check_yahoo_logo()
    assert result
