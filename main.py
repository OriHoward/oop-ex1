import argparse
import json

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

    elevators = []
    for elev in data["_elevators"]:
        elevators.append(Elevator(
            elev["_id"], elev["_speed"], elev["_minFloor"],
            elev["_maxFloor"], elev["_closeTime"], elev["_openTime"],
            elev["_startTime"], elev["_stopTime"]))
