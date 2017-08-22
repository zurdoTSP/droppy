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
import controlInfo
import padre
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
		self.tlocal=local.Local()
		self.setWindowTitle("Droppy")
		self.localM=False
		iconCar=QIcon(self.ruta+'New-Folder-icon.png')
		iconFil=QIcon(self.ruta+'nfile.png')
		iconBor=QIcon(self.ruta+'papelera.png')
		self.iconDrop=QIcon(self.ruta+'apps.png')
		iconApp=QIcon("app.png")
		self.control=controlInfo.ControlInfo()
		self.directorioP=[]
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
		self.drop.buscar()
		#Asociar botones a funciones
		self.bCarpeta.clicked.connect(self.crearCarpeta)
		self.bDropb.clicked.connect(self.cambio)
		self.bFichero.clicked.connect(self.crearFich)
		self.bBorrar.clicked.connect(self.borrar)
		self.lineEdit.returnPressed.connect(self.filtrar)
		lectura=str(self.drop.abrirFichero("etiquetas.txt"),'cp1252')
		self.control.leeYSepara(lectura)
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
		self.lista=self.tlocal.listar()
		for x in self.lista:
			item=QListWidgetItem(x.getNombre())
			item.setIcon(iconCar)
			self.carpetas.addItem(item)

	#----------------------------------------------------------------------
	def buscar(self,cad):
		"""
		Función que busca la posición en la que se encuentra una carpeta en la lista de Dropbox.

		Parámetros:
		cad -- nombre de la carpeta.

		Salida:
		t -- Posición de la carpeta
		"""
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
		"""
		Función que busca la posición en la que se encuentra una carpeta en la lista de local.

		Parámetros:
		cad -- nombre de la carpeta.

		Salida:
		t -- Posición de la carpeta
		"""
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

			if(len(self.lista)>0):
				for j in self.lista[n].getHijo():
					i=self.transformar(j)
					item=QListWidgetItem(i)
					item.setIcon(iconCar)
					self.ficheros.addItem(item)

		#----------------------------------------------------------------------
	def convertir(self,cad):
		"""
		Función que elimina el directorio de la cadena de los hijos.

		Parámetros:
		cad --  variable a convertir.

		Salida:
		lista -- variable convertida.
		"""
		lista=cad.split('/')
		if(len(lista)>1):
			return(lista[2])
			print(x)
		else:
			return(lista[0])
		def fname(arg):
			pass
