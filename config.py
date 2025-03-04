import pygame

# Define screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Drawing Shapes')
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    return True
