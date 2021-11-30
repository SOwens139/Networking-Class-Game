# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 18:46:13 2021

@author: Sean Owens
"""

import socket
from _thread import*
import sys

server = "10.0.0.196"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
    print("port bound")
    
except socket.error as e:
    str(e)

    
s.listen(2)
print("Waiting for connection, Server Started")

data = [0, 0, 0, 0, 0, 0]

def threaded_client(conn, player):
    print("Thread Created")
    while True:

        try:
            coins, timer, currentMap, mapFlag = [int(i) for i in conn.recv(4096).decode().split('\n')]
            
            
            
            if not coins:
                print ("Coin Disconnected")
                break
            else:
                if player == 0:
                    data[0] = coins * timer
                
                    print("sending player 1 score " +  str(data[0]))
                elif player == 1:
                    data[1] = coins * timer
                    
                    print("sending player 2 score " +  str(data[1]))
                else:
                    break
                
                if mapFlag == 1:
                    mapFlag = 0
                    currentMap += 1
                   
                data[2] = currentMap
                print("sending currentMap " +  str(data[2]))
                data[3] = mapFlag 
                print("sending mapFlag " +  str(data[3]))
                data[4] = player
                print("sending currentPlayer " +  str(data[4]))
                if currentMap == 8:
                    if plScore > p2Score:
                        data[5] = 1
                    else:
                        data[5] = 2
            conn.send(str(data).encode())
        except:
            break
    print("lost connection")
    conn.close()

currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
    if currentPlayer == 2:
        currentPlayer = 0
    