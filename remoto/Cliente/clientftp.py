#!/usr/bin/python
# -*- encoding: utf-8 -*-

import zmq
import random
import sys
import time
import os

port = "5556"
ip=sys.argv[1]
context = zmq.Context()
socket = context.socket(zmq.PAIR)
#socket.connect("tcp://localhost:%s" % port)
socket.connect("tcp://%s:5556" % ip)
while True:
    msg = socket.recv()
    print msg
    opcion=""
    opcion=raw_input("[Introduzca opcion] - ")
    socket.send(opcion)
    #socket.send("client message to server")
    time.sleep(1)