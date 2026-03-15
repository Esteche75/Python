import pygame
import numpy as np

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

max_iter = 100

# skapa komplex grid
x = np.linspace(-2.0, 1.0, WIDTH)
y = np.linspace(-1.5, 1.5, HEIGHT)
X, Y = np.meshgrid(x, y)
C = X + 1j * Y

Z = np.zeros_like(C)
div_time = np.zeros(C.shape, dtype=int)
mask = np.ones(C.shape, dtype=bool)

for i in range(max_iter):
    Z[mask] = Z[mask]**2 + C[mask]

    diverged = np.abs(Z) > 2
    div_now = diverged & mask

    div_time[div_now] = i
    mask[diverged] = False

color = (255 * div_time / max_iter).astype(np.uint8)

rgb = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
rgb[:,:,1] = color
rgb[:,:,2] = color

surface = pygame.surfarray.make_surface(rgb.swapaxes(0,1))

screen.blit(surface, (0,0))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()