# app.py
import pygame
import random
from libs import block
from libs import grid
from libs import config
Config = config.Config

class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            Config['SCREEN_SIZE'], pygame.HWSURFACE | pygame.DOUBLEBUF )
        self.clock = pygame.time.Clock()
        self.grid = grid.Grid()
        self.all_sprites = pygame.sprite.Group()
        for _ in range(Config['BLOCK_AMOUNT']):
            self.all_sprites.add(block.Block((random.uniform(50,Config['SCREEN_SIZE'][0]-50), random.uniform(50,Config['SCREEN_SIZE'][1]-50)), \
                                 Config['BLOCK_SIZE'], Config['BLOCK_SPEED']))
        self.font = pygame.font.Font(None, 24)
        self.running = True
        
    def handle_events(self):  # sourcery skip: merge-nested-ifs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.MOUSEWHEEL:
                mods = pygame.key.get_mods()
                if mods & pygame.KMOD_CTRL:
                    if event.y == 1:
                        Config['BLOCK_AMOUNT'] += 1000
                    elif event.y == -1:
                        if Config['BLOCK_AMOUNT'] > 1000:
                            Config['BLOCK_AMOUNT'] -= 1000
                elif mods & pygame.KMOD_SHIFT:
                    if event.y == 1:
                        Config['BLOCK_AMOUNT'] += 100
                    elif event.y == -1:
                        if Config['BLOCK_AMOUNT'] > 100:
                            Config['BLOCK_AMOUNT'] -= 100
                else:
                    if event.y == 1:
                        Config['BLOCK_AMOUNT'] += 10
                    elif event.y == -1:
                        if Config['BLOCK_AMOUNT'] > 00:
                            Config['BLOCK_AMOUNT'] -= 10

    def update(self, dt):
        if Config['BLOCK_AMOUNT'] > len(self.all_sprites.sprites()):
            for _ in range(Config['BLOCK_AMOUNT'] - len(self.all_sprites.sprites())):
                self.all_sprites.add(block.Block((random.uniform(50,Config['SCREEN_SIZE'][0]-50), random.uniform(50,Config['SCREEN_SIZE'][1]-50)), \
                                    Config['BLOCK_SIZE'], Config['BLOCK_SPEED']))
        elif Config['BLOCK_AMOUNT'] < len(self.all_sprites.sprites()):
            self.all_sprites.remove(self.all_sprites.sprites())
        self.all_sprites.update(dt)
        self.grid.update()

    def draw_text(self):
        text_list_top = [
            f'{int(self.clock.get_fps())} FPS',
            f'{Config["GRID_UPDATE_INTERVAL"]} ms/Update'
        ]
        text_list_bottom = [
            f'Surface: {Config["SCREEN_SIZE"][0]}px*{Config["SCREEN_SIZE"][1]}px',
            f'Grid: {Config["GRID_SIZE"][0]}*{Config["GRID_SIZE"][1]}',
            f'Gridsize: {Config["SCREEN_SIZE"][0]/Config["GRID_SIZE"][0]}px*{Config["SCREEN_SIZE"][1]/Config["GRID_SIZE"][1]}px',
            f'Blocks: {Config["BLOCK_SIZE"][0]}px*{Config["BLOCK_SIZE"][1]}px (Amount: {Config["BLOCK_AMOUNT"]})',
            ' ',
            '   +/- 10 Block',
            '   +/- 100 Block (SHIFT)',
            '   +/- 1000 Block (CTRL)',
            'Add/Remove Blocks with Scrolling:',
        ]
        vertical_offset_t = 10
        vertical_offset_b = Config['SCREEN_SIZE'][1] - 10

        for text in text_list_top:
            text_surface = self.font.render(text, True, pygame.Color("white"))
            self.screen.blit(text_surface, (10, vertical_offset_t))
            vertical_offset_t += 25
        for text in text_list_bottom:
            text_surface = self.font.render(text, True, pygame.Color("white"))
            self.screen.blit(
                text_surface, (10, vertical_offset_b - 10))
            vertical_offset_b -= 25

    def draw(self):
        self.screen.fill(Config['BACKGROUND_COLOR'])
        self.screen.blit(self.grid.grid_surface, (0, 0))
        self.all_sprites.draw(self.screen)
        self.draw_text()
        pygame.display.flip()

    def run(self):
        while self.running:
            dt = self.clock.tick(2000) / 1000.0

            self.handle_events()
            self.update(dt)
            self.draw()
            pygame.display.flip()
            self.clock.tick(2000)
        pygame.quit()
        # Close the second window when the pygame loop ends
