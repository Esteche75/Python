import numpy as np
import pygame

def update_grid_size(state):

    
    state.width, state.height = state.screen.get_size()
    state.rows = state.height // state.grid_size
    state.cols = state.width // state.grid_size
    state.grid = np.zeros((state.rows, state.cols), dtype=np.uint8)

def toggle_fullscreen(state):

    state.fullscreen = not state.fullscreen    
    if state.fullscreen:
        state.screen = pygame.display.set_mode((0,0), pygame.NOFRAME)
    else:
        state.screen = pygame.display.set_mode((1280,720))    
    update_grid_size(state)

def update_grid(state):

    neighbors = (
        np.roll(state.grid, 1, 0) +
        np.roll(state.grid, -1, 0) +
        np.roll(state.grid, 1, 1) +
        np.roll(state.grid, -1, 1) +
        np.roll(np.roll(state.grid, 1,0),1,1) +
        np.roll(np.roll(state.grid, 1,0),-1,1) +
        np.roll(np.roll(state.grid,-1,0),1,1) +
        np.roll(np.roll(state.grid,-1,0),-1,1)
    )
    return ((neighbors == 3) | ((state.grid == 1) & (neighbors == 2))).astype(int)

def event_input(state):

    for event in pygame.event.get():
# keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state.paused = not state.paused
            elif event.key == pygame.K_q:
                state.running = False
            elif event.key == pygame.K_r:
                state.grid = (np.random.random((state.rows, state.cols)) < 0.2).astype(np.uint8)
            elif event.key == pygame.K_c:
                state.grid = np.zeros((state.rows, state.cols), dtype=np.uint8)
            elif event.key == pygame.K_f:
                toggle_fullscreen(state)
# mouse input
        if state.paused:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            col = mouse_x // state.grid_size
            row = mouse_y // state.grid_size
            buttons = pygame.mouse.get_pressed()
            if buttons[0]:
                if 0 <= row < state.rows and 0 <= col < state.cols:
                    state.grid[row, col] = 1
            if buttons[2]:
                if 0 <= row < state.rows and 0 <= col < state.cols:
                    state.grid[row, col] = 0    

def draw_surface(state):

# töm skärmen
    state.screen.fill(state.BLACK)
# rita upp grid och flip till skärm
    state.live_cells = np.sum(state.grid)
    state.surface = pygame.surfarray.make_surface((state.grid * 255).T)
    state.surface = pygame.transform.scale(
        state.surface,
        (state.cols * state.grid_size, state.rows * state.grid_size)
    )
    state.screen.blit(state.surface,(0,0))
    text = f"Gen: {state.generation}  Alive: {state.live_cells}"
    surface = state.font.render(text, True, state.CYBER_BLUE)
    state.screen.blit(surface, (10,10))

def check_timing(state):
    
    state.current_time = pygame.time.get_ticks()
    if not state.paused and state.current_time - state.last_update > state.simulation_speed:
        state.grid = update_grid(state)
        state.generation += 1
        state.last_update = state.current_time