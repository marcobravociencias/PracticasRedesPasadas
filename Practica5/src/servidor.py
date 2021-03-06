#!/usr/bin/python
# -*- coding: utf-8 -*-
from cStringIO import StringIO
from numpy.lib import format
import cv2
import argparse
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import sys
import pyaudio
import numpy
import threading
from usuario import Usuario

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class Servidor:
    
    def __init__(self):
        self.buffer = list()
        self.stream = None
        self.frames = []
        self.videoinicia = 1
        self.creaHiloVideo()
        self.usuarios = list()
        self.ipEntrante = 'disponible'
    
    def ping(self):
        return True
    
    #Ponemos la ip del usuario que quiere conectarse.
    def setMiIp(self,ipEntrante): 
        self.ipEntrante = ipEntrante
    def getTuIp(self):
        return self.ipEntrante        

    def setUsuario(self,usr,ip):
        usr = Usuario(usr,ip)
        self.usuarios.append(usr)
    
    def removeUsuario(self,ip1,usr):
        var = False
        for m in self.usuarios[:]:
            if(usr==m.getUsr() and ip1==m.getIp()):
                self.usuarios.remove(m)
                var = True
        return var             

    def getAll(self):
        cat = ''
        for m in self.usuarios:
           cat = cat +'\n'+m.getUsr()+'-'+m.getIp()+','
        return cat        
    
    def enviarMensaje(self,msj):
        self.buffer.append(msj)
        
    def vaciaBuffer(self):
        buffer = ''
        for m in self.buffer:
            buffer += m
            print buffer
            self.buffer = list()
        return buffer

    def recibeAudio(self,audio):
        CHUNK = 1024
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = 5 
        DELAY_SIZE = RECORD_SECONDS * RATE / (1000 * CHUNK)
        p = pyaudio.PyAudio()
        FORMAT = p.get_format_from_width(2)
        stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    frames_per_buffer=CHUNK)
        data = audio.data
        stream.write(data)
        stream.close()
        p.terminate()

    def recibeVideo(self,video):
        self.frames.append(toArray(video.data))

    def creaHiloVideo(self):
        if(self.videoinicia==0):
            stopVideo()
        self.videoThread = threading.Thread(target=self.reproduceVideo)
        self.videoThread.setDaemon(True)
        self.videoThread.start()
        self.videoinicia = 0
    
    def stopVideo(self):
        self.videoThread.stop()        

            
    def toArray(s):
        f=StringIO(s)
        arr=format.read_array(f)
        return arr 

    def reproduceVideo(self):
        while True:
            if len(self.frames) > 0:
                cv2.imshow('Servidor',self.frames.pop(0))
                if cv2.waitKey(1) & 0xFF==ord('q'):
                    break
        cv2.destroyAllWindows()
    
    