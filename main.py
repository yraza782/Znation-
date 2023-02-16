import pygame
import math
from game import Game
from player import Player
pygame.init()

clock = pygame.time.Clock()
FPS = 60

pygame.display.set_caption("SHATTA SURVIVOR")
screen = pygame.display.set_mode((1024, 800))


background = pygame.image.load('assets/bg.png')
background = pygame.transform.scale(background, (1024, 800))

banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (666, 375))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/6.5)
banner_rect.y = math.ceil(screen.get_height()/5.5)


play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (549, 454))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 4.5)
play_button_rect.y = math.ceil(screen.get_height() / 2)

game = Game()
player = Player(game)
running = True

while running:

    screen.blit(background, (0, 0))


    if game.is_playing:

        game.update(screen)

    else:

        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)


    pygame.display.flip()


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeux !")

        elif event.type == pygame.KEYDOWN:

            game.pressed[event.key] = True

            if event.key == pygame.K_d:
                game.player.launch_projectile()

            if event.key == pygame.K_q:
                game.player.launch_projectile1()



        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if play_button_rect.collidepoint(event.pos):

                game.start()
                game.sound_manager.play1('bg')
                game.sound_manager.play('play')

clock.tick(FPS)