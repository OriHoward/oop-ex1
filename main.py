import argparse
import csv
import sys

from allocation_algo import add_qualified_calls
from input_parser import parse_input_csv, parse_input_building


def execute_algo(calls, elevators):
    for call in calls:
        if call.curr_allocation == -1:
            min_value = sys.maxsize
            chosen_elev = None
            path_to_execute = []
            for elev in elevators:
                potential_calls = add_qualified_calls(call, calls, elev)
                curr_min = elev.get_path_load_factor_estimation(potential_calls)
                if curr_min < min_value:
                    min_value = curr_min
                    chosen_elev = elev
                    path_to_execute = potential_calls
            chosen_elev.allocate_calls_with_loadfactor(path_to_execute)


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
        if len(calls) > 0:
            execute_algo(calls, building.elevator_list)
            write_output_file(calls, args.output_file)
        else:
            print("calls file didn't match building configuration")
    except FileNotFoundError:
        print('Error allocating elevators, please make sure you provided the right arguments')
    except Exception as e:
        print(f'error during also execution please check given arguments{e}')


if __name__ == '__main__':
    main()
