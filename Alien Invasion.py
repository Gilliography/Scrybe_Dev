import sys
import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        
        # Set background color
        self.bg_color = (230, 230, 230)
        
        # Define a simple object (a rectangle)
        self.rect_color = (60, 60, 60)  # Dark gray
        self.rect = pygame.Rect(50, 50, 200, 150)  # x, y, width, height
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Fill the screen with the background color.
            self.screen.fill(self.bg_color)
            
            # Draw the rectangle on the screen.
            pygame.draw.rect(self.screen, self.rect_color, self.rect)
            
            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

