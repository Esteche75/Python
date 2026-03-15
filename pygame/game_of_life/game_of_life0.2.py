# 1 en cell med mindre än 2 grannar dör av underpopulation.
# 2 en cell med 2 eller 3 lever vidare till nästa generation.
# 3 en cell med mer än 3 levande grannar dör av överpopulation.
# 4 en död cell med exakt 3 levande grannar blir levande och föds. 

import random
import os
import numpy as np
import cupy as cp
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"   # placera på primära skärmen
import pygame
from game_logic import update_grid_size, event_input, check_timing, draw_surface
pygame.init()
from gamestate import GameState
state = GameState()
update_grid_size(state)

# main loop

while state.running:
    state.clock.tick(60)
    event_input(state)
    check_timing(state)
    draw_surface(state)
    pygame.display.flip()
