"""
Tile representation
"""

TILE_SIZE = 10

class Tile(object):
    def __init__(self, x, y, pheromone_a=0, pheromone_b=0):
        self.position = (x, y)
        self.pheromone_a = pheromone_a
        self.pheromone_b = pheromone_b

    def update(self, tau_a, tau_b):
        self.pheromone_a = tau_a if tau_a < 1 else 1
        self.pheromone_b = tau_b if tau_b < 1 else 1

    def render(self):
        rect = [self.position[0], self.position[1],
                TILE_SIZE, TILE_SIZE]
        color = (255*self.pheromone_b, 0, 255*self.pheromone_a)
        return rect, color
