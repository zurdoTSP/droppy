import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5 import QtPrintSupport

#Clase	heredada	de	QMainWindow	(Constructor	de	ventanas)
class Arbol(QMainWindow):
	#Método	constructor	de	la	clase
	def __init__(self,dx):
		#Iniciar	el	objeto	QMainWindow
		QMainWindow.__init__(self)
		#Cargar	la	configuración	del	archivo	.ui	en	el	objeto
		uic.loadUi("mainwindow2.ui",self)
		self.drop=dx
		self.setWindowTitle("Cambiando	el	título	de	la	ventana")
#		iconCar=QIcon(ruta+'New-Folder-icon.png')
#		iconFil=QIcon(ruta+'nfile.png')
#		iconBor=QIcon(ruta+'papelera.png')
		
		self.carpetas.itemClicked.connect(self.hijos)
		self.forma()
		
	def forma(self):
		iconCar=QIcon('New-Folder-icon.png')
		self.directorio=self.drop.listarCarpetas()
		for x in self.directorio:
			item=QListWidgetItem(x.getNombre())
			item.setIcon(iconCar)
			self.carpetas.addItem(item)

	def hijos(self):
		self.ficheros.clear()
		iconCar=QIcon('text-plain-icon.png')
		x=self.carpetas.currentItem().text()
		for i in self.directorio:
			if x==i.getNombre():
				for j in i.getHijo():	
					item=QListWidgetItem(j)
					item.setIcon(iconCar)
					self.ficheros.addItem(item)
		print(x)
		

