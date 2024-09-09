import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    containers = ()
    def __init__(self, x, y, radious):
        super().__init__(x, y, radious)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)