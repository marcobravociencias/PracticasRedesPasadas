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
Servidor Basico, dira si un numero
es para o impar
"""
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

def is_even(n):
    return n%2 == 0
server = SimpleXMLRPCServer(("192.168.13.91", 8000))
print "Escuchando por el puerto 8000"
server.register_function(is_even, "is_even")
server.serve_forever()




