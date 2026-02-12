import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 60
BACKGROUND_COLOR = (255, 255, 255)
TRUNK_LENGTH = 100
BRANCH_REDUCTION = 0.7

class FractalTree:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Interactive Recursive Fractal Tree")
        
    def draw_branch(self, start_pos, length, angle, depth):
        if depth == 0:
            return
        
        # Calculate end position using trigonometry
        x_end = start_pos[0] + length * math.cos(math.radians(angle))
        y_end = start_pos[1] - length * math.sin(math.radians(angle))  # Inverted Y-axis for Pygame
        
        # Calculate thickness and color based on depth
        thickness = max(1, int(TRUNK_LENGTH / (depth * 2)))
        brown = (139, 69, 19)
        green = (34, 139, 34)
        ratio = depth / 12.0
        color = (
            int(brown[0] + (green[0] - brown[0]) * ratio),
            int(brown[1] + (green[1] - brown[1]) * ratio),
            int(brown[2] + (green[2] - brown[2]) * ratio)
        )
        
        # Draw the branch
        pygame.draw.line(self.screen, color, start_pos, (x_end, y_end), thickness)
        
        # Recursively draw sub-branches
        self.draw_branch((x_end, y_end), length * BRANCH_REDUCTION, angle - spread_angle/2, depth - 1)
        self.draw_branch((x_end, y_end), length * BRANCH_REDUCTION, angle + spread_angle/2, depth - 1)

    def run(self):
        clock = pygame.time.Clock()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            
            # Get mouse position and calculate parameters
            mouse_x, _ = pygame.mouse.get_pos()
            global spread_angle
            spread_angle = (mouse_x / WIDTH) * 120  # Map to 0-120 degrees
            
            # Calculate recursion depth based on mouse Y
            _, mouse_y = pygame.mouse.get_pos()
            max_depth = int((mouse_y / HEIGHT) * 10 + 2)
            current_depth = min(max(2, max_depth), 12)
            
            self.screen.fill(BACKGROUND_COLOR)
            
            # Draw the tree from bottom-center
            start_x = WIDTH // 2
            start_y = HEIGHT - 50
            
            self.draw_branch((start_x, start_y), TRUNK_LENGTH, 90, current_depth)
            
            pygame.display.flip()
            clock.tick(FPS)

if __name__ == "__main__":
    tree = FractalTree()
    spread_angle = 60  # Default spread angle
    tree.run()
