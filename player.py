import pygame
from Projectile import Projectile, Projectile1
import animation

class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('desir')
        self.game = game
        self.healt = 100
        self.max_healt = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 450
        self.game = game

    def damage(self, amount):
        if self.healt - amount > amount:
            self.healt -= amount
        else:
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_healt_bar(self, surface):

        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_healt, 7])
        pygame.draw.rect(surface, (111, 210, 46),  [self.rect.x + 50, self.rect.y + 20, self.healt, 7])

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
        self.start_animation()
        self.game.sound_manager.play('rhum')

    def launch_projectile1(self):
        self.all_projectiles.add(Projectile1(self))
        self.start_animation()
        self.game.sound_manager.play('rhum')

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_lef(self):
        self.rect.x -= self.velocity