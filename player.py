import circleshape
import pygame
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_MOVE_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN

class Player(circleshape.CircleShape):

    containers = ()
    cooldown = 0

    def __init__(self, x, y):
        circleshape.CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        # Draw player on screen
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)

    def rotate(self, dt):
        # Rotate player
        self.rotation += PLAYER_TURN_SPEED*dt

    def update(self, dt):
        # Update rotation and position of player
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.cooldown > 0:
                self.cooldown -= dt
            else:
                self.shoot()
                self.cooldown = PLAYER_SHOOT_COOLDOWN

    def move(self, dt):
        # Move player
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_MOVE_SPEED * dt

    def shoot(self):
        # Spawn a new shot at player
        x,y = self.position.x, self.position.y

        bullet = Shot(x, y)

        forward = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        bullet.velocity = forward
