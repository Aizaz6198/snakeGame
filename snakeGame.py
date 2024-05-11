import pygame
import time
import random

# Constants
snake_speed = 15
WINDOW_X = 720
WINDOW_Y = 480
BLOCK_SIZE = 10
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0 , 0, 0)

# Initialize pygame
pygame.init()
game_window = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
pygame.display.set_caption('Snake Game')
fps = pygame.time.Clock()

# Directions dictionary
DIRECTIONS = {
    pygame.K_UP: 'UP',
    pygame.K_DOWN: 'DOWN',
    pygame.K_LEFT: 'LEFT',
    pygame.K_RIGHT: 'RIGHT'
}

# Functions
def show_score(score, font, size, color):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    game_window.blit(score_surface, (10, 10))

def game_over(score):
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, RED)
    game_over_rect = game_over_surface.get_rect(midtop=(WINDOW_X / 2, WINDOW_Y / 4))
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main Function
def main():
    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    fruit_position = [random.randrange(1, (WINDOW_X // BLOCK_SIZE)) * BLOCK_SIZE,
                      random.randrange(1, (WINDOW_Y // BLOCK_SIZE)) * BLOCK_SIZE]
    score = 0
    direction = 'RIGHT'
    change_to = direction

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key in DIRECTIONS:
                    change_to = DIRECTIONS[event.key]

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            snake_position[1] -= BLOCK_SIZE
        if direction == 'DOWN':
            snake_position[1] += BLOCK_SIZE
        if direction == 'LEFT':
            snake_position[0] -= BLOCK_SIZE
        if direction == 'RIGHT':
            snake_position[0] += BLOCK_SIZE

        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_position = [random.randrange(1, (WINDOW_X // BLOCK_SIZE)) * BLOCK_SIZE,
                              random.randrange(1, (WINDOW_Y // BLOCK_SIZE)) * BLOCK_SIZE]
        else:
            snake_body.pop()

        game_window.fill(BLACK)
        for pos in snake_body:
            pygame.draw.rect(game_window, GREEN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(game_window, WHITE, pygame.Rect(fruit_position[0], fruit_position[1], BLOCK_SIZE, BLOCK_SIZE))

        if snake_position[0] < 0 or snake_position[0] >= WINDOW_X or snake_position[1] < 0 or snake_position[1] >= WINDOW_Y:
            game_over(score)

        for block in snake_body[1:]:
            if snake_position == block:
                game_over(score)

        show_score(score, 'times new roman', 20, WHITE)

        pygame.display.update()
        fps.tick(snake_speed)

if __name__ == "__main__":
    main()
