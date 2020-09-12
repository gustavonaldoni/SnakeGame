import pygame
from pygame.locals import *
import random

# Screen w/h
WIDTH = 600
HEIGHT = 600

# Colors
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
FLUO_GREEN = (57, 255, 20)
GRAY = (40,40,40)

# Directions
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Square size
squareSize = 10

def correctRandomPos():
    x = random.randint(0,WIDTH-squareSize)
    y = random.randint(0,HEIGHT-squareSize)
    return (x//10 * 10, y//10 * 10)

def collision (c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

# Initialize PyGame
pygame.init()

# Setting the screen and changing it name
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Snake')

# Snake 
snake = [(200,200), (210,200), (220,200)]
snakeDirection = LEFT

snakeSkin = pygame.Surface((squareSize,squareSize))
snakeSkin.fill(WHITE)

# Food
food = pygame.Surface((squareSize,squareSize))
food.fill(FLUO_GREEN)

# Food position
foodPos = correctRandomPos()

# Add the score
font = pygame.font.Font('helveticabold.ttf', 25)
score = 0

clock = pygame.time.Clock()

gameOver = False
# Main loop
while not gameOver:
    clock.tick(20)
    # Close the game event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    # Keys 
    if event.type == KEYDOWN:
        if event.key == K_UP:
            snakeDirection = UP
        if event.key == K_DOWN:
            snakeDirection = DOWN
        if event.key == K_LEFT:
            snakeDirection = LEFT
        if event.key == K_RIGHT:
            snakeDirection = RIGHT

    # Collision with food
    if collision(snake[0],foodPos):
        foodPos = correctRandomPos()
        snake.append((0,0))
        score += 1

    # Check if snake collided with boundaries
    if snake[0][0] == WIDTH or snake[0][1] == HEIGHT or snake[0][0] < 0 or snake[0][1] < 0:
        gameOver = True
        break

    # Check if snake hit itself
    for i in range(1,len(snake)-1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            gameOver = True
            break

    if gameOver:
        break

    # Snake movimentation
    for i in range(len(snake)-1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])   

    # Key pressing
    if snakeDirection == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if snakeDirection == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if snakeDirection == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if snakeDirection == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    # Update the screen color every repetition
    screen.fill(BLACK)

    # Food
    screen.blit(food,foodPos)

    # Add the grid
    for x in range(0, WIDTH, squareSize): # Horizontal lines
        pygame.draw.line(screen, GRAY, (x,0), (x,HEIGHT))
    for y in range(0, HEIGHT, squareSize): # Vertical lines
        pygame.draw.line(screen, GRAY, (0,y), (WIDTH,y))

    # Render the score
    score_font = font.render('Your score : %s' % (score), True, WHITE)
    score_rect = score_font.get_rect()
    score_rect.topleft = (WIDTH - (WIDTH - squareSize), squareSize)
    screen.blit(score_font,score_rect)

    for pos in snake:
        screen.blit(snakeSkin,pos)

    pygame.display.update()

while True:
    screen.fill(BLACK)
    gameOver_font = pygame.font.Font('helveticabold.ttf', 75)
    gameOver_screen = gameOver_font.render('Game Over', True, WHITE)  

    gameOver_font_score = pygame.font.Font('helveticabold.ttf', 30)
    gameOver_screen_score = gameOver_font_score.render(f'Your score : {score}', True, FLUO_GREEN)

    gameOver_rect = gameOver_screen.get_rect()
    gameOver_rect_score = gameOver_screen.get_rect()

    gameOver_rect.midtop = (WIDTH/2, 4*squareSize)  
    gameOver_rect_score.midtop = (WIDTH/1.5, 20*squareSize)

    screen.blit(gameOver_screen, gameOver_rect)
    screen.blit(gameOver_screen_score, gameOver_rect_score)

    pygame.display.update()
    pygame.time.wait(500)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()