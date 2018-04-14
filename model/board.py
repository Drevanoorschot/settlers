import random

from model.board_config import numbers, mapping_sequence, TileType, tile_set, board_representation


class Board:
    def __init__(self):
        self.data = []
        tiles = []
        for entry in tile_set:
            for i in range(0, tile_set[entry]):
                tiles.append(Tile(entry))
        random.shuffle(tiles)
        self.assign_number_tokens(tiles)
        self.build_board(tiles)

    def build_board(self, tiles):
        for line in board_representation.splitlines():
            row = []
            for char in line:
                if char == ' ':
                    row.append(None)
                elif char == 'o':
                    row.append(Node())
                elif char == 'x':
                    row.append(Edge())
                elif char == '0':
                    row.append(tiles.pop())
            self.data.append(row)

    def assign_number_tokens(self, tiles):
        j = 0
        for i in mapping_sequence:
            if tiles[i].resource != TileType.DESERT:
                tiles[i].number = numbers[j]
                j += 1

    def __repr__(self):
        obj_rep = ""
        for row in self.data:
            for obj in row:
                if obj is None:
                    obj_rep += ' '
                else:
                    obj_rep += repr(obj)
            obj_rep = obj_rep + "\n"
        return obj_rep


class Tile:
    def __init__(self, resource):
        self.number = None
        self.resource = resource

    def __repr__(self):
        return "0"


class Node:
    def __init__(self):
        self.structure = None
        self.owner = None

    def __repr__(self):
        return "o"


class Edge:
    def __init__(self):
        self.structure = None
        self.owner = None

    def __repr__(self):
        return "x"
