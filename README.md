# oop-ex1

## Running the script

### Prerequisites: Python 3.9.7

The `main.py` script needs the following arguments to run:

1. `json` file that contains the building information
2. `csv` file that contains the calls that need to get allocated
3. **optional** `csv` file that will contain the calls that were allocated from the calls file the default output file
   is `out.csv`

example without the optional argument:

`python main.py Ex1_Buildings/B3.json Ex1_Calls/Calls_c.csv`

created a csv file `out.csv` (default) with the allocation results

example with the optional argument:

`python main.py Ex1_Buildings/B3.json Ex1_Calls/Calls_c.csv B3C3.csv`

created a csv file `B3C3.csv` (default) with the allocation results

running the output using the simulator given:

`java -jar Ex1_checker_V1.2_obf.jar 12,12 ./Ex1_Buildings/B4.json out.csv out.log`