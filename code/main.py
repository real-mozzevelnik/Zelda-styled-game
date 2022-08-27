import pygame, sys
from settings import *
from level import Level
from game_stats import Menu

class Game:
    def __init__(self):

        # general setup
        pygame.mixer.pre_init(44100, -16, 2, 1024)
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

        self.level = Level()
        self.menu = Menu(self.level)

        # sound
        main_sound = pygame.mixer.Sound('../audio/main.ogg')
        main_sound.set_volume(0.5)
        main_sound.play(loops=-1)

    def check_stat(self):
        if self.level.stat == 'menu':
            self.menu.run()
        elif self.level.stat == 'run_level':
            self.level.run()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)
            self.check_stat()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()