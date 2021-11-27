import pygame
from pygame import image
from pygame.locals import *
import socket
import re

'''
serverName = '10.0.0.196'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

    try:
        #sending all the variables with commas to be split by the server \n is used
        #to mark thee beggining of a message
        clientSocket.sendall(str.encode("\n".join([str(coins),str(timer)])))
        #message from the server containing the score variables
        scores = clientSocket.recv(1024).decode()
        scores = re.split(',|\[|\]',scores)
        #storing the score variables 
        p1Score = int(scores[1])
        p2Score = int(scores[2])

       
    except socket.error as e:
        print(e)
        
clientSocket.close()
   
'''
pygame.init()

#game window size
screen_width = 1000
screen_height = 750

#creating game window
screen = pygame.display.set_mode((screen_width, screen_height))
#setting game name in display
pygame.display.set_caption('Life and Sword')

#game vars
tile_size = 64
coins = 0 
currentMap = 0 
p1Score = 0
p2Score = 0

#image loading into memory
fireflys_image = pygame.image.load('Assets/Effect_fireflys.png')
sky_image = pygame.image.load('Assets/sky.png')


start_ticks=pygame.time.get_ticks() #starter tick

class World():
    #constructor
    def __init__(self, data):
        self.tile_list = []

        #loading images/blocks
        dirt_image = pygame.image.load('Assets/dirt.png')
        grass_image = pygame.image.load('Assets/grassBlock.png')
        player_image = pygame.image.load('Assets/player.png')
        water_image = pygame.image.load('Assets/water.png')
        underwater_image = pygame.image.load('Assets/underWater.png')
        door_image = pygame.image.load('Assets/door.png')
        
        row_count = 0

        #in this for loop blocks are mapped based on world data list values (i.e. 1 is dirt block 2 is grass block)
        for row in data:
            column_count = 0
            for tile in row:

                #if tile is 1 add dirt block
                if tile == 1:

                    #scaling tiles to tile_size
                    image = pygame.transform.scale(dirt_image, (tile_size, tile_size))

                    #converting image into a rectangle object for coordinates or collision
                    image_rect = image.get_rect()
                    image_rect.x = column_count *tile_size
                    image_rect.y = row_count *tile_size
                    tile = (image, image_rect)

                    #recording/storing all 1's and their coordinates in a list
                    self.tile_list.append(tile)

                    #if tile is 2 add grass block
                if tile == 2:
                    image = pygame.transform.scale(grass_image, (tile_size, tile_size))
                    image_rect = image.get_rect()
                    image_rect.x = column_count *tile_size
                    image_rect.y = row_count *tile_size
                    tile = (image, image_rect)
                    self.tile_list.append(tile)
                    
                if tile == 3:
                    image = pygame.transform.scale(player_image, (round(tile_size*.3), round(tile_size*.3)))
                    image_rect = image.get_rect()
                    image_rect.x = column_count * tile_size + round(tile_size *.38)
                    image_rect.y = row_count * tile_size + round(tile_size *.5)
                    tile = (image, image_rect)
                    self.tile_list.append(tile)
                    
                if tile == 4:
                    image = pygame.transform.scale(water_image, (tile_size, tile_size))
                    image_rect = image.get_rect()
                    image_rect.x = column_count *tile_size
                    image_rect.y = row_count *tile_size
                    tile = (image, image_rect)
                    self.tile_list.append(tile)
                    
                if tile == 5:
                    image = pygame.transform.scale(underwater_image, (tile_size, tile_size))
                    image_rect = image.get_rect()
                    image_rect.x = column_count *tile_size
                    image_rect.y = row_count *tile_size
                    tile = (image, image_rect)
                    self.tile_list.append(tile)
                    
                if tile ==6:
                    image = pygame.transform.scale(door_image, (tile_size, tile_size))
                    image_rect = image.get_rect()
                    image_rect.x = column_count *tile_size
                    image_rect.y = row_count *tile_size
                    tile = (image, image_rect)
                    self.tile_list.append(tile)

                    #incrementing row and column count
                column_count += 1
            row_count += 1

    #iterating through tile_list
    def draw(self):
        for tile in self.tile_list:

            #drawing items onto screen
            screen.blit(tile[0], tile[1])




#data list for dirt and grass blocks etc
world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 6, 1],
[1, 2, 2, 2, 1, 2, 4, 4, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 1, 1, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1],
]

world_data_two = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 2, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 1],
[1, 0, 0, 3, 2, 0, 0, 2, 0, 0, 0, 0, 3, 0, 0, 1],
[1, 0, 0, 2, 1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 6, 1],
[1, 2, 2, 1, 1, 4, 4, 4, 4, 4, 1, 1, 1, 2, 2, 1],
[1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1],
]


world_data_three = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 2, 3, 6, 1],
[1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 2, 2, 1, 2, 2, 1],
[1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 3, 1, 0, 0, 2, 0, 0, 0, 0, 1],
[1, 2, 2, 2, 2, 2, 2, 1, 4, 4, 4, 4, 4, 4, 4, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 1],
]

world_data_four = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 1],
[1, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
[1, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1],
[1, 0, 3, 0, 2, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 1],
[1, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 1],
[1, 4, 1, 4, 4, 4, 1, 4, 4, 4, 1, 4, 1, 4, 4, 1],
[1, 5, 1, 5, 5, 5, 1, 5, 5, 5, 1, 5, 1, 5, 5, 1],
]

