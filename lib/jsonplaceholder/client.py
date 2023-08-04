"""Jsonplaceholder client for generating test data"""
from src.http_client import HttpClient
from random import randint
from .constants import BASE_URL


class Jsonplaceholder(HttpClient):
    """Jsonplaceholder python library"""

    def __init__(self):
        super().__init__(base_url=BASE_URL)
        self.user = self.get_user(randint(1, 10))

    def get_users(self):
        return self.get("/users").response

    def get_user(self, id):
        return self.get(f"/users/{id}").response


jsonplaceholder = Jsonplaceholder()
