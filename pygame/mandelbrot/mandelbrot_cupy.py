import pygame
import cupy as cp
import numpy as np

center_x = -0.5
center_y = 0.0
zoom = 1.0

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

max_iter = 100

scale = 1 / zoom

x_min = center_x - 1.5 * scale
x_max = center_x + 1.5 * scale

y_min = center_y - 1.5 * scale
y_max = center_y + 1.5 * scale

x = cp.linspace(x_min, x_max, WIDTH)
y = cp.linspace(y_min, y_max, HEIGHT)

X, Y = cp.meshgrid(x, y)
C = X + 1j * Y

Z = cp.zeros((HEIGHT, WIDTH), dtype=cp.complex64)
div_time = cp.zeros((HEIGHT, WIDTH), dtype=cp.int32)

for i in range(max_iter):
    Z *= Z
    Z += C
    diverged = cp.abs(Z) > 2
    div_time[(diverged) & (div_time == 0)] = i

# färg
color = (255 * div_time / max_iter).astype(cp.uint8)

rgb = cp.zeros((HEIGHT, WIDTH, 3), dtype=cp.uint8)
t = div_time / max_iter

rgb[:,:,0] = (cp.sin(6.28318*(t+0.0)) * 127 + 128).astype(cp.uint8)
rgb[:,:,1] = (cp.sin(6.28318*(t+0.33)) * 127 + 128).astype(cp.uint8)
rgb[:,:,2] = (cp.sin(6.28318*(t+0.66)) * 127 + 128).astype(cp.uint8)

# kopiera tillbaka till CPU för pygame
rgb_cpu = cp.asnumpy(rgb)

surface = pygame.surfarray.make_surface(rgb_cpu.swapaxes(0,1))

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                zoom *= 1.2
            else:
                zoom /= 1.2
        if pygame.mouse.get_pressed()[0]:

            dx, dy = pygame.mouse.get_rel()
            scale = 3 / zoom / WIDTH
            center_x -= dx * scale
            center_y -= dy * scale

    # skapa nya koordinater
    scale = 1/zoom

    x = cp.linspace(center_x-1.5*scale, center_x+1.5*scale, WIDTH)
    y = cp.linspace(center_y-1.5*scale, center_y+1.5*scale, HEIGHT)

    X,Y = cp.meshgrid(x,y)
    C = X + 1j*Y

    # Mandelbrot GPU
    Z[:] = 0
    div_time[:] = 0

    for i in range(max_iter):
        Z = Z*Z + C
        diverged = (Z.real*Z.real + Z.imag*Z.imag) > 4
        div_time[(diverged) & (div_time == 0)] = i

# färg
    t = div_time / max_iter

    rgb = cp.zeros((HEIGHT, WIDTH, 3), dtype=cp.uint8)

    rgb[:,:,0] = (cp.sin(6.28318*(t+0.0)) * 127 + 128).astype(cp.uint8)
    rgb[:,:,1] = (cp.sin(6.28318*(t+0.33)) * 127 + 128).astype(cp.uint8)
    rgb[:,:,2] = (cp.sin(6.28318*(t+0.66)) * 127 + 128).astype(cp.uint8)

    rgb[div_time == 0] = 0

    surface = pygame.surfarray.make_surface(cp.asnumpy(rgb).swapaxes(0,1))

    screen.blit(surface,(0,0))
    pygame.display.flip()
pygame.quit()