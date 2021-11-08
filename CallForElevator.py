from DirectionEnum import DirectionEnum


class CallForElevator:
    def __init__(self, time, source, dest):
        self.time = float(time)
        self.source = float(source)
        self.dest = float(dest)
        self.call_direction = DirectionEnum.Up if source < dest else DirectionEnum.Down
