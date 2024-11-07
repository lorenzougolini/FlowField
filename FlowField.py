import random
import math
from perlin_noise import PerlinNoise
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