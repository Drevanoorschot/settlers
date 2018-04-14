import random

from model.board_config import numbers, mapping_sequence, TileType, tile_set


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
