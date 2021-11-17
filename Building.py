from Elevator import Elevator


class Building:
    def __init__(self, min_floor, max_floor, elevator_list: list[Elevator]):
        self.min_floor: int = int(min_floor)
        self.max_floor: int = int(max_floor)
        self.elevator_list: list[Elevator] = elevator_list
