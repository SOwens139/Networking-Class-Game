import pygame
from pygame import image
from pygame.locals import *
from socket import *

'''
serverName = 'localHost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
clientSocket.sendall(str.encode("\n".join([str(coins),str(round(timer)),str(currentMap)])))
score = clientSocket.recv(1024)
print('From Server: ',score.decode())
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

#image loading into memory
fireflys_image = pygame.image.load('Effect_fireflys.png')
sky_image = pygame.image.load('sky.png')


start_ticks=pygame.time.get_ticks() #starter tick

class World():
    #constructor
    def __init__(self, data):
        self.tile_list = []

        #loading images/blocks
        dirt_image = pygame.image.load('dirt.png')
        grass_image = pygame.image.load('grassBlock.png')
        player_image = pygame.image.load('player.png')
        
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
[1, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 3 , 2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1],
[1, 0, 0, 2 , 1, 0, 0, 3, 0, 0, 2, 2, 2, 0, 0, 1],
[1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


world_data_two = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 1],
[1, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1],
[1, 2, 2, 2 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

world_data_three = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 1],
[1, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1],
[1, 2, 2, 2 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

world_data_four = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 1],
[1, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1],
[1, 2, 2, 2 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

world_data_five = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 1],
[1, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1],
[1, 2, 2, 2 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

world_data_six = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 1],
[1, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1],
[1, 2, 2, 2 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

world_data_seven = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 1],
[1, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1],
[1, 2, 2, 2 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0 , 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1],
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
    timer = 500 - seconds #creates the timer variable to be passed to server 
    if seconds>500: # if more than 500 seconds close the game
        break 

 
    #drawing images onto screen
    screen.blit(sky_image, (0, 0))
    screen.blit(fireflys_image, (100, 100))

    #calling draw function
    if timer >= 490:
        world.draw()
        currentMap = 1
      

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
    
    # this must come after world.draw or it will put it behind the tile assets
    font = pygame.font.Font('freesansbold.ttf', 32)
    dispCoin = font.render('Coins: ' + str(coins), True, (255,255,255))
    coinRect = dispCoin.get_rect()
    coinRect = (0, 15)
    
    dispTimer = font.render('Time Left: '+ str(round(timer)), True, (255,255,255))
    timerRect = dispTimer.get_rect()
    timerRect = (0,45)
    
    dispCurrentMap = font.render('Current Level: '+ str(currentMap), True, (255,255,255))
    mapNumRect = dispCurrentMap.get_rect()
    mapNumRect = (0,75)
    
    screen.blit(dispCoin, coinRect)
    screen.blit(dispTimer,timerRect)
    screen.blit(dispCurrentMap, mapNumRect)
    
    
    

    #making event handler to look for QUIT input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            

    pygame.display.update()

pygame.quit()