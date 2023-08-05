import pytest
from lib.jsonplaceholder import jsonplaceholder
import os
from dotenv import load_dotenv


@pytest.fixture(scope="class")
def get_auth_credentials(request):
    load_dotenv()
    request.cls.user = {
        "login": os.environ.get("LOGIN"),
        "password": os.environ.get("PASSWORD"),
    }
    request.cls.fake_user = {
        "login": jsonplaceholder.user["username"],
        "password": jsonplaceholder.user["website"],
    }
