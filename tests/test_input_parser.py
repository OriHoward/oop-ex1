from unittest import TestCase
from unittest.mock import patch, mock_open

from input_parser import parse_input_csv


class Test(TestCase):
    def test_parse_input_csv(self):
        with patch("builtins.open", mock_open(read_data="Elevator call,4.993816266,-6,78,0,-1")) as mock_file:
            assert open("path/to/open").read() == "Elevator call,4.993816266,-6,78,0,-1"
            parse_input_csv(-10, 90, "path/to/open")
            mock_file.assert_called_with("path/to/open")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_parse_input_building(self):
        self.assertEqual('foo'.upper(), 'FOO')
