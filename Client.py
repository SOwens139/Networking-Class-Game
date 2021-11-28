# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 13:17:49 2021

@author: Owner
"""

import socket
import re
serverName = '10.0.0.196'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
#variables to be passed to server
coins = 25
timer = 10
currentMap = 1
mapFlag = 0
p1Score = 0
p2Score = 0
playerNum = 0

#sending all the variables with commas to be split by the server \n is used
#to mark thee beggining of a message
while True:
    try:
        #sending all the variables with commas to be split by the server \n is used
        #to mark thee beggining of a message
        clientSocket.sendall(str.encode("\n".join([str(coins),str(timer), str(currentMap), str(mapFlag)])))
        #message from the server containing a score
        data = clientSocket.recv(1024).decode()
        data = re.split(',|\[|\]',data)
        p1Score = int(data[1])
        p2Score = int(data[2])
        currentMap = int(data[3])
        mapFlag = int(data[4])
        playerNum = int(data[5])
        print(data)
        
        print('Player One Score: ',p1Score)
        print('Player Two Score: ',p2Score)
        print('Current map: ',currentMap)
        print('Map Flag: ',mapFlag)
        print('Player Number: ',playerNum)
       
    except socket.error as e:
        print(e)
    
#closing connection
clientSocket.close()