class Ground:

    def __init__(self, image, y):
        self.image = image
        self.width = image.get_width()
        self.y = y
        self.offset = 0

    def update(self, speed):
        self.offset = (self.offset + speed) % self.width

    def draw(self, screen):
        screen.blit(self.image, (self.offset - self.width, self.y))
        screen.blit(self.image, (self.offset, self.y))