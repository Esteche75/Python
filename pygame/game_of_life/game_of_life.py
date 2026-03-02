# 1 en cell med mindre än 2 grannar dör av underpopulation.
# 2 en cell med 2 eller 3 lever vidare till nästa generation.
# 3 en cell med mer än 3 levande grannar dör av överpopulation.
# 4 en död cell med exakt 3 levande grannar blir levande och föds. 


# Example file showing a basic pygame "game loop"
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

grid = [[1 if random.random() < 0.1 else 0 for _ in range(COLS)] for _ in range(ROWS)]

def update_grid(grid):
    new_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    for row in range(ROWS):
        for col in range(COLS):

            neighbors = 0

            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:

                    if dr == 0 and dc == 0:
                        continue

                    r = row + dr
                    c = col + dc

                    if 0 <= r < ROWS and 0 <= c < COLS:
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

while running:

    dt = clock.tick(60)   # ← EN gång, högst upp

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = pygame.time.get_ticks()

    if current_time - last_update > simulation_speed:
        grid = update_grid(grid)
        last_update = current_time

    screen.fill(BLACK)

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