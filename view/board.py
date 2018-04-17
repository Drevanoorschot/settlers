from math import sqrt
from tkinter import PhotoImage, Canvas

from model.board import Tile, Node
from model.board_config import TileType, DockType, dock_locations

tile_path = "graphics/tiles"
number_path = "graphics/numbers"
dock_path = "graphics/docks"

tile_resolution = (180, 155)

x_offset = 200
y_offset = 150
x_distance = 2 * (sqrt(3) / 2 * tile_resolution[1]) / 8
y_distance = tile_resolution[1] / 4
x_token_offset = tile_resolution[0] / 2
y_token_offset = tile_resolution[1] / 2

token_radius = 20
token_border_radius = 5


def load_images(frame):
    # tiles
    desert = PhotoImage(file='{}/desert.png'.format(tile_path))
    frame.desert = desert
    brick = PhotoImage(file='{}/brick.png'.format(tile_path))
    frame.brick = brick
    wool = PhotoImage(file='{}/wool.png'.format(tile_path))
    frame.wool = wool
    wood = PhotoImage(file='{}/wood.png'.format(tile_path))
    frame.wood = wood
    ore = PhotoImage(file='{}/ore.png'.format(tile_path))
    frame.ore = ore
    grain = PhotoImage(file='{}/grain.png'.format(tile_path))
    frame.grain = grain

    # docks
    frame.docks = []


    # numbers
    n2 = PhotoImage(file='{}/2.png'.format(number_path))
    frame.n2 = n2
    n3 = PhotoImage(file='{}/3.png'.format(number_path))
    frame.n3 = n3
    n4 = PhotoImage(file='{}/4.png'.format(number_path))
    frame.n4 = n4
    n5 = PhotoImage(file='{}/5.png'.format(number_path))
    frame.n5 = n5
    n6 = PhotoImage(file='{}/6.png'.format(number_path))
    frame.n6 = n6
    n8 = PhotoImage(file='{}/8.png'.format(number_path))
    frame.n8 = n8
    n9 = PhotoImage(file='{}/9.png'.format(number_path))
    frame.n9 = n9
    n10 = PhotoImage(file='{}/10.png'.format(number_path))
    frame.n10 = n10
    n11 = PhotoImage(file='{}/11.png'.format(number_path))
    frame.n11 = n11
    n12 = PhotoImage(file='{}/12.png'.format(number_path))
    frame.n12 = n12


def draw_board(board, frame):
    load_images(frame)
    draw_tiles(board, frame)
    draw_number_tokens(board, frame)
    draw_docks(board, frame)


def draw_tiles(board, frame):
    for y in range(len(board.data)):
        for x in range(len(board.data[y])):
            if isinstance(board.data[y][x], Tile):
                tile = board.data[y][x]
                pos = (x_offset + x * x_distance, y_offset + y * y_distance)
                if tile.resource == TileType.DESERT:
                    frame.create_image(pos, image=frame.desert)
                elif tile.resource == TileType.BRICK:
                    frame.create_image(pos, image=frame.brick)
                elif tile.resource == TileType.WOOL:
                    frame.create_image(pos, image=frame.wool)
                elif tile.resource == TileType.WOOD:
                    frame.create_image(pos, image=frame.wood)
                elif tile.resource == TileType.ORE:
                    frame.create_image(pos, image=frame.ore)
                elif tile.resource == TileType.GRAIN:
                    frame.create_image(pos, image=frame.grain)


def draw_number_tokens(board, frame):
    for y in range(len(board.data)):
        for x in range(len(board.data[y])):
            if isinstance(board.data[y][x], Tile) and board.data[y][
                x].number is not None:
                tile = board.data[y][x]
                pos = (x_offset + x * x_distance, y_offset + y * y_distance)
                if tile.number == 2:
                    frame.create_image(pos, image=frame.n2)
                elif tile.number == 3:
                    frame.create_image(pos, image=frame.n3)
                elif tile.number == 4:
                    frame.create_image(pos, image=frame.n4)
                elif tile.number == 5:
                    frame.create_image(pos, image=frame.n5)
                elif tile.number == 6:
                    frame.create_image(pos, image=frame.n6)
                elif tile.number == 8:
                    frame.create_image(pos, image=frame.n8)
                elif tile.number == 9:
                    frame.create_image(pos, image=frame.n9)
                elif tile.number == 10:
                    frame.create_image(pos, image=frame.n10)
                elif tile.number == 11:
                    frame.create_image(pos, image=frame.n11)
                elif tile.number == 12:
                    frame.create_image(pos, image=frame.n12)


def draw_docks(board, frame):
    for dock_location in dock_locations:
        x = dock_location[0][0][1]
        y = dock_location[0][0][0]
        node = board.data[y][x]
        image = get_image(node.dock, frame, node.dock_orientation)
        if node.dock_orientation == 0:
            pos = (x_offset + x * x_distance + x_distance, y_offset + y * y_distance - y_distance * 2)
        elif node.dock_orientation == 60:
            pos = (x_offset + x * x_distance - x_distance * 3, y_offset + y * y_distance)
        elif node.dock_orientation == 120:
            pos = (x_offset + x * x_distance - x_distance, y_offset + y * y_distance + y_distance * 2)
        elif node.dock_orientation == 180:
            pos = (x_offset + x * x_distance + x_distance, y_offset + y * y_distance + y_distance * 2)
        elif node.dock_orientation == 240:
            pos = (x_offset + x * x_distance + x_distance, y_offset + y * y_distance + y_distance * 2)
        elif node.dock_orientation == 300:
            pos = (x_offset + x * x_distance + 3 * x_distance, y_offset + y * y_distance)
        frame.create_image(pos, image=image)



def get_image(dock, frame, rotation):
        image = PhotoImage(file="{}/{}/{}.png".format(dock_path, rotation, dock))
        frame.docks.append(image)
        return frame.docks[frame.docks.index(image)]
