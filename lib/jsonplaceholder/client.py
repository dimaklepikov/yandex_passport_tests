"""Jsonplaceholder client for generating test data"""
from src.http_client import HttpClient
from random import choice
from .constants import BASE_URL


class Jsonplaceholder(HttpClient):
    """Jsonplaceholder python library"""

    def __init__(self):
        super().__init__(base_url=BASE_URL)
        self.user = choice(self.get_users())

    def get_users(self):
        return self.get("/users").response


jsonplaceholder = Jsonplaceholder()
