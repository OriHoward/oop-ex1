import CallForElevator
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
        self.curr_end_time = 0
        self.intermediate_stops = set()
        self.tasks = []

    def allocate_call(self, call):
        self.tasks.append(call)
        self.intermediate_stops.add(call.dest)
        self.intermediate_stops.add(call.source)
        self.update_time(call)

    def calculate_load_factor(self, new_call):
        time_for_call = (abs(new_call.source - new_call.dest)) / self.speed
        time_for_call = time_for_call + self.stop_time + self.start_time + self.close_time + self.open_time
        return time_for_call

    def is_intermediate_stop(self, new_call: CallForElevator):
        """
        check the current task compared to the last task we are performing
        :param new_call:
        :return:
        """

        if len(self.tasks) > 0:
            # we only compare to the last call if the call is in the same direction as the new call
            curr_call = self.tasks[-1]
            if new_call.call_direction == curr_call.call_direction:
                time_delta = abs(new_call.time - curr_call.time)
                floor_delta = self.speed * time_delta
                if new_call.call_direction == StatusEnum.UP and (
                        floor_delta) + curr_call.source <= new_call.source:
                    gap = abs(new_call.source - (curr_call.source + floor_delta))
                    self.tasks.append(new_call)
                    return True
                elif new_call.call_direction == StatusEnum.DOWN and (
                        curr_call.source - floor_delta) >= new_call.source:
                    self.tasks.append(new_call)
                    return True
        return False

    def clear_intermediate_stops(self, new_call):
        if new_call.time > self.curr_end_time:
            self.intermediate_stops.clear()

    def update_time(self, new_call):
        self.curr_end_time += (abs(new_call.dest - new_call.source) / self.speed) + new_call.time
        total_stop_time = self.stop_time + self.start_time + self.close_time + self.open_time
        self.curr_end_time += (len(self.intermediate_stops) * total_stop_time)

    def allocate_by_load_factor(self, new_call):
        if len(self.tasks) > 0:
            curr_call = self.tasks[-1]
            dest_to_source = abs(new_call.source - curr_call.dest) / self.speed
            return abs(self.curr_end_time + dest_to_source - new_call.time)
        return self.calculate_load_factor(new_call)
