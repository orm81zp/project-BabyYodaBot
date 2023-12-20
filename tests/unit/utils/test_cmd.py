import unittest
from unittest.mock import patch
from baby_yoda_bot.utils.cmd import request_input, parse_input

class TestMyModule(unittest.TestCase):
    """Tests cmd utils"""

    @patch('builtins.input', return_value='add-phone')
    def test_request_input(self, mock_input):
        result = request_input()
        self.assertEqual(result, 'add-phone')

    @patch('builtins.input', return_value='add-phone 123 321')
    def test_request_input_with_args(self, mock_input):
        result = request_input()
        self.assertEqual(result, 'add-phone 123 321')

    def test_parse_input(self):
        test_cases = [
            ("command arg1 arg2", "command", ["arg1", "arg2"]),
            ("  Command   Arg1   Arg2   ", "command", ["Arg1", "Arg2"]),
            ("just-command", "just-command", [])
        ]

        for user_input, expected_command, expected_args in test_cases:
            with self.subTest(user_input=user_input):
                cmd, args = parse_input(user_input)
                self.assertEqual(cmd, expected_command)
                self.assertEqual(args, expected_args)

if __name__ == '__main__':
    unittest.main()