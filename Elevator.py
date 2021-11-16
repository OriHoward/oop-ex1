from CallForElevator import *
from StatusEnum import StatusEnum


class Elevator:
    def __init__(self, _id, speed, min_floor, max_floor, close_time, open_time, start_time, stop_time):
        self.id = int(_id)
        self.speed = float(speed)
        self.min_floor = float(min_floor)
        self.max_floor = float(max_floor)
        self.close_time = float(close_time)
        self.open_time = float(open_time)
        self.start_time = float(start_time)
        self.stop_time = float(stop_time)
        self.tasks: list[CallForElevator] = []
        self.total_stop_time = float(close_time) + float(open_time) + float(start_time) + float(stop_time)
        self.load_factor = 0

    def get_path_load(self, calls: list[CallForElevator]):
        intermediate_stops = set()
        path_load = 0
        for call in calls:
            intermediate_stops.add(call.source)
            intermediate_stops.add(call.dest)

        path_load += abs(max(intermediate_stops) - min(intermediate_stops)) / self.speed
        path_load += (len(intermediate_stops)) * self.total_stop_time

        return path_load

    def get_path_load_factor_estimation(self, calls):
        return self.load_factor + self.get_path_load(calls)

    def allocate_calls_with_loadfactor(self, calls: list[CallForElevator]):
        for call in calls:
            call.curr_allocation = self.id
            call.status = StatusEnum.DONE

        self.load_factor += self.get_path_load(calls)
        self.tasks.extend(calls)

    def get_call_load_factor(self, new_call):
        time_for_call = ((abs(new_call.source - new_call.dest)) / self.speed) + self.total_stop_time
        if len(self.tasks) > 0:
            curr_call = self.tasks[-1]
            dest_to_source = (abs(new_call.source - curr_call.dest) / self.speed)
            return dest_to_source + time_for_call
        return time_for_call

    def get_call_endtime(self, curr_call):
        return ((abs(curr_call.dest - curr_call.source)) / self.speed) + curr_call.time + self.total_stop_time
