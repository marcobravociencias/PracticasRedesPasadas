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
Cliente para el servidor s1
"""
import xmlrpclib



proxy = xmlrpclib.ServerProxy("http://192.168.13.91:8000/")
print "3 es par: %s" % str(proxy.is_even(3))
print "7 es par: %s" % str(proxy.is_even(7))
