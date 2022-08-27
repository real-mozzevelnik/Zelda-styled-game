import pygame
from settings import *

class Menu:
    def __init__(self, level):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, 72)
        self.back = pygame.image.load('../graphics/tilemap/menu_back.png').convert_alpha()

        # stat sys
        self.level = level

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.level.stat = 'run_level'

    def draw_button(self, l, t, w, h, text, color):
        info_surf = self.font.render(text, False, color)
        rect = pygame.Rect(l,t,w,h)

        pygame.draw.rect(self.display_surface, HEALTH_COLOR, rect)
        self.display_surface.blit(info_surf, (l,t))

    def run(self):
        self.display_surface.blit(self.back,(0,0))
        self.draw_button(500, 200, 285, 100, 'Start', UI_BORDER_COLOR)
        self.input()