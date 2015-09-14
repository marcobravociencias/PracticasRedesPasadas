#-*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *
import threading
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from servidor import Servidor
import xmlrpclib
from cliente import Bob
import time


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

main_class = uic.loadUiType("servidor.ui")[0]

class VentanaServidor(QMainWindow,main_class):
	def __init__(self,usuario,ip1,ipServidor):
		QMainWindow.__init__(self)
		self.setupUi(self)
		self.act.clicked.connect(self.actualizar)
		self.usr = usuario
		self.ip1 = ip1
		self.ipServidor = ipServidor
		#Generamos un proxy
		self.proxy = xmlrpclib.ServerProxy("http://"+self.ipServidor+":8000",allow_none=True) 
		self.proxy.setUsuario(self.usr,self.ip1)
		self.conec.clicked.connect(self.conectar)
		self.desc.clicked.connect(self.desconectar)
		#Headers
		self.header(0)		
		self.max = -1
		self.Escuchar = threading.Thread(target=self.EscuchaPeticion)
		self.Escuchar.start()
 
	def EscuchaPeticion(self):
		while True:
			time.sleep(1)
			server = xmlrpclib.ServerProxy("http://"+self.ip1+":8000",allow_none=True) 
			ip = server.getMiIp()
			if(ip!='NO'):
				server.setMiIp('NO') #Mandamos nuestra ip al otro usuario
				self.c = Bob(self.usuario,self.ip1,ip) #ponemos la ip que desea conectarse
				self.c.show()

	def desconectar(self):
		self.proxy.removeUsuario(self.ip1)
		
 
	def actualizar(self):
		self.tableWidget.clear()
		cadena = self.proxy.getAll().split(',') # obtenemos un arreglo con usuarios y sus ips
		cont = 0
		self.header(len(cadena))
		self.max = len(cadena)
		for i in cadena:
			subCadena = i.split('-')
			usr = QtGui.QLineEdit(subCadena[0])
			self.tableWidget.setItem(cont, 0, QtGui.QTableWidgetItem(usr.text()))
			ip = QtGui.QLineEdit(subCadena[1])
			self.tableWidget.setItem(cont, 1, QtGui.QTableWidgetItem(ip.text()))
			cont = cont+1
	
	def conectar(self):
		
		if(self.max<0):
			return
		id_row = int(str(self.id_row.toPlainText())) #obtenemos el di con el que deseamos conectar
		if(self.max<id_row or id_row < 0):
			return
		#Recuperamos info
		usuario = str(self.tableWidget.item(id_row,0).text())
		ip =  str(self.tableWidget.item(id_row,1).text())
		print usuario+' '+ip
		##self.usuario mia
		#self.ip mia
		server = xmlrpclib.ServerProxy("http://"+ip+":8000",allow_none=True)
		server.setMiIp(self.ip1) #Mandamos nuestra ip al otro usuario
		self.c = Bob(self.usuario,self.ip1,ip) #ponemos la ip que desea conectarse
		self.c.show()



		
	def header(self,row):						  
		self.tableWidget.setRowCount(row)
		self.tableWidget.setColumnCount(2)
		header = (QStringList() << 'Usuario' << 'Direccion IP')
		self.tableWidget.setHorizontalHeaderLabels(header)
							  
	
class App(QApplication):
	def __init__(self, *args):
		QApplication.__init__(self, *args)
		self.main = VentanaServidor(None)
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