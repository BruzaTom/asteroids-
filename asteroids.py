import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radious):
        super().__init__(x, y, radious)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        newAngle = random.uniform(20, 50)
        velo1 = self.velocity.rotate(newAngle)
        velo2 = self.velocity.rotate(-newAngle)
        lil1 = Asteroid(self.position.x, self.position.y, newRadius)
        lil1.velocity = velo1 * 1.2
        lil2 = Asteroid(self.position.x, self.position.y, newRadius)
        lil2.velocity = velo2 * 1.2