import pygame

pygame.init()
win = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
FPS = 60
font = pygame.font.SysFont("comicsans", 20)
# Rectangle
surface_rect = pygame.Surface((200, 100)).get_rect()
CENTER = (300, 100)
surface_rect.center = CENTER
# color
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SKY_BLUE = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
GRAY = (128, 128, 128)
OLIVE = (128, 128, 0)
NAVY = (0, 0, 128)
PURPLE = (128, 0, 128)

run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # fill the window
    win.fill((255, 255, 255))
    # draw rectangle
    pygame.draw.rect(win, (255, 0, 0), surface_rect)

    # draw background point
    for x in range(0, 800, 100):
        for y in range(0, 600, 100):
            font_surface = font.render(f"{x, y}", True, (0, 0, 0))
            win.blit(font_surface, (x, y+10))
            pygame.draw.circle(win, (0, 0, 0), (x, y), 5)

    # pygame.draw.circle(win, (RGB), (x, y), radius)
    pygame.draw.circle(win, BLUE, surface_rect.center, 5)
    pygame.draw.circle(win, GREEN, (surface_rect.x, surface_rect.y), 5)
    pygame.draw.circle(win, MAGENTA, surface_rect.midtop, 5)
    pygame.draw.circle(win, OLIVE, surface_rect.topright, 5)
    pygame.draw.circle(win, YELLOW, surface_rect.midright, 5)
    pygame.draw.circle(win, SKY_BLUE, surface_rect.bottomright, 5)
    pygame.draw.circle(win, NAVY, surface_rect.midbottom, 5)
    pygame.draw.circle(win, GRAY, surface_rect.bottomleft, 5)
    pygame.draw.circle(win, PURPLE, surface_rect.midleft, 5)
    pygame.display.update()
pygame.quit()
