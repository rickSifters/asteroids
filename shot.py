import pygame
from constants import SHOT_RADIUS
import circleshape

class Shot(circleshape.CircleShape):
    
    containers = ()
    
    def __init__(self, x, y):
        circleshape.CircleShape.__init__(self, x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.position), SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)