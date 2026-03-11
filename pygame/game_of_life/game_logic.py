import numpy as np
import pygame

class Slider:

    def __init__(self, x, y, width, min_val, max_val, start_val):

        self.rect = pygame.Rect(x, y, width, 4)

        self.min_val = min_val
        self.max_val = max_val

        self.knob_radius = 8
        self.dragging = False

        t = (start_val - min_val) / (max_val - min_val)
        self.knob_x = x + t * width
        self.y = y


    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            mx, my = pygame.mouse.get_pos()

            knob_rect = pygame.Rect(
                self.knob_x - self.knob_radius,
                self.y - self.knob_radius,
                self.knob_radius * 2,
                self.knob_radius * 2
            )

            if knob_rect.collidepoint(mx, my):
                self.dragging = True

            elif self.rect.collidepoint(mx, my):
                self.knob_x = mx


        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False


        elif event.type == pygame.MOUSEMOTION and self.dragging:

            mx, _ = pygame.mouse.get_pos()
            self.knob_x = mx


        self.knob_x = max(self.rect.left, min(self.knob_x, self.rect.right))


    def draw(self, screen):

        pygame.draw.rect(screen, (0,120,255), self.rect)

        pygame.draw.circle(
            screen,
            (0,200,255),
            (int(self.knob_x), self.y + 2),
            self.knob_radius
        )


    def get_value(self):

        t = (self.knob_x - self.rect.left) / self.rect.width
        return self.min_val + t * (self.max_val - self.min_val)

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
                state.grid = (np.random.random((state.rows, state.cols)) < state.density).astype(np.uint8)
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
            if not state.ui_rect.collidepoint(mouse_x, mouse_y):
                if buttons[0]:
                    if 0 <= row < state.rows and 0 <= col < state.cols:
                        state.grid[row, col] = 1
                if buttons[2]:
                    if 0 <= row < state.rows and 0 <= col < state.cols:
                        state.grid[row, col] = 0  

            state.density_slider.handle_event(event)
            state.speed_slider.handle_event(event)
            state.grid_slider.handle_event(event)
            state.density = state.density_slider.get_value()
            state.simulation_speed = state.speed_slider.get_value()
            old_grid_size = state.grid_size
            state.grid_size = int(state.grid_slider.get_value())

            if state.grid_size != old_grid_size:
                update_grid_size(state)
          

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
    draw_ui(state)

def check_timing(state):
    
    state.current_time = pygame.time.get_ticks()
    if not state.paused and state.current_time - state.last_update > state.simulation_speed:
        state.grid = update_grid(state)
        state.generation += 1
        state.last_update = state.current_time

def text_ui(state, text, x, y):

    glow = state.font.render(text, True, (0,120,255))
    state.screen.blit(glow, (x+1, y+1))
    text_surface = state.font.render(text, True, (0,200,255))
    state.screen.blit(text_surface, (x, y))

def draw_ui(state):

    # skapa transparent surface
    ui_surface = pygame.Surface((300, 120), pygame.SRCALPHA)
   
    # rita en halvtransparent rektangel

    pygame.draw.rect(ui_surface, (20, 20, 40, 180), ui_surface.get_rect(), border_radius=8)
    pygame.draw.rect(ui_surface, (0, 180, 255), ui_surface.get_rect(), 2, border_radius=8)

    # rita den ovanpå spelet
    state.screen.blit(ui_surface, (20, 20))
    text = f"Gen: {state.generation}  Alive: {state.live_cells}"
    text_ui(state, text, 30, 30)
    text_ui(state, 'Density', 30, 50)
    text_ui(state, 'Speed', 30, 70)
    text_ui(state, 'Grid size',30, 90)
    state.density_slider.draw(state.screen)
    state.speed_slider.draw(state.screen)
    state.grid_slider.draw(state.screen)