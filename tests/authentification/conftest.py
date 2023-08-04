import pytest
from lib.jsonplaceholder import jsonplaceholder


@pytest.fixture
def prepare_login_data(request):
    request.cls.user = jsonplaceholder.user
