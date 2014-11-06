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
        self.pheromone_a = pheromone_a
        self.pheromone_b = pheromone_b

    def render(self):
        rect = [self.position[0], self.position[1],
                self.position[0]+TILE_SIZE, self.position[1]+TILE_SIZE]
        color = (255*self.pheromone_b, 0, 255*self.pheromone_a)
        return rect, color
