import random

from model.board_config import numbers, mapping_sequence, TileType, tile_set, board_representation, dock_set, \
    dock_locations


class Board:
    def __init__(self):
        self.data = []
        tiles = []
        for entry in tile_set:
            for i in range(0, tile_set[entry]):
                tiles.append(Tile(entry))
        random.shuffle(tiles)
        self.build_board(tiles)
        self.assign_number_tokens()
        self.place_docks()

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

    def assign_number_tokens(self):
        tiles = []
        for row in self.data:
            for entry in row:
                if isinstance(entry, Tile):
                    tiles.append(entry)
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

    def place_docks(self):
        docks = []
        for dock_type in dock_set:
            for i in range(0, dock_set[dock_type]):
                docks.append(dock_type)
        random.shuffle(docks)
        j = 0
        for dock_location in dock_locations:
            for coord_pair in dock_location[0:1]:
                for coord in coord_pair:
                    self.data[coord[0]][coord[1]].dock = docks[j]
                    self.data[coord[0]][coord[1]].dock_orientation = dock_location[1]
                j += 1


class Tile:
    def __init__(self, resource):
        self.number = None
        self.resource = resource

    def __repr__(self):
        if self.number is None:
            return "0"
        else:
            return str(self.number)


class Node:
    def __init__(self):
        self.structure = None
        self.owner = None
        self.dock = None
        self.dock_orientation = None

    def __repr__(self):
        return "o"


class Edge:
    def __init__(self):
        self.structure = None
        self.owner = None

    def __repr__(self):
        return "x"
