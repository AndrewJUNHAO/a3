import pygame
import random

pygame.init()
#color
white= (255, 255, 255)
yellow = (255, 255, 100)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
K_SPACE=32
#screen size
screen_width = 900
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
#title
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
#grid size
GRID_SIZE = 15
#snake speed
snake_speed = 10
#font
font_style = pygame.font.SysFont("arial", 25)
score_font = pygame.font.SysFont("arial", 50)
#food postion
foodPostion=(0,0)
#snake body list
snake_List = []
#snake body length
Length_of_snake = 3

# draw score
def draw_score(score):
    value = score_font.render("Score: " + str(score), True, blue)
    screen.blit(value, [0, 0])

# draw snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

#draw message
def message(msg, color,height):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width // 3, height])
#draw grid
def draw_grid():
    for x in range(0, screen_width, GRID_SIZE):
        for y in range(0, screen_height, GRID_SIZE):
            pygame.draw.line(screen, black, (x, 0), (x, screen_height))
            pygame.draw.line(screen, black, (0, y), (screen_width, y))
# create random food position
def random_food():
    global foodPostion
    foodx = round(random.randrange(0, screen_width - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
    foody = round(random.randrange(0, screen_height - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
    foodPostion = (foodx, foody)
#check if snake eat food
def eatFood():
    if snake_List[-1][0] == foodPostion[0] and snake_List[-1][1] == foodPostion[1]:return True
    return False
#game loop
def gameLoop():
    global Length_of_snake
    isGameOver = False
    isGameClose = False

    x1 = screen_width // 2
    y1 = screen_height // 2
    #snake direction
    x_dir = GRID_SIZE
    y_dir = 0

    #initial food position
    random_food()
    # game_close=True
    while not isGameOver:
        #game over
        while isGameClose == True:
            screen.fill(white)
            message("If you lose, press the space ", red,screen_height // 3)
            message("bar to restart Q key to exit", red,screen_height // 3+GRID_SIZE*3)
            draw_score(Length_of_snake - 3)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        isGameOver = True
                        isGameClose = False
                        pygame.quit()

                    if event.key == K_SPACE:
                        gameLoop()
        # keyboard event

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                #quit game
                if event.key == pygame.K_q:
                    isGameOver = True
                    isGameClose = False
                    pygame.quit()
                #press Direction key
                if event.key == pygame.K_LEFT:
                    x_dir ,y_dir= (-GRID_SIZE,0)

                elif event.key == pygame.K_RIGHT:
                    x_dir ,y_dir= (GRID_SIZE,0)
                elif event.key == pygame.K_UP:
                    x_dir ,y_dir= (0,-GRID_SIZE)
                elif event.key == pygame.K_DOWN:
                    x_dir ,y_dir= (0,GRID_SIZE)
        #check if snake hit the wall
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            isGameClose = True
        x1 += x_dir
        y1 += y_dir
        snake_Head = (x1, y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                isGameClose = True

        screen.fill(white)
        # draw food
        pygame.draw.rect(screen, red, [foodPostion[0], foodPostion[1], GRID_SIZE, GRID_SIZE])
        #draw snake
        draw_snake(GRID_SIZE, snake_List)
        #draw grid
        draw_grid()
        #draw score
        draw_score(Length_of_snake - 3)


        #check if snake eat food
        if eatFood():
            random_food()
            Length_of_snake += 1
        #update screen
        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()