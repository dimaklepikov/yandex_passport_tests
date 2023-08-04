import pytest
from lib.jsonplaceholder import jsonplaceholder
import os
from dotenv import load_dotenv


@pytest.fixture(scope="class")
def prepare_fake_login_data(request):
    request.cls.fake_user = {
        "login": jsonplaceholder.user["login"],
        "password": jsonplaceholder.user["website"],
    }


@pytest.fixture(scope="class")
def login_credentials(request):
    load_dotenv()
    request.cls.user = {
        "login": os.environ.get("LOGIN"),
        "password": os.environ.get("PASSWORD"),
    }
