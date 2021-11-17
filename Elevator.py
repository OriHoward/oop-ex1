from CallForElevator import CallForElevator
from StatusEnum import StatusEnum


class Elevator:
    def __init__(self, _id, speed, min_floor, max_floor, close_time, open_time, start_time, stop_time):
        self.id: int = int(_id)
        self.speed: float = float(speed)
        self.min_floor: float = float(min_floor)
        self.max_floor: float = float(max_floor)
        self.close_time: float = float(close_time)
        self.open_time: float = float(open_time)
        self.start_time: float = float(start_time)
        self.stop_time: float = float(stop_time)
        self.tasks: list[CallForElevator] = []
        self.total_stop_time: float = float(close_time) + float(open_time) + float(start_time) + float(stop_time)
        self.load_factor: float = 0

    def get_path_load(self, calls: list[CallForElevator]) -> float:
        """
        given a list of calls the calls are all in the same direction and each call in on the way on each call after it
        this function calculates the amount of time it takes for the elevator to complete the path

        :param calls: a list of calls
        :return: returns the amount of time it takes for the elevator to complete the path
        """
        intermediate_stops = set()
        path_load = 0
        for call in calls:
            intermediate_stops.add(call.source)
            intermediate_stops.add(call.dest)

        path_load += abs(max(intermediate_stops) - min(intermediate_stops)) / self.speed
        path_load += (len(intermediate_stops)) * self.total_stop_time

        return path_load

    def get_path_load_factor_estimation(self, calls: list[CallForElevator]) -> int:
        """
        :param calls: list of calls
        :return: the load estimation if the elevators takes the calls
        """
        return self.load_factor + self.get_path_load(calls)

    def allocate_calls_with_loadfactor(self, calls: list[CallForElevator]) -> None:
        """
        allocates the given list of calls to this elevator and adds the time it takes to the load_factor of the elevator
        :param calls: list of calls to allocate
        :return:
        """
        for call in calls:
            call.curr_allocation = self.id
            call.status = StatusEnum.ALLOCATED

        self.load_factor += self.get_path_load(calls)
        self.tasks.extend(calls)

    def get_call_endtime(self, curr_call) -> float:
        return ((abs(curr_call.dest - curr_call.source)) / self.speed) + curr_call.time + self.total_stop_time
