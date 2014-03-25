import pygame
import os.path

class Player(pygame.sprite.Sprite):
    screen = None
    change_x = 20
    change_y = 20
    max_height = 0
    max_width = 0
    rect = None
    image_player_left = None
    image_player_right = None
    image_player_death = None

    def __init__(self, screen, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        # load pictures
        base_path = os.path.dirname(__file__)
        self.image_player_right = pygame.image.load(os.path.join(base_path, "Graphics/", "player_right.png"))
        self.image_player_left = pygame.image.load(os.path.join(base_path, "Graphics/", "player_left.png"))
        self.image_player_death = pygame.image.load(os.path.join(base_path, "Graphics/", "player_death.png"))
        self.image = self.image_player_left
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.max_height = screen.get_height()
        self.max_width = screen.get_width()
        # debug
        # print "x= %s" % self.rect.x
        # print "y= %s" % self.rect.y


    def change_sppeed(self, x, y):
        self.change_x = x
        self.change_y = y

    def player_death(self):
        self.image = self.image_player_death

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.image = self.image_player_left
            if self.rect.left - self.change_x >= 0:
                self.rect.x -= self.change_x
            else:
                self.rect.x = 0
        if key[pygame.K_RIGHT]:
            self.image = self.image_player_right
            if self.rect.right + self.change_x <= self.max_width:
                self.rect.x += self.change_y
            else:
                self.rect.x = self.max_width - self.rect.width