#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Convierte temperaturas
# www.pythondiario.com
from modelo import fichero
import sys
from PyQt4 import QtCore, QtGui, uic
 
# Cargar nuestro archivo .ui
form_class = uic.loadUiType("login.ui")[0]
 
class MyWindowClass(QtGui.QMainWindow, form_class):
 def __init__(self, parent=None):
  QtGui.QMainWindow.__init__(self, parent)
  self.setupUi(self)
  self.botonLogin.clicked.connect(self.botonLogin_clicked)
  
 
 
 # Evento del boton de login
 def botonLogin_clicked(self):
  usser = str(self.usserLogin.text())
  passw = str(self.passLogin.text())
  print usser + passw
  if usser == "" or passw == "":
   print "Error"
   #llamada a la ventana de error
  else:
   print "No Vacio Usser"
   #llamda a la calculadora con el if de el login de la funcion checalogin
   if fichero(usser,passw):
    print "Calculadora"
   else:
    print "Ventana de Error"

app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()