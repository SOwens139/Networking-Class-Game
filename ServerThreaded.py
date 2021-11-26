# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 18:46:13 2021

@author: Sean Owens
"""

import socket
from _thread import*
import sys

server = "10.0.0.196"
port = 12000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
    
except socket.error as e:
    str(e)

    
s.listen(2)
print("Waiting for connection, Server Started")

def threaded_client(conn):
    
    while True:
        try:
            coins, timer, currentMap = [int(i) for i in conn.recv(1024).decode().split('\n')]
            
            if not coins:
                print ("Disconnected")
                break
            else:
                score = coins * round(timer)
                
                print("sending " +  str(score))
                
            conn.send(str(score).encode())
        except:
            break
    print("lost connection")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    
    start_new_thread(threaded_client, (conn,))
    