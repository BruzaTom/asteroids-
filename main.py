import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroid_field import AsteroidField
from shot import Shot

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    #groups
    updatableGroup = pygame.sprite.Group()
    drawableGroup = pygame.sprite.Group()
    asteroidsGroup = pygame.sprite.Group()
    shotsGroup = pygame.sprite.Group()
    #fill class containers
    Player.containers = (updatableGroup, drawableGroup)
    Asteroid.containers = (asteroidsGroup, updatableGroup, drawableGroup)
    AsteroidField.containers = (updatableGroup)
    Shot.containers = (shotsGroup)
    #create objects
    field = AsteroidField()
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while(True):
        screen.fill('Black')        
        for item in updatableGroup:
            item.update(dt)
        for item in drawableGroup:
            item.draw(screen)
        for item in asteroidsGroup:
            for shot in shotsGroup:
                if shot.collisions(item):
                    shot.kill()
                    item.kill()
            if item.collisions(ship):
                print('Game over!')
                return
        for item in shotsGroup:
            item.draw(screen)
            item.update(dt)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        pygame.display.flip()#dont ever forget

    

if __name__ == "__main__":
    main()