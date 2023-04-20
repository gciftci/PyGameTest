# block.py
import pygame
import random
import math
from libs import config
Config = config.Config

class Block(pygame.sprite.Sprite):
    def __init__(self, position, size, speed):
        super().__init__()
        self.x = position[0]
        self.y = position[1]
        self.image = pygame.Surface(size)
        self.image.fill(Config['BLOCK_COLOR'])
        self.rect = self.image.get_rect(center=position)
        self.speed = speed
        self.direction = [random.uniform(0, 2* math.pi),random.uniform(0, 2* math.pi)]

    def update(self, dt):
        if self.rect.left <= 0 or self.rect.right >= Config['SCREEN_SIZE'][0]:
            self.direction[0] *= -1
        if self.rect.top <= 0 or self.rect.bottom >= Config['SCREEN_SIZE'][1]:
            self.direction[1] *= -1

        self.rect.x += self.speed * self.direction[0]
        self.rect.y += self.speed * self.direction[1]
