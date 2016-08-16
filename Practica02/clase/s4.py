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
Multillamadas
"""
from SimpleXMLRPCServer import SimpleXMLRPCServer

def suma(x,y):
    return x+y

def resta(x, y):
    return x-y

def multiplicacion(x, y):
    return x*y

def division(x, y):
    return x/y

server = SimpleXMLRPCServer(("192.168.13.91", 8000))
print "Escuchando por el puerto 8000..."
server.register_multicall_functions()
server.register_function(suma, 'suma1')
server.register_function(resta, 'resta1')
server.register_function(multiplicacion, 'multiplicacion1')
server.register_function(division, 'division1')
server.serve_forever()
