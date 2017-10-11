# Import everything

import pygame
import msvcrt
import random
import time
from math import *

# initialize all imported pygame modules + text for game over
pygame.init()
pygame.font.init()


def keys_pressed():
    keys = pygame.event.get()
    for event in keys:
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.K_ESCAPE:
            game_start = True
            return game_start


class Screen:
    def __init__(self):
        self.width = 1500
        self.height = 750
        self.set_screen = pygame.display.set_mode((self.width, self.height))
        self.screen_caption = pygame.display.set_caption('Collision')
        self.colour_background = (255, 255, 255)
        self.colour_text = (0, 0, 0)

    def wipe(self):
        self.set_screen.fill(self.colour_background)

    def sleep(self, seconds):
        time.sleep(seconds)

    def update(self):
        pygame.display.flip()

    def print_middle(self, text, size):
        used_font = pygame.font.SysFont('freesansbold.ttf', size)
        text_surface = used_font.render(text, True, self.colour_text)
        text_rect = text_surface.get_rect()
        text_rect.center = ((self.width / 2), (self.height / 2))
        self.set_screen.blit(text_surface, text_rect)

    def game_start(self):
        self.print_middle("Let's start", 100)
        self.update()
        self.sleep(1)
        self.wipe()

        self.print_middle("3 ....", 75)
        self.update()
        self.sleep(1)
        self.wipe()

        self.print_middle("2 ....", 75)
        self.update()
        self.sleep(1)
        self.wipe()

        self.print_middle("1 ....", 75)
        self.update()
        self.sleep(1)
        self.wipe()

        self.print_middle("GOOOOO", 75)
        self.update()
        self.sleep(1)
        self.wipe()


class Block:
    def __init__(self):
        pass


class Obstacle:
    def __init__(self):
        pass


class Camera:
    def __init__(self):
        pass


class Upgrades:
    def __init__(self):
        pass


class GameObject(Screen):
    def __init__(self):
        super().__init__()

        self._x = self.width
        self._y = random.randrange(0, self.height)

        self.velocity = 20

        self.time = pygame.time.get_ticks()
        self.collided = False

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    def move(self):
        delta_time = pygame.time.get_ticks() - self.time
        self.time = pygame.time.get_ticks()

        self._x -= self.velocity * delta_time

    def check_collision(self, player: object):
        # TODO: PLAYER POSITION PRESUMED TO BE ON THE EDGE OF THE SCREEN, CHANGE THIS
        if self._x == 0:
            if self._y == player.y:
                self.collided = True

    def update(self):
        self.check_collision()

# Calling screen class to make screen
screen = Screen()
screen.wipe()

# Countdown till start
game_start = False

while True:
    screen.wipe()
    keys_pressed()
    print(game_start)
    if game_start == True:
        print('...')
        break


while game_start:
    screen.game_start()
    game_start = False

while True:
    pygame.display.flip()
