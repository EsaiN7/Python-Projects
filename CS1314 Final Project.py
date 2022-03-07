#Esai Barron
#Python Project

import pygame
import time
import random

pygame.init()

#color pallate
green = (0,128,0)
red = (255, 0, 0)
black = (0,0,0)
yellow = (255,255,0)
#screen dimensions
displayWidth = 600
displayHeight = 400

#snake dimensions
snakeDimension = 10

#create display and play area
display = pygame.display.set_mode((displayWidth,displayHeight)) #this makes the screen, use a tuple
pygame.display.set_caption('Made by Esai Barron')

#speed of snakes movement
speed = 20
speedM = pygame.time.Clock()


#fonts
font_style = pygame.font.SysFont("bahnschrift", 25)

def playerSnake(snakeDimension, snakeLst):
    for x in snakeLst:
        pygame.draw.rect(display, green, [x[0], x[1], snakeDimension, snakeDimension])

#game over message
def gameOverMessage(mesg, color):
    mesg = font_style.render(mesg, True, color)
    display.blit(mesg, [displayWidth/6,displayHeight/3])
    
def playerScore(score):
    pScore = font_style.render("Your Score: " + str(score), True, yellow)
    display.blit(pScore, [0, 0])

def gameLoop():  #put the main game loop into a function
    gameEnd = False
    gameExit = False
 
    xp = displayWidth / 2
    yp = displayHeight / 2
 
    xUpdate = 0
    yUpdate = 0
    
    snakeLst = []
    snakeLen = 1
 
    foodx = round(random.randrange(0, displayWidth - snakeDimension) / 10.0) * 10.0
    foody = round(random.randrange(0, displayWidth - snakeDimension) / 10.0) * 10.0

    while not gameEnd:    

        while gameExit == True:
          display.fill(black)
          gameOverMessage("You lost! Press F to quit or P to play again!", red)
          pygame.display.update()
          
          for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        gameEnd = True
                        gameExit = False
                    if event.key == pygame.K_p:
                        gameLoop()

        for event in pygame.event.get(): 
        
            if event.type == pygame.QUIT: #allows player to exit game
                gameEnd = True
            
            #take in player input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xUpdate = -10
                    yUpdate = 0
                elif event.key == pygame.K_RIGHT:
                    xUpdate = 10
                    yUpdate = 0
                elif event.key == pygame.K_DOWN:
                    xUpdate = 0
                    yUpdate = 10
                elif event.key == pygame.K_UP:
                    xUpdate = 0
                    yUpdate = -10
                    
                    
                    
        #game ends when player hits edge of screen
        if xp >= displayWidth or xp < 0 or yp >= displayHeight or yp < 0:
            gameExit = True
            
        #update snake's position according to player input
        xp += xUpdate
        yp += yUpdate
        display.fill(black) #THIS IS NEEDED OR SNAKE WILL LEAVE A TRAIL!!!!
        
        #reposition snake according to updated coords and make new food
        pygame.draw.rect(display, red, [foodx, foody, snakeDimension, snakeDimension])
        
        snakeHead = []
        snakeHead.append(xp)
        snakeHead.append(yp)
        snakeLst.append(snakeHead)
        if len(snakeLst) > snakeLen:
            del snakeLst[0]
 
        for x in snakeLst[:-1]: #end game if play collides with themselves
            if x == snakeHead:
                gameExit = True
 
        playerSnake(snakeDimension, snakeLst)
        playerScore(snakeLen - 1)
        
        
        pygame.display.update() #updates the game screen
        
        if xp == foodx and yp == foody:
            foodx = round(random.randrange(0, displayWidth - snakeDimension) / 10.0) * 10.0
            foody = round(random.randrange(0, displayHeight - snakeDimension) / 10.0) * 10.0
            snakeLen += 1
        
        speedM.tick(speed) #will determine speed of snake


    pygame.quit()
    quit()

gameLoop()
