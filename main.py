# Owen Perez
# 3/5/2025
# shapes-using-dictionaries

import pygame
import random
import shapes
import sys
import config

def main():
    screen = config.init_game()
    clock = pygame.time.Clock()
    shapes_list = []

    running = True
    while running:
        running = config.handle_events()
        screen.fill((255, 255, 255))  # Use white directly instead of config.WHITE if undefined.

        # Create a new shape
        shape_type = random.randrange(3)  # Get a random shape type
        new_shape = None  # Initialize new shape

        if shape_type == 0:
            # Draw a circle
            new_shape = {
                'type': 'circle',
                'color': (random.randrange(256), random.randrange(256), random.randrange(256)),
                'position': (random.randrange(config.SCREEN_WIDTH), random.randrange(config.SCREEN_HEIGHT)),
                'radius': random.randrange(20, 100)  # Avoid 0-radius circles
            }
        elif shape_type == 1:
            # Draw a rectangle
            new_shape = {
                'type': 'rect',
                'color': (random.randrange(256), random.randrange(256), random.randrange(256)),
                'position': (random.randrange(config.SCREEN_WIDTH), random.randrange(config.SCREEN_HEIGHT)),
                'width': random.randrange(20, 100),
                'height': random.randrange(20, 100)
            }
        elif shape_type == 2:
            # Draw a line
            new_shape = {
                'type': 'line',
                'color': (random.randrange(256), random.randrange(256), random.randrange(256)),
                'start_pos': (random.randrange(config.SCREEN_WIDTH), random.randrange(config.SCREEN_HEIGHT)),
                'end_pos': (random.randrange(config.SCREEN_WIDTH), random.randrange(config.SCREEN_HEIGHT)),
                'width': random.randrange(1, 10)
            }

        # Add the new shape to the list
        if new_shape:
            shapes_list.append(new_shape)

        # Draw all shapes
        for shape in shapes_list:
            if shape['type'] == 'circle':
                shapes.draw_circle(screen, shape)
            elif shape['type'] == 'rect':
                shapes.draw_rect(screen, shape)
            elif shape['type'] == 'line':
                shapes.draw_line(screen, shape)

        pygame.display.flip()  # Refresh the screen
        clock.tick(30)  # Limit FPS to 30

if __name__ == "__main__":
    main()
