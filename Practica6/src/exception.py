#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *
import pyaudio


main_class = uic.loadUiType("exception.ui")[0]
class Chat(QMainWindow,main_class):
	def __init__(self,mensaje,parent="chatLlamadas.ui"):
		QMainWindow.__init__(self, parent)
		self.setupUi(self)

	def setTexto(self,mensaje):
		self.msj.insertPlainText(mensaje) #interfaz
		
	def close(self):
		self.hide()