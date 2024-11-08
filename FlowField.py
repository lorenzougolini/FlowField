import random
import math
from perlin_noise import PerlinNoise
from pygame import draw
import numpy as np

class FlowField():
    def __init__(self, rows: int, cols: int, noiseScale: float = 0.1) -> None:
        self.rows = rows
        self.cols = cols

        self.noise = PerlinNoise()
        self.scale = noiseScale
        self.angleGrid = np.zeros((rows, cols))
        
        self.zdim = 0

        self.createFlowField()

    def gridInit(self):
        self.angleGrid[0][0] = random.uniform(0, 4*math.pi)

    def createFlowField(self):
        for r in range(0, self.rows):
            for c in range(0, self.cols):
                noise_val = self.noise([r*self.scale, c*self.scale, self.zdim*self.scale])
                self.angleGrid[r][c] = (noise_val+1)/2 *4*math.pi

    def draw(self, screen, WIDTH: int, HEIGHT: int, blockSize: int):
        screen.fill((190, 190, 190))
        
        for x in range(0, WIDTH, blockSize):
            for y in range(0, HEIGHT, blockSize):
                
                angle = self.angleGrid[y//blockSize][x//blockSize]

                origin = (x + blockSize // 2, y + blockSize // 2)
                end_x = origin[0] + blockSize // 2 * math.cos(angle)
                end_y = origin[1] + blockSize // 2 * math.sin(angle)
                draw.line(screen, (0, 0, 0), origin, (end_x, end_y))
        
        # pygame.display.update()