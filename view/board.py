from math import sqrt
from tkinter import PhotoImage, Canvas

from exceptions import InvalidDockOrientation
from model.board import Tile
from model.board_config import TileType, dock_locations
from view.color import Color

tile_path = "graphics/tiles"
number_path = "graphics/numbers"
dock_path = "graphics/docks"

frame_resolution = (1000, 1000)

tile_resolution = (180, 155)

x_offset = 150
y_offset = 150
x_distance = 2 * (sqrt(3) / 2 * tile_resolution[1]) / 8
y_distance = tile_resolution[1] / 4
x_token_offset = tile_resolution[0] / 2
y_token_offset = tile_resolution[1] / 2

token_radius = 20
token_border_radius = 5


class BoardView:
    def __init__(self, screen, board):
        self.screen = screen
        self.board = board

        self.board_frame = Canvas(self.screen, bg=Color.BLUE.value, width=frame_resolution[0], height=frame_resolution[1])
        self.board_frame.grid(row=0, column=0)

        self.load_images()
        self.draw_tiles()
        self.draw_number_tokens()
        self.draw_docks()

    def load_images(self):
        # tiles
        self.board_frame.desert = PhotoImage(file='{}/desert.png'.format(tile_path))
        self.board_frame.brick = PhotoImage(file='{}/brick.png'.format(tile_path))
        self.board_frame.wool = PhotoImage(file='{}/wool.png'.format(tile_path))
        self.board_frame.wood = PhotoImage(file='{}/wood.png'.format(tile_path))
        self.board_frame.ore = PhotoImage(file='{}/ore.png'.format(tile_path))
        self.board_frame.grain = PhotoImage(file='{}/grain.png'.format(tile_path))

        # docks
        self.board_frame.docks = []

        # numbers
        self.board_frame.n2 = PhotoImage(file='{}/2.png'.format(number_path))
        self.board_frame.n3 = PhotoImage(file='{}/3.png'.format(number_path))
        self.board_frame.n4 = PhotoImage(file='{}/4.png'.format(number_path))
        self.board_frame.n5 = PhotoImage(file='{}/5.png'.format(number_path))
        self.board_frame.n6 = PhotoImage(file='{}/6.png'.format(number_path))
        self.board_frame.n8 = PhotoImage(file='{}/8.png'.format(number_path))
        self.board_frame.n9 = PhotoImage(file='{}/9.png'.format(number_path))
        self.board_frame.n10 = PhotoImage(file='{}/10.png'.format(number_path))
        self.board_frame.n11 = PhotoImage(file='{}/11.png'.format(number_path))
        self.board_frame.n12 = PhotoImage(file='{}/12.png'.format(number_path))

    def draw_tiles(self):
        for y in range(len(self.board.data)):
            for x in range(len(self.board.data[y])):
                if isinstance(self.board.data[y][x], Tile):
                    tile = self.board.data[y][x]
                    pos = (x_offset + x * x_distance, y_offset + y * y_distance)
                    if tile.resource == TileType.DESERT:
                        self.board_frame.create_image(pos, image=self.board_frame.desert)
                    elif tile.resource == TileType.BRICK:
                        self.board_frame.create_image(pos, image=self.board_frame.brick)
                    elif tile.resource == TileType.WOOL:
                        self.board_frame.create_image(pos, image=self.board_frame.wool)
                    elif tile.resource == TileType.WOOD:
                        self.board_frame.create_image(pos, image=self.board_frame.wood)
                    elif tile.resource == TileType.ORE:
                        self.board_frame.create_image(pos, image=self.board_frame.ore)
                    elif tile.resource == TileType.GRAIN:
                        self.board_frame.create_image(pos, image=self.board_frame.grain)

    def draw_number_tokens(self):
        for y in range(len(self.board.data)):
            for x in range(len(self.board.data[y])):
                if isinstance(self.board.data[y][x], Tile) and self.board.data[y][
                    x].number is not None:
                    tile = self.board.data[y][x]
                    pos = (x_offset + x * x_distance, y_offset + y * y_distance)
                    if tile.number == 2:
                        self.board_frame.create_image(pos, image=self.board_frame.n2)
                    elif tile.number == 3:
                        self.board_frame.create_image(pos, image=self.board_frame.n3)
                    elif tile.number == 4:
                        self.board_frame.create_image(pos, image=self.board_frame.n4)
                    elif tile.number == 5:
                        self.board_frame.create_image(pos, image=self.board_frame.n5)
                    elif tile.number == 6:
                        self.board_frame.create_image(pos, image=self.board_frame.n6)
                    elif tile.number == 8:
                        self.board_frame.create_image(pos, image=self.board_frame.n8)
                    elif tile.number == 9:
                        self.board_frame.create_image(pos, image=self.board_frame.n9)
                    elif tile.number == 10:
                        self.board_frame.create_image(pos, image=self.board_frame.n10)
                    elif tile.number == 11:
                        self.board_frame.create_image(pos, image=self.board_frame.n11)
                    elif tile.number == 12:
                        self.board_frame.create_image(pos, image=self.board_frame.n12)

    def draw_docks(self):
        for dock_location in dock_locations:
            x = dock_location[0][0][1]
            y = dock_location[0][0][0]
            node = self.board.data[y][x]
            image = self.get_image(node.dock, self.board_frame, node.dock_orientation)
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
            else:
                raise InvalidDockOrientation(node.dock_orientation)
            self.board_frame.create_image(pos, image=image)

    @staticmethod
    def get_image(dock, frame, rotation):
        image = PhotoImage(file="{}/{}/{}.png".format(dock_path, rotation, dock))
        frame.docks.append(image)
        return frame.docks[frame.docks.index(image)]
