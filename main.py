import pygame
import random
import pnoise_lib as fun
import math


def sigmoid(x):
  return 255 / (1 + math.exp(-x))


pygame.init()


FPS = 60
width = 512
height = 512
size = (width, height)
FONT = pygame.font.Font(None, 40)
dx = width // fun.da
dc = 1

running = True
x, y, a, b = 0, 0, 0, 0
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

level_slider = fun.Slider((20, 80), dc / 2)
sliders = [level_slider]

noize_temp = fun.noise()

'''
def color_from_weight(w):
    return w * 255, w * 255, w * 255
'''


def color_from_weight(w):
    global dc
    if w <= 0.5 * dc:
        print(int(50 * w * 2), int(50 * w * 2), int(255 * w * 1.5))
        return int(0.2 * sigmoid(w)), int(0.2 * sigmoid(w)), int(sigmoid(w))
    elif w <= 0.60 * dc:
        return 255, 224, 66
    elif w <= 0.75 * dc:
        return 148, 255, 66
    elif w <= 0.95 * dc:
        return 7, 130, 39
    else:
        return 250, 250, 250


def render(sc, noize):
    for c in range(fun.da):
        for c1 in range(fun.da):
            pygame.draw.rect(sc, color_from_weight(noize[c][c1]), (c * dx, c1 * dx, dx, dx))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEMOTION:
            a, b = event.pos
            for slider in sliders:
                if slider.pressed:
                    if 0 < a - 15 < 400:
                        slider.xp = a - 15
                slider.crossing(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for slider in sliders:
                if slider.crossing((x, y)):
                    slider.press()
        if event.type == pygame.MOUSEBUTTONUP:
            for slider in sliders:
                if slider.pressed:
                    if slider == level_slider:
                        dc = slider.get_pos() * 2

    screen.fill((40, 40, 40))
    render(screen, noize_temp)
    screen.blit(FONT.render(str(int(clock.get_fps())), True, (200, 50, 50)), (5, 5))

    for slider in sliders:
        slider.render(screen)

    pygame.display.flip()
    clock.tick(FPS)
