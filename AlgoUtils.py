from StatusEnum import StatusEnum


def add_qualified_calls(call, calls, elev, qualified_calls):
    for new_call in calls:
        end_time = elev.update_end_time(call)
        if call.time < new_call.time < end_time and call.call_direction == new_call.call.direction:
            if call.call_direction == StatusEnum.UP:
                if call.source < new_call.source:
                    qualified_calls.append(new_call)



