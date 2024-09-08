import pygame
from constants import *
from player import Player

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while(True):
        screen.fill('Black')        
        ship.draw(screen)
        ship.update(dt)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        pygame.display.flip()#dont ever forget

    

if __name__ == "__main__":
    main()