import pygame as pg
from os import listdir
from random import choice
# dvelop branch
pg.init()
pg.font.init()

win = pg.display.set_mode((500, 300))
pg.display.set_caption("Music Box")
clock = pg.time.Clock()
running = True

image = pg.image.load('img/bg.jpg')
bg = pg.transform.scale(image, (500, 300))

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    win.fill('purple') # заливка фона
    # win.blit(bg, (0, 0))
    pg.display.update()
    clock.tick(40)  # limits FPS to 60

# TODO: мерцание цветов фона
# TODO: быстрое переключение фонового изображения
# TODO: изменение фона по нажатию на любую из клавиш

# 1 TODO - 1 коммит

import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 300))
clock = pg.time.Clock()
running = True
clr = (255, 255, 255, 255)
clr2 = (0, 225, 0)
clr3 = (255, 0, 225)
color = ['red', 'orange', 'yellow', 'green', 'blue']
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # keys = pg.key.get_pressed()
        # if keys[pg.K_1] == True:
        #     screen.fill(clr)
        # elif keys[pg.K_2] == True:
        #     screen.fill(clr2)
        # elif keys[pg.K_3] == True:
        #     screen.fill(clr3) 
        random_clr = choice(color)
        screen.fill('purple') 
    pg.display.update()
    clock.tick(60)