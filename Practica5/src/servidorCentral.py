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
		self.puerto = 8001
		#Generamos un proxy para mandar la informacion al servidor
		conexion = "http://"+self.ipServidor+":"+str(self.puerto)
		self.proxy = xmlrpclib.ServerProxy(conexion,allow_none=True) 
		#Agregamos un nuevo usuario
		self.proxy.setUsuario(self.usr,self.ip1)
		self.conec.clicked.connect(self.conectar)
		self.desc.clicked.connect(self.desconectar)
		#Headers
		self.max = -1
		self.actualizar()
 		self.Escuchar = threading.Thread(target=self.EscuchaPeticion)
		self.Escuchar.start()
	
	#Se dedica a escuchar si hay una ip que quiere conversar con el		
	def EscuchaPeticion(self):
		while True:
			time.sleep(1)
			server = xmlrpclib.ServerProxy("http://"+self.ip1+":8000",allow_none=True) 
			ipOtro = server.getTuIp()
			print 'IP de otra persona '+str(ipOtro)
			if(ipOtro!='disponible'):
				server.setMiIp('disponible') #Marcamos la ip como disponible
				self.c = Bob(self.usr,self.ip1,ipOtro) #ponemos la ip que desea conectarse
				self.c.show()
	#Se borra del servidor con su ip el usuario.				
	def desconectar(self):
		self.proxy.removeUsuario(self.usr,self.ip1)
		
 
	def actualizar(self):
		self.tableWidget.clear()
		cadena = self.proxy.getAll().split(',') # obtenemos un arreglo con usuarios y sus ips
		cont = 0
		self.header(len(cadena))
		self.max = len(cadena)
		if(len(cadena)==1): #solo hay una persona
			return
		for i in cadena:
			subCadena = i.split('-')
			if(len(subCadena)==1):
				return
			ip = QtGui.QLineEdit(subCadena[1]).text()
			usr = QtGui.QLineEdit(subCadena[0]).text()[1:]
			print 'usuario '+self.usr+' - '+usr+' Hizo salto de renglon'
			if((self.usr!=usr[:1])):# and self.ip1!=ip.text()) or True):
				self.tableWidget.setItem(cont, 0, QtGui.QTableWidgetItem(usr))
				self.tableWidget.setItem(cont, 1, QtGui.QTableWidgetItem(ip))
				cont = cont+1
		
	
	#Contectamos con el otro usuario
	def conectar(self):
		
		if(self.max<0):
			return
		id_row = int(str(self.id_row.toPlainText()))-1 #obtenemos el di con el que deseamos conectar
		if(self.max<id_row or id_row < 0):
			return
		#Recuperamos info
		usuario = str(self.tableWidget.item(id_row,0).text())
		ip =  str(self.tableWidget.item(id_row,1).text())
		print 'Conectando con '+usuario+' '+ip
		
		self.hiloServidorOtro = threading.Thread(target=self.mandarIp,args=(ip,))
		self.hiloServidorOtro.start()
		self.c = Bob(self.usr,self.ip1,ip) #ponemos la ip que desea conectarse
		self.c.show()
	
	def mandarIp(self,ipconectar):
		server = xmlrpclib.ServerProxy("http://"+ipconectar+":8000",allow_none=True)
		server.setMiIp(self.ip1) #Mandamos nuestra ip al otro usuario
		

	#Encabezados de la tabla Usuario | IP 	
	def header(self,row):						  
		self.tableWidget.setRowCount(row-1)
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