"""Inner pytest configuration file where credentials are obtained"""
import pytest
from lib.jsonplaceholder import jsonplaceholder
import os
from dotenv import load_dotenv

from src.models.user import User
from .models.auth_page import AuthPage


@pytest.fixture(scope="class")
def set_auth_credentials(request):
    load_dotenv()
    request.cls.user = User(
        username=os.environ.get("LOGIN"),
        password=os.environ.get("PASSWORD")
    )
    request.cls.fake_user = User(
        username=jsonplaceholder.user["username"],
        password=jsonplaceholder.user["website"]
    )


@pytest.fixture(autouse=True)
def auth_page(request, driver):
    """Fixture to open Auth page for each test"""
    request.cls.driver = driver
    request.cls.page = AuthPage(request.cls.driver)
    request.cls.page.get()
