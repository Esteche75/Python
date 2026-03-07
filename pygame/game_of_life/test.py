import pygame
pygame.init()
desktop_size = pygame.display.get_desktop_sizes()[0]
screen_width, screen_height = desktop_size[0] // 2, desktop_size[1] // 2

print(f'{desktop_size[0], desktop_size[1]}')
      
