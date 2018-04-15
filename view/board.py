from math import sqrt
from tkinter import PhotoImage

from model.board import Tile
from model.board_config import TileType

tile_resolution = (180, 155)

x_offset = 200
y_offset = 100
x_distance = 4 * (sqrt(3) / 2 * tile_resolution[1] / 2) / 8
y_distance = tile_resolution[1] / 4
x_token_offset = tile_resolution[0] / 2
y_token_offset = tile_resolution[1] / 2

token_radius = 20
token_border_radius = 5


def draw_board(board, frame):
    draw_tiles(board, frame)
    # draw_number_tokens(board, screen)


def draw_tiles(board, frame):
    desert = PhotoImage(file='graphics/desert.png')
    frame.desert = desert
    brick = PhotoImage(file='graphics/brick.png')
    frame.brick = brick
    wool = PhotoImage(file='graphics/wool.png')
    frame.wool = wool
    wood = PhotoImage(file='graphics/wood.png')
    frame.wood = wood
    ore = PhotoImage(file='graphics/ore.png')
    frame.ore = ore
    grain = PhotoImage(file='graphics/grain.png')
    frame.grain = grain
    for y in range(len(board.data)):
        for x in range(len(board.data[y])):
            if isinstance(board.data[y][x], Tile):
                tile = board.data[y][x]
                pos = (x_offset + x * x_distance, y_offset + y * y_distance)
                if tile.resource == TileType.DESERT:
                    frame.create_image(pos, image=desert)
                elif tile.resource == TileType.BRICK:
                    frame.create_image(pos, image=brick)
                elif tile.resource == TileType.WOOL:
                    frame.create_image(pos, image=wool)
                elif tile.resource == TileType.WOOD:
                    frame.create_image(pos, image=wood)
                elif tile.resource == TileType.ORE:
                    frame.create_image(pos, image=ore)
                elif tile.resource == TileType.GRAIN:
                    frame.create_image(pos, image=grain)


def draw_number_tokens(board, screen):
    for tile in board.tiles:
        if tile.resource != TileType.DESERT:
            x_pos = int(x_offset + x_token_offset + tile.coordinates[0] * x_distance)
            y_pos = int(y_offset + y_token_offset + tile.coordinates[1] * y_distance)
            pos = (x_pos, y_pos)
            text_pos = (x_pos - token_radius // 2, y_pos - token_radius // 2)
            draw_number_token(screen, pos, text_pos, tile.number)


def draw_number_token(screen, pos, text_pos, number):
    circle(screen, pygame.Color("black"), pos, token_radius + token_border_radius)
    circle(screen, pygame.Color("white"), pos, token_radius)
    text = pygame.font.SysFont("monospace sans", 30).render(str(number), 1, pygame.Color("black"))
    screen.blit(text, text_pos)
