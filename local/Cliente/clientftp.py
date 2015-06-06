#!/usr/bin/python
# -*- encoding: utf-8 -*-

import zmq
import random
import sys
import time
import os

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
#socket.connect("tcp://localhost:%s" % port)
socket.connect("tcp://localhost:%s" % port)
while True:
    msg = socket.recv()
    print msg
    opcion=""
    opcion=raw_input("[Introduzca opcion] - ")
    socket.send(opcion)
    #socket.send("client message to server")
    time.sleep(1)