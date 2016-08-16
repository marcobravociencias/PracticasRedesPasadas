import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *
from Interchat import Chat
import xmlrpclib



main_class = uic.loadUiType("login.ui")[0]
class Ventana(QMainWindow,main_class):
	def __init__(self, parent=None):
		QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.boton_login.clicked.connect(self.OK)
				
 
	def OK(self):
		usuario = str(self.text_usser.toPlainText()).replace(' ','')
		ip1 = str(self.text_ip1.toPlainText()).replace(' ','')
		ip2 = str(self.text_ip2.toPlainText()).replace(' ','')
		#abrir otra interfaz
		#self.c = Chat(usuario,ip)
		self.c = Chat()
		#self.c.gets(usuario,ip1,ip2)
		self.c.gets('Marco','192.168.13.91','192.168.13.98')
		self.c.show()
		self.hide()

						  
	
class App(QApplication):
	def __init__(self, *args):
		QApplication.__init__(self, *args)
		self.main = Ventana()
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