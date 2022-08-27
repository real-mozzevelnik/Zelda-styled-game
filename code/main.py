import pygame, sys
from settings import *
from level import Level
from menu import Menu
from game_stats import Stat
from file_path import res

class Game:
    def __init__(self):

        # general setup
        pygame.mixer.pre_init(44100, -16, 2, 1024)
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

        # stat
        self.stat = Stat()

        self.level = Level(self.stat)
        self.menu = Menu(self.stat)

        # sound
        main_sound = pygame.mixer.Sound(res('../audio/main.ogg'))
        main_sound.set_volume(0.5)
        main_sound.play(loops=-1)

    def check_stat(self):
        if self.stat.stat_now == 'menu':
            self.menu.run()
        elif self.stat.stat_now == 'run_level':
            self.level.run()
        elif self.stat.stat_now == 'death':
            self.level = None
            self.level = Level(self.stat)
            self.stat.stat_now = 'menu'
        elif self.stat.stat_now == 'win':
            self.level = None
            self.level = Level(self.stat)
            self.stat.stat_now = 'menu'

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m and self.level.level_is_running:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)
            self.check_stat()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()