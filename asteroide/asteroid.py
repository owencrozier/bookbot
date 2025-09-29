from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid (CircleShape):
    def __init__ (self, x, y, radius):
        super().__init__(x,y,radius)
        # self.pos_x = x
        # self.pos_y = y
        # self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        
        self.position += self.velocity * dt
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        random_angle = random.uniform(20, 50)
        opposite_random_angle = -random_angle

        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(opposite_random_angle)

        newborns_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroide1 = Asteroid ( self.position.x, self.position.y, newborns_radius)
        asteroide2 = Asteroid ( self.position.x, self.position.y, newborns_radius)

        asteroide1.velocity = vector1
        asteroide2.velocity = vector2

        self.kill()
        return [asteroide2, asteroide1]
        



    
