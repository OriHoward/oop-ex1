from DirectionEnum import DirectionEnum


class CallForElevator:
    def __init__(self, time, source, dest):
        self.time = time
        self.source = source
        self.dest = dest
        self.call_direction = DirectionEnum.Up if source < dest else DirectionEnum.Down
