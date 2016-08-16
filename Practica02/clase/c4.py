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
Cliente del s4
"""

import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://192.168.13.91:8000/")
multicall = xmlrpclib.MultiCall(proxy)
multicall.suma1(7,3)
multicall.resta1(7,3)
multicall.multiplicacion1(7,3)
multicall.division1(7,3)
resultado = multicall()

print "7+3=%d, 7-3=%d, 7*3=%d, 7/3=%d" % tuple(resultado)
