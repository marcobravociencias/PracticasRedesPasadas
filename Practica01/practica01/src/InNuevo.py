import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *
from modelo.modelo import fichero


existe = uic.loadUiType("existe.ui")[0]

class Error(QtGui.QMainWindow, existe):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.botonRegresaLogin.clicked.connect(self.salir)

    def salir(self):
        self.hide()
        

exito = uic.loadUiType("exito.ui")[0]

class Exito(QtGui.QMainWindow, exito):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.botonRegresaLogin.clicked.connect(self.salir)

    def salir(self):
        self.hide()

        


main_class = uic.loadUiType("agregaUsuario.ui")[0]
class Nuevo(QMainWindow,main_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.agregaUsser.clicked.connect(self.agregaUsr)
        self.w = None
        self.o = None
        
    
    def agregaUsr(self):
        usuario = str(self.usserNuevoText.text()).replace(' ','')
        password = str(self.passNuevoText.text()).replace(' ','')
        regis = fichero(usuario,password)
        if regis.busca():
            self.w = Exito()
            self.w.show()
        else:
            self.o = Error()
            self.o.show()            
    
    
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