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
        self.curr_end_time = 0
        self.intermediate_stops = set()
        self.tasks = []

    def allocate_call(self, call):
        self.tasks.append(call)
        self.intermediate_stops.add(call.dest)
        self.intermediate_stops.add(call.source)
        self.update_time(call)

    def calculate_loadfactor(self, new_call):
        time_for_call = (abs(new_call.source - new_call.destination)) / self.speed
        time_for_call = time_for_call + self.stop_time + self.start_time + self.close_time + self.open_time

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
                if new_call.call_direction == DirectionEnum.Up and (
                        self.speed * time_delta) + curr_call.source <= new_call.source:
                    self.tasks.append(new_call)
                    return True
                elif new_call.call_direction == DirectionEnum.Down and (
                        curr_call.source - self.speed * time_delta) >= new_call.source:
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
