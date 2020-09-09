import json

from rarCracker.provider import Provider
import requests
import logging


class NetworkProvider(Provider):
    GET = requests.get
    POST = requests.post
    PUT = requests.put
    DELETE = requests.delete
    HEAD = requests.head
    OPTION = requests.options

    def __init__(self, url, method=GET, on_decode=None, **kwargs):
        super().__init__()
        self.result = method(url, **kwargs)
        if on_decode is None:
            self.on_decode = self.default_decode
        else:
            self.on_decode = on_decode

    def default_decode(self, result):
        return json.loads(self.result.text)

    def generate(self, file) -> iter:
        yield from self.on_decode(self.result)
