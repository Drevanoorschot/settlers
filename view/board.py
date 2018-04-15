import os

import pygame
from math import sqrt
from pygame._freetype import Font
from pygame.draw import circle

from model.board import Tile
from model.board_config import TileType

tile_resolution = (180, 155)

x_offset = 500
y_offset = 100
x_distance = 4 * (sqrt(3) / 2 * tile_resolution[1] / 2) / 8
y_distance = tile_resolution[1] / 4
x_token_offset = tile_resolution[0] / 2
y_token_offset = tile_resolution[1] / 2

token_radius = 20
token_border_radius = 5


def draw_board(board, screen):
    draw_tiles(board, screen)
    # draw_number_tokens(board, screen)


def draw_tiles(board, screen):
    desert = pygame.image.load(os.path.join('graphics/desert.png'))
    brick = pygame.image.load(os.path.join('graphics/brick.png'))
    wool = pygame.image.load(os.path.join('graphics/wool.png'))
    wood = pygame.image.load(os.path.join('graphics/wood.png'))
    ore = pygame.image.load(os.path.join('graphics/ore.png'))
    grain = pygame.image.load(os.path.join('graphics/grain.png'))
    for y in range(len(board.data)):
        for x in range(len(board.data[y])):
            if isinstance(board.data[y][x], Tile):
                tile = board.data[y][x]
                pos = (x_offset + x * x_distance, y_offset + y * y_distance)
                if tile.resource == TileType.DESERT:
                    screen.blit(desert, pos)
                elif tile.resource == TileType.BRICK:
                    screen.blit(brick, pos)
                elif tile.resource == TileType.WOOL:
                    screen.blit(wool, pos)
                elif tile.resource == TileType.WOOD:
                    screen.blit(wood, pos)
                elif tile.resource == TileType.ORE:
                    screen.blit(ore, pos)
                elif tile.resource == TileType.GRAIN:
                    screen.blit(grain, pos)


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
