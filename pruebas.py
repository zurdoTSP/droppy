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
		iconCar=QIcon('New-Folder-icon.png')
		iconFil=QIcon('nfile.png')
		self.drop = dr
		self.setStyleSheet("background-color:#0099FF; color: #fff;font-size:bold")
		self.treeWidget.setStyleSheet("background-color:#0099FF; color: #fff;font-size:bold")
		self.nCarpeta.clicked.connect(self.crearFolder)
		self.treeWidget.itemDoubleClicked.connect(self.openElement)
		self.formar()
		self.dirCrear=""
		self.nCarpeta.setText("")
		self.nCarpeta.setIcon(iconCar)
		self.nFile.setIcon(iconFil)
		self.nFile.clicked.connect(self.crearFich)

	def formar(self):

		t=self.drop.listarCarpetas()
		t2=t.getDirectorios()
		hijos=t.getHijos()
		header=QTreeWidgetItem(["Droppy"])
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

	def crearFolder(self):
		value,crear= QInputDialog.getText(self, "crear archivo", "Nombre del archivo nuevo:")
		if crear and value!='':
			print('Nombre:', value)
			self.drop.crearCarpeta(value)
			self.treeWidget.clear()
			self.formar()

	def crearFich(self):
		self.drop.archivoMod()
		print("mierda")

	def openElement(self):
		item = self.treeWidget.currentItem()
		y=item.parent()
		y=y.text(0)
		n=item.text(0)
		final=y+"/"+n
		if(y=="dropbox"):
			print("ruta establecida")
			self.dirCrear=y
		else:
			self.directorio.setText(self.drop.abrirFichero(final).decode('UTF-8'))
		

"""

barA = QTreeWidgetItem(A, ["bar", "i"])
bazA = QTreeWidgetItem(A, ["baz", "a"])

self.treeWidget.setEditTriggers(self.treeWidget.NoEditTriggers)

self.treeWidget.itemDoubleClicked.connect(self.checkEdit)
"""
