import pygame
import random

# Настройки игры
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20
FPS = 10

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Направление змейки
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = RIGHT
        self.head = self.body[0]

    def move(self):
        self.head = (self.head[0] + self.direction[0] * CELL_SIZE, 
                     self.head[1] + self.direction[1] * CELL_SIZE)
        self.body.insert(0, self.head)
        if not self.eat_food():
            self.body.pop()

    def change_direction(self, new_direction):
        if new_direction == (0, -1) and self.direction != DOWN:
            self.direction = new_direction
        elif new_direction == (0, 1) and self.direction != UP:
            self.direction = new_direction
        elif new_direction == (-1, 0) and self.direction != RIGHT:
            self.direction = new_direction
        elif new_direction == (1, 0) and self.direction != LEFT:
            self.direction = new_direction

    def draw(self, screen):
        for x, y in self.body:
            pygame.draw.rect(screen, GREEN, (x, y, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)

    def eat_food(self):
        global food
        if self.head == food:
            food = (random.randrange(0, WIDTH, CELL_SIZE),
                    random.randrange(0, HEIGHT, CELL_SIZE))
            return True
        return False

    def check_collision(self):
        if self.head[0] < 0 or self.head[0] >= WIDTH or self.head[1] < 0 or self.head[1] >= HEIGHT:
            return True
        for x, y in self.body[1:]:
            if self.head == (x, y):
                return True
        return False

def draw_food(screen):
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, BLACK, (food[0], food[1], CELL_SIZE, CELL_SIZE), 1)

def main():
    global food
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Змейка")
    clock = pygame.time.Clock()

    snake = Snake()
    food = (random.randrange(0, WIDTH, CELL_SIZE), 
            random.randrange(0, HEIGHT, CELL_SIZE))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(UP)
                if event.key == pygame.K_DOWN:
                    snake.change_direction(DOWN)
                if event.key == pygame.K_LEFT:
                    snake.change_direction(LEFT)
                if event.key == pygame.K_RIGHT:
                    snake.change_direction(RIGHT)

        screen.fill(BLACK)

        snake.move()
        if snake.check_collision():
            running = False

        draw_food(screen)
        snake.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()