from lib.model import Model


class User(Model):
    """A class for a User entity"""
    def __init__(self, email, password, login):
        super().__init__(email=email, password=password, login=login)
