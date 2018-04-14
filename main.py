import pygame
from pygame._freetype import Font

from model.board import Board
from view.board import draw_board


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1600, 900))
    pygame.display.set_caption('Settlers')
    board = Board()
    draw_board(board, screen)
    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    board = Board()
                    draw_board(board, screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
