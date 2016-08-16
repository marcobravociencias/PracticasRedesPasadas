#! /usr/bin/env python


#####################################################
# PURPOSE:                                          #
#                                                   #
# Vilchis Dominguez Miguel Alonso                   #
#       <mvilchis@ciencias.unam.mx>                 #
#                                                   #
# Notes:                                            #
#                                                   #
# Copyright   17-08-2015                            #
#                                                   #
# Distributed under terms of the MIT license.       #
#####################################################

"""

"""

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
# Restringir a un directorio particular
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Creamos la instancia que revisara los mensajes entrantes
server = SimpleXMLRPCServer(("10.0.0.3", 5000), requestHandler=RequestHandler) 
server.register_introspection_functions()
server.register_multicall_functions()

class Listener:
    def __init__(self,messageReply=None):
        global message
        message = messageReply
    def ping(self):
        return True
    def sentMessage(self, messageSent):
        message.setText(messageSent)

server.register_instance(Listener()) 
try:
        print 'Use Control-C to exit'
        server.serve_forever()
except KeyboardInterrupt:
        print 'Exiting'
        
