import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *
from InCalculadora import VentanaCalculadora
from modelo.modelo import fichero

regisError = uic.loadUiType("regisError.ui")[0]

class Error(QtGui.QMainWindow, regisError):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.botonRegresaLogin.clicked.connect(self.salir)

	def salir(self):
		self.hide()
        

main_class = uic.loadUiType("login.ui")[0]
class Ventana(QMainWindow,main_class):
	def __init__(self, parent=None):
		QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.botonLogin.clicked.connect(self.OK)
		self.w = None
		self.c = None
		
		
 
	def OK(self):
		usuario = str(self.usserLogin.text()).replace(' ','')
		password = str(self.passLogin.text()).replace(' ','')
		log = fichero(usuario,password)
		if log.login():
			#abrir otra interfaz
			self.c = VentanaCalculadora()
			self.c.show()
			self.hide()
		else:
			self.w = Error()
			self.w.show()
						  
	
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