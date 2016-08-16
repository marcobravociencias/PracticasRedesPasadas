#-*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import threading
import time
from chatN import Chat
from ThreadParable import *
import pyaudio


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
		self.chat.boton_salir.clicked.connect(self.terminarLlamada)
				
		
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

		# crea algo de tipo Interfaz Llamada para que eventualmente
		# el usuario vea que hay llamada en curso
		#self.interfaz_llamada = InterfazLlamada()
		#self.interfaz_llamada.termina.clicked.connect(self.termina_llamada)
		
		# muestra la ventanita de llamada en curso
		#self.interfaz_llamada.show()

		# utilizamos una cola para almacenar datos de audio
		self.stack = multiprocessing.Queue(10000)

		# hilo que captura el audio local y lo mete en la cola
		#self.hiloEscucha = threading.Thread(target=self.reprodAudio)
		self.hiloEscucha = ThreadEx(targetp=self.reprodAudio,namep='hiloEscucha')
		self.hiloEscucha.start()
		# hilo que saca lo que hay en la cola y lo envía al servidor remoto
		#self.hiloManda = threading.Thread(target=self.enviaAudio)
		self.hiloManda = ThreadEx(targetp=self.enviaAudio,namep='hiloManda')
		self.hiloManda.start()

	def reprodAudio(self):
		"""
		Permanece en escucha permanente del audio local y mete los datos en la cola
		"""
		# parámetros del stream de entrada
		CHUNK = 1024
		WIDTH = 2
		CHANNELS = 2
		RATE = 44100
		p = pyaudio.PyAudio()
		FORMAT = p.get_format_from_width(WIDTH)

		# stream que captura el audio
		stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)

		while True:
			# checamos si el usuario aún no termina la llamada
			if self.hiloManda.isStopEx():
				return 1

			# tamaño del buffer que almacena datos de audio
			n = 50
			# arreglo para almacenar el buffer
			frame = []

			# agregamos n muestras de audio del stream al arreglo frame
			for i in range(0,n):
				frame.append(stream.read(CHUNK))

			# convertimos la "cadena" frame a datos binarios con el tipo de dato uint8
			audioBinario = numpy.fromstring(''.join(frame), dtype=numpy.uint8)

			# verificamos que la cola no esté llena y si lo está sacamos algo
			if self.stack.full():
				self.stack.get_nowait()

			# metemos los datos binarios a la cola
			self.stack.put(audioBinario)

	def enviaAudio(self):
		"""
		Permanentemente toma los datos (binarios) que hay en la cola y los envía
		al servidor remoto
		"""
		while True:
			# checamos si el usuario aún no termina la llamada
			if self.hiloManda.isStopEx():
				return 1
			# primer elemento de la cola
			d = self.stack.get()
			# convertimos a una instancia de datos binarios
			data = xmlrpclib.Binary(d)
			# los enviamos al servidor remoto
			self.alice.recibeAudio(data)

	def terminarLlamada(self):
		"""
		Termina los hilos correspondientes a la llamada de voz y cierra la ventanita
		"""
		self.hiloEscucha.stopEx()
		self.hiloManda.stopEx()
		#self.interfaz_llamada.close()	