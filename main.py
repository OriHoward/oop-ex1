import argparse
import csv
import json
import sys

from CallForElevator import CallForElevator
from Elevator import Elevator
from StatusEnum import StatusEnum

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
        calls.append(CallForElevator(row[1], row[2], row[3], row[4], row[5]))

    elevators = []
    for idx, elev in enumerate(data["_elevators"]):
        elevators.append(Elevator(
            idx, elev["_speed"], elev["_minFloor"],
            elev["_maxFloor"], elev["_closeTime"], elev["_openTime"],
            elev["_startTime"], elev["_stopTime"]))

    for call in calls:
        min_value = sys.maxsize
        chosen_elev = None
        for elev in elevators:
            curr_min = elev.allocate_by_load_factor(call)
            if curr_min < min_value:
                min_value = curr_min
                chosen_elev = elev
        chosen_elev.allocate_call(call)
        call.curr_allocation = chosen_elev.id
        call.status = StatusEnum.DONE

    with open('./output.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for call in calls:
            writer.writerow(call.to_papa())
