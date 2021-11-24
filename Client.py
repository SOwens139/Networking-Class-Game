# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 13:17:49 2021

@author: Owner
"""

from socket import *
serverName = '10.0.0.196'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
#variables to be passed to server
coin = 25
timer = 10
map = 1
while True:
#sending all the variables with commas to be split by the server \n is used
#to mark thee beggining of a message
    clientSocket.sendall(str.encode("\n".join([str(coin),str(timer),str(map)])))
#message from thee server containing a score
    score = clientSocket.recv(1024)
    print('From Server: ',score.decode())
#closing connection
clientSocket.close()