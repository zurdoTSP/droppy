import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5 import QtPrintSupport
import os.path
import padre
import ctypes 
import AESCipher
from colores import bcolors
#Clase	heredada	de	QMainWindow	(Constructor	de	ventanas)
class Lector(QMainWindow):
	#Método	constructor	de	la	clase
	def __init__(self,dx, fich,pad):
		#Iniciar	el	objeto	QMainWindow
		QMainWindow.__init__(self)
		#Cargar	la	configuración	del	archivo	.ui	en	el	objeto
		self.ruta=os.getcwd()+"/icons/"
		uic.loadUi("mainwindow3.ui",self)
		self.clave=AESCipher.AESCipher()
		self.drop=dx
		self.setWindowTitle(fich)
		self.fichero=fich
		self.abrir(self.fichero)
		self.padre=pad

		iconSa=QIcon(self.ruta+'save-icon.png')
		iconL=QIcon(self.ruta+'lista-icon.png')
		iconN=QIcon(self.ruta+'bold.png')
		iconSub=QIcon(self.ruta+'underline.png')
		self.abierto=QIcon(self.ruta+'abierto.png')
		self.cerrado=QIcon(self.ruta+'cerrado.png')
		self.encrip=False

		self.saves.setIcon(iconSa)
		self.negrita.setIcon(iconN)
		self.listaB.setIcon(iconL)
		self.subButton.setIcon(iconSub)
		self.bEncrip.setIcon(self.abierto)
		self.saves.clicked.connect(self.save)
		self.negrita.clicked.connect(self.bold)
		self.listaB.clicked.connect(self.lista)
		self.subButton.clicked.connect(self.subra)
		self.bEncrip.clicked.connect(self.cambiarEncriptador)
		QShortcut(QtGui.QKeySequence("Ctrl+B"), self, self.bold)
		QShortcut(QtGui.QKeySequence("Ctrl+L"), self, self.lista)
		QShortcut(QtGui.QKeySequence("Ctrl+U"), self, self.subra)
		QShortcut(QtGui.QKeySequence("Ctrl+S"), self, self.save)
		QShortcut(QtGui.QKeySequence("Ctrl+F"), self, self.busqueda)
		QShortcut(QtGui.QKeySequence("Ctrl+P"), self, self.imprimir)
	#----------------------------------------------------------------------
	def abrir(self,fich):
		if  fich.endswith(".enc"):
			value,crear= QInputDialog.getText(self, "CONTRASEÑA", "Dame la contraseña con la que cifrarás el fichero:",QLineEdit.Password)
			if crear and value!='':
				x=self.drop.abrirFichero(fich)
				t=str(self.clave.decrypt(value,x),'cp1252')
				self.editor.setText(t)
		else:
			x=str(self.drop.abrirFichero(fich),'cp1252')
			print(type(x))
			#self.directorio.setText(self.drop.abrirFichero(final).decode('UTF-8'))
			self.editor.setText(x)
	#----------------------------------------------------------------------
	def imprimir(self):
		"""
		Función que imprime o convierte a PDF la nota abierta.
		
		"""
		dialog = QtPrintSupport.QPrintDialog()

		if dialog.exec_() == QDialog.Accepted:
			self.editor.document().print_(dialog.printer())
	#----------------------------------------------------------------------

	"""###########################################################

			FUNCIONES DE EDICIÓN DE TEXTO

	###########################################################"""
	def bold(self):
		"""
		Función para poner letras en negrita.
		"""
		if self.editor.fontWeight() == QtGui.QFont.Bold:
			self.editor.setFontWeight(QtGui.QFont.Normal)
		else:
			self.editor.setFontWeight(QtGui.QFont.Bold)
	#----------------------------------------------------------------------
	def lista(self):
		"""
		Función para añadir listas.
		"""
		cursor = self.editor.textCursor()
		cursor.insertList(QtGui.QTextListFormat.ListDisc)
	#----------------------------------------------------------------------
	def subra(self):
		"""
		Función para subrayar texto.
		"""
		state = self.editor.fontUnderline()

		self.editor.setFontUnderline(not state)
	#----------------------------------------------------------------------
	def cambiarH(self):
		"""
		Función para subrayar texto.
		"""
		self.padre.forma()
	#----------------------------------------------------------------------
	def busqueda(self):
		"""
		Función que busca una cadena dentro de la nota.
		
		"""
		value,crear= QInputDialog.getText(self, "Buscar", "Introduce los caracteres a buscar:")
		if crear and value!='':
			self.editor.find(value)
	#----------------------------------------------------------------------
	def cambiarEncriptador(self):
		if(self.encrip==False):
			self.encrip=True
			self.bEncrip.setIcon(self.cerrado)
		else:
			self.encrip=False
			self.bEncrip.setIcon(self.abierto)
		print (self.encrip)
	#----------------------------------------------------------------------
	"""###########################################################

			FUNCIONES DE DROPBOX

	###########################################################"""
	def save(self):
		"""
		Función para salvar el texto editado y subirlo a Dropbox.
		"""

		if self.encrip==True:
			value,crear= QInputDialog.getText(self, "CONTRASEÑA", "Dame la contraseña con la que cifrarás el fichero:",QLineEdit.Password)
			if crear and value!='':
				if not self.fichero.endswith(".enc"):
					self.drop.saveF(self.clave.encrypt(value,self.editor.toHtml()),self.fichero+".enc")
					self.drop.borrarF(self.fichero)
					self.cambiarH()
				else:
					self.drop.saveF(self.clave.encrypt(value,self.editor.toHtml()),self.fichero)
				
		else:
			self.drop.saveF(self.editor.toHtml(),self.fichero)
		print(bcolors.WARNING+"Se ha guardado el fichero"+bcolors.ENDC)
	#----------------------------------------------------------------------			
