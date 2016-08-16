from modelo import fichero
import sys
from PyQt4 import QtCore, QtGui, uic
 
# Cargar nuestro archivo .ui
form_class = uic.loadUiType("noRegis.ui")[0]
 
class MyWindowClass(QtGui.QMainWindow, form_class):
 def __init__(self, parent=None):
  QtGui.QMainWindow.__init__(self, parent)
  self.setupUi(self)
  self.botonRegresaLogin.clicked.connect(self.botonRegresaLogin_clicked)
  
 
 
 # Evento del boton de login
 def botonRegresaLogin_clicked(self):
 	print "picaste el boton"
 	#cerrar la ventana



app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()