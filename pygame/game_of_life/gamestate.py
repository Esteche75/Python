import pygame
import numpy as np

class GameState:

    def __init__(self):
        self.fullscreen = False
        self.grid_size = 5
        self.clock = pygame.time.Clock()
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.CYBER_BLUE = (0,200,255)
        self.running = True
        self.simulation_speed = 100
        self.last_update = 0
        self.paused = True
        self.screen = pygame.display.set_mode((1280,720))
        self.width = 0
        self.height = 0
        self.rows = 0
        self.cols = 0
        self.grid = 0
        self.current_time = 0
        self.generation = 0
        self.live_cells = 0
        self.font = pygame.font.SysFont("consolas", 18)