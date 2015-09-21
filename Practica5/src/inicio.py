#-*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *
import threading
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from servidorCentral import VentanaServidor #despliega la tabla de los usuarios
#from servidorGeneral import ServidorCentral #servidor que escuchara las peticiones de los demas
from servidor import Servidor 
import xmlrpclib


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

main_class = uic.loadUiType("inicio.ui")[0]

class Ventana(QMainWindow,main_class):
	def __init__(self, parent=None):
		QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.boton_login.clicked.connect(self.OK)
				
 	#Aceptamos la peticion del usuario obteniendo todos los datos proporcionados
	def OK(self):
		usuario = str(self.text_usser.toPlainText())
		ip1 = str(self.text_ip1.toPlainText())
		servidor= str(self.text_ip2.toPlainText())
		#cargar servidor de peticiones
		self.hiloServidorPrivado = threading.Thread(target=self.IniciaServidorPrivado,args=(ip1,))
		self.hiloServidorPrivado.start()
		#cargar interfaz
		self.s = VentanaServidor(usuario,ip1,servidor)
		self.s.show()
		self.hide()

	#Ejejcutamos un servidor para escuchar peticiones que llegan de conversaciones
	def IniciaServidorPrivado(self,ip1):
		server = SimpleXMLRPCServer((ip1, 8000),requestHandler=RequestHandler,allow_none=True)
		server.register_introspection_functions()
		server.register_instance(Servidor())
		try:
			server.serve_forever()
			print 'Use Control-C to exit'
		except KeyboardInterrupt:
			print 'Exiting'			

	
						  
	
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