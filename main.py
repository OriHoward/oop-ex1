import argparse
import csv
import json
import sys

from CallForElevator import CallForElevator
from Elevator import Elevator
from StatusEnum import StatusEnum

parser = argparse.ArgumentParser()
parser.add_argument('building_file')
parser.add_argument('calls_file')

args = parser.parse_args()
print(args.building_file)
print(args.calls_file)


def parse_input_csv():
    parsed_calls = []
    file = open(args.calls_file)
    csv_reader = csv.reader(file)
    for row in csv_reader:
        parsed_calls.append(CallForElevator(row[1], row[2], row[3], row[4], row[5]))

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

    return parsed_elevators


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
    for call in calls:
        filtered_elevs = list(filter(lambda elev: elev.is_intermediate_stop(call), elevators))
        if filtered_elevs:
            chosen_elev = get_elev_by_loadfactor(call, filtered_elevs)
        else:
            chosen_elev = get_elev_by_loadfactor(call, elevators)
        chosen_elev.allocate_call(call)
        call.curr_allocation = chosen_elev.id
        call.status = StatusEnum.DONE


def write_output_file(calls, output_file_name):
    with open(output_file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        for call in calls:
            writer.writerow(call.to_papa())


def main():
    calls = parse_input_csv()
    elevators = parse_input_building()

    execute_algo(calls, elevators)

    write_output_file(calls, "output.csv")


if __name__ == '__main__':
    main()
