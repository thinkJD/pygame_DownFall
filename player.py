import pygame
import os.path

class Player(pygame.sprite.Sprite):
    lives = 0
    change_x = 20
    change_y = 20
    max_height = 0
    max_width = 0
    rect = None
    image_player_dead = None
    image_player_right = None
    image_player_left = None
    sound_player_start = None
    sound_player_dead = None
    sound_player_change_dir = None
    direction = "left"

    def __init__(self, screen, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        base_path = os.path.dirname(__file__)

        self.image_player_left = pygame.image.load(os.path.join(base_path, "Graphics/", "player_left.png"))
        self.image_player_right = pygame.transform.flip(self.image_player_left, 1, 0)
        self.sound_player_dead = pygame.mixer.Sound(os.path.join(base_path, "Sound/" "sfx/", "Drop.wav"))
        self.sound_player_change_dir = pygame.mixer.Sound(os.path.join(base_path, "Sound/", "sfx", "player_dir_change.wav"))

        self.image = self.image_player_left
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.max_height = screen.get_height()
        self.max_width = screen.get_width()

    def change_sppeed(self, x, y):
        self.change_x = x
        self.change_y = y

    def player_hit(self):
        self.sound_player_dead.play()

    def player_change_dir(self):
        self.sound_player_change_dir.play()

    def __change_player_dir(self, direction):
        if direction == "left":
            self.image = self.image_player_left
        else:
            self.image = self.image_player_right

    def player_dead(self):
        self.image = self.image_player_dead

    def go_right(self):
        self.sound_player_change_dir.play()
        self.direction = "right"
        if self.rect.right + self.change_x <= self.max_width:
            self.rect.x += self.change_y
        else:
            self.rect.x = self.max_width - self.rect.width

    def go_left(self):
        self.sound_player_change_dir.play()
        self.direction = "left"
        if self.rect.left - self.change_x >= 0:
            self.rect.x -= self.change_x
        else:
            self.rect.x = 0

    def update(self):
        self.__change_player_dir(self.direction)
