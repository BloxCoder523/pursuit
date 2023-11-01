# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,too-few-public-methods,invalid-name
import random
from random import randint, randrange

from components import Position, Velocity
import entities.bullet

class Wander:
    def think(self, pos: Position, vel: Velocity):
        vel.x = randint(-1, 1)
        vel.y = randint(-1, 1)

        fire_bullet = randrange(0, 100)
        if fire_bullet <= 20:
            direction = random.choices(['UP', 'DOWN', 'LEFT', 'RIGHT'])
            entities.bullet.create(direction, pos.x, pos.y)
