import random
from operator import add
from config import WIDTH, HEIGHT
import math
import pygame

class Particle():
    def __init__(self, pos: tuple, vel: tuple, acc: tuple) -> None:
        self.pos = self.prev_pos = pos
        self.vel = vel
        self.acc = acc
        
        self.color = (random.randrange(50, 256), random.randrange(0, 50), random.randrange(0, 50), 50)
        self.head_color = tuple(self.color[:-1])

    def update(self):
        self.vel = tuple(map(add, self.vel, self.acc))

        max_speed = 1.5
        self.vel = (min(max(self.vel[0], -max_speed), max_speed),
                    min(max(self.vel[1], -max_speed), max_speed))
        
        p = list(map(add, self.pos, self.vel))
        if p[0] > WIDTH or p[0] < 0 or p[1] > HEIGHT or p[1] < 0:
            self.pos = self.prev_pos = (random.randrange(0, WIDTH), random.randrange(0, HEIGHT))
        else:
            self.prev_pos = self.pos
            self.pos = tuple(p)

        # self.pos = ((self.pos[0]+self.vel[0])%WIDTH, (self.pos[1]+self.vel[1])%HEIGHT)

        self.acc = (0,0)

    def follow(self, vects: list, blockSize: int, magnitude: float = 0.5):
        """
        vects: matrix of angles
        blockSize: size of each cell in the matrix
        magnitude: the amount of force to apply
        """
        row = min(int(self.pos[1] // blockSize), len(vects) - 1)
        col = min(int(self.pos[0] // blockSize), len(vects[0]) - 1)
        angle = vects[row][col]
        v = (magnitude*math.cos(angle), magnitude*math.sin(angle))

        self.apply(v)

    def apply(self, force: tuple):
        """
        force[0]: angle
        force[1]: magnitude
        """
        self.acc = tuple(map(add, self.acc, force))
    
    def show(self, screen):
        # particle_surface = pygame.Surface((4,4), pygame.SRCALPHA)
        # pygame.draw.circle(particle_surface, (0, 0, 0, 50), (2,2), 2, width=2)
        # screen.blit(particle_surface, (int(self.pos[0]), int(self.pos[1])))
        
        # line_surface = pygame.Surface((4,4), pygame.SRCALPHA)
        pygame.draw.circle(screen, self.head_color, self.pos, radius=2, width=2)
        pygame.draw.line(screen, self.color, self.prev_pos, self.pos, width=2)