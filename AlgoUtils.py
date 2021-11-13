from CallForElevator import CallForElevator
from Elevator import Elevator
from StatusEnum import StatusEnum


def add_qualified_calls(allocated_call: CallForElevator, calls: list[CallForElevator], elev: Elevator):
    """
    we currently intruduce a naive approach in this function, this might be a bug
    :param allocated_call:
    :param calls:
    :param elev:
    :return:
    """
    qualified_calls = []
    interval_to_check = elev.get_call_endtime(allocated_call)
    for call in calls:
        if allocated_call.time < call.time < interval_to_check and call.curr_allocation != -1 and call.call_direction == allocated_call.call_direction:
            if call.call_direction == StatusEnum.UP and allocated_call.source < call.source < allocated_call.dest:
                if allocated_call.dest < call.dest and elev.get_call_endtime(call) > interval_to_check:
                    allocated_call = call
                    interval_to_check = elev.get_call_endtime(call)
                qualified_calls.append(call)
            if call.call_direction == StatusEnum.DOWN and allocated_call.source > call.source > allocated_call.dest:
                if allocated_call.dest > call.dest and elev.get_call_endtime(call) > interval_to_check:
                    allocated_call = call
                    interval_to_check = elev.get_call_endtime(call)
                qualified_calls.append(call)
    qualified_calls = filter_to_qualified_calls(allocated_call, qualified_calls, elev)
    return qualified_calls


def filter_to_qualified_calls(allocated_call, qualified_calls: list[CallForElevator], elev):
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
        qualified_calls.sort(key=lambda potential_call: potential_call.source)
        for call in qualified_calls:
            time_diff = abs(curr_time_stamp - call.time)
            curr_floor = allocated_call.source + (time_diff * elev.speed)
            if call.source > curr_floor:
                curr_time_stamp += elev.total_stop_time + ((abs(curr_floor - call.source)) / elev.speed)
                good_calls.append(call)
    good_calls.sort(key=lambda nice_call:nice_call.time)
    return good_calls
