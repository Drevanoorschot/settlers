from tkinter import *

from model.board import Board
from view.board import draw_board
from view.color import Color

screen = Tk()
screen.title("Settlers")
board = Board()
board_frame = Canvas(screen, bg=Color.BLUE.value)
board_frame.grid(row=0, column=0)
draw_board(board, board_frame)

screen.mainloop()
