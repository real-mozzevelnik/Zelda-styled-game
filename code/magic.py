import pygame
from settings import *
from random import randint
from file_path import res

class MagicPlayer:
    def __init__(self, animation_player):
        self.animation_player = animation_player
        self.sounds = {
        'heal': pygame.mixer.Sound(res('../audio/heal.wav')),
        'flame': pygame.mixer.Sound(res('../audio/Fire.wav'))}

    def heal(self, player, strength, cost, groups):
        if player.energy >= cost and player.health != player.stats['health']:
            self.sounds['heal'].play()
            player.health += strength
            player.energy -= cost
            if player.health >= player.stats['health']:
                player.health = player.stats['health']
            self.animation_player.create_particles('aura', player.rect.center, groups)
            self.animation_player.create_particles('heal', player.rect.center + pygame.math.Vector2(0, -60), groups)

    def flame(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost
            self.sounds['flame'].play()

            if player.status.split('_')[0] == 'right': direction = pygame.math.Vector2(1,0)
            elif player.status.split('_')[0] == 'left': direction = pygame.math.Vector2(-1,0)
            elif player.status.split('_')[0] == 'up': direction = pygame.math.Vector2(0,-1)
            else: direction = pygame.math.Vector2(0,1)

            for i in range(1, 6):
                if direction.x: # horizontal
                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x + randint(-TILESIZE//3, TILESIZE//3)
                    y = player.rect.centery + randint(-TILESIZE//3, TILESIZE//3)
                    self.animation_player.create_particles('flame', (x,y), groups)
                else: # vertical
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx + randint(-TILESIZE // 3, TILESIZE // 3)
                    y = player.rect.centery + offset_y  + randint(-TILESIZE // 3, TILESIZE // 3)
                    self.animation_player.create_particles('flame', (x, y), groups)
