import pygame
import random
import sys

pygame.init()
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS = 10

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Snake Game")
clock = pygame.time.Clock()

def draw_snake(snake):
    for x, y in snake:
        pygame.draw.rect(screen, GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def spawn_food(snake):
    while True:
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if pos not in snake:
            return pos

snake = [(5, 5), (6, 5), (7, 5)]
direction = (1, 0)
food = spawn_food(snake)
score = 0
font = pygame.font.SysFont(None, 35)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    head_x, head_y = snake[-1]
    new_head = ((head_x + direction[0]) % GRID_WIDTH, (head_y + direction[1]) % GRID_HEIGHT)
    if new_head in snake:
        print("Game Over! Final Score:", score)
        pygame.quit()
        sys.exit()

    snake.append(new_head)
    if new_head == food:
        score += 1
        food = spawn_food(snake)
    else:
        snake.pop(0)

    screen.fill(BLACK)
    draw_snake(snake)
    draw_food(food)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(FPS)
