import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import threading
import time
from chatN import Chat


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
		
			
	
		
		
