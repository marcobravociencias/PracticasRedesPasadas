from modelo import fichero
import sys
from PyQt4 import QtCore, QtGui, uic
from collections import deque
 
# Cargar nuestro archivo .ui
form_class = uic.loadUiType("calculadora.ui")[0]
cola = list() 
class MyWindowClass(QtGui.QMainWindow, form_class):
 def __init__(self, parent=None):
  QtGui.QMainWindow.__init__(self, parent)
  self.setupUi(self)
  self.boton_0.clicked.connect(self.boton_0_clicked)
  self.boton_1.clicked.connect(self.boton_1_clicked)
  self.boton_2.clicked.connect(self.boton_2_clicked)
  self.boton_3.clicked.connect(self.boton_3_clicked)
  self.boton_4.clicked.connect(self.boton_4_clicked)
  self.boton_5.clicked.connect(self.boton_5_clicked)
  self.boton_6.clicked.connect(self.boton_6_clicked)
  self.boton_7.clicked.connect(self.boton_7_clicked)
  self.boton_8.clicked.connect(self.boton_8_clicked)
  self.boton_9.clicked.connect(self.boton_9_clicked)
  self.boton_sum.clicked.connect(self.boton_sum_clicked)
  self.boton_res.clicked.connect(self.boton_res_clicked)
  self.boton_div.clicked.connect(self.boton_div_clicked)
  self.boton_mul.clicked.connect(self.boton_mul_clicked)
  self.boton_igual.clicked.connect(self.boton_igual_clicked)
  self.boton_punto.clicked.connect(self.boton_punto_clicked)
  self.usserNuevoDespliega.clicked.connect(self.usserNuevoDespliega_clicked)
  
 # Evento de botones
 def boton_0_clicked(self):
  print "picaste el boton cero"
  cola.append(0)
  self.display.setText(str(cola))
 	#Escribir el cero en la pantalla
 def boton_1_clicked(self):
 	print "picaste el boton uno"
 	cola.append(1)
 	self.display.setText(str(cola))
 	#Escribir el cero en la pantalla
 def boton_2_clicked(self):
 	print "picaste el boton dos"
 	cola.append(2)
 	self.display.setText(str(cola))
 	#Escribir el cero en la pantalla
 def boton_3_clicked(self):
 	print "picaste el boton tres"
 	cola.append(3)
 	self.display.setText(str(cola))
 	#Escribir el cero en la pantalla
 def boton_4_clicked(self):
 	print "picaste el boton cuatro"
 	cola.append(4)
 	self.display.setText(str(cola))
 	#Escribir el cero en la pantalla
 def boton_5_clicked(self):
 	print "picaste el boton cinco"
 	cola.append(5)
 	self.display.setText(str(cola))
 	#Escribir el cero en la pantalla
 def boton_6_clicked(self):
 	print "picaste el boton seis"
 	cola.append(6)
 	self.display.setText(str(cola))
 	#Escribir el cero en la pantalla
 def boton_7_clicked(self):
 	print "picaste el boton siete"
 	cola.append(7)
 	self.display.setText(str(cola))
 	#Escribir el cero en la pantalla
 def boton_8_clicked(self):
 	print "picaste el boton ocho"
 	cola.append(8)
 	self.display.setText(str(cola))
 	#Escribir el cero en la pantalla
 def boton_9_clicked(self):
 	print "picaste el boton nueve"
 	cola.append(9)
 	self.display.setText(str(cola))
 	#Escribir el cero en la pantalla
 def boton_sum_clicked(self):
 	print "picaste el boton sum"
 	cola.append("+")
 	self.display.setText(str(cola))
 	#Escribir el cero en la pantalla
 def boton_res_clicked(self):
 	print "picaste el boton red"
 	cola.append("-")
 	self.display.setText(str(cola))
 	#Escribir el cero en la pantalla
 def boton_div_clicked(self):
 	print "picaste el boton div"
 	cola.append("/")
 	self.display.setText(str(cola))
 	#Escribir el cero en la pantalla
 def boton_mul_clicked(self):
 	print "picaste el boton mul"
 	cola.append("*")
 	self.display.setText(str(cola))
 	#Escribir el cero en la pantalla
 def boton_igual_clicked(self):
 	print "picaste el boton igual"
 	#Escribir el cero en la pantalla
 def boton_punto_clicked(self):
 	print "picaste el boton limp"
 	cola.empty()
 	#Escribir el cero en la pantalla

 def usserNuevoDespliega_clicked(self):
 	print "picaste el boton Despliega Nuevo Usuario"
 	#Escribir el cero en la pantalla

app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()