import pytest
from .models.auth_page import AuthPage


@pytest.mark.usefixtures("get_auth_credentials")
class TestLogin:

    # TODO: Add configuration parsing - https://docs.python.org/3/library/configparser.html
    # TODO: Add write-to-file sample service + fixture on teardown
    # TODO: Add setup fixture where credentials are obtained + document it
    # TODO: Add POM Locators for the Auth page

    def test_login_page_is_displayed(self, driver):
        page = AuthPage(driver)
        page.get()
        page.wait_element_visible(page)
