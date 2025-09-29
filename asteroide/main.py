import pygame 
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    delta = pygame.time.Clock()
    
    shots = pygame.sprite.Group()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    AsteroidField.containers = (updatable)

    Asteroid.containers = (asteroids, updatable, drawable)

    asteroidfield = AsteroidField()

 
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)

    dt = 0
    
    player = Player(x = SCREEN_WIDTH / 2 , y = SCREEN_HEIGHT / 2)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
    


        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    
                    shot.kill()
                    print("bowwwwwwwwwwwwwww")
                    new_asteroids = asteroid.split()
                    if new_asteroids:
                        asteroids.add(new_asteroids)





        screen.fill("black")

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        
        dt = delta.tick(60) / 1000




if __name__ == "__main__":
    main()
