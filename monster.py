import pygame
import random
import animation

class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.health = 100
        self.max_health = 100
        self.attack = 0.3

        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 490 - offset
        self.game = game
        self.start_animation()
        self.loot_amount = 0

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, self.default_speed)

    def damage(self, amount):

        self.health -= amount

        if self.health <= 0:

            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health


            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)

                self.game.comet_event.attempt_fall()


            self.game.add_score(self.loot_amount)

    def set_loot_amount(self, amount):
        self.loot_amount += amount

    def update_animation(self):
        self.animate(True)
    def update_health_bar(self, surface):


        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])


    def forward(self):

        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity


        else:

            self.game.player.damage(self.attack)



class Policier(Monster):

    def __init__(self, game):
        super().__init__(game, "policier", (130, 130))
        self.set_speed(4)
        self.set_loot_amount(20)


class Gouja(Monster):
    def __init__(self, game):
        super().__init__(game, "gouja", (300, 300), 130)
        self.health = 1
        self.max_health = 1
        self.set_speed(2)
        self.attack = 0.5
        self.set_loot_amount(50)

class Vigile(Monster):
    def __init__(self, game):
        super().__init__(game, "vigile", (300, 300), 130)
        self.health = 1
        self.max_health = 1
        self.set_speed(1)
        self.attack = 0.8
        self.set_loot_amount(80)


