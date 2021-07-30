import pygame

pygame.init()
win = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
FPS = 60

run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # fill the window
    win.fill((0, 0, 255))
    # create semi-transparent surface
    transparent_surface = pygame.Surface((100, 100), pygame.SRCALPHA)
    transparency = 0  # define transparency: 0~255, 0 is fully transparent
    # draw the rectangle on the transparent surface
    pygame.draw.rect(transparent_surface, (255, 0, 0, transparency), [0, 0, 50, 50])

    win.blit(transparent_surface, (400, 400))
    pygame.display.update()
pygame.quit()
