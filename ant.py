"""
Ant representation
"""

class Ant(object):
    def __init__(self, id, position, carries_food=False):
        self.id = id
        self.position = position
        self.carries_food = carries_food

    def update(self, position, carries_food):
        self.position = position
        self.carries_food = carries_food

