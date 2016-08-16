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
Thread
"""
import threading

def worker(count):
    print "Thread %s vivo Nombre %s " % (count,threading.currentThread().getName())
    return

threads = list()

for i in range(3):
    t = threading.Thread(target=worker, args=(i,), name=`i+1`)
    threads.append(t)
    t.start()

