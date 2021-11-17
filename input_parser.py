import csv
import json

from Building import Building
from CallForElevator import CallForElevator
from Elevator import Elevator


def parse_input_csv(max_floor: int, min_floor: int, calls_file_path: str) -> list[CallForElevator]:
    """
    parses the calls file
    :param max_floor: max floor of the parsed building
    :param min_floor: min floor of the parsed building
    :param calls_file_path: the path to the calls file
    :return: returns a list of the parsed elevator calls or returns an empty array if one of the calls is out of the range
    """
    parsed_calls = []
    with open(calls_file_path) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            prefix, time, source, dest, status, curr_allocation = row
            if not (min_floor <= int(source) <= max_floor and min_floor <= int(dest) <= max_floor):
                return []
            else:
                parsed_calls.append(CallForElevator(time, source, dest, status, curr_allocation))

    return parsed_calls


def parse_input_building(building_file_path: str) -> Building:
    """
    parses a json file the contains the information about the building
    :param building_file_path:
    :return:
    """
    parsed_elevators = []
    with open(building_file_path) as f:
        data = json.load(f)

    for idx, elev in enumerate(data["_elevators"]):
        parsed_elevators.append(Elevator(
            idx, elev["_speed"], elev["_minFloor"],
            elev["_maxFloor"], elev["_closeTime"], elev["_openTime"],
            elev["_startTime"], elev["_stopTime"]))

    building = Building(data["_minFloor"], data["_maxFloor"], parsed_elevators)

    return building
