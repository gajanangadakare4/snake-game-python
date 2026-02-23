import pygame
import random
import sys

# Initialize
pygame.init()


# Screen
WIDTH, HEIGHT = 600, 600
CELL = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
WHITE = (255, 255, 255)

# Snake
snake = [(300, 300)]
direction = (CELL, 0)
score = 0

# Food
def random_food():
    x = random.randint(0, (WIDTH // CELL) - 1) * CELL
    y = random.randint(0, (HEIGHT // CELL) - 1) * CELL
    return (x, y)

food = random_food()

def draw_grid():
    for x in range(0, WIDTH, CELL):
        pygame.draw.line(screen, (40,40,40), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL):
        pygame.draw.line(screen, (40,40,40), (0, y), (WIDTH, y))

def game_over():
    text = font.render("GAME OVER", True, RED)
    screen.blit(text, (WIDTH//2 - 100, HEIGHT//2 - 20))
    pygame.display.update()
    pygame.time.wait(2000)

def reset_game():
    global snake, direction, score, food
    snake = [(300, 300)]
    direction = (CELL, 0)
    score = 0
    food = random_food()

# Game loop
running = True
while running:
    clock.tick(10)
    screen.fill(BLACK)
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL):
                direction = (0, -CELL)
            if event.key == pygame.K_DOWN and direction != (0, -CELL):
                direction = (0, CELL)
            if event.key == pygame.K_LEFT and direction != (CELL, 0):
                direction = (-CELL, 0)
            if event.key == pygame.K_RIGHT and direction != (-CELL, 0):
                direction = (CELL, 0)

    # Move snake
    head_x = snake[0][0] + direction[0]
    head_y = snake[0][1] + direction[1]
    new_head = (head_x, head_y)

    # Collision with wall
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        game_over()
        reset_game()
        continue

    # Collision with itself
    if new_head in snake:
        game_over()
        reset_game()
        continue

    snake.insert(0, new_head)

    # Eat food
    if new_head == food:
        score += 1
        food = random_food()
    else:
        snake.pop()

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL, CELL))

    # Draw food
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL, CELL))

    # Score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
sys.exit()