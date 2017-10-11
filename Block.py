# Import everything

import pygame
import msvcrt
import random
import time
from math import *

# initialize all imported pygame modules + text for game over
pygame.init()
pygame.font.init()

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

class GameObject:
    def __init__(self):
        pass

class GameManager:
    def __init__(self):
        pass

class Coin(GameObject):
    def __init__(self):
        self.score = 0
        self.radius = 5


class Wall(GameObject):
    def __init__(self):
        pass

class Upgrades:
    def __init__(self):
        pass

class Player:
    def __init__(self):
        self.colour = (32, 178, 170)
        self.width = 25
        self.height = 25
        self.x = 125
        self.y = 375
        self.speed_y = 0
        self.a = 0
        self.speed_max_y = 0

    def update_position(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.speed_y = 0
                    self.a = 1
                    self.speed_max_y = 3
                    break
                if event.key == pygame.K_UP:
                    self.speed_y = 0
                    self.a = -1
                    self.speed_max_y = -3
                    break
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    break
                if event.key == pygame.K_UP:
                    break

    def move(self):
        if self.y < 0:
            self.speed_y = 0
            self.y += 1
        elif self.y > screen.height - self.height:
            self.speed_y = 0
            self.y -= 1
        else:
            if self.speed_y < abs(self.speed_max_y):
                self.speed_y += self.a
            elif self.speed_y > abs(self.speed_max_y):
                self.speed_y = self.speed_max_y

        self.y += self.speed_y
        self.y += self.speed_y

    def draw(self):
        screen.set_screen.fill(self.colour, (self.x, self.y, self.width, self.height))

    def update(self):
        self.update_position()
        self.move()
        self.draw()



# Calling screen class to make screen
screen = Screen()
player = Player()
screen.wipe()

# Countdown till start
game_start = True

while game_start:
    screen.game_start()
    game_start = False

# Game loop
while True:
    screen.wipe()
    player.update()
    pygame.display.flip()
