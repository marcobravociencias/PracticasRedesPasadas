#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import argparse
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import threading
import time
from chat import Chat
from ThreadEx import *
import pyaudio
import numpy
import numpy as np
import multiprocessing as mp
from cStringIO import StringIO
from numpy.lib import format
from videoClase import VideoLLamada



class Bob():

	def __init__(self,usr,ip1,ip2):
		self.usr = usr
		self.ip1 = ip1
		self.ip2 = ip2
		self.alice = xmlrpclib.ServerProxy("http://"+self.ip2+":8000",allow_none=True) 
		self.tem = threading.Event()
		self.chat = Chat(self.tem)
		self.chat.show()
		self.chat.boton_send.clicked.connect(self.enviar)
		self.hilo_Bob = threading.Thread(target=self.escucha)
		self.hilo_Bob.start()
		self.chat.boton_call.clicked.connect(self.iniciaLlamada)
		self.chat.boton_callVideo.clicked.connect(self.terminarLlamada)
		#self.stopVideo = 0
				
		
	def escucha(self):
		while True:
			time.sleep(1)
			server = xmlrpclib.ServerProxy("http://"+self.ip1+":8000",allow_none=True) 
			msj = server.vaciaBuffer()
			if(len(msj)!=0):
				self.chat.setTexto(msj)
				print 'MI mensaje es :'+msj
		
 
	def enviar(self):
		print 'Mando mensaje'
		if(self.alice.ping()):
			print 'Entramos'
			msj = self.usr+' : '+str(self.chat.text_send.toPlainText())+'\n'
			self.alice.enviarMensaje(msj)
			self.chat.setTexto(msj)
			print 'se hizo ping con exito'
		
	
	def iniciaLlamada(self):
		import multiprocessing
		self.stack = multiprocessing.Queue(10000)
		self.hiloManda = ThreadEx(targetp=self.enviaAudio,namep='hiloManda')
		self.hiloManda.start()
		self.hiloEscucha = ThreadEx(targetp=self.reprodAudio,namep='hiloEscucha')
		self.hiloEscucha.start()
		

	def reprodAudio(self):
		CHUNK = 1024
		WIDTH = 2
		CHANNELS = 2
		RATE = 44100
		p = pyaudio.PyAudio()
		FORMAT = p.get_format_from_width(WIDTH)
		
		stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)

		while True:
			if self.hiloManda.isStopEx():
				return 1
			n = 50
			frame = []
			for i in range(0,n):
				frame.append(stream.read(CHUNK))

			audioBinario = numpy.fromstring(''.join(frame), dtype=numpy.uint8)

			if self.stack.full():
				self.stack.get_nowait()
			self.stack.put(audioBinario)

	def enviaAudio(self):
		while True:
			if self.hiloManda.isStopEx():
				return 1
			d = self.stack.get()
			data = xmlrpclib.Binary(d)
			self.alice.recibeAudio(data)

	def terminarLlamada(self):
		self.hiloEscucha.stopEx()
		self.hiloManda.stopEx()	
	
	def video(self):
		'''
		if(self.stopVideo!=0):
			self.hilo_video.stop()	
		self.stopVideo = 1
		#self.alice.creaHiloVideo()
		'''
		self.hilo_video = threading.Thread(target=self.iniciaVideo)
		self.hilo_video.start()

		
	def iniciaVideo(self):
		self.video = VideoLLamada(self.ip2)