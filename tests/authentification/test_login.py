import pytest
from .constants import REDIRECT_URL


@pytest.mark.auth
@pytest.mark.usefixtures("set_auth_credentials", "auth_page")
class TestLogin:

    # TODO: Add configuration parsing - https://docs.python.org/3/library/configparser.html
    # TODO: Add write-to-file sample service + fixture on teardown
    # TODO: Refactor User to be an entity model

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
        # Enter login
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
        self.page.click(self.page.enter_button)
        # Blank username field
        assert self.page.wait_element_not_visible(self.page.password_input, timeout=5)

        self.page.send_keys(self.page.login_input, self.user["login"])
        self.page.click(self.page.enter_button)
        self.page.wait_element_visible(self.page.password_input)
        # Blank password field
        self.page.click(self.page.enter_button)

        self.page.wait_until_url_is_not_changed_to(REDIRECT_URL, timeout=5)
        # Убедитесь, что пользователь не может войти в систему с пустым полем имени пользователя или пароля
        assert self.driver.current_url != REDIRECT_URL

    def test_user_cant_login_with_invalid_credentails(self, driver):
        # Enter fake login
        self.page.send_keys(self.page.login_input, self.fake_user["login"])
        self.page.click(self.page.enter_button)
        self.page.wait_element_visible(self.page.password_input)
        # Enter fake password
        self.page.send_keys(self.page.password_input, self.fake_user["password"])
        self.page.click(self.page.enter_button)
        self.page.wait_until_url_is_not_changed_to(REDIRECT_URL, timeout=5)
        # Убедитесь, что пользователь не может войти в систему с неправильным именем пользователя или паролем
        assert self.driver.current_url != REDIRECT_URL


x