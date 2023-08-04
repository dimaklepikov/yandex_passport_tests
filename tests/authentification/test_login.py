import pytest


@pytest.mark.usefixtures("prepare_registration_data")
class TestLogin:

    def test_click_on_create_id(self):
        print(self.user)
        pass

    def test_registration_page_appearance(self):
        pass
