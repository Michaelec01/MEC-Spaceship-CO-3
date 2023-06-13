import pygame
from pygame.sprite import Sprite
from game.utils.constants import SCREEN_HEIGHT, SPACESHIP
from game.utils.constants import SCREEN_WIDTH


class Spaceship(Sprite):
    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (60, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 500

    def update(self, user_input):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
    
    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 10
        elif self.rect.left <= 0 and abs(self.rect.left >= -50 ) :
            self.rect.x -= 10
        else:
            self.rect.x = SCREEN_WIDTH
        
    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10
        elif self.rect.left <= SCREEN_WIDTH and abs(self.rect.left - SCREEN_WIDTH) >= 1:
            self.rect.x += 10
        else: 
            self.rect.x = (SCREEN_WIDTH) - (SCREEN_WIDTH - -50)

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= 10
         
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 50:
            self.rect.y += 10

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


