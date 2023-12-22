import unittest
import io
from unittest.mock import patch
from baby_yoda_bot import yoda_say


class TestBabyYoda(unittest.TestCase):
    """Tests Baby Yoda Bot"""

    def setUp(self):
        pass

    @patch("builtins.input", side_effect=["exit"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_exit(self, *_):
        """Check if stop on exit command"""
        yoda_say()


if __name__ == "__main__":
    unittest.main()
