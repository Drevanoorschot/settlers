import random
from enum import Enum

numbers = {
    0: 5,
    1: 2,
    2: 6,
    3: 3,
    4: 8,
    5: 10,
    6: 9,
    7: 12,
    8: 11,
    9: 4,
    10: 8,
    11: 10,
    12: 9,
    13: 4,
    14: 5,
    15: 6,
    16: 3,
    17: 11
}
mapping_sequence = [0, 5, 13, 14, 15, 8, 4, 12, 18, 17, 16, 9, 1, 6, 7, 3, 11, 10, 2]


class TileType(Enum):
    DESERT = 0
    GRAIN = 1
    WOOD = 2
    WOOL = 3
    ORE = 4
    BRICK = 5


tile_set = {
    TileType.DESERT: 1,
    TileType.GRAIN: 4,
    TileType.WOOD: 4,
    TileType.WOOL: 4,
    TileType.ORE: 3,
    TileType.BRICK: 3
}


class DockTypes(Enum):
    UNIVERSAL = 0
    GRAIN = 1
    WOOD = 2
    WOOL = 3
    ORE = 4
    BRICK = 5


class Board:
    def __init__(self):
        self.tiles = []
        for entry in tile_set:
            for i in range(0, tile_set[entry]):
                self.tiles.append(Tile(entry))
        random.shuffle(self.tiles)
        self.distribute_coordinates()
        self.assign_number_tokens()

    def distribute_coordinates(self):
        for i in range(0, 5):
            self.tiles[i].coordinates = (0, i)
        for i in range(5, 9):
            self.tiles[i].coordinates = (-0.5, i - 5 + 0.5)
        for i in range(9, 13):
            self.tiles[i].coordinates = (0.5, i - 9 + 0.5)
        for i in range(13, 16):
            self.tiles[i].coordinates = (-1, i - 13 + 1)
        for i in range(16, 19):
            self.tiles[i].coordinates = (1, i - 16 + 1)

    def assign_number_tokens(self):
        j = 0
        for i in mapping_sequence:
            if self.tiles[i].resource != TileType.DESERT:
                self.tiles[i].number = numbers[j]
                j += 1


class Tile:
    def __init__(self, resource):
        self.number = None
        self.resource = resource
        self.coordinates = None

    def __repr__(self):
        return "{}, {}, {}".format(self.number, self.resource, self.coordinates)
