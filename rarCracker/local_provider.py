import os

from rarCracker.provider import Provider


class LocalProvider(Provider):

    def __init__(self, path):
        super().__init__()
        if os.path.exists(path):
            self.path = path
        else:
            raise FileNotFoundError(path)

    def generate(self, file) -> iter:
        with open(self.path, 'r') as file:
            for i in file.readlines():
                yield i.replace('\n', '')
