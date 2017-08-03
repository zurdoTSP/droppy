import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5 import QtPrintSupport
import os.path
import padre
import fichero
import ficheroL
import local
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
		self.localM=False
		iconCar=QIcon(self.ruta+'New-Folder-icon.png')
		iconFil=QIcon(self.ruta+'nfile.png')
		iconBor=QIcon(self.ruta+'papelera.png')
		self.iconDrop=QIcon(self.ruta+'apps.png')
		iconApp=QIcon("app.png")
		#########################Barra de menú##########################
		self.systray = QSystemTrayIcon(iconApp, self)
		show_action = QAction("Show", self)
		quit_action = QAction("Exit", self)
		hide_action = QAction("Hide", self)
		show_action.triggered.connect(self.show)
		hide_action.triggered.connect(self.hide)
		quit_action.triggered.connect(qApp.quit)
		tray_menu = QMenu()
		tray_menu.addAction(show_action)
		tray_menu.addAction(hide_action)
		tray_menu.addAction(quit_action)
		self.systray.setContextMenu(tray_menu)
		self.systray.show()
		######################Icono visible dock########################
		self.setWindowIcon(iconApp) 
		################################################################
		self.bCarpeta.setIcon(iconCar)
		self.bFichero.setIcon(iconFil)
		self.bDropb.setIcon(self.iconDrop)
		self.bBorrar.setIcon(iconBor)
		self.carpetas.itemClicked.connect(self.hijos)
		self.ficheros.itemClicked.connect(self.borrarfich)
		self.ficheros.itemDoubleClicked.connect(self.abrir)
		self.forma()
		#self.formaLocal()
		self.boCarpeta=""
		self.boFichero=""
		#Asociar botones a funciones
		self.bCarpeta.clicked.connect(self.crearFolder)
		self.bDropb.clicked.connect(self.cambio)
		self.bFichero.clicked.connect(self.crearFich)
		self.bBorrar.clicked.connect(self.borrar)
		QShortcut(QtGui.QKeySequence("Ctrl+B"), self, self.selectRuta)


	#----------------------------------------------------------------------
	def cambio(self):
		"""
		Función que cambia entre local y Dropbox
		"""
		self.carpetas.clear()
		self.ficheros.clear()
		if self.localM==True:
			self.localM=False
			self.bDropb.setIcon(self.iconDrop)
			self.restablece()
		else:
			iconCar=QIcon(self.ruta+'home-icon.png')
			self.bDropb.setIcon(iconCar)
			self.localM=True
			self.formaLocal()

	#----------------------------------------------------------------------
	def restablece(self):
		"""
		Función que rstablece los valores de Dropbox
		"""
		iconCar=QIcon(self.ruta+'home-icon.png')
		for x in self.directorio:
			item=QListWidgetItem(x.getNombre())
			item.setIcon(iconCar)
			self.carpetas.addItem(item)

	#----------------------------------------------------------------------

	def forma(self):
		"""
		Función que rellena la lista que contiene las carpetas de Dropbox
		"""
		iconCar=QIcon(self.ruta+'home-icon.png')
		self.directorio=self.drop.listarCarpetas()
		for x in self.directorio:
			item=QListWidgetItem(x.getNombre())
			item.setIcon(iconCar)
			self.carpetas.addItem(item)

	#----------------------------------------------------------------------
	def formaLocal(self):
		"""
		Función que rellena la lista que contiene las carpetas locales
		"""
		iconCar=QIcon(self.ruta+'home-iconL.png')
		#self.directorio=self.drop.listarCarpetas()
		self.tlocal=local.Local("/home/zurdotsp/python/local")
		self.lista=self.tlocal.listar()
		for x in self.lista:
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
	#----------------------------------------------------------------------
	def buscarl(self,cad):
		x=0
		t=0
		while(x<len(self.lista)):
			if(self.lista[x].getNombre()==cad):
				t=x
				x=len(self.lista)+1
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
		if self.localM==False:
			x=self.carpetas.currentItem().text()
			self.carpetaActual=x
			self.boCarpeta=x
			n=self.buscar(x)
			for j in self.directorio[n].getHijo():
				item=QListWidgetItem(self.convertir(j))
				item.setIcon(iconCar)
				self.ficheros.addItem(item)
		else:
			x=self.carpetas.currentItem().text()
			self.carpetaActual=x
			self.boCarpeta=x
			n=self.buscarl(x)
			for j in self.lista[n].getHijo():
				item=QListWidgetItem(j)
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
			if self.localM==False:
				print('Nombre:', value)
				self.drop.crearCarpeta(value)
				iconCar=QIcon(self.ruta+'home-icon.png')
				item=QListWidgetItem("/"+value)
				item.setIcon(iconCar)
				self.carpetas.addItem(item)
				p=padre.Padre("/"+value)
				self.directorio.append(p)
			else:
				print('Nombre:', value)
				
				iconCar=QIcon(self.ruta+'home-iconL.png')
				item=QListWidgetItem("/"+value)
				item.setIcon(iconCar)
				self.carpetas.addItem(item)
				self.tlocal.crearCarpeta(value)

#----------------------------------------------------------------------
	def crearFich(self):
		iconCar=QIcon(self.ruta+'text-plain-icon.png')
		if(self.carpetaActual!=""):
			value,crear= QInputDialog.getText(self, "crear archivo", "Nombre del nuevo fichero:")
			if crear and value!='':
				if not value.endswith(".writer"):
					value=value+".writer"
				if self.localM==False:
					self.drop.archivoMod(value,self.carpetaActual)
					item=QListWidgetItem(value)
					item.setIcon(iconCar)#setHijo
					self.ficheros.addItem(item)
					n=self.buscar(self.carpetaActual)
					print(n)
					self.directorio[n].setHijo(self.carpetaActual+"/"+value)
				else:
					self.tlocal.crearFichero(value,self.carpetaActual,"")
					item=QListWidgetItem(value)
					item.setIcon(iconCar)#setHijo
					self.ficheros.addItem(item)
					n=self.buscarl(self.carpetaActual)
					print(n)
					self.lista[n].setHijo(self.carpetaActual+"/"+value)
		else:
			print("debes establecer la ruta")
			QMessageBox.warning(self, "WARNING", "Debes establecer una ruta para poder crear un fichero")
#----------------------------------------------------------------------

	def borrar(self):
		"""
		Función para crear carpetas en Dropbox.
		"""
		if(self.boCarpeta!=""):
			self.drop.borrarF(self.boCarpeta)
			self.carpetas.clear()
			self.ficheros.clear()
			self.forma()
		else:
			if(self.boFichero==""):
				QMessageBox.warning(self, "WARNING", "Debes seleccionar una carpeta o un fichero")
			else:
				self.drop.borrarF(self.boFichero)
				self.carpetas.clear()
				self.ficheros.clear()
				self.forma()
				
#----------------------------------------------------------------------
	def borrarfich(self):
		print(self.boCarpeta+" se anula y ")
		self.boFichero=self.boCarpeta+"/"+self.ficheros.currentItem().text()
		self.boCarpeta=""
		print(self.boFichero)
#----------------------------------------------------------------------
	def abrir(self):
		if self.localM==False:
			x=self.ficheros.currentItem().text()
			self.ventana2=fichero.Lector(self.drop,self.carpetaActual+"/"+x,self)
			self.ventana2.show()
		else:
			x=self.ficheros.currentItem().text()
			print(self.carpetaActual+x+" zurdinio")
			self.ventana3=ficheroL.Lector("/home/zurdotsp/python/local",self.carpetaActual+x)
			self.ventana3.show()
	def ChildRemoved(self,event):
		print("hola")

	def contextMenuEvent(self, event):  
		menu = QMenu(self)
		quitAction = menu.addAction("Quit")
		action = menu.exec_(self.mapToGlobal(event.pos()))
		if action == quitAction:
			qApp.quit()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	def selectRuta(self):
		file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
		print(file)
