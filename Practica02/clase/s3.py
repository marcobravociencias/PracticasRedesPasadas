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
import xmlrpclib

def python_logo():
     with open("call.png", "rb") as handle:
         return xmlrpclib.Binary(handle.read())

server = SimpleXMLRPCServer(("10.0.0.3", 8000))
print "escuchando por el puerto 8000..."
server.register_function(python_logo, 'python_logo')

server.serve_forever()
