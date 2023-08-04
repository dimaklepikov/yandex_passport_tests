import pytest


@pytest.mark.usefixtures("login_credentials")
class TestLogin:

    def test_login(self):
        # A user to login to the YP service
        a = self.user
        pass

    def test_login_with_a_fake_user(self):
        pass
