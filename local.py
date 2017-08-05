import os
from os import listdir
from colores import bcolors
import padre
class Local:
	def __init__(self):
		self.__ruta=os.getcwd()+"/notas"
	def crearCarpeta(self,nombre):
		os.mkdir(self.__ruta+"/"+nombre)

	def crearCarpetaInicio(self):
		os.mkdir(os.getcwd()+"/notas")

	def crearFichero(self,nombre,carpeta, texto):
		f = open(self.__ruta+"/"+carpeta+"/"+nombre,'w')
		mensaje = texto
		f.write(mensaje)
		f.close()
	def crearFicheroU(self,fich, texto):
		f = open(self.__ruta+fich,'w')
		mensaje = texto
		f.write(mensaje)
		f.close()

	def crearFicheroUE(self,fich, texto):
		f = open(self.__ruta+fich,'wb')
		mensaje = texto
		f.write(mensaje)
		f.close()

	def leerFichero(self,entrada):
		ObjFichero = open(self.__ruta+entrada)
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

	def eliminarFichero(self,fic):
		os.remove(self.__ruta+fic)

	def eliminarCarpeta(self, carpeta):
		os.removedirs(self.__ruta+carpeta)
