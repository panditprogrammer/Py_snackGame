#this game is designed by panditprogrammer.com
#feel free to costomize this code as your choice 
import pygame
import random

#initializing game
pygame.init()
screen_width =900
screen_height = 600

#color
orange = (202 , 101 , 0)
brown = (53 , 0 , 0)
white = (255,255,255)
red = (159 , 19 , 30)
green = (0 , 111 , 0)
bgover = (181 , 181 , 181)
playagain = (128 , 128 , 128)
background = (183 , 202 , 185)

#creating game window
window = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake Game - PanditProgrammer.com")

#pygame.display.set_icon(icon)

pygame.display.update()
clock = pygame.time.Clock()

#game sound variables
pygame.mixer.init()
#eating  = pygame.mixer.Sound(os.path.join(ROOT_DIR,'eat.wav'))
#key  = pygame.mixer.Sound(os.path.join(ROOT_DIR,'key.wav'))


#show score
font = pygame.font.SysFont(None,55)

def text_screen(text,color,x,y):
    show = font.render(text,True,color)
    window.blit(show,[x,y])

#plotting snake 
def plot_snake(window,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(window,color,[x,y,snake_size,snake_size])

# main game loop 
def mainloop():
    #game variables
    over = False
    exit = False
    snake_x = 100
    snake_y = 100

    #initial velocity of snake
    initial_velocity =5
    velocity_x = 0
    velocity_y = 0
    
    # snake length variables
    snake_list = []
    snake_size = 20
    food_size = 20
    fps = 30
    score =0

    #creating food
    food_x = random.randint(10,screen_width-50)
    food_y = random.randint(10,screen_height-50)

    snake_length = 1

    while not exit:
        if over:
            window.fill(bgover)
            text_screen(f"Game Over! Your Score is {score}",red,200,200)
            text_screen("Press Enter To Play Again",playagain,220,260)
            
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        
                        mainloop()
        
        else:
            #event handling 
            for event in pygame.event.get():
                #print(event)    
                if event.type == pygame.QUIT:
                    exit = True

                if event.type ==pygame.KEYDOWN:
                    if (event.key == pygame.K_RIGHT):
                        
                        velocity_x = +initial_velocity
                        velocity_y = 0

                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        
                        velocity_x = -initial_velocity
                        velocity_y = 0

                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        
                        velocity_y = -initial_velocity
                        velocity_x = 0
                        

                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        
                        velocity_y = +initial_velocity
                        velocity_x = 0

                
            #moving snake
            snake_x = snake_x +velocity_x
            snake_y =snake_y+velocity_y
            #reploting food and updating score
            if abs(snake_x- food_x) <10 and abs(snake_y - food_y)<10:
                score+=10

                # snake_length increment
                snake_length += 5

                #updating velocity 
                if(score== 200):
                    initial_velocity += 1

                #show score
                food_x = random.randint(20,screen_width-5)
                food_y = random.randint(20,screen_height-5)
            
            window.fill(background)
            text_screen("Score "+str(score),green,710,10)
            pygame.draw.rect(window,brown,[snake_x,snake_y,snake_size,snake_size])
            pygame.draw.rect(window,orange,[food_x,food_y,food_size,food_size])

            #showing first time head of snake
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            #removing first element of snake_list
            if len(snake_list) > snake_length:
                del snake_list[0]

            if (snake_x <0) or (snake_x > screen_width) or (snake_y< 0) or (snake_y > screen_height-5):
                over = True
            if head in snake_list[:-1]:
                over = True
            #plotting snake
            plot_snake(window,brown,snake_list,snake_size)

        pygame.display.update()
        clock.tick(fps)
        
    pygame.quit()
    quit()
try:
    mainloop()
except Exception :
    pass