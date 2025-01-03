import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable   = pygame.sprite.Group()
    drawable    = pygame.sprite.Group()
    asteroids   = pygame.sprite.Group()
    shots       = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(pygame.Color(0, 0, 0))

        for u in updatable:
            u.update(dt)

        # check for collisions with the player
        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game over!")
                return

        # check for shot collisions with asteroids
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collides(bullet):
                    asteroid.split()
                    bullet.kill()

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = (game_clock.tick(60) / 1000)

if __name__ == "__main__":
    main()