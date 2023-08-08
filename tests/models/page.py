"""Base Page model. Other pages can inherit from it"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver, locator, url):
        self.driver = driver
        self.locator = locator
        self.url = url

    def get(self):
        self.driver.get(self.url)

    def wait_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_until_url_is_changed_to(self, url, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(url)
        )

    def click(self, locator):
        element = self.wait_for_element_to_be_clickable(locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.wait_element_visible(locator)
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait_element_visible(locator)
        return element.text

    def navigate_to(self, url):
        self.driver.get(url)
