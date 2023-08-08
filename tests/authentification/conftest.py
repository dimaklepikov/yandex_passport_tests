"""Inner pytest configuration file where credentials are obtained"""
import pytest
import os
from dotenv import load_dotenv

from lib.jsonplaceholder import jsonplaceholder
from src.models.user import User
from .models.auth_page import AuthPage


@pytest.fixture(scope="class")
def set_auth_credentials(request):
    load_dotenv()
    request.cls.user = User(
        login=os.environ.get("LOGIN"),
        password=os.environ.get("PASSWORD"),
        email=""
    )
    request.cls.fake_user = User(
        login="",
        email=jsonplaceholder.user["email"],
        password=jsonplaceholder.user["website"],
    )


@pytest.fixture(autouse=True)
def auth_page(request, driver):
    """Fixture to open Auth page for each test"""
    request.cls.driver = driver
    request.cls.page = AuthPage(request.cls.driver)
    request.cls.page.get()
