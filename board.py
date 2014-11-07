"""
Gameboard representation
"""

import pygame

from ant import Ant
from tile import Tile, TILE_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BROWN = (102, 51, 0)

class Board(object):
    def __init__(self, width, height, colony, food):
        self.width = width
        self.height = height
        self.colony = [
                        colony[0]*TILE_SIZE, colony[1]*TILE_SIZE,
                        TILE_SIZE, TILE_SIZE
                        ]
        self.food = food
        screen_size = [width*TILE_SIZE, height*TILE_SIZE]
        self.screen = pygame.display.set_mode(screen_size)
        self.screen.fill(WHITE)
        self.tiles = []
        self.ants = {}

        # Populate grid
        for h in range(0, height):
            for w in range(0, width):
                square = Tile(w*TILE_SIZE, h*TILE_SIZE)
                self.tiles.append(square)
                rect, color = square.render()
                pygame.draw.rect(self.screen, color, rect)
        # Place colony
        pygame.draw.rect(self.screen, GREEN, self.colony)
        # Place food
        food_pos = food['position']
        pile = [[food_pos[0]*TILE_SIZE+TILE_SIZE/2, food_pos[1]*TILE_SIZE],
                [food_pos[0]*TILE_SIZE, (food_pos[1]+1)*TILE_SIZE],
                [(food_pos[0]+1)*TILE_SIZE, (food_pos[1]+1)*TILE_SIZE]]
        pygame.draw.polygon(self.screen, YELLOW, pile)
        pygame.display.set_caption("Ant colony visualization")
        pygame.display.flip()

    def update(self, data):
        map(lambda tile, pheromones: tile.update(**pheromones),
            self.tiles, data['board'])
        for tile in self.tiles:
            rect, color = tile.render()
            pygame.draw.rect(self.screen, color, rect)
        for ant_repr in data['ants']:
            if ant_repr['id'] in self.ants:
                ant = self.ants[ant_repr['id']]
                ant.position = ant_repr['position']
            else:
                print ant_repr
                ant = Ant(**ant_repr)
                self.ants[ant_repr['id']] = ant
            pos = map(lambda coord: coord*TILE_SIZE+TILE_SIZE/2, ant.position)
            pygame.draw.circle(self.screen, GREEN, pos, TILE_SIZE/5)
        # Place colony
        pygame.draw.rect(self.screen, GREEN, self.colony)
        # Place food
        food_pos = self.food['position']
        pile = [[food_pos[0]*TILE_SIZE+TILE_SIZE/2, food_pos[1]*TILE_SIZE],
                [food_pos[0]*TILE_SIZE, (food_pos[1]+1)*TILE_SIZE],
                [(food_pos[0]+1)*TILE_SIZE, (food_pos[1]+1)*TILE_SIZE]]
        pygame.draw.polygon(self.screen, YELLOW, pile)
        pygame.display.flip()

    def exit(self):
        pygame.quit()
