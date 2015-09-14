#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading

class ThreadEx(threading.Thread):
    def __init__(self,targetp,namep):
        super(ThreadEx,self).__init__(target=targetp,name=namep)
        self._stop = threading.Event()

    def stopEx(self):
        self._stop.set()

    def isStopEx(self):
        return self._stop.isSet()