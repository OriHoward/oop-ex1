import argparse
import csv
import json

from CallForElevator import CallForElevator
from Elevator import Elevator

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('building_file')
    parser.add_argument('calls_file')

    args = parser.parse_args()
    print(args.building_file)
    print(args.calls_file)

    with open(args.building_file) as f:
        data = json.load(f)

    file = open(args.calls_file)
    csv_reader = csv.reader(file)
    calls = []
    for row in csv_reader:
        calls.append(CallForElevator(row[1],row[2],row[3]))

    elevators = []
    for elev in data["_elevators"]:
        elevators.append(Elevator(
            elev["_id"], elev["_speed"], elev["_minFloor"],
            elev["_maxFloor"], elev["_closeTime"], elev["_openTime"],
            elev["_startTime"], elev["_stopTime"]))


    elevators[0].allocate_call(calls[0])
    asdf =elevators[0].allocate_by_time(calls[1])
