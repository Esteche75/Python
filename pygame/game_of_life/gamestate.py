import pygame
import numpy as np
from game_logic import Slider

class GameState:

    def __init__(self):
        self.fullscreen = False
        self.clock = pygame.time.Clock()
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.CYBER_BLUE = (0,200,255)
        self.running = True
        self.last_update = 0
        self.paused = True
        self.screen = pygame.display.set_mode((1280,720))
        self.width = 0
        self.height = 0
        self.rows = 0
        self.cols = 0
        self.grid_slider = Slider(130, 100, 170, 2, 10, 5)
        self.grid = 0
        self.grid_size = int(self.grid_slider.get_value())
        self.current_time = 0
        self.generation = 0
        self.live_cells = 0
        self.font = pygame.font.SysFont("consolas", 18)
        self.density_slider = Slider(130, 60, 170, 0.0, 1.0, 0.25)
        self.density = self.density_slider.get_value()
        self.speed_slider = Slider(130, 80, 170, 200, 0, 100)
        self.simulation_speed = self.speed_slider.get_value()
        self.ui_rect = pygame.Rect(20,20,300,120)
        
        