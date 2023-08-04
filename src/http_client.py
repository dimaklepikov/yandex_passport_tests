import requests
from requests.exceptions import JSONDecodeError


class HttpClient:
    """A simple http client (requests wrapper) to handle requests for REST resources"""

    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers

    def send_request(self, method, endpoint, data=None, params=None):
        try:
            response = requests.request(
                method,
                url=f"{self.base_url}{endpoint}",
                json=data,
                params=params,
                headers=self.headers
            )
            return ResponseModel(response)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def get(self, endpoint, params=None):
        return self.send_request('GET', endpoint, params=params)

    def post(self, endpoint, data=None):
        return self.send_request('POST', endpoint, data=data)

    def put(self, endpoint, data=None):
        return self.send_request('PUT', endpoint, data=data)

    def delete(self, endpoint):
        return self.send_request('DELETE', endpoint)


class ResponseModel(requests.Response):
    """Wrapper for a requests Response object. Demonstrating how we can extend behaviour for extra requirements"""

    def __init__(self, response: requests.Response):
        super().__init__()
        self.response = self.response_content(response)
        self.status_code = response.status_code
        self.request = response.request

    @staticmethod
    def response_content(response):
        try:
            content = response.json()
        except JSONDecodeError:
            content = response.text

        return content
