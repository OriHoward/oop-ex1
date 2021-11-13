import argparse
import csv
import json
import sys

import AlgoUtils
from Building import Building
from CallForElevator import CallForElevator
from Elevator import Elevator

parser = argparse.ArgumentParser()
parser.add_argument('building_file')
parser.add_argument('calls_file')

args = parser.parse_args()
print(args.building_file)
print(args.calls_file)

def parse_input_csv(max_floor, min_floor):
    parsed_calls = []
    file = open(args.calls_file)
    csv_reader = csv.reader(file)
    for row in csv_reader:
        prefix, time, source, dest, status, curr_allocation = row
        if min_floor <= int(source) <= max_floor and min_floor <= int(dest) <= max_floor:
            parsed_calls.append(CallForElevator(time, source, dest, status, curr_allocation))

    return parsed_calls


def parse_input_building():
    parsed_elevators = []
    with open(args.building_file) as f:
        data = json.load(f)

    for idx, elev in enumerate(data["_elevators"]):
        parsed_elevators.append(Elevator(
            idx, elev["_speed"], elev["_minFloor"],
            elev["_maxFloor"], elev["_closeTime"], elev["_openTime"],
            elev["_startTime"], elev["_stopTime"]))

    building = Building(data["_minFloor"], data["_maxFloor"], parsed_elevators)

    return building


def get_elev_by_loadfactor(call, elevators):
    min_value = sys.maxsize
    chosen_elev = None
    for elev in elevators:
        curr_min = elev.get_predicted_load_factor(call)
        if curr_min < min_value:
            min_value = curr_min
            chosen_elev = elev
    return chosen_elev


def execute_algo(calls, elevators):
    uncompleted_calls = filter(lambda curr_call: curr_call.curr_allocation == -1, calls.copy())
    for call in uncompleted_calls:
        chosen_elev = get_elev_by_loadfactor(call, elevators)
        potential_calls = AlgoUtils.add_qualified_calls(call, calls, chosen_elev)

        if len(potential_calls) > 0:
            potential_calls.insert(0, call)
            chosen_elev.allocate_calls(potential_calls)
        else:
            chosen_elev.allocate_call(call)


def write_output_file(calls, output_file_name):
    with open(output_file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        for call in calls:
            writer.writerow(call.to_csv_array())


def main():
    building = parse_input_building()
    calls = parse_input_csv(building.max_floor, building.min_floor)

    execute_algo(calls, building.elevator_list)

    write_output_file(calls, "output.csv")


if __name__ == '__main__':
    main()
