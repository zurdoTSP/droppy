import os
from os import listdir
from colores import bcolors
import padre
class Local:
	def __init__(self,ruta):
		self.__ruta=ruta
	def crearCarpeta(self,nombre):
		os.mkdir(self.__ruta+"/"+nombre)

	def crearFichero(self,nombre,carpeta, texto):
		f = open(self.__ruta+"/"+carpeta+"/"+nombre,'w')
		mensaje = texto
		f.write(mensaje)
		f.close()

	def leerFichero(self,nombre,carpeta):
		ObjFichero = open(self.__ruta+"/"+carpeta+"/"+nombre)
		x=ObjFichero.read()
		ObjFichero.close()
		return x

	def listar(self):
		"""
		for base, dirs, files in os.walk(self.__ruta):
			print(fie)
		"""
		a=[]
		for carpeta in listdir(self.__ruta):
			print(bcolors.nuevo+carpeta+bcolors.ENDC)
			p=padre.Padre("/"+carpeta)
			for fichero in listdir(self.__ruta+"/"+carpeta):
				p.setHijo("/"+fichero)
				print("\t"+bcolors.morado+fichero+bcolors.ENDC)
			a.append(p)
		return a

	def eliminarFichero(self, carpeta, nombre):
		os.remove(self.__ruta+carpeta+nombre)

	def eliminarCarpeta(self, carpeta):
		os.remove(self.__ruta+carpeta)
