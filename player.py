import pygame

class Player(pygame.sprite.Sprite):
    screen = None
    change_x = 10
    change_y = 10
    max_height = 0
    max_width = 0
    movement = "undefined"
    rect = None

    def __init__(self, screen, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./Grapics/spriteSplayer.png")
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

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if self.rect.left - self.change_x >= 0:
                self.rect.x -= self.change_x
            else:
                self.rect.x = 0
        if key[pygame.K_RIGHT]:
            if self.rect.right + self.change_x <= self.max_width:
                self.rect.x += self.change_y
            else:
                self.rect.x = self.max_width - self.rect.width



