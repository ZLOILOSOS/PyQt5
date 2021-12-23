import pygame
import sys
import os
import random

pygame.init()
width, height = 800, 600
size = width, height
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PyGame")

fps = 40
speed = 40
durability = 1
amount = 8


def set_parameters():
    pass


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()

    return image


all_sprites = pygame.sprite.Group()


def menu_window():
    pass


def game_window():
    clock = pygame.time.Clock()
    fps = 40
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def end_winodw():
    pass


if __name__ == '__main__':
    # pygame.mouse.set_visible(False)

    menu_window()
    game_window()

    pygame.quit()
