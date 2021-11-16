from unittest import TestCase
from unittest.mock import patch, mock_open

from CallForElevator import CallForElevator
from input_parser import parse_input_csv, parse_input_building
import json


class Test(TestCase):
    def test_parse_input_csv(self):
        with patch("builtins.open", mock_open(read_data="Elevator call,4.993816266,-6,78,0,-1")):
            calls = parse_input_csv(90, -10, "path/to/open")
            filtered_calls = parse_input_csv(50, -10, "path/to/open")
        self.assertEqual(calls, [CallForElevator('4.993816266', '-6', '78', '0', '-1')])
        self.assertEqual(filtered_calls, [])

    def test_parse_input_building(self):
        json_data = {
            "_minFloor": -2,
            "_maxFloor": 10,
            "_elevators": [
                {
                    "_id": 0,
                    "_speed": 0.5,
                    "_minFloor": -2,
                    "_maxFloor": 10,
                    "_closeTime": 2.0,
                    "_openTime": 2.0,
                    "_startTime": 3.0,
                    "_stopTime": 3.0
                }
            ]
        }
        with patch("builtins.open", mock_open(read_data=json.dumps(json_data))):
            buidling = parse_input_building("path/to/open")
            self.assertEqual(buidling.max_floor, json_data["_maxFloor"])
            self.assertEqual(buidling.min_floor, json_data["_minFloor"])
