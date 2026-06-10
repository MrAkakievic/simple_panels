
import pygame, simple_panels as sps
pygame.init()


screen = pygame.display.set_mode((900, 900))
sps.select_display(screen)
cl = pygame.time.Clock()

pos = [450, 450]
def move_left():
    global pos
    pos[0] -= 10
def move_right():
    global pos
    pos[0] += 10
def move_up():
    global pos
    pos[1] -= 10
def move_down():
    global pos
    pos[1] += 10

square = pygame.surface.Surface((50, 50))
square.fill((255, 255, 0))

def_design = sps.Design.button(animation_time = 5, press_animation = sps.Animation.NO_ANIMATION, release_animation = sps.Animation.SLASHING_EASE)
left_button = sps.TapButton('<', (20, 740, 80, 80), move_left, def_design)
right_button = sps.TapButton('>', (140, 740, 80, 80), move_right, def_design)
up_button = sps.TapButton('^', (80, 680, 80, 80), move_up, def_design)
down_button = sps.TapButton('v', (80, 800, 80, 80), move_down, def_design)

while True:
    screen.fill((0, 0, 0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    sps.handle(events)
    screen.blit(square, pos)
    left_button.pict()
    right_button.pict()
    up_button.pict()
    down_button.pict()
    pygame.display.flip()
    sps.update()
    cl.tick(60)


