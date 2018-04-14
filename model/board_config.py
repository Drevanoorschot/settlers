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