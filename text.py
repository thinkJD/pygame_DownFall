import pygame

class Text(pygame.sprite.Sprite):
    font = None
    rect = None
    text = None
    text_color = None

    def __init__(self, text, height, pos_x, pos_y, text_color):
        pygame.sprite.Sprite.__init__(self)
        self.text_color = text_color
        self.text = text
        self.font = pygame.font.Font(None, height)
        self.image = self.font.render(self.text, True, self.text_color, None)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update_text(self, text):
        # render new image
        self.text = text
        self.__update_rect__()

    def update_color(self, text_color):
        self.text_color = text_color
        self.__update_rect__()

    def update(self):
        return True

    def __update_rect__(self):
        # render text, store old coordinates and set new text rect to old position
        self.image = self.font.render(self.text, True, self.text_color, None)
        old_rect_y = self.rect.y
        old_rect_x = self.rect.x
        self.rect = self.image.get_rect()
        self.rect.x = old_rect_x
        self.rect.y = old_rect_y
