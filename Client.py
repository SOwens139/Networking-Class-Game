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
p1Score = 0
p2Score = 0

#sending all the variables with commas to be split by the server \n is used
#to mark thee beggining of a message
while True:
    try:
        #sending all the variables with commas to be split by the server \n is used
        #to mark thee beggining of a message
        clientSocket.sendall(str.encode("\n".join([str(coins),str(timer)])))
        #message from the server containing a score
        scores = clientSocket.recv(1024).decode()
        scores = re.split(',|\[|\]',scores)
        p1Score = int(scores[1])
        p2Score = int(scores[2])
        print('Player One Score: ',p1Score)
        print('Player Two Score: ',p2Score)
       
    except socket.error as e:
        print(e)
    
#closing connection
clientSocket.close()