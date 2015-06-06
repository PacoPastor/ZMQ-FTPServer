#!/usr/bin/python
# -*- encoding: utf-8 -*-
import zmq
import random
import sys
import time
import os
import subprocess
import re

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)
instruccion=""
inicio=False

while True:
    if inicio==False:
        socket.send("------------------------------\n-----------MENU----------------\n---A continuacion, tiene usted-\n---la posibilidad de manejar un\n---FTP, podra utilizar los —--\n---siguientes comandos:--------\n-----*ls - Visor de ficheros---\n-------------------------------\n---Las siguientes instrucciones\ndeberas de utilizar correctamen\nte, sucedidos de las direccio--\nnes fisicas--------------------\n-----*cp - Copia de ficheros---\n-----*mv - Mover ficheros------\n-----*rm - Borrar ficheros-----\n-----*help - Vovler a ver esto-\n-------------------------------\n")
        inicio=True
    instruccion=""
    msg = socket.recv()
    mov = re.search("(mv.+)", msg)
    cop = re.search("(cp.+)", msg)
    delete = re.search("(rm.+)", msg)
    no_borrar = re.search ("(mv\ server.*)", msg)
    if msg=="ls":
        f=os.popen("ls")
        instruccion+="\n"
        for i in f.readlines():
            instruccion+=i
        socket.send(instruccion)
    elif mov:
        f=os.popen(msg)
        socket.send("El archivo ha sido transferido correctamente")
    elif cop:
        f=os.popen(msg)
        socket.send("El archivo ha sido copiado correctamente")
    elif delete:
        f=os.popen(msg)
        socket.send("El archivo ha sido borrado correctamente")
    elif msg=="help":
    	inicio=False
    else:
    	inicio=False
    time.sleep(1)