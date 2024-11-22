import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *


def main():
    pygame.init()

    # Variables required for main loop
    clock = pygame.time.Clock()
    FPS = 60
    dt = 0
    end_game = False

    # Sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    x_init = SCREEN_WIDTH / 2
    y_init = SCREEN_HEIGHT / 2

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x_init, y_init)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color=(0, 0, 0))

        # Update positions
        for object in updatable:
            object.update(dt)

        # Check for collisions
        for object in asteroids:
            if player.collide_check(object):
                print(f"\nGame over!")
                pygame.event.post(pygame.event.Event(pygame.QUIT))

            for bullet in shots:
                if bullet.collide_check(object):
                    object.split()

        # Process movement
        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        ticker = clock.tick(FPS)
        dt = ticker / 1000

if __name__ == "__main__":
    main()