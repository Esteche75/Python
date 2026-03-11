# 1 en cell med mindre än 2 grannar dör av underpopulation.
# 2 en cell med 2 eller 3 lever vidare till nästa generation.
# 3 en cell med mer än 3 levande grannar dör av överpopulation.
# 4 en död cell med exakt 3 levande grannar blir levande och föds. 

import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRID_SIZE = 5
ROWS = 160
COLS = 160
running = True
simulation_speed = 100  # millisekunder (100ms = 10 per sekund)
last_update = 0
paused = False
pygame.display.set_caption("Game of Life - RUNNING (R=random, C=clear, SPACE=pause)")
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# Funktioner

def update_grid(grid):
    new_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    for row in range(ROWS):
        for col in range(COLS):

            neighbors = 0

            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:

                    if dr == 0 and dc == 0:
                        continue

                    r = (row + dr) % ROWS
                    c = (col + dc) % COLS

                    neighbors += grid[r][c]

            # Game of Life rules
            if grid[row][col] == 1:
                if neighbors < 2:
                    new_grid[row][col] = 0
                elif neighbors in [2, 3]:
                    new_grid[row][col] = 1
                else:
                    new_grid[row][col] = 0
            else:
                if neighbors == 3:
                    new_grid[row][col] = 1

    return new_grid

def update_caption():
    pygame.display.set_caption(
        "Game of Life - PAUSED (R=random, C=clear, SPACE=unpause)"
        if paused else
        "Game of Life - RUNNING (R=random, C=clear, SPACE=pause)"
    )

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

            elif event.key == pygame.K_r:
                grid = [[1 if random.random() < 0.1 else 0 for _ in range(COLS)] for _ in range(ROWS)]
            elif event.key == pygame.K_c:
                grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
# Muskontroll

    if paused:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        col = mouse_x // GRID_SIZE
        row = mouse_y // GRID_SIZE

        buttons = pygame.mouse.get_pressed()

        if buttons[0]:
            grid[row][col] = 1
        if buttons[2]:
            grid[row][col] = 0   
        

    current_time = pygame.time.get_ticks()

    if not paused and current_time - last_update > simulation_speed:
        grid = update_grid(grid)
        last_update = current_time

    screen.fill(BLACK)

# Rita upp grid och flip till skärm

    for row in range(ROWS):
        for col in range(COLS):

            x = col * GRID_SIZE
            y = row * GRID_SIZE

            if grid[row][col] == 1:
                color = WHITE
            else:
                color = BLACK

            pygame.draw.rect(screen, color, (x, y, GRID_SIZE, GRID_SIZE))

    pygame.display.flip()