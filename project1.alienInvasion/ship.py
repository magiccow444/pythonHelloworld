import pygame

class Ship:
    def __init__(self, aiGame):
        self.screen = aiGame.screen
        self.screenRect = aiGame.screen.get_rect()
        self.settings = aiGame.settings

        self.image = pygame.image.load("project1.alieninvasion/images/rocket.png")
        self.image = pygame.transform.scale(self.image, (40, 60))

        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screenRect.midbottom

        # Stre a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        self.isMovingRight = False
        self.isMovingLeft = False

    def update(self):
        if self.isMovingRight and self.rect.right < self.screenRect.right:
            self.x += self.settings.shipSpeed
        if self.isMovingLeft and self.rect.left > 0:
            self.x -= self.settings.shipSpeed

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)