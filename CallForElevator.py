from StatusEnum import StatusEnum


class CallForElevator:
    def __init__(self, time, source, dest, status, curr_allocation):
        self.time = float(time)
        self.source = int(source)
        self.dest = int(dest)
        self.status = status
        self.curr_allocation: int = int(curr_allocation)
        self.call_direction = StatusEnum.UP if self.source < self.dest else StatusEnum.DOWN

    def __str__(self):
        return f"Elevator call,{self.time},{self.source},{self.dest},{self.status},{self.curr_allocation}"

    def __eq__(self, other):
        return self.source == other.source and \
               self.dest == other.dest and \
               self.curr_allocation == other.curr_allocation and self.status == other.status

    def to_csv_array(self):
        return ["Elevator call", self.time, self.source, self.dest, self.status.value, self.curr_allocation]
