import pygame

class Wall(pygame.sprite.Sprite):
    wall_speed = 0
    screen = None
    line_color = (255, 255, 0)
    rect = None

    def __init__(self, screen, speed, y_offset, width, thickness=10):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.Surface((width, thickness))
        self.image.fill(self.line_color)
        self.rect = self.image.get_rect()
        self.rect.y = screen.get_height()
        self.rect.x = y_offset
        self.wall_speed = speed

    def change_speed(self, speed):
        self.wall_speed = speed

    def update(self):
        self.rect.y -= self.wall_speed
        if self.rect.y < 0:
            self.kill()