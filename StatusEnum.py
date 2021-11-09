from enum import Enum


class StatusEnum(Enum):
    UP = 1
    DOWN = -1
    LEVEL = 0
    INIT = 0
    GOING_TO_SRC = 1
    GOING_TO_DEST = 2
    DONE = 3
