import argparse
import csv
import sys

import AlgoUtils
from input_parser import parse_input_csv, parse_input_building


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
        if call.curr_allocation == -1:
            chosen_elev = get_elev_by_loadfactor(call, elevators)
            potential_calls = AlgoUtils.add_qualified_calls(call, calls, chosen_elev)

            if len(potential_calls) > 0:
                potential_calls.insert(0, call)
                chosen_elev.allocate_calls_with_loadfactor(potential_calls)
            else:
                chosen_elev.allocate_call(call)


def write_output_file(calls, output_file_name):
    with open(output_file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        for call in calls:
            writer.writerow(call.to_csv_array())


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('building_file', nargs='?', help='building input file, in json format')
        parser.add_argument('calls_file', nargs='?', help='calls input file, in csv format')
        parser.add_argument('output_file', nargs='?', default='out.csv', help='output file, in csv format')

        args = parser.parse_args()
        print(f"these are the arguments: {args.building_file} {args.calls_file} {args.output_file}")

        building = parse_input_building(args.building_file)
        calls = parse_input_csv(building.max_floor, building.min_floor, args.calls_file)

        execute_algo(calls, building.elevator_list)

        write_output_file(calls, args.output_file)
    except FileNotFoundError:
        print('Error allocating elevators, please make sure you provided the right arguments')
    except Exception as e:
        print(f'error during also execution please check given arguments{e}')


if __name__ == '__main__':
    main()
