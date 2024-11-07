import numpy as np
from perlin_noise import PerlinNoise
from config import WIDTH, HEIGHT, SCALE
import random
import math
from FlowField import FlowField
from Particle import Particle
import pygame

class Simulation():
    def __init__(self, num_particles: int) -> None:
        self.num_particles = num_particles
        
        self.num_rows = int(HEIGHT/SCALE)
        self.num_cols = int(WIDTH/SCALE)

        self.flowfield = FlowField(self.num_rows, self.num_cols, noiseScale=0.15)
        self.blockSize = int(WIDTH/self.flowfield.cols)
        
        self.particles = self.instantiateParticles()

    def instantiateParticles(self):
        return [
            Particle(
                (random.randrange(0, WIDTH), random.randrange(0, HEIGHT)),
                (random.uniform(-0.5,0.5), random.uniform(-0.5,0.5)),
                (0,0)
                )
            for _ in range(self.num_particles)
            ]
    
    def update(self):
        self.flowfield.zdim += 0.05
        self.flowfield.createFlowField()

        for p in self.particles:
            p.update()
            p.follow(self.flowfield.angleGrid, blockSize=self.blockSize, magnitude=0.2)