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
Cliente para el servidor s2
"""

import xmlrpclib

server = xmlrpclib.Server('http://10.0.0.3:8000')
print server.chop_in_half('Probando el metodo chop')
print server.repeat('quiero pasar el curso\n', 5)
#print server._privateFunction() #excepcion
