import pygame
from game import Game
from player import Player

pygame.init()

pygame.display.set_caption("Z NATION")
screen = pygame.display.set_mode((1024, 800))

background = pygame.image.load('assets/bg.png')

game =Game()
player = Player()

running = True

while running :

    screen.blit(background, (0,0))

    screen.blit(game.player.image, game.player.rect)

    for projectile in game.player.all_projectiles:
        projectile.move()

    game.player.all_projectiles.draw(screen)

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x >0:
        game.player.move_left()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

