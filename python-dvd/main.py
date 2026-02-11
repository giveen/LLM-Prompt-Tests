import pygame
import random

class DVDLogo:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        
        # Text properties
        self.font = pygame.font.SysFont(None, 72)
        self.text_surface = None
        self.update_text("DVD", (0, 255, 0))
        
        # Position and velocity vectors
        self.rect = self.text_surface.get_rect()
        self.rect.center = (self.width // 2, self.height // 2)
        self.velocity_x = random.choice([-3, -2, -1, 1, 2, 3])
        self.velocity_y = random.choice([-3, -2, -1, 1, 2, 3])

    def update_text(self, text, color):
        """Update the text surface with new color"""
        self.text_surface = self.font.render(text, True, color)
        
    def move(self):
        """Move the logo and handle collisions"""
        # Update position
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        
        # Check for wall collisions (with precise hitbox calculations)
        if self.rect.left < 0 or self.rect.right > self.width:
            self.velocity_x *= -1
            self.update_text("DVD", self.random_color())
            
        if self.rect.top < 0 or self.rect.bottom > self.height:
            self.velocity_y *= -1
            self.update_text("DVD", self.random_color())

    def random_color(self):
        """Generate a bright RGB color"""
        return (random.randint(50, 255), 
                random.randint(50, 255),
                random.randint(50, 255))

    def draw(self):
        """Draw the logo on the screen"""
        self.screen.blit(self.text_surface, self.rect)

def main():
    pygame.init()
    
    # Set up display
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("DVD Screensaver")
    
    clock = pygame.time.Clock()
    dvd_logo = DVDLogo(screen)
    
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update and render
        screen.fill((0, 0, 0))  # Black background
        dvd_logo.move()
        dvd_logo.draw()
        
        pygame.display.flip()
        clock.tick(60)  # Maintain 60 FPS
    
    pygame.quit()

if __name__ == "__main__":
    main()
