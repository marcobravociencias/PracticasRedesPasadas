from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import sys

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class Servidor:
    
    def __init__(self):
        self.buffer = list()
    
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
