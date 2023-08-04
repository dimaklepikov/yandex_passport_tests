"""Abstract class to generate a model from JSON response"""


class Model:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)
