import os
import unittest
from datetime import datetime, timedelta
from src.data_readers import data_reader_io


class TestDataReaderIO(unittest.TestCase):
    def test_get_path_to_memory_file(self):
        self.assertEqual(
            data_reader_io.get_path_to_memory_file(576235893342),
            "data/stats/576235893342.json",
        )

    def test_read_memory(self):
        data_reader_io.read_memory(43526456435)
        self.assertTrue(os.path.exists("data/stats/43526456435.json"))
    
    def test_add_client(self):
        data_reader_io.add_client(1, 1)
        self.assertFalse(data_reader_io.is_timespan_long_enough(1, 1))
    
    def test_is_timespan_long_enough(self):
        # Random numbers to test the first if clause
        self.assertTrue(data_reader_io.is_timespan_long_enough(8437628945, 4375629384))
        one_hour_ago = datetime.now() - timedelta(days=2)
        one_hour_ago_iso = one_hour_ago.isoformat()
        data_reader_io.add_client(2, 2, one_hour_ago_iso)
        self.assertTrue(data_reader_io.is_timespan_long_enough(2, 2))   
        data_reader_io.add_client(3, 3)
        self.assertFalse(data_reader_io.is_timespan_long_enough(3, 3))

