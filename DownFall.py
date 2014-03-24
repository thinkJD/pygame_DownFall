# My first Python Game
# Its called Downfall, a brick with a specific (changable) shape muss be rotate and translated to fit a hole.

# imports
import pygame, sys, os
from pygame.locals import *
from player import *
from wall_ import *

# constants
# General
cScreenSize = width, height = 500, 700
# Colors
cColorBlack = (0, 0, 0)
cColorWhite = (255, 255, 255)
cColorSkyBlue = (135, 206, 250)
cColorOrange = (255, 165, 0)

class Downfall(object):
    # member
    clock = None
    running = False
    player = None
    all_Sprites = None
    enemy_sprites = None
    score = 0
    screen = None
    # sounds
    sound_death = None

    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

        self.player = Player(screen, 100, 100)
        self.all_sprites.add(self.player)
        tmp_wall = Wall(self.screen, 5)
        self.enemy_sprites.add(tmp_wall)
        self.all_sprites.add(tmp_wall)

        # load sounds
        self.sound_death = pygame.mixer.Sound("./Sound/sfx/Drop.wav")

        self.sound_music.play()


    def checkEvents(self):
        # handle QUIT event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def checkKeys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            # fire QUIT event
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    def update(self):
        self.all_sprites.update()
        collision_list = pygame.sprite.spritecollide(self.player, self.enemy_sprites, True)
        if len(collision_list) > 0:
            self.sound_death.play()
        self.all_sprites.draw(self.screen)


def main():
    pygame.init()
    screen = pygame.display.set_mode(cScreenSize)
    pygame.display.set_caption("Downfall")
    game = Downfall(screen)
    running = True

    while running:
        running = game.checkEvents()

        # Limit frame rate to 30 FPS
        game.clock.tick(30)
        game.checkKeys()
        # Draw game screen
        screen.fill(cColorSkyBlue)
        game.update()
        pygame.display.flip()

    # clean up
    pygame.quit()

# Call main() if this module called directly
if __name__ == "__main__": main()