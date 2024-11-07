import numpy as np
from math import cos, sin
import pygame
from config import WIDTH, HEIGHT, FPS

class Renderer():
    def __init__(self, simulation, record: bool = False) -> None:
        self.simulation = simulation
        self.record = record
        
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) if not self.record else pygame.Surface((WIDTH, HEIGHT))
        self.background_color = (190,190,190,255)
        self.screen.fill(self.background_color)

        self.clock = pygame.time.Clock()
    
    def render_flow(self):

        fade_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        fade_surface.fill((190, 190, 190, 30))
        self.screen.blit(fade_surface, (0,0))

        for particle in self.simulation.particles:
            particle.show(self.screen)
        
        if not self.record:
            pygame.display.flip()

        self.clock.tick(FPS)
    
    def draw_field(self, field, blockSize: int):
        
        self.screen.fill((190, 190, 190))
        
        for x in range(0, WIDTH, blockSize):
            for y in range(0, HEIGHT, blockSize):
                
                angle = field[y//blockSize][x//blockSize]

                origin = (x + blockSize // 2, y + blockSize // 2)
                end_x = origin[0] + blockSize // 2 * cos(angle)
                end_y = origin[1] + blockSize // 2 * sin(angle)
                pygame.draw.line(self.screen, (0, 0, 0), origin, (end_x, end_y))
        
        pygame.display.update()
    
    def get_frame(self):
        frame = pygame.surfarray.array3d(self.screen)
        frame = np.transpose(frame, (1,0,2))
        return frame

    def exit_requested(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False
    
    def close(self):
        pygame.quit()