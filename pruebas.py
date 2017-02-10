import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import ctypes 
import completo
import os.path
#Clase heredada de QMainWindow (Constructor de ventanas)


  #Asignar estilos CSS
  #self.setStyleSheet("background-color: #000; color: #fff;")


class MainWindow(QMainWindow):
 #Método constructor de la clase
	def __init__(self,dr):
  #Iniciar el objeto QMainWindow
		QMainWindow.__init__(self)
  #Cargar la configuración del archivo .ui en el objeto
		uic.loadUi("mainwindow2.ui", self)
		self.drop = dr
		self.setStyleSheet("background-color:#0099FF; color: #fff;font-size:bold")
		self.treeWidget.setStyleSheet("background-color:#0099FF; color: #fff;font-size:bold")
		self.formar()

	def formar(self):

		t=self.drop.listarCarpetas()

		t2=t.getDirectorios()
		hijos=t.getHijos()
		header=QTreeWidgetItem(["Tree"])
		#header.setBackgroundColor(0, QtGui.QColor('green'))
		icon=QIcon('home-icon.png')
		icon2=QIcon('text-plain-icon.png')
		self.treeWidget.setHeaderItem(header)   #Another alternative is setHeaderLabels(["Tree","First",...])
		root = QTreeWidgetItem(self.treeWidget, ["dropbox"])
		for i in range(len(t2)):
			q=[]
			q.append(t2[i])
			A = QTreeWidgetItem(root,q)
			A.setIcon(0,icon)
			for j in range(len(hijos)):
				#print(hijos[j].getNombre())
				if ("/"+hijos[j].getPadre())==t2[i]:
					q=[]
					q.append(hijos[j].getNombre())
					barA = QTreeWidgetItem(A,q)
					barA.setIcon(0,icon2)

"""

barA = QTreeWidgetItem(A, ["bar", "i"])
bazA = QTreeWidgetItem(A, ["baz", "a"])

self.treeWidget.setEditTriggers(self.treeWidget.NoEditTriggers)

self.treeWidget.itemDoubleClicked.connect(self.checkEdit)
"""
