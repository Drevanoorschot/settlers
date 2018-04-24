"""overlay to show possible street location"""
from tkinter import PhotoImage

from model.board import Edge, Node
from view.view_config import *

overlay_path = "graphics/overlay"


class EdgeOverlay:
    def __init__(self, board, board_view, player):
        self.player = player
        self.board_view = board_view
        self.board = board

        self.load_images()
        self.draw_active_edges()

    def load_images(self):
        self.board_view.board_frame.active = PhotoImage(file='{}/active.png'.format(overlay_path))

    def draw_active_edges(self):
        for y in range(len(self.board.data)):
            for x in range(len(self.board.data[y])):
                if isinstance(self.board.data[y][x], Edge):
                    edge = self.board.data[y][x]
                    pos = (x_offset + x * x_distance, y_offset + y * y_distance)
                    # TODO make it so that only relevant edges are drawn upon
                    self.board_view.board_frame.create_image(pos, image=self.board_view.board_frame.active)


class NodeOverlay:
    def __init__(self, board, board_view, player):
        self.player = player
        self.board_view = board_view
        self.board = board

        self.load_images()
        self.draw_active_nodes()

    def load_images(self):
        self.board_view.board_frame.active = PhotoImage(file='{}/active.png'.format(overlay_path))

    def draw_active_nodes(self):
        for y in range(len(self.board.data)):
            for x in range(len(self.board.data[y])):
                if isinstance(self.board.data[y][x], Node):
                    node = self.board.data[y][x]
                    pos = (x_offset + x * x_distance, y_offset + y * y_distance)
                    # TODO make it so that only relevant nodes are drawn upon
                    self.board_view.board_frame.create_image(pos, image=self.board_view.board_frame.active)
