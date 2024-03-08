import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define screen dimensions
WIDTH = 800
HEIGHT = 600

# Define snake block size
BLOCK_SIZE = 20

# Define speed
SPEED = 15  # Adjust for desired speed

# Define font
FONT_STYLE = pygame.font.SysFont(None, 50)


def message(msg, color):
    """Displays a message on the screen."""
    mesg = FONT_STYLE.render(msg, True, color)
    gameDisplay.blit(mesg, [WIDTH / 6, HEIGHT / 3])


def draw_snake(snake_block, snake_list):
    """Draws the snake on the screen."""
    for x in snake_list:
        pygame.draw.rect(gameDisplay, snake_block[1], [x[0], x[1], BLOCK_SIZE, BLOCK_SIZE])


def draw_food(food_x, food_y):
    """Draws the food on the screen."""
    pygame.draw.rect(gameDisplay, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])


def game_loop():
    """Main game loop."""
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    clock = pygame.time.Clock()

    # Game initialization
    pygame.init()
    gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake Game')

    while not game_over:

        while game_close:
            gameDisplay.fill(WHITE)
            message("You Lost! A Press Q - Quit or C - Play Again", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != BLOCK_SIZE:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -BLOCK_SIZE:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != BLOCK_SIZE:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change != -BLOCK_SIZE:
                    y1_change = BLOCK_SIZE

        x1 += x1_change
        y1 += y1_change

        gameDisplay.fill(BLACK)
        pygame.draw.rect(gameDisplay, GREEN, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for collisions with boundaries or itself
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0 or snake_head in snake_list[:-1]:
            game_close = True

        draw_snake(WHITE, snake_list)
        draw_food(food
