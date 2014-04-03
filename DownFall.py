import os
import pygame
import dumbmenu as dm
from player import *
from wall_ import *
from text import *

import json

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
    level = None
    enemy_sprites = None
    score = 0
    screen = None
    # sounds
    sound_death = None
    sound_level = None
    bar_count = 0
    score_counter = None
    direction = "left"

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
        self.score_counter = Text("Lives: ", 40, 10, 10, cColorOrange)

        # load sounds
        self.all_sprites.add(self.score_counter)

    def load_level(self, path):
        path_level_file = os.path.join(path, "level.json")
        level_file = open(path_level_file, 'r')
        self.level = json.load(level_file)
        self.sound_level = pygame.mixer.Sound(os.path.join(path, "Track1.mp3"))

        # debug
        print "Level Information:"
        print "  level_name : %s" % self.level['level_name']
        print "  next_wall : %s" % self.level['next_wall']
        print "  lives : %s" % self.level['lives']
        print "  play_field: %s" % self.level['play_field']
        print "end Level Information"

    def check_keys(self):
        pygame.event.pump()
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.player.go_right()
        if key[pygame.K_LEFT]:
            self.player.go_left()
        if key[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    def check_events(self):
        # handle QUIT event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.time.wait(1000)
                return False
        return True

    def handle_collision(self):
        # check collision between player and enemy sprites
        collision_list = pygame.sprite.spritecollide(self.player, self.enemy_sprites, True)
        # if a collision is detected, handle player death
        if len(collision_list) > 0:
            self.player.player_hit()
            self.score_counter.update_color([255, 255, 255])
            if self.level['lives'] > 0:
                self.level['lives'] -= 1
                print "Remaining lives: %s" % self.level['lives']
            else:
                # game over
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    def draw_walls(self):
        # first run
        if len(self.enemy_sprites) == 0:
            self.draw_wall()
        else:
            # calculate distance to the nearest sprite
            near_sprite = max(self.enemy_sprites, key=lambda w: w.rect.bottom)
            # if the distance is greater than next walls distance
            if self.screen.get_height() - near_sprite.rect.bottom >= self.level['next_wall']:
                self.draw_wall()

    def draw_wall(self):
        # if draw_wall is set do it
        if self.bar_count < len(self.level['play_field']):
            print "draw a wall"
            # get next wall_info list
            wall_info = list(self.level['play_field'][self.bar_count])
            self.bar_count += 1
            print wall_info
            self.level['next_wall'] = wall_info[2]
            tmp_wall = Wall(self.screen, 10, wall_info[0], wall_info[1], 10)
            self.enemy_sprites.add(tmp_wall)
            self.all_sprites.add(tmp_wall)
            if wall_info[2] == 0:
                print "0 Distance, draw next wall"
                self.draw_wall()

    def update(self):
        self.check_keys()
        self.draw_walls()
        self.all_sprites.update()
        self.handle_collision()
        self.screen.fill(cColorSkyBlue)
        self.score_counter.update_text("Lives: " + str(self.level["lives"]))
        self.all_sprites.draw(self.screen)


def main():
    pygame.init()
    screen = pygame.display.set_mode(cScreenSize)
    pygame.display.set_caption("Downfall")

    screen.fill(cColorBlack)
    decision = dm.dumbmenu(screen, ["Start", "Help", "Quit Game"], 70, 70, None, 32, 1.4, cColorWhite, cColorOrange )

    if decision == 0:
        game = Downfall(screen, "./Level/Level_1/")
        running = True

        while running:
            running = game.check_events()
            # Limit frame rate to 30 FPS
            game.clock.tick(30)
            # Draw game screen
            game.update()
            pygame.display.flip()

    elif decision == 1:
        print "looool als ob"

    elif decision == 2:
        print "Quit Game"

    # clean up
    pygame.quit()

# Call main() if this module called directly
if __name__ == "__main__": main()