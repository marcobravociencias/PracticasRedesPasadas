#-*- coding: utf-8 -*-

import threading

class ThreadEx(threading.Thread):
    """
    Clase Thread con un método detener(). El hilo puede detenerse externamente
    y consultar el "estado" con el método detenido()
    """
    def __init__(self,targetp,namep):
        super(ThreadEx,self).__init__(target=targetp,name=namep)
        # usamos una bandera _stop
        self._stop = threading.Event()

    def stopEx(self):
        self._stop.set()

    def isStopEx(self):
        return self._stop.isSet()