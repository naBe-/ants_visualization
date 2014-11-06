"""
Gameboard representation
"""

import pygame

from tile import Tile, TILE_SIZE

class Board(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        screen_size = [width*TILE_SIZE, height*TILE_SIZE]
        self.screen = pygame.display.set_mode(screen_size)
        self.screen.fill((255, 255, 255))
        self.tiles = []
        self.ants = {}

        # Populate grid
        for h in range(0, height):
            for w in range(0, width):
                square = Tile(w*TILE_SIZE, h*TILE_SIZE)
                self.tiles.append(square)
                rect, color = square.render()
                pygame.draw.rect(self.screen, color, rect)
        pygame.display.set_caption("Ant colony visualization")
        pygame.display.flip()

    def update(self, data):
        map(lambda tile, pheromones: tile.update(**pheromones),
                                                 self.tiles, data.board)
        for tile in self.tiles:
            rect, color = tile.render()
            pygame.draw.rect(self.screen, color, rect)
        pygame.display.flip()
