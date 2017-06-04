import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5 import QtPrintSupport
import os.path
#Clase	heredada	de	QMainWindow	(Constructor	de	ventanas)
class Arbol(QMainWindow):
	#Método	constructor	de	la	clase
	def __init__(self,dx):
		#Iniciar	el	objeto	QMainWindow
		QMainWindow.__init__(self)
		#Cargar	la	configuración	del	archivo	.ui	en	el	objeto
		self.ruta=os.getcwd()+"/icons/"
		uic.loadUi("mainwindow2.ui",self)
		self.carpetaActual=""
		self.drop=dx
		self.setWindowTitle("Droppy")
		iconCar=QIcon(self.ruta+'New-Folder-icon.png')
		iconFil=QIcon(self.ruta+'nfile.png')
		iconBor=QIcon(self.ruta+'papelera.png')
		self.bCarpeta.setIcon(iconCar)
		self.bFichero.setIcon(iconFil)
		self.bBorrar.setIcon(iconBor)
		self.carpetas.itemClicked.connect(self.hijos)
		self.forma()
		#Asociar botones a funciones
		self.bCarpeta.clicked.connect(self.crearFolder)
	#----------------------------------------------------------------------

	def forma(self):
		"""
		Función que rellena la lista que contiene las carpetas
		"""
		iconCar=QIcon(self.ruta+'home-icon.png')
		self.directorio=self.drop.listarCarpetas()
		for x in self.directorio:
			item=QListWidgetItem(x.getNombre())
			item.setIcon(iconCar)
			self.carpetas.addItem(item)

		#----------------------------------------------------------------------
	def buscar(self,cad):
		x=0
		t=0
		while(x<len(self.directorio)):
			if(self.directorio[x].getNombre()==cad):
				t=x
				x=len(self.directorio)+1
			else:
				x=x+1
		return t
	#---------------------------------------------------------------------

	def hijos(self):
		"""
		Función que rellena el arbol de ficheros según su carpeta contenedora
		"""
		self.ficheros.clear()
		iconCar=QIcon(self.ruta+'text-plain-icon.png')
		x=self.carpetas.currentItem().text()
		self.carpetaActual=x
		n=self.buscar(x)
		for j in self.directorio[n].getHijo():
			item=QListWidgetItem(self.convertir(j))
			item.setIcon(iconCar)
			self.ficheros.addItem(item)

		#----------------------------------------------------------------------
	def convertir(self,cad):
		"""
		Función que elimina el directorio de la cadena de los hijos
		"""
		lista=cad.split('/')
		return(lista[2])
		print(x)
		def fname(arg):
			pass
#----------------------------------------------------------------------

	def crearFolder(self):
		"""
		Función para crear carpetas en Dropbox.
		"""
		value,crear= QInputDialog.getText(self, "crear archivo", "Nombre de la nueva carpeta:")
		if crear and value!='':
			print('Nombre:', value)
			self.drop.crearCarpeta(value)
			iconCar=QIcon(self.ruta+'home-icon.png')
			item=QListWidgetItem("/"+value)
			item.setIcon(iconCar)
			self.carpetas.addItem(item)
#----------------------------------------------------------------------
