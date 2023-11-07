import pygame as pg
from os import listdir
from random import choice

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
