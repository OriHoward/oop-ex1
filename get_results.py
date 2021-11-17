import csv
import os
from subprocess import check_output

# change the directories to relevant directories when running
buildings_dir = r"./Ex1_Buildings"
calls_dir = r"./Ex1_Calls"
allocated_calls_file = 'allocated.csv'
submitters_ids = '208201939,313356784'

to_report = []
for building_file in os.listdir(buildings_dir):
    for calls_file in os.listdir(calls_dir):
        curr_building_path = os.path.join(buildings_dir, building_file)
        curr_calls_path = os.path.join(calls_dir, calls_file)

        check_output(['python', 'main.py', curr_building_path, curr_calls_path, allocated_calls_file])

        if os.path.exists(allocated_calls_file):
            out = check_output(
                ['java', '-jar', 'Ex1_checker_V1.2_obf.jar', submitters_ids, curr_building_path, allocated_calls_file,
                 'out.log'])

            last_line = out.splitlines()[-1].decode('utf-8').split(',')
            last_line.insert(0, building_file)
            last_line.insert(0, calls_file)
            to_report.append(last_line)
            os.unlink(allocated_calls_file)

with open('results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for report in to_report:
        writer.writerow(report)
