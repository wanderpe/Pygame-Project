import pygame , sys

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("space invaders")
screen = pygame.display.set_mode((800, 500))
screen_rect = screen.get_rect()

while True:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
