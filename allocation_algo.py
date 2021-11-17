from CallForElevator import CallForElevator
from Elevator import Elevator
from StatusEnum import StatusEnum


def add_qualified_calls(allocated_call: CallForElevator, calls: list[CallForElevator], elev: Elevator):
    """
    this function is trying to build a path of calls according to the direction time and floors of a given call.
    the calls that are in the calls' interval (time it takes for the call to complete)
    :param allocated_call: Elevator call to start path from
    :param calls: calls to try and find a path in
    :param elev: elevator that is used to estimate the path according to the elevators' parameters
    :return: a list of calls that form a path in the same direction
    """
    initial_call = allocated_call
    qualified_calls = []
    interval_to_check = elev.get_call_endtime(allocated_call)
    curr_call = allocated_call
    for call in calls:
        if curr_call.time < call.time < interval_to_check and call.curr_allocation == -1 and call.call_direction == curr_call.call_direction:
            if call.call_direction == StatusEnum.UP and curr_call.source < call.source < curr_call.dest:
                if curr_call.dest < call.dest and elev.get_call_endtime(curr_call) < elev.get_call_endtime(call):
                    interval_to_check = elev.get_call_endtime(call)
                    curr_call = call
                qualified_calls.append(call)
            if call.call_direction == StatusEnum.DOWN and curr_call.source > call.source > curr_call.dest:
                if curr_call.dest > call.dest and elev.get_call_endtime(curr_call) < elev.get_call_endtime(call):
                    interval_to_check = elev.get_call_endtime(call)
                    curr_call = call
                qualified_calls.append(call)
    qualified_calls = filter_qualified_calls(initial_call, qualified_calls, elev)
    qualified_calls.insert(0, initial_call)
    return qualified_calls


def filter_qualified_calls(allocated_call, qualified_calls: list[CallForElevator], elev):
    good_calls = []
    curr_time_stamp = allocated_call.time
    if allocated_call.call_direction == StatusEnum.DOWN:
        qualified_calls.sort(key=lambda potential_call: potential_call.source, reverse=True)
        for call in qualified_calls:
            time_diff = abs(curr_time_stamp - call.time)
            curr_floor = allocated_call.source - (time_diff * elev.speed)
            if call.source < curr_floor:
                curr_time_stamp += elev.total_stop_time + ((abs(curr_floor - call.source)) / elev.speed)
                good_calls.append(call)
    else:
        curr_position = allocated_call.source
        curr_time = allocated_call.time
        for call in qualified_calls:
            floors_traveled = (abs(curr_time - call.time) * elev.speed)
            curr_position = floors_traveled + curr_position
            curr_time = call.time
            if curr_position < call.source:
                good_calls.append(call)
    good_calls.sort(key=lambda nice_call: nice_call.time)
    return good_calls