world_data_five = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
[1, 0, 1, 0, 1, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 1],
[1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 2, 0, 1, 0, 1],
[1, 0, 2, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 2, 0, 2, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 6, 1],
[1, 2, 1, 2, 2, 2, 1, 2, 1, 4, 4, 1, 2, 1, 2, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 1, 1, 1, 1, 1],
]

world_data_six = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 0, 1],
[1, 5, 3, 0, 0, 0, 0, 0, 0, 0, 6, 1, 0, 1, 0, 1],
[1, 5, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 0, 1],
[1, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
[1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
]

world_data_seven = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


#creating instances of the maps
world = World(world_data)
worldTwo = World(world_data_two)
worldThree = World(world_data_three)
worldFour = World(world_data_four)
worldFive = World(world_data_five)
worldSix = World(world_data_six)
worldSeven = World(world_data_seven)

run = True
while run == True:
    
    #creates the timer for the game
    seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
    timer = 500 - round(seconds) #creates the timer variable to be passed to server 
    
    #Creating each of the message variable to display text on screen
    font = pygame.font.Font('freesansbold.ttf', 32)
    #coin display top left
    dispCoin = font.render('Coins: ' + str(coins), True, (255,255,255))
    coinRect = dispCoin.get_rect()
    coinRect = (0, 10)
    
    #timer display top left
    dispTimer = font.render('Time Left: '+ str(timer), True, (255,255,255))
    timerRect = dispTimer.get_rect()
    timerRect = (0,50)
    
    #current mapp display top left
    dispCurrentMap = font.render('Current Level: '+ str(currentMap), True, (255,255,255))
    mapNumRect = dispCurrentMap.get_rect()
    mapNumRect = (0,90)
    
    #player 1 score display top right
    dispP1Score = font.render('Player 1 Score: '+ str(p1Score), True, (255,255,255))
    p1scoreRect = dispP1Score.get_rect()
    p1scoreRect = (600,10)
    
    #player 2 score display top right
    dispP2Score = font.render('Player 2 Score: '+ str(p2Score), True, (255,255,255))
    p2scoreRect = dispP2Score.get_rect()
    p2scoreRect = (600,90)
    
    #display for current winner top right
    if p1Score > p2Score:
        dispCurrentWin = font.render('Current Winner: Player 1', True, (255,255,255))
        currentWinRect = dispCurrentWin.get_rect()
        currentWinRect = (600,50)
    elif p2Score > p1Score:
        dispCurrentWin = font.render('Current Winner: Player 2', True, (255,255,255))
        currentWinRect = dispCurrentWin.get_rect()
        currentWinRect = (600,50)
    else:
        dispCurrentWin = font.render('Current Winner: Draw', True, (255,255,255))
        currentWinRect = dispCurrentWin.get_rect()
        currentWinRect = (600,50)
        
    #Game Tutorial display for first level   
    dispMoveTutorial = font.render('To move use the arrow keys', True, (0,0,0))
    tutorialRect = dispMoveTutorial.get_rect()
    tutorialRect = (65, 140)
    
    dispWaterTutorial = font.render('Avoid water it kills', True, (0,0,0))
    waterTutorialRect = dispWaterTutorial.get_rect()
    waterTutorialRect = (65, 180)
    
    dispCoinTutorial = font.render('Collect coins to boost your score', True, (0,0,0))
    coinTutorialRect = dispCoinTutorial.get_rect()
    coinTutorialRect = (65, 220)
    
    dispDoorTutorial = font.render('Reach the door to go to the next level', True, (0,0,0))
    doorTutorialRect = dispDoorTutorial.get_rect()
    doorTutorialRect = (65, 260)
    
    
    #drawing images onto screen
    screen.blit(sky_image, (0, 0))
    screen.blit(fireflys_image, (100, 100))

    #calling draw function
    if timer >= 490:
        world.draw()
        currentMap = 1
        screen.blit(dispMoveTutorial, tutorialRect)
        screen.blit(dispWaterTutorial, waterTutorialRect)
        screen.blit(dispCoinTutorial, coinTutorialRect)
        screen.blit(dispDoorTutorial, doorTutorialRect)

    elif timer >= 480 and timer < 490:
        worldTwo.draw()
        currentMap = 2
        
    elif timer >= 470 and timer < 480:
        worldThree.draw()
        currentMap = 3
        
    elif timer >= 460 and timer < 470:
        worldFour.draw()
        currentMap = 4
    
    elif timer >= 450 and timer < 460:
        worldFive.draw()
        currentMap = 5
    
    elif timer >= 440 and timer < 450:
        worldSix.draw()
        currentMap = 6
        
    else:
        worldSeven.draw()
        currentMap = 7
    
   
    
    #This calls the text display objects made above
    # this must come after world.draw or it will put it behind the tile assets
    screen.blit(dispCoin, coinRect)
    screen.blit(dispTimer,timerRect)
    screen.blit(dispCurrentMap, mapNumRect)
    screen.blit(dispP1Score, p1scoreRect)
    screen.blit(dispP2Score, p2scoreRect)
    screen.blit(dispCurrentWin, currentWinRect)

    #making event handler to look for QUIT input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
            

    pygame.display.update()

pygame.quit()