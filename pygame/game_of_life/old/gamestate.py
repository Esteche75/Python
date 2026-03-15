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
        self.rle1 = """2o41b$o42b$o11bo30b$12b3o14b3o11b5$3b2o38b$3bo39b12$29bo11bob$29b3o10b
o$42bo$25bo15b2o$24b2o!"""
        self.rle2 = """b2o36b$b2o17bo18b$19bobo12bobo2b$20bo12bo5b$2o7b2o23bo2bob$2obo5b2o23b
obobo$3bo23bo7bo2bo$3bo23b2o7b2ob$o2bo17b2o5bo10b$b2o18bo17b$21b3o15b$
36b2ob$36b2ob$b2o36b$o2bo35b$obobo16bobo4b2o5b2o2b$bo2bo17b2o4b2o5b2ob
o$5bo12bo3bo15bo$2bobo12bobo18bo$18bo16bo2bo$36b2o!"""
        
        