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
            if call.call_direction == StatusEnum.UP and allocated_call.source < call.source:
                potential_calls.append(call)
            if call.call_direction == StatusEnum.DOWN and allocated_call.source > call.source:
                potential_calls.append(call)

    return filter_potential_calls(allocated_call, potential_calls, elev)


def filter_potential_calls(allocated_call: CallForElevator, potential_calls: list[CallForElevator], elev: Elevator):
    merged_calls: list[CallForElevator] = potential_calls.copy()
    merged_calls.insert(0, allocated_call)
    compared_to_index = 0
    floors_passed = 0
    filtered = [allocated_call]
    while compared_to_index + 1 < len(merged_calls):
        prev_call = merged_calls[compared_to_index]
        curr_call = merged_calls[compared_to_index + 1]
        floors_passed += ((curr_call.time - prev_call.time) * elev.speed) + prev_call.source
        if curr_call.call_direction == StatusEnum.UP:
            if floors_passed < curr_call.source:
                filtered.append(curr_call)
        if curr_call.call_direction == StatusEnum.DOWN:
            if floors_passed > curr_call.source:
                filtered.append(curr_call)
        compared_to_index += 1
    return filtered
