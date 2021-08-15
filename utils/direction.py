from enum import Enum
from point import Point


class Direction(Enum):
    UP = 0, Point(0, -1), 'u'
    DOWN = 1, Point(0, 1), 'd'
    LEFT = 2, Point(-1, 0), 'l'
    RIGHT = 3, Point(1, 0), 'r'

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    # ignore the first param since it's already set by __new__
    def __init__(self, _: str, direction: Point, s: str):
        self._direction = direction
        self.string = s

    def __str__(self):
        return self.string

    # this makes sure that the description is read-only
    @property
    def direction(self):
        return self._direction

    @staticmethod
    def from_string(s):
        for direction in Direction:
            if direction.string == s:
                return direction