#-*- coding: utf-8 -*-
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import sys
import pyaudio

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class Servidor:
    
    def __init__(self):
        self.buffer = list()
        self.stream = None
    
    def ping(self):
        return True
    
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
