import CallForElevator
from DirectionEnum import DirectionEnum


class Elevator:
    def __init__(self, _id, speed, min_floor, max_floor, close_time, open_time, start_time, stop_time):
        self.id = float(_id)
        self.speed = float(speed)
        self.min_floor = float(min_floor)
        self.max_floor = float(max_floor)
        self.close_time = float(close_time)
        self.open_time = float(open_time)
        self.start_time = float(start_time)
        self.stop_time = float(stop_time)
        self.curr_call = None
        self.curr_end_time = 0
        self.intermediate_stops = set()

    def allocate_call(self, call):
        if self.curr_call is None:
            self.curr_call = call
            self.intermediate_stops.add(self.curr_call.dest)
            self.intermediate_stops.add(self.curr_call.source)
            self.update_time(call)

    def calculate_loadfactor(self, call):
        time_for_call = (abs(call.source - call.destination)) / self.speed
        time_for_call = time_for_call + self.stop_time + self.start_time + self.close_time + self.open_time

    def is_intermediate_stop(self, new_call: CallForElevator):
        if self.curr_call is not None:
            if new_call.call_direction == self.curr_call.call_direction:
                time_delta = abs(new_call.time - self.curr_call.time)
                if new_call.call_direction == DirectionEnum.Up and (
                        self.speed * time_delta) + self.curr_call.source <= new_call.source:
                    return True
                elif new_call.call_direction == DirectionEnum.Down and (
                        self.curr_call.source - self.speed * time_delta) >= new_call.source:
                    return True
        return False

    def clear_intermediate_stops(self, new_call):
        if new_call.time > self.curr_end_time:
            self.intermediate_stops.clear()

    def update_time(self, curr_call):
        self.curr_end_time += (abs(curr_call.dest - curr_call.source) / self.speed) + curr_call.time
        total_stop_time = self.stop_time + self.start_time + self.close_time + self.open_time
        self.curr_end_time += (len(self.intermediate_stops) * total_stop_time)
