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
        self.curr_end_time = 0
        self.intermediate_stops = set()
        self.tasks: list[CallForElevator] = []
        self.total_stop_time = float(close_time) + float(open_time) + float(start_time) + float(stop_time)
        self.load_factor = 0

    def allocate_call(self, call):
        self.load_factor += self.get_call_load_factor(call)
        self.tasks.append(call)

    def is_intermediate_stop(self, new_call: CallForElevator):
        """
        check the current task compared to the last task we are performing
        :param new_call:
        :return:
        """
        if len(self.tasks) > 0:
            # we only compare to the last call if the call is in the same direction as the new call
            curr_task: CallForElevator = self.tasks[-1]
            if curr_task.call_direction == new_call.call_direction:
                if curr_task.call_direction == StatusEnum.UP and curr_task.source < new_call.source:
                    return True
                if curr_task.call_direction == StatusEnum.DOWN and curr_task.source > new_call.source:
                    return True

        return False

    def get_call_load_factor(self, new_call):
        time_for_call = (abs(new_call.source - new_call.dest)) / self.speed + self.total_stop_time
        if len(self.tasks) > 0:
            curr_call = self.tasks[-1]
            dest_to_source = abs(new_call.source - curr_call.dest) / self.speed

            return dest_to_source + time_for_call
        return time_for_call

    def get_predicted_load_factor(self, new_call):
        return self.load_factor + self.get_call_load_factor(new_call)

    def update_end_time(self,curr_call):
        self.curr_end_time = ((abs(curr_call.dest - curr_call.source))/self.speed) + curr_call.time
        return self.curr_end_time
