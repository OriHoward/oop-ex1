from StatusEnum import StatusEnum


class CallForElevator:
    def __init__(self, time, source, dest, status, curr_allocation):
        self.time = float(time)
        self.source = int(source)
        self.dest = int(dest)
        self.status = status
        self.curr_allocation = curr_allocation
        self.is_allocated = False
        self.call_direction = StatusEnum.UP if self.source < self.dest else StatusEnum.DOWN

    def __str__(self):
        return f"Elevator call,{self.time},{self.source},{self.dest},{self.status},{self.curr_allocation}"

    def to_papa(self):
        return ["Elevator call", self.time, self.source, self.dest, self.status.value, self.curr_allocation]

