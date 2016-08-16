import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import threading
import time


main_class = uic.loadUiType("chat.ui")[0]
class Chat(QMainWindow,main_class):
	def __init__(self, parent=None):
		QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.boton_send.clicked.connect(self.enviar)
		self.boton_salir.clicked.connect(self.salir)
		#self.usr = usr
		#self.ip = ip
		#self.usr = 'Jose'
		#self.ip = '192.168.13.91'
		#self.proxy = xmlrpclib.ServerProxy("http://"+self.ip+":8000")
		#server = SimpleXMLRPCServer((self.ip, 8000),requestHandler=RequestHandler)
		#server.register_introspection_functions()
		#server.register_instance(Listener())
		#t1 = threading.Thread(tarjet=server.serve_forever())
		#t1.start()


	def gets(self,usr,ip1,ip2): 				
		self.usr = usr
		self.ip1 = ip1 #Mia 
		self.ip2 = ip2 #Tuya
		self.server = SimpleXMLRPCServer((self.ip1, 8000),requestHandler=RequestHandler) #Dire mia
		self.server.register_introspection_functions()
		self.server.register_instance(Listener())
		t1 = threading.Thread(target=self.server.serve_forever)
		t1.start()
		self.proxy = xmlrpclib.ServerProxy("http://"+self.ip2+":8000",allow_none=True) #Dire tuya
		self.hilo = threading.Thread(target=self.Escucha, name='hilo')
		self.hilo.start()
		
	def Escucha(self):
		while True:
			time.sleep(1)
			server = xmlrpclib.ServerProxy("http://"+self.ip1+":8000",allow_none=True) 
			msj = server.vaciaBuffer()
			coloca(msj)
			print 'Me llamo'
		
	def salir(self):
		self.hide()		
 
	def enviar(self):
		msj = str(self.text_send.text())
		var = self.texr_recived.toPlainText()
		self.texr_recived.setPlainText(var+'\n'+self.usr+" : "+msj) #interfaz
		self.proxy.mensaje(self.usr+' : '+msj)
	
	def coloca(self,msj):	
		self.texr_recived.setPlainText(msj) #interfaz
		
class Listener:

    def __init__(self,messageReply=None):
        global message
        message = messageReply
        self.buffer = list()
    def ping(self):
        return True
    def sentMessage(self, messageSent):
        message.setText(messageSent)
    def mensaje(self,msj):
    	self.buffer.append(msj)
    	print msj
	def vaciaBuffer():
		buffer = ''
		for m in self.buffer:
			buffer += m
			print buffer
        return buffer

        

class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths = ('/RPC2',)

	
class App(QApplication):
	def __init__(self, *args):
		QApplication.__init__(self, *args)
		self.main = Chat()
		self.connect(self, SIGNAL("lastWindowClosed()"), self.byebye )
		self.main.show()

	def byebye( self ):
		self.exit(0)    
 
def main(args):
	global app
	app = App(args)
	app.exec_()

if __name__ == "__main__":
	main(sys.argv)