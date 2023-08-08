import pytest
from .constants import REDIRECT_URL


@pytest.mark.auth
@pytest.mark.usefixtures("set_auth_credentials", "auth_page")
class TestLogin:

    # TODO: Add configuration parsing - https://docs.python.org/3/library/configparser.html
    # TODO: Add write-to-file sample service + fixture on teardown
    # TODO: Add POM Locators for the Auth page

    def test_login_page_is_displayed(self):
        # Убедитесь, что страница входа доступна и правильно загружается
        assert self.page.wait_element_visible(self.page.locator)

    def test_login_fields_are_displayed(self, driver):
        # Убедитесь, что страница входа содержит необходимые поля (имя пользователя, пароль и кнопку входа)
        # Login field
        assert self.page.wait_element_visible(self.page.login_input)

        self.page.send_keys(self.page.login_input, self.user["login"])
        self.page.wait_element_visible(self.page.enter_button)
        self.page.click(self.page.enter_button)
        # Password field
        assert self.page.wait_element_visible(self.page.password_input)

    def test_user_can_login_by_username(self):
        self.page.wait_element_visible(self.page.login_input)
        # Enter password
        self.page.send_keys(self.page.login_input, self.user["login"])
        self.page.click(self.page.enter_button)
        self.page.wait_element_visible(self.page.password_input)
        # Enter password
        self.page.send_keys(self.page.password_input, self.user["password"])
        self.page.click(self.page.enter_button)
        self.page.wait_until_url_is_changed_to(REDIRECT_URL)
        # Убедитесь, что пользователь перенаправляется на правильную страницу после успешного входа в систему
        assert self.driver.current_url == REDIRECT_URL

    def test_user_cant_login_with_blank_fields(self, driver):
        # Убедитесь, что пользователь не может войти в систему с пустым полем имени пользователя или пароля
        pass

    def test_user_cant_login_with_invalid_credentails(self, driver):
        # Убедитесь, что пользователь не может войти в систему с неправильным именем пользователя или паролем
        pass


