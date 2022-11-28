import random
from time import time


class FileProducer:
    # odawana implementacja wielkości przychodzących danych i nazw plików
    @staticmethod
    def get_file_size():
        return random.randint(5_000_000, 15_000_000)

    @staticmethod
    def get_filename():
        return f"{time}-data.parquet"


class ParquetArchiver:
    def __init__(self):
        self._producer = FileProducer()
        self._filename = "cache.tmp"
        self._is_file_save = False

    def save_or_cache(self):
        size = self._producer.get_file_size()
        # wrzucamy do cache pliki jeżeli są mniejsze niż 10 mega
        if size < 10_000_000:
            self._merge_with_next_file()
            pass
        # albo zapisujemy je od razu jeżeli są większe
        else:
            self._filename = self._producer.get_filename()
            self._is_file_save = True

    @property
    def is_file_saved(self):
        return self._is_file_save

    def _merge_with_next_file(self):
        pass