#----------------------------------------------------------------------

	def crearCarpeta(self):
		"""
		Función para crear carpetas en Dropbox o local.
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
				self.tlocal.crearCarpeta(value)
				self.carpetas.clear()
				self.ficheros.clear()
				self.formaLocal()

#----------------------------------------------------------------------
	def crearFich(self):
		"""
		Función para crear un fichero dentro de una carpeta en Dropbox o local.
		"""
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
					self.control.nuevoD(self.carpetaActual,value)
				else:
					self.tlocal.crearFichero(value,self.carpetaActual,"")
					item=QListWidgetItem(value)
					item.setIcon(iconCar)#setHijo
					self.ficheros.addItem(item)
					n=self.buscarl(self.carpetaActual)

					self.lista[n].setHijo(self.carpetaActual+"/"+value)
					self.control.nuevoL(self.carpetaActual,value)
		else:
			print("debes establecer la ruta")
			QMessageBox.warning(self, "WARNING", "Debes establecer una ruta para poder crear un fichero")
#----------------------------------------------------------------------

	def borrar(self):
		"""
		Función para borrar carpetas o ficheros en Dropbox o local.
		"""
		if self.localM==False:
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
		else:
			if(self.boCarpeta!=""):
				self.tlocal.eliminarCarpeta(self.boCarpeta)
				self.carpetas.clear()
				self.ficheros.clear()
				self.formaLocal()
			else:
				if(self.boFichero==""):
					QMessageBox.warning(self, "WARNING", "Debes seleccionar una carpeta o un fichero")
				else:
					self.tlocal.eliminarFichero(self.boFichero)
					self.carpetas.clear()
					self.ficheros.clear()
					self.formaLocal()
#----------------------------------------------------------------------
	def borrarfich(self):
		"""
		Función que modifica el valor de una variable para indicar que ese fichero sería borrado en caso de desearlo.
		"""
		print(self.boCarpeta+" se anula y ")
		self.boFichero=self.boCarpeta+"/"+self.ficheros.currentItem().text()
		self.boCarpeta=""
		print(self.boFichero)

#----------------------------------------------------------------------
	def abrir(self):
		"""
		Función que abre en el editor la nota indicada en Dropbox o local.
		"""
		if self.localM==False:
			x=self.ficheros.currentItem().text()
			self.ventana2=fichero.Lector(self.drop,self.carpetaActual+"/"+x,self)
			self.ventana2.show()
		else:
			x=self.ficheros.currentItem().text()

			print(self.carpetaActual+x+" zurdinio")
			self.ventana3=ficheroL.Lector(self.carpetaActual+"/"+x,self)
			self.ventana3.show()

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	def contextMenuEvent(self, event):
		menu = QMenu(self)
		quitAction = menu.addAction("Quit")
		action = menu.exec_(self.mapToGlobal(event.pos()))
		if action == quitAction:
			qApp.quit()

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	def transformar(self,var):
		"""
		Función que adapta una cadena para que el programa funcione correctamente

		Parámetros:
		var --  variable a convertir.

		Salida:
		l -- variable convertida.
		"""
		t=var.split("/")
		if(len(t)>2):
			l=t[2]
		else:
			l=var[1:]
		return l

	def filtrar(self):
		"""
		Función que muestra las carpetas y ficheros que contienen la etiqueta indicada en el buscador.
		También restablece los valores por defecto.
		"""
		lisca=[]
		if self.localM==True:
			x=self.control.buscarL(self.lineEdit.text())
			if(x==[]):
				self.carpetas.clear()
				self.ficheros.clear()
				self.formaLocal()
			else:
				self.lista=[]
				for i in x:
					if(i.getPadre() in lisca):
						for q in self.lista:
							if(q.getNombre()==i.getPadre()):
								q.setHijo("/"+i.getHijo())
					else:
						p=padre.Padre(i.getPadre())
						print(i.getPadre())
						p.setHijo("/"+i.getHijo())
						self.lista.append(p)
					lisca.append(i.getPadre())
				self.carpetas.clear()
				self.ficheros.clear()
				iconCar=QIcon(self.ruta+'home-iconL.png')
				for x in self.lista:
					item=QListWidgetItem(x.getNombre())
					item.setIcon(iconCar)
					self.carpetas.addItem(item)
		else:
			iconCar=QIcon(self.ruta+'home-icon.png')
			x=self.control.buscarD(self.lineEdit.text())
			if(x==[]):
				self.carpetas.clear()
				self.ficheros.clear()
				self.directorio=self.directorioP
				for x in self.directorio:
					item=QListWidgetItem(x.getNombre())
					item.setIcon(iconCar)
					self.carpetas.addItem(item)
			else:
				self.directorioP=self.directorio
				self.directorio=[]
				for i in x:
					if(i.getPadre() in lisca):
						for q in self.directorio:
							if(q.getNombre()==i.getPadre()):
								q.setHijo(i.getHijo())
					else:
						p=padre.Padre(i.getPadre())
						print(i.getPadre())
						p.setHijo(i.getHijo())
						self.directorio.append(p)
					lisca.append(i.getPadre())
				self.carpetas.clear()
				self.ficheros.clear()

				for x in self.directorio:
					item=QListWidgetItem(x.getNombre())
					item.setIcon(iconCar)
					self.carpetas.addItem(item)


	def anadir(self,fich,tipo,nueva):
		"""
		Función que añade una etiqueta a un fichero.

		Parámetros:
		fich -- ruta del fichero.
		tipo -- puede ser lc de local o dx de dropbox, indica a que lista debe añadirlo.
		nueva -- la etiqueta que se va a añadir.

		"""
		if(tipo=="lc"):
			self.control.nEtiquetaL(fich,nueva)
		else:
			self.control.nEtiquetaD(fich,nueva)
		print(self.control.crearCadenaD())


	def closeEvent(self, event):
		"""
		Evento que se activa al cerrar la aplicación, en este caso guardará las etiquetas.

		"""
		x=self.control.crearCadenaL()
		y=self.control.crearCadenaD()
		self.drop.saveF(y,"etiquetas.txt")
		self.tlocal.volcar(x)
