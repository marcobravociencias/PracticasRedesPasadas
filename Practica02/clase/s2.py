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
import SimpleXMLRPCServer

class StringFunctions:
    def __init__(self):
        #Acceso a las cadenas con python_string.func_name
        import string
        self.python_string = string

    def _privateFunction(self): #Si comienza por _ no puede ser 
        #llamada
        pass
    
    def chop_in_half(self, astr):
        return astr[:len(astr)/2]

    def repeat(self, astr, times):
        return astr * times
    
server = SimpleXMLRPCServer.SimpleXMLRPCServer(("10.0.0.3", 8000))
server.register_instance(StringFunctions())
server.serve_forever()
