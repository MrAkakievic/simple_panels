import pygame, simple_panels as sps
pygame.init()

DISPLAY_SIZE = (1600, 900)
FPS = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode(DISPLAY_SIZE)
sps.select_display(screen)

def func():                      # Logic when button clicked
    ...
button = sps.TapButton('Tap Me', (300, 300, 300, 200), func)

while True:
    screen.fill((0, 0, 0))
    events = pygame.event.get()
    sps.handle(events)
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    sps.pict()
    sps.update()
    pygame.display.flip()
    clock.tick(FPS)
