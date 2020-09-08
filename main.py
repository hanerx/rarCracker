# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import itertools
import os
import sys
from string import ascii_letters, digits, punctuation
import threading
import fastzipfile
import rarfile
import logging


class RarCracker:

    def __init__(self, file_path: str, start: int = 1, stop: int = 10, charset=None, output: str = './output',
                 workers: int = 4, level=logging.INFO, unrar_tool: str = 'unrar'):
        rarfile.UNRAR_TOOL = unrar_tool
        if os.path.exists(file_path):
            self.file_path = file_path
            if file_path.endswith('.zip'):
                self.file = fastzipfile.FastZipExtFile(file_path)
            elif file_path.endswith('.rar'):
                self.file = rarfile.RarFile(file=file_path)

            else:
                raise TypeError('unexpect file type')
            self.start = start
            self.stop = stop
            self.output = output
            self.workers = workers
            if charset is None:
                self.charset = digits + ascii_letters + punctuation
            else:
                self.charset = charset
            logging.basicConfig(level=level,
                                format='%(asctime)s - [Thread:%(thread)d] - %(levelname)s: %(message)s')
        else:
            raise FileNotFoundError(file_path)

    def generate_password(self):
        for i in range(self.start, self.stop + 1):
            iterable = itertools.product(self.charset, repeat=i)
            for j in iterable:
                yield ''.join(j)

    def crack(self):
        if self.file.needs_password():
            lock = threading.Lock()
            sema = threading.Semaphore(value=self.workers)
            for i in self.generate_password():
                if lock.locked():
                    return
                else:
                    thread = self.CrackThread(self.file, self.output, lock, i, sema)
                    thread.start()
        else:
            logging.info('password empty')

    class CrackThread(threading.Thread):
        def __init__(self, file, output, lock, password, sema):
            super().__init__()
            self.file = file
            self.output = output
            self.lock = lock
            self.password = password
            self.sema = sema

        def run(self) -> None:
            self.sema.acquire()
            if self.lock.locked():
                # logging.debug('password found')
                self.sema.release()
                sys.exit()
            else:
                try:
                    logging.debug('try password: {}'.format(self.password))
                    self.file.extractall(path=self.output, pwd=self.password)
                    logging.info('password {} is correct, password found'.format(self.password))
                    self.lock.acquire()
                    self.sema.release()
                    sys.exit()
                except Exception as e:
                    logging.debug(e)
                    logging.info('password {} is not correct'.format(self.password))
                    self.sema.release()
                    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cracker = RarCracker('./test.rar', 3, 3, workers=2, charset='1234567890')
    cracker.crack()