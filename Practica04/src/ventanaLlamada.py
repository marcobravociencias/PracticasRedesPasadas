#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *
import pyaudio


main_class = uic.loadUiType("llamada.ui")[0]
class VentanaLlamada(QMainWindow,main_class):
	def __init__(self,parent=None):
		QMainWindow.__init__(self, parent)
		self.setupUi(self)
		