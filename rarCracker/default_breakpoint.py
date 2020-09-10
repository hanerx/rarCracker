import os

from rarCracker.breakpoint import BreakPoint
from rarCracker.provider import Provider


class DefaultBreakPoint(BreakPoint):
    def __init__(self):
        super().__init__()

    def generate(self, provider: Provider, file) -> iter:
        yield from provider.generate(file)
