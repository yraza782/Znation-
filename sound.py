import pygame

class SoundManager:
    def __init__(self):
        self.sounds = {
            'bg': pygame.mixer.Sound("sound/cocotte.wav"),
            'play': pygame.mixer.Sound("sound/play.wav"),
            'mort': pygame.mixer.Sound("sound/introo.wav"),
            'rhum': pygame.mixer.Sound("sound/rhum.wav"),
            'eau': pygame.mixer.Sound("sound/eau.wav"),

        }

    def play1(self, name):
        self.sounds[name].play(loops=-1, maxtime=0, fade_ms=0)

    def play(self, name):
            self.sounds[name].play()
