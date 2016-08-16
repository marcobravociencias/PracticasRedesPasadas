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
Cliente
"""
import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://10.0.0.3:8000/")
with open("imagen_descargada.png", "wb") as handle:
    handle.write(proxy.python_logo().data)
