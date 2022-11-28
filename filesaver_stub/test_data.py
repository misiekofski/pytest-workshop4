from unittest.mock import Mock

from dataproducer import ParquetArchiver, FileProducer


class StubFileProducer:
    @staticmethod
    def get_file_size():
        return 10_000_001

    @staticmethod
    def get_filename():
        return f"stub-producer-file.parquet"


def test_file_producer_without_save():
    archiver = ParquetArchiver()
    assert not archiver.is_file_saved


def test_file_save():
    archiver = ParquetArchiver(producer=StubFileProducer())
    archiver.save_or_cache()
    assert archiver.is_file_saved


def test_file_save_with_mock():
    stub_producer = Mock(FileProducer)
    stub_producer.get_file_size.return_value = 10_000_001
    archiver = ParquetArchiver(stub_producer)
    archiver.save_or_cache()
    assert archiver.is_file_saved
