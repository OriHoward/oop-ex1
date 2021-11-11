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
    potential_calls = []

    interval_to_check = elev.get_call_endtime(allocated_call)
    for call in calls:
        if allocated_call.time < call.time < interval_to_check and call.curr_allocation != -1 and call.call_direction == allocated_call.call_direction:
            if call.call_direction == StatusEnum.UP and allocated_call.source< call.source:
                potential_calls.append(call)
            if call.call_direction == StatusEnum.DOWN and allocated_call.source > call.source:
                potential_calls.append(call)
    return potential_calls
