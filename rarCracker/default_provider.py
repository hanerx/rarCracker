import itertools
from string import digits, ascii_letters, punctuation

from rarCracker.provider import Provider


class DefaultProvider(Provider):

    def __init__(self, start: int = 1, stop: int = 10, charset=None):
        super().__init__()
        self.start = start
        self.stop = stop
        if charset is None:
            self.charset = digits + ascii_letters + punctuation
        else:
            self.charset = charset

    def generate(self, file) -> iter:
        for i in range(self.start, self.stop + 1):
            iterable = itertools.product(self.charset, repeat=i)
            for j in iterable:
                yield ''.join(j)
