import pygame
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_manager import EnemyManager
from game.components.menu import Menu
from game.components.death_menu import DeathMenu
from game.components.power_ups.powerups_manager import PowerupsManager


from game.components.spaceship import Spaceship

from game.utils.constants import BG, FINAL_TITLE_1, FONT_STYLE, GAMEOVER, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP_DESTROY, TITLE, FPS, DEFAULT_TYPE, TITLE_1, TITLE_2


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.score = 0
        self.death_count = 0 
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.enemy = Enemy()
        self.bullet_manager = BulletManager()
        self.running = False
        self.menu = Menu(ICON, TITLE_1, TITLE_2, "", text_size=24)
        self.death_menu = DeathMenu(SPACESHIP_DESTROY,GAMEOVER, FINAL_TITLE_1, "message 3")
        self.power_up_manager = PowerupsManager()



    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def play(self):
        self.reset_all()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            
    
    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self.bullet_manager) 
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def draw_power_up_duration(self):
        if self.player.has_power_up:
            font = pygame.font.Font(FONT_STYLE, 22)
            current_time = pygame.time.get_ticks()
            time_left = max(0, self.duration - (current_time - self.power_up_start_time))
            time_text = font.render(f"Power-up Duration: {time_left / 1000:.1f}s", True, (255, 255, 255))
            time_text_rect = time_text.get_rect()
            time_text_rect.center = (1000, 80)
            self.screen.blit(time_text, time_text_rect)

    def show_menu(self):
        if self.death_count > 0:
            self.death_menu.update_highest_score(self.score)
            self.highest_score = self.death_menu.highest_score
        
            self.death_menu.update_message( SPACESHIP_DESTROY ,GAMEOVER, FINAL_TITLE_1, f"DEATHS: {self.death_count}")
            
            self.death_menu.draw(self.screen)
            self.menu.events(self.on_close, self.play)
        else:
            self.menu.draw(self.screen)
            self.menu.events(self.on_close, self.play)

    def on_close(self):
        self.playing = False
        self.running = False
    
    def reset_all(self):
        self.bullet_manager.reset()
        self.enemy_manager.reset()
        self.playing = True
        self.score = 0
        self.power_up_manager.reset()
        

    
