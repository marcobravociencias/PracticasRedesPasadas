#-*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *
import threading
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from ServidorN import Servidor
import xmlrpclib
from usuarioN import Bob
import pyaudio


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

main_class = uic.loadUiType("login.ui")[0]

class Ventana(QMainWindow,main_class):
	def __init__(self, parent=None):
		QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.boton_login.clicked.connect(self.OK)
				
 
	def OK(self):
		usuario = str(self.text_usser.toPlainText())
		ip1 = str(self.text_ip1.toPlainText())
		ip2 = str(self.text_ip2.toPlainText())
		#SObra
		usuario = 'Marco'
		ip1 = 'localhost'
		ip2 = 'localhost'
		self.hiloSer = threading.Thread(target=self.IniciaServidor,args=(ip1,))
		self.hiloSer.start()
		self.c = Bob(usuario,ip1,ip2)
		self.hide()

	
	def IniciaServidor(self,ip1):
		server = SimpleXMLRPCServer((ip1, 8000),requestHandler=RequestHandler,allow_none=True)
		server.register_introspection_functions()
		server.register_instance(Servidor())
		print "Listening on port 8000..."
		try:
			server.serve_forever()
			print 'Use Control-C to exit'
		except KeyboardInterrupt:
			print 'Exiting'			
		'''
		try:
			print 'Use Control-C to exit'
    	except KeyboardInterrupt:
    		print 'Exiting'
'''
						  
	
class App(QApplication):
	def __init__(self, *args):
		QApplication.__init__(self, *args)
		self.main = Ventana(None)
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