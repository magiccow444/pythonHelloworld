import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    def __init__(self):
        # Initialize the game, and create game resources.
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screenWidth = self.screen.get_rect().width
        self.settings.screenHeight = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        # Start the main loop for the game.
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            
    def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                  
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.isMovingRight = True
        elif event.key == pygame.K_LEFT:
            self.ship.isMovingLeft = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fireBullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.isMovingRight = False
        elif event.key == pygame.K_LEFT:
            self.ship.isMovingLeft = False

    def fireBullet(self):
        if (len(self.bullets) < self.settings.bulletsAllowed):
            newBullet = Bullet(self)
            self.bullets.add(newBullet)
    
    def _update_bullets(self):
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            print(len(self.bullets))

    def _update_screen(self):
        self.screen.fill(self.settings.bgColor)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.drawBullet()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()  
    ai.run_game() 