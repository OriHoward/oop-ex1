import csv
import json

from Building import Building
from CallForElevator import CallForElevator
from Elevator import Elevator


def parse_input_csv(max_floor, min_floor, calls_file):
    parsed_calls = []
    with open(calls_file) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            prefix, time, source, dest, status, curr_allocation = row
            if min_floor <= int(source) <= max_floor and min_floor <= int(dest) <= max_floor:
                parsed_calls.append(CallForElevator(time, source, dest, status, curr_allocation))

    return parsed_calls


def parse_input_building(building_file):
    parsed_elevators = []
    with open(building_file) as f:
        data = json.load(f)

    for idx, elev in enumerate(data["_elevators"]):
        parsed_elevators.append(Elevator(
            idx, elev["_speed"], elev["_minFloor"],
            elev["_maxFloor"], elev["_closeTime"], elev["_openTime"],
            elev["_startTime"], elev["_stopTime"]))

    building = Building(data["_minFloor"], data["_maxFloor"], parsed_elevators)

    return building
