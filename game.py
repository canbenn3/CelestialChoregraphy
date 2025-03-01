import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1200, 800
GRID_SIZE = 40
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Snake 1 settings
snake1 = [(200, 200), (160, 200), (120, 200)]
direction1 = (GRID_SIZE, 0)

# Snake 2 settings
snake2 = [(600, 600), (440, 600), (520, 600)]
direction2 = (-GRID_SIZE, 0)  # Moving left initially

# Function to generate food at a location that isn't occupied
def generate_food():
    while True:
        new_food = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                    random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)
        if new_food not in snake1 and new_food not in snake2:
            return new_food

# Generate initial food
food = generate_food()

# Game clock
clock = pygame.time.Clock()
running = True

while running:
    screen.fill((0, 0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Controls for snake 1
            if event.key == pygame.K_UP and direction1 != (0, GRID_SIZE):
                direction1 = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and direction1 != (0, -GRID_SIZE):
                direction1 = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and direction1 != (GRID_SIZE, 0):
                direction1 = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction1 != (-GRID_SIZE, 0):
                direction1 = (GRID_SIZE, 0)

            # Controls for snake 2 (WASD)
            if event.key == pygame.K_w and direction2 != (0, GRID_SIZE):
                direction2 = (0, -GRID_SIZE)
            elif event.key == pygame.K_s and direction2 != (0, -GRID_SIZE):
                direction2 = (0, GRID_SIZE)
            elif event.key == pygame.K_a and direction2 != (GRID_SIZE, 0):
                direction2 = (-GRID_SIZE, 0)
            elif event.key == pygame.K_d and direction2 != (-GRID_SIZE, 0):
                direction2 = (GRID_SIZE, 0)

    # Move snake 1
    new_head1 = (snake1[0][0] + direction1[0], snake1[0][1] + direction1[1])
    if new_head1 in snake1 or new_head1[0] < 0 or new_head1[1] < 0 or new_head1[0] >= WIDTH or new_head1[1] >= HEIGHT:
        running = False  # Game over
    snake1.insert(0, new_head1)

    # Move snake 2
    new_head2 = (snake2[0][0] + direction2[0], snake2[0][1] + direction2[1])
    if new_head2 in snake2 or new_head2[0] < 0 or new_head2[1] < 0 or new_head2[0] >= WIDTH or new_head2[1] >= HEIGHT:
        running = False  # Game over
    snake2.insert(0, new_head2)

    # Check for food collision and generate new food
    if new_head1 == food:
        food = generate_food()
        snake2.pop()  # Snake 2 shrinks when snake 1 eats food
    else:
        snake1.pop()  # Only pop if snake 1 does not eat food

    if new_head2 == food:
        food = generate_food()
        snake1.pop()  # Snake 1 shrinks when snake 2 eats food
    else:
        snake2.pop()  # Only pop if snake 2 does not eat food

    # Check for collision between snakes
    if new_head1 in snake2 or new_head2 in snake1 or new_head1 == new_head2:
        running = False  # Game over if they touch

    # Draw food
    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))

    # Draw snake 1
    for segment in snake1:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    # Draw snake 2
    for segment in snake2:
        pygame.draw.rect(screen, BLUE, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    pygame.display.update()
    clock.tick(10)  # Control speed

pygame.quit()
