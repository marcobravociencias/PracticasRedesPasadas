import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *


main_class = uic.loadUiType("chat.ui")[0]
class Chat(QMainWindow,main_class):
	def __init__(self,espera_mensaje_local,parent=None):
		QMainWindow.__init__(self, parent)
		self.setupUi(self)
		

	def getTexto(self): 				
		msj = str(self.text_send.text())
		return msj

	def setTexto(self,mensaje):
		var = self.texr_recived.toPlainText()
		self.texr_recived.setPlainText(var+'\n'+mensaje) #interfaz
		

		
	
		
