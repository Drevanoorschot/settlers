from enum import Enum


class Color(Enum):
    RED = 0
    BLUE = 1
    WHITE = 2
    ORANGE = 3


class Player:
    def __init__(self, color):
        self.color = color
        self.points = 0
        self.pieces = {
            "towns": 4,
            "villages": 5,
            "roads": 15
        }
        self.resources = {
            "grain": 0,
            "ore": 0,
            "brick": 0,
            "wood": 0,
            "wool": 0
        }
