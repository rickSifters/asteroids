import pygame
import circleshape
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(circleshape.CircleShape):
    
    containers = ()
    
    def __init__(self, x, y, radius):
        circleshape.CircleShape.__init__(self, x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.position), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):

        self.kill()
        
        if self.radius > ASTEROID_MIN_RADIUS:

            angle = random.uniform(20, 50)
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            for rotation in [angle, -angle]:
                new_velocity = self.velocity.rotate(rotation)
                new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
                new_asteroid.velocity = new_velocity*1.2

        else:
            return
        