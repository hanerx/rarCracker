import os

from rarCracker.breakpoint import BreakPoint
from rarCracker.provider import Provider


class LocalBreakPoint(BreakPoint):
    def __init__(self, breakpoint_path='./breakpoint.txt', breakpoint_count: int = 1000):
        super().__init__()
        self.breakpoint_count = breakpoint_count
        self.breakpoint_path = breakpoint_path
        if os.path.exists(breakpoint_path):
            with open(breakpoint_path) as file:
                self.start = int(file.read().replace('\n', ''))
        else:
            self.start = 0
        self.count = 0

    def generate(self, provider: Provider, file) -> iter:
        for i in provider.generate(file):
            if self.count > self.start and self.count % self.breakpoint_count == 0:
                with open(self.breakpoint_path, 'w') as f:
                    f.write(str(self.count))
            self.count += 1
            if self.count > self.start:
                yield i
