# imports
import pygame, sys, os
from pygame.locals import *
from player import *
from wall_ import *
import json
from os import path

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
    level = None
    lives_count = 0
    bar_count = 0


    def __init__(self, screen, path_level):
        self.screen = screen
        self.path_level = path_level
        # load level file
        self.load_level(path_level)

        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

        self.player = Player(screen, 100, 100)
        self.all_sprites.add(self.player)

        # load sounds
        self.sound_death = pygame.mixer.Sound("./Sound/sfx/Drop.wav")


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

    def handle_collision(self):
        # check collision between player and enemy sprites
        collision_list = pygame.sprite.spritecollide(self.player, self.enemy_sprites, True)
        # if a collision is detected, handle player death
        if len(collision_list) > 0:
            print "Collision detected"
            if self.level['lives'] > 0:
                self.level['lives'] -= 1
                print "Remaining lives: %s" % self.level['lives']
            else:
                # game over
                self.sound_death.play()
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    def draw_walls(self):
        draw_wall = False
        # first run
        if len(self.enemy_sprites) == 0:
            draw_wall = True
        else:
            # calculate distance to the nearest sprite
            near_sprite = max(self.enemy_sprites, key=lambda w: w.rect.bottom)
            # if the distance is greater the clock, set a flag
            if self.screen.get_height() - near_sprite.rect.bottom >= self.level['base_clock']:
                draw_wall = True
        # if draw_wall is set do it
        if draw_wall and self.bar_count < len(self.level['play_field']):
            wall_info = list(self.level['play_field'][self.bar_count])
            self.bar_count += 1
            tmp_wall = Wall(self.screen, 10, wall_info[0], wall_info[1], 10)
            self.enemy_sprites.add(tmp_wall)
            self.all_sprites.add(tmp_wall)

    def update(self):
        # read Input data from keyboard
        self.checkKeys()
        # draw walls if needed
        self.draw_walls()
        # call update() on all sprites in list
        self.all_sprites.update()
        # handle collisions
        self.handle_collision()
        # draw sky
        self.screen.fill(cColorSkyBlue)
        # draw all sprites (not just enemy sprites)
        self.all_sprites.draw(self.screen)

    def load_level(self, path):
        path_level_file = os.path.join(path, "level.json")
        level_file = open(path_level_file, 'r')
        self.level = json.load(level_file)
        self.lives_count = self.level['lives']

        # debug
        print "Level Information:"
        print "  level_name : %s" % self.level['level_name']
        print "  base_clock : %s" % self.level['base_clock']
        print "  lives : %s" % self.level['lives']
        print "  play_field: %s" % self.level['play_field']
        print "end Level Information"


def main():
    pygame.init()
    screen = pygame.display.set_mode(cScreenSize)
    pygame.display.set_caption("Downfall")
    game = Downfall(screen, "./Level/Level_1/")
    running = True

    while running:
        running = game.checkEvents()
        # Limit frame rate to 30 FPS
        game.clock.tick(30)
        # Draw game screen
        game.update()
        pygame.display.flip()
    # clean up
    pygame.quit()

# Call main() if this module called directly
if __name__ == "__main__": main()