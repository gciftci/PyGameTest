# grid.py
import pygame
import random
from libs import config
Config = config.Config

class Grid:
    def __init__(self):
        self.grid_surface = pygame.Surface(Config['SCREEN_SIZE']).convert_alpha()
        self.opacities = [[random.randint(150, 175) for _ in range(
            Config['GRID_SIZE'][1])] for _ in range(Config['GRID_SIZE'][0])]
        self.last_update = pygame.time.get_ticks()
        self.cell_width = Config['SCREEN_SIZE'][1] // Config['GRID_SIZE'][1]
        self.cell_height = Config['SCREEN_SIZE'][0] // Config['GRID_SIZE'][0]

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update > Config['GRID_UPDATE_INTERVAL']:
            self.last_update = current_time
            self.opacities = [[random.randint(150, 175) for _ in range(
                Config['GRID_SIZE'][1])] for _ in range(Config['GRID_SIZE'][0])]

        for i in range(Config['GRID_SIZE'][1]):
            for j in range(Config['GRID_SIZE'][0]):
                cell_rect = pygame.Rect(
                    i * self.cell_width, j * self.cell_height,
                    self.cell_width, self.cell_height)
                if self.opacities[j][i]:
                    opacity = self.opacities[j][i]
                color = pygame.Color(255, 0, 0, opacity)
                pygame.draw.rect(self.grid_surface, color, cell_rect)
