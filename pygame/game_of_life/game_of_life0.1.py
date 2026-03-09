# 1 en cell med mindre än 2 grannar dör av underpopulation.
# 2 en cell med 2 eller 3 lever vidare till nästa generation.
# 3 en cell med mer än 3 levande grannar dör av överpopulation.
# 4 en död cell med exakt 3 levande grannar blir levande och föds. 

import random
import os
import numpy as np
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"   # placera på primära skärmen
import pygame

# Funktioner

def update_grid_size():
    global rows, cols, grid

    width, height = screen.get_size()

    rows = height // grid_size
    cols = width // grid_size

    grid = np.zeros((rows, cols), dtype=np.uint8)


def toggle_fullscreen():
    global screen, fullscreen
    
    fullscreen = not fullscreen
    
    if fullscreen:
        screen = pygame.display.set_mode((0,0), pygame.NOFRAME)
    else:
        screen = pygame.display.set_mode((1280,720))
    
    update_grid_size()

def update_grid(grid):

    neighbors = (
        np.roll(grid, 1, 0) +
        np.roll(grid, -1, 0) +
        np.roll(grid, 1, 1) +
        np.roll(grid, -1, 1) +
        np.roll(np.roll(grid, 1,0),1,1) +
        np.roll(np.roll(grid, 1,0),-1,1) +
        np.roll(np.roll(grid,-1,0),1,1) +
        np.roll(np.roll(grid,-1,0),-1,1)
    )

    return ((neighbors == 3) | ((grid == 1) & (neighbors == 2))).astype(int)

def update_caption():
    pygame.display.set_caption(
        "Game of Life - PAUSED (R=random, C=clear, SPACE=unpause)"
        if paused else
        "Game of Life - RUNNING (R=random, C=clear, SPACE=pause)"
    )

# pygame setup
pygame.init()
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
grid_size = 5
running = True
simulation_speed = 100  # millisekunder (100ms = 10 per sekund)
last_update = 0
paused = False
fullscreen = False
pygame.display.set_caption("Game of Life - RUNNING (R=random, C=clear, SPACE=pause)")
#grid = [[0 for _ in range(cols)] for _ in range(rows)]
screen = pygame.display.set_mode((1280,720))
update_grid_size()



while running:

    dt = clock.tick(60)   # ← EN gång, högst upp

# Eventloop - Ta in knapptryckningar
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:        
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
                update_caption()
            elif event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_r:
                grid = (np.random.random((rows, cols)) < 0.2).astype(np.uint8)
            elif event.key == pygame.K_c:
                grid = np.zeros((rows, cols), dtype=np.uint8)
            elif event.key == pygame.K_f:
                toggle_fullscreen()
                

# Muskontroll

    if paused:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        col = mouse_x // grid_size
        row = mouse_y // grid_size

        buttons = pygame.mouse.get_pressed()

        if buttons[0]:
            grid[row, col] = 1
        if buttons[2]:
            grid[row, col] = 0   
        

    current_time = pygame.time.get_ticks()

    if not paused and current_time - last_update > simulation_speed:
        grid = update_grid(grid)
        last_update = current_time

    screen.fill(BLACK)

# Rita upp grid och flip till skärm

    surface = pygame.surfarray.make_surface((grid * 255).T)

    surface = pygame.transform.scale(
        surface,
        (cols * grid_size, rows * grid_size)
    )

    screen.blit(surface,(0,0))

    pygame.display.flip()