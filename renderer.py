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
        fade_surface.fill((190, 190, 190, 50))
        self.screen.blit(fade_surface, (0,0))

        if self.simulation.draw_field:
            self.simulation.flowfield.draw(self.screen, WIDTH, HEIGHT, self.simulation.blockSize)

        if self.simulation.draw_particles:
            for particle in self.simulation.particles:
                particle.show(self.screen)
        
        if not self.record:
            pygame.display.flip()

        self.clock.tick(FPS)
    
    def get_frame(self):
        frame = pygame.surfarray.array3d(self.screen)
        frame = np.transpose(frame, (1,0,2))
        return frame

    def exit_requested(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
        return False
    
    def close(self):
        pygame.quit()