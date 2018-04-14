import os

import pygame
from pygame._freetype import Font
from pygame.draw import circle

from model.board_config import TileType

x_offset = 500
y_offset = 100
x_distance = 270
y_distance = 155
x_token_offset = 90
y_token_offset = 75

token_radius = 20
token_border_radius = 5


def draw_board(board, screen):
    draw_tiles(board, screen)
    for tile in board.tiles:
        if tile.resource != TileType.DESERT:
            x_pos = int(x_offset + x_token_offset + tile.coordinates[0] * x_distance)
            y_pos = int(y_offset + y_token_offset + tile.coordinates[1] * y_distance)
            pos = (x_pos, y_pos)
            text_pos = (x_pos - token_radius // 2, y_pos - token_radius // 2)
            draw_number_token(screen, pos, text_pos, tile.number)


def draw_tiles(board, screen):
    desert = pygame.image.load(os.path.join('graphics/desert.png'))
    brick = pygame.image.load(os.path.join('graphics/brick.png'))
    wool = pygame.image.load(os.path.join('graphics/wool.png'))
    wood = pygame.image.load(os.path.join('graphics/wood.png'))
    ore = pygame.image.load(os.path.join('graphics/ore.png'))
    grain = pygame.image.load(os.path.join('graphics/grain.png'))
    for tile in board.tiles:
        pos = (x_offset + tile.coordinates[0] * x_distance, y_offset + tile.coordinates[1] * y_distance)
        if tile.resource == TileType.DESERT:
            screen.blit(desert, pos)
        if tile.resource == TileType.BRICK:
            screen.blit(brick, pos)
        if tile.resource == TileType.WOOL:
            screen.blit(wool, pos)
        if tile.resource == TileType.WOOD:
            screen.blit(wood, pos)
        if tile.resource == TileType.ORE:
            screen.blit(ore, pos)
        if tile.resource == TileType.GRAIN:
            screen.blit(grain, pos)


def draw_number_token(screen, pos, text_pos, number):
    circle(screen, pygame.Color("black"), pos, token_radius + token_border_radius)
    circle(screen, pygame.Color("white"), pos, token_radius)
    text = pygame.font.SysFont("monospace sans", 30).render(str(number), 1, pygame.Color("black"))
    screen.blit(text, text_pos)
