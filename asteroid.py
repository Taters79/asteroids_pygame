import pygame
import random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,
                        pygame.Color(255, 255, 255),
                        self.position,
                        self.radius, 2)

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        vec1 = self.velocity.rotate(random.uniform(20, 50))
        vec2 = -self.velocity.rotate(random.uniform(20, 50))

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vec1 * 1.2

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vec2 * 1.2

    def update(self,dt):
        self.position += (self.velocity * dt)