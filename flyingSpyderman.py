import pygame
import time
from random import randint, randrange

## global variables ##

# color
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
greenyellow = (184, 255, 0)
orange = (255, 204, 103)
pink = (255, 153, 204)
yellow = (255, 236, 0)
skyblue = (153, 255, 255)
block_color_choices = [greenyellow, orange, pink, yellow, skyblue]


# surface size
surface_width = 800
surface_height = 600

# image size
image_width = 96
image_height = 96

## initialize the game settings ##
pygame.init()
surface = pygame.display.set_mode((surface_width, surface_height))#((800, 400)) # window
pygame.display.set_caption("Flying Spyderman")      # window caption
clock = pygame.time.Clock() # clock
img = pygame.image.load("Spyderman.png") # spydrman image


# draw the spyderman
def spyderman(x, y, image):
    surface.blit(img, (x,y))

# draw two blocks with gap distance between them
#   where gap + height1 + height2 = surface_height
def blocks(block_x, block_y, block_width, block_height, gap, color):
    pygame.draw.rect(surface, color, [block_x, block_y, block_width, block_height]) # top block
    pygame.draw.rect(surface, color, [block_x, block_y + block_height + gap, block_width, surface_height - block_height - gap]) # bottom block


# draw the score
def score(curr_score):
    font = pygame.font.Font("freesansbold.ttf", 20)
    text = font.render("Score: " + str(curr_score), True, white)
    surface.blit(text, [0,0])


# draw the level
def level(curr_level):
    font = pygame.font.Font("freesansbold.ttf", 20)
    text = font.render("Level: " + str(curr_level), True, white)
    surface.blit(text, [1,20])
    

# wait for the player to make decision: replay or quit
def replay_or_quit():
    for event in pygame.event.get([pygame.KEYUP, pygame.KEYDOWN, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            continue
        return event.type
    return None


# game over and draw the game over message
def gameover():
    smallText_font = pygame.font.Font("freesansbold.ttf", 40)
    largeText_font = pygame.font.Font("freesansbold.ttf", 50)
    
    smallText_surface = smallText_font.render("Press any key to replay", True, red)
    smallText_rect = smallText_surface.get_rect()
    smallText_rect.center =  (surface_width / 2 , surface_height / 3 + 100) 
    surface.blit(smallText_surface, smallText_rect)
    
    largeText_surface = largeText_font.render("OOPS! You lose!" , True, red)
    largeText_rect = largeText_surface.get_rect()
    largeText_rect.center = (surface_width / 2, surface_height / 3)
    surface.blit(largeText_surface, largeText_rect)
    

    pygame.display.update()
    time.sleep(1)

    # wait for gamer to make choice
    while replay_or_quit() == None:
        clock.tick()
    main() # restart game
        

 # game loop
def main():
    game_over = False
    
    # spyderman
    x = 150 
    y = 250 
    y_move = 0
    
    # block
    block_x = surface_width
    block_y = 0
    block_width = 110
    block_height = randint(0, surface_height / 2)
    gap = image_height * 3 
    block_move = 4
    block_color = block_color_choices[randrange(0, len(block_color_choices))] # choose block color
    
    # score
    curr_score = 0
    
    # level
    curr_level = 1
    add_level = False
    
    
    while game_over == False :
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               game_over = True # break the while loop
           if event.type == pygame.KEYDOWN: # key is pressed
               if event.key == pygame.K_UP:
                   y_move = -5  # spyderman goes up
           if event.type == pygame.KEYUP:   # key is released
               if event.key == pygame.K_UP:
                   y_move = 5   # spydrman goes down
            
        # fill surface into black
        surface.fill(black)
        
        # draw spyderman
        spyderman(x, y, img)
        
        # draw blocks
        blocks(block_x, block_y, block_width, block_height, gap, block_color)
        
        # draw score
        score(curr_score)
        
        # draw level
        level(curr_level)
        
        if curr_level == 10:
            font = pygame.font.Font("freesansbold.ttf", 30)
            text = font.render("Good job! You are in the highest level!!!", True, white)
            surface.blit(text, [1,50])
        
        # update 
        y += y_move
        block_x -= block_move
        
        
        # check boundary -> crash -> game over
        if y > surface_height - 40 or y < 0:
            gameover()
        
        # check block_x out of screen
        if block_x < (-1 * block_width):
            block_x = surface_width
            block_height = randint(0, surface_height / 2)
            block_color = block_color_choices[randrange(0, len(block_color_choices))]
            
            curr_score += 1 # update score
    
            # check adding level
            if curr_score == 3:
                block_move = 5
                gap = image_height * 2.9
                add_level = True
            elif curr_score == 10: 
                block_move = 6
                gap = image_height * 2.8
                add_level = True
            elif curr_score == 20: 
                block_move = 7
                gap = image_height * 2.7
                add_level = True
            elif curr_score == 30: 
                block_move = 8
                gap = image_height * 2.6
                add_level = True
            elif curr_score == 40: 
                block_move = 9
                gap = image_height * 2.5
                add_level = True
            elif curr_score == 50: 
                block_move = 10
                gap = image_height * 2.5
                add_level = True
            elif curr_score == 60: 
                block_move = 11
                gap = image_height * 2.5
                add_level = True
            elif curr_score == 70: 
                block_move = 12
                gap = image_height * 2.5
                add_level = True
            elif curr_score == 80: 
                block_move = 13
                gap = image_height * 2.4
                add_level = True
            
            if add_level:
                curr_level += 1
                level(curr_level)
                print("add level")
                add_level = False
        
        # check hitting blocks
        if x + image_width > block_x:
            print("spyderman crossover")
            if x < block_x + block_width: # check top block
                print("possibly within the boundaries of x upper")
                if y < block_height:
                    print("y crossover upper")
                    if x - image_width < block_width + block_x:
                        print("game over hit upper")
                        gameover()
            if y + image_height > block_height + gap: # check bottom block
                print("y crossover lower")
                if x < block_width + block_x:
                    print("game over hit lower")
                    gameover()
        
        pygame.display.update() # update screen   
        clock.tick(60) # 60 frames per second




main()
pygame.quit()
quit()

         