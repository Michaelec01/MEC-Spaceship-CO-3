import pygame
import random
from game.utils.constants import  ENEMY_TYPE, METEOR_1, SCREEN_HEIGHT, SCREEN_WIDTH
from game.components.enemies.enemy import Enemy


class Meteor(Enemy):
    X_POS_LIST = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900]
    Y_POS = -50
    SPEED_Y = 7

    def __init__(self):
        self.image = pygame.transform.scale(METEOR_1,(30, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.type = ENEMY_TYPE
        self.speed_y = self.SPEED_Y


    def update(self, ships):
        self.rect.y += self.speed_y
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
