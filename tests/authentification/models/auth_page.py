from tests.models.page import Page
from selenium.webdriver.common.by import By

from ..constants import AUTH_URL


class AuthPage(Page):
    def __init__(self, driver, locator='//*[@id="root"]', url=AUTH_URL):
        super().__init__(driver, locator, url)

        self.locator = (By.XPATH, locator)
        self.login_input = (By.XPATH, '//*[@data-t="field:input-login"]')
        self.phone_input = (By.XPATH, '//*[@data-t="button:clear"]')
        self.password_input = (By.XPATH, '//*[@data-t="field:input-passwd"]')
        self.enter_button = (By.XPATH, '//*[@id="passp:sign-in"]')
        self.phone_button = (By.XPATH, '//*[@data-t="button:clear"]')
        self.google_sso_button = (By.XPATH, '//*[@data-t="icon:gg"]')
