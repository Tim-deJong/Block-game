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
        self.speed = 10
        self.score = 0


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

    def create_object(self,object_to_create,y):
        object_to_create()
        object_to_create.y = random.randint(0,self.width)

    def move_object(self):
        pass


class Block:
    def __init__(self):
        pass

class GameManager:
    def __init__(self):
        pass

class GameObject(Screen):
    def _init_(self):
        super()._init_()

        self._x = 100
        self._y = 500
        # self._x = self.width
        # self._y = random.randrange(0, self.height)

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



    def check_collision(self, player: object):
        # TODO: PLAYER POSITION PRESUMED TO BE ON THE EDGE OF THE SCREEN, CHANGE THIS
        if self._x == 0:
            if self._y == player.y:
                self.collided = True

    def update(self):
        self.check_collision()

class Coin(GameObject):
    """Generates food particles and the choose a random position to deploy them, code also deploys them"""

    def __init__(self):
        """This will generate a random x position, y position, collor and radius for the food"""
        super().__init__()
        self.radius = random.randint(4)
        self.x_coordinate_coin = self.width
        self.y_coordinate_coin = random.randint(self.width)

        self.location = (self._x, self._y)
        self.colour = (255,255,0)

    def draw(self):
        pygame.draw.circle(screen.set_screen,self.colour,self.location,self.radius)
    def add_score(self):
        if self.collided == True:
            del self
            self.score += 1
            self.draw(self)

# Calling screen class to make screen
screen = Screen()
player = Player()
screen.wipe()
coin = Coin()
player = Player()

# Countdown till start
game_start = True

while True:
    tnow = float(pygame.time.get_ticks()) / 1000.
    dt = min((tnow - t0) * 2, maxdt)
    screen.fill(colour_background)
    pygame.event.pump()

    screen.wipe()
    keys_pressed()
    print(game_start)
    if game_start == True:
        print('...')
        break


while game_start:
    screen.game_start()
    game_start = False

# Game loop
while True:
    screen.wipe()
    player.update()
    pygame.display.flip()