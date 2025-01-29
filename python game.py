import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the game loop
clock = pygame.time.Clock()
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Update the game state
    x = 100
    y = 100
    # Render the graphics
    screen.fill((255, 255, 255))
    # Update the display
    pygame.display.flip()
    # Cap the frame rate
    clock.tick(60)