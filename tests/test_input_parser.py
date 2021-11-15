from unittest import TestCase
from unittest.mock import patch, mock_open

from CallForElevator import CallForElevator
from input_parser import parse_input_csv


class Test(TestCase):
    def test_parse_input_csv(self):
        with patch("builtins.open", mock_open(read_data="Elevator call,4.993816266,-6,78,0,-1")):
            calls = parse_input_csv(90, -10, "path/to/open")
            filtered_calls = parse_input_csv(50, -10, "path/to/open")
        self.assertEqual(calls, [CallForElevator('4.993816266', '-6', '78', '0', '-1')])
        self.assertEqual(filtered_calls, [])

    def test_parse_input_building(self):
        self.assertEqual('foo'.upper(), 'FOO')
