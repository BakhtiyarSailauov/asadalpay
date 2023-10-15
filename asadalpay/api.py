import requests


class AsadalPayAPI:
    def __init__(self, api_key, base_url="https://api-dev.asadalpay.com"):
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "api-key": self.api_key,
            "Content-Type": "application/json"
        })

    def _make_request(self, method, endpoint, data=None):
        url = self.base_url + endpoint
        response = getattr(self.session, method)(url, json=data)
        response.raise_for_status()
        return response.json()
