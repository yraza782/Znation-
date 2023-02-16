import pygame
import random


class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False

    def start_animation(self):
        self.animation = True

    def animate(self, loop = False):


        if self.animation:


            self.current_image += random.randint(0, 1)
            if self.current_image >= len(self.images):
                self.current_image = 0
                if loop is False:
                    self.animation = False

            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)



def load_animation_images(sprite_name):
    images = []

    path = f'assets/{sprite_name}/{sprite_name}'

    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    return images



animations = {
    'policier': load_animation_images('policier'),
    'desir': load_animation_images('desir'),
    'gouja': load_animation_images('gouja'),
    'vigile': load_animation_images('vigile')
}