import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5 import QtGui
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
		iconSa=QIcon('save-icon.png')
		iconL=QIcon('lista-icon.png')
		iconN=QIcon('bold.png')
		iconApp=QIcon('app.png')
		self.drop = dr
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
		self.setWindowIcon(iconApp) 
		#self.setStyleSheet("background-color:#0099FF; color: #fff;font-size:bold")
		#self.treeWidget.setStyleSheet("background-color:#0099FF; color: #fff;font-size:bold")
		self.nCarpeta.clicked.connect(self.crearFolder)
		self.saves.clicked.connect(self.save)
		self.negrita.clicked.connect(self.bold)
		self.listaB.clicked.connect(self.lista)
		self.treeWidget.itemDoubleClicked.connect(self.openElement)
		self.formar()
		self.dirCrear=""
		self.nCarpeta.setText("")
		self.nCarpeta.setIcon(iconCar)
		self.nFile.setIcon(iconFil)
		self.saves.setIcon(iconSa)
		self.abierto=""
		self.negrita.setIcon(iconN)
		self.listaB.setIcon(iconL)
		self.negrita.setToolTip('This is an example button')
		self.nFile.clicked.connect(self.crearFich)
		QShortcut(QtGui.QKeySequence("Ctrl+B"), self, self.bold)
		QShortcut(QtGui.QKeySequence("Ctrl+L"), self, self.lista)
		

	def formar(self):

		t=self.drop.listarCarpetas()
		t2=t.getDirectorios()
		hijos=t.getHijos()
		header=QTreeWidgetItem(["Droppy"])
		icon=QIcon('home-icon.png')
		icon2=QIcon('text-plain-icon.png')

		self.treeWidget.setHeaderItem(header) 
		root = QTreeWidgetItem(self.treeWidget, ["dropbox"])
		for i in range(len(t2)):
			q=[]
			q.append(t2[i])
			A = QTreeWidgetItem(root,q)
			A.setIcon(0,icon)
			for j in range(len(hijos)):
				if ("/"+hijos[j].getPadre())==t2[i]:
					q=[]
					q.append(hijos[j].getNombre())
					barA = QTreeWidgetItem(A,q)
					barA.setIcon(0,icon2)

	def crearFolder(self):
		value,crear= QInputDialog.getText(self, "crear archivo", "Nombre de la nueva carpeta:")
		if crear and value!='':
			print('Nombre:', value)
			self.drop.crearCarpeta(value)
			self.treeWidget.clear()
			self.formar()

	def crearFich(self):
		if(self.dirCrear!=""):
			value,crear= QInputDialog.getText(self, "crear archivo", "Nombre del nuevo fichero:")
			if crear and value!='':
				if not value.endswith(".writer"):
					value=value+".writer"
				self.drop.archivoMod(value,self.dirCrear)
				self.treeWidget.clear()
				self.formar()
		else:
			print("debes establecer la ruta")
			QMessageBox.warning(self, "WARNING", "Debes establecer una ruta para poder crear un fichero")
		

	def openElement(self):
		item = self.treeWidget.currentItem()
		y=item.parent()
		y=y.text(0)
		n=item.text(0)
		final=y+"/"+n
		if(y=="dropbox"):
			print("ruta establecida ",n)
			self.dirCrear=n
		else:
			self.abierto=final
			x=str(self.drop.abrirFichero(final),'cp1252')
			print(type(x))
			#self.directorio.setText(self.drop.abrirFichero(final).decode('UTF-8'))
			self.directorio.setText(x)
	def save(self):
		self.drop.saveF(self.directorio.toHtml(),self.abierto)
		"""
		filename = QFileDialog.getSaveFileName(self, 'Save File')[0]

		if filename:
			if not filename.endswith(".writer"):
				filename += ".writer"


			with open(filename,"wt") as file:
		"""
          		     # file.write(self.directorio.toHtml())
			
	def bold(self):

		if self.directorio.fontWeight() == QtGui.QFont.Bold:
			self.directorio.setFontWeight(QtGui.QFont.Normal)
		else:
			self.directorio.setFontWeight(QtGui.QFont.Bold)

	def lista(self):
		cursor = self.directorio.textCursor()
		cursor.insertList(QtGui.QTextListFormat.ListDisc)

"""

barA = QTreeWidgetItem(A, ["bar", "i"])
bazA = QTreeWidgetItem(A, ["baz", "a"])

self.treeWidget.setEditTriggers(self.treeWidget.NoEditTriggers)

self.treeWidget.itemDoubleClicked.connect(self.checkEdit)
"""
