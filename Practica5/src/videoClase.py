import numpy as np
import cv2
import multiprocessing as mp
import time
import xmlrpclib
import numpy
from cStringIO import StringIO
from numpy.lib import format


class VideoLLamada():

    def __init__(self,ip2):
        CHUNK = 1024
        CHANNELS = 1 
        RATE = 44100
        RECORD_SECONDS = 2 
        self.cap = cv2.VideoCapture(0)
        self.proxy = xmlrpclib.ServerProxy("http://"+ip2+":8000",allow_none=False)
        queue = mp.Queue()
        p = mp.Process(target=self.graba,args=(self.proxy,self.cap,))
        p.start()


    def toString(self,data):
        f= StringIO()
        format.write_array(f,data)
        return f.getvalue()
    
    def graba(self,cap,proxy):
        while(True):
            ret, frame = cap.read()
            cv2.imshow('Cliente',frame) 
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            data = xmlrpclib.Binary(toString(frame))
            proxy.playVideo(data) 
        cap.release()
        cv2.destroyAllWindows()


    
