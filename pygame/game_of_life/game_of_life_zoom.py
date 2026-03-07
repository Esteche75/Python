# 1 en cell med mindre än 2 grannar dör av underpopulation.
# 2 en cell med 2 eller 3 lever vidare till nästa generation.
# 3 en cell med mer än 3 levande grannar dör av överpopulation.
# 4 en död cell med exakt 3 levande grannar blir levande och föds. 

import pygame
import random

# Funktioner

def update_grid_size():
    global rows, cols, grid

    width, height = screen.get_size()

    rows = height // grid_size
    cols = width // grid_size

    grid = [[0 for _ in range(cols)] for _ in range(rows)]

def toggle_fullscreen():
    global screen, fullscreen

    fullscreen = not fullscreen

    if fullscreen:
        screen = pygame.display.set_mode((0,0), pygame.NOFRAME, display=0)
    else:
        screen = pygame.display.set_mode((1280,720))

    update_grid_size()

def update_grid(grid):
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            neighbors = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    r = (row + dr) % rows
                    c = (col + dc) % cols
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

            elif event.key == pygame.K_r:
                grid = [[1 if random.random() < 0.15 else 0 for _ in range(cols)] for _ in range(rows)]
            elif event.key == pygame.K_c:
                grid = [[0 for _ in range(cols)] for _ in range(rows)]
            elif event.key == pygame.K_f:
                toggle_fullscreen()
                

# Muskontroll

    if paused:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        col = mouse_x // grid_size
        row = mouse_y // grid_size

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

    for row in range(rows):
        for col in range(cols):

            x = col * grid_size
            y = row * grid_size

            if grid[row][col] == 1:
                color = WHITE
                pygame.draw.rect(screen, color, (x, y, grid_size, grid_size))

    pygame.display.flip()