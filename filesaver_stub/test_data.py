from unittest.mock import Mock

from dataproducer import ParquetArchiver, FileProducer


class StubFileProducer:
    # odawana implementacja wielkości przychodzących danych i nazw plików
    @staticmethod
    def get_file_size():
        return 9_000_000

    @staticmethod
    def get_filename():
        return f"stub-file.parquet"

def test_file_producer_without_save():
    archiver = ParquetArchiver()
    assert not archiver.is_file_saved


def test_file_save():
    archiver = ParquetArchiver(producer=StubFileProducer())
    archiver.save_or_cache()
    assert archiver.is_file_saved


def test_file_save_with_mock():
    stub_producer = Mock(FileProducer)
    stub_producer.get_file_size.return_value = 9_000_000

    archiver = ParquetArchiver(producer=stub_producer)
    archiver.save_or_cache()
    assert archiver.is_file_saved
