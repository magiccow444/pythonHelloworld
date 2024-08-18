import sys

import pygame

from settings import Settings
from ship import Ship

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

    def run_game(self):
        # Start the main loop for the game.
        while True:
            self._check_events()
            self.ship.update()
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

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.isMovingRight = False
        elif event.key == pygame.K_LEFT:
            self.ship.isMovingLeft = False

    def _update_screen(self):
        self.screen.fill(self.settings.bgColor)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()