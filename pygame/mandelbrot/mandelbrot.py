import pygame

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

surface = pygame.Surface((WIDTH, HEIGHT))

max_iter = 100

for x in range(WIDTH):
    for y in range(HEIGHT):

        # Mappa pixel → komplexa tal
        real = -2.0 + (x / WIDTH) * 3.0
        imag = -1.5 + (y / HEIGHT) * 3.0
        c = complex(real, imag)

        z = 0
        iterations = 0

        while abs(z) <= 2 and iterations < max_iter:
            z = z*z + c
            iterations += 1

        color = int(255 * iterations / max_iter)
        surface.set_at((x, y), (0, color, color))

screen.blit(surface, (0, 0))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()