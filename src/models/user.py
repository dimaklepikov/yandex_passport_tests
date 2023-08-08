from lib.model import Model


class User(Model):
    """A class for a User entity"""
    def __init__(self, username, password):
        super().__init__(username=username, password=password)
