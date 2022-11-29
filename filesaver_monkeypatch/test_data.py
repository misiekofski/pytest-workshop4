from unittest.mock import patch, Mock
from dataproducer import ParquetArchiver


@patch('dataproducer.FileProducer')
def test_file_save_with_mock(test_producer_class):
    stub_producer = Mock()
    stub_producer.get_file_size.return_value = 10_000_001
    stub_producer.get_filename.return_value = "placek.parquet"

    test_producer_class.return_value = stub_producer

    archiver = ParquetArchiver()
    archiver.save_or_cache()

    assert archiver.is_file_saved
    assert archiver.filename == "placek.parquet"
