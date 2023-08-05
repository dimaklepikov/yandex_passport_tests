"""Runners file allows us to create vary of drivers with any preferred options"""
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def firefox():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    return driver


def chrome():
    # FIXME: Remove hardcoded driver manager version
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(driver_version="114.0.5735.16").install()))
    return driver
