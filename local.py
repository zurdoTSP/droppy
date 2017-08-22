import os
from os import listdir
from colores import bcolors
import padre
class Local:
	"""
	Clase encargada de interacturar con el almacenamiento interno de nuestro dispositivo.
	"""
	def __init__(self):
		"""
		Constructor
		"""
		self.__ruta=os.getcwd()+"/notas"
	#----------------------------------------------------------------------
	def crearCarpeta(self,nombre):
		"""
		Función encargada de crear carpetas.
		Parámetros:
		nombre -- nombre de la carpeta.
		"""
		os.mkdir(self.__ruta+"/"+nombre)
	#----------------------------------------------------------------------
	def crearCarpetaInicio(self):
		"""
		Función que crea la carpeta donde se almacenarán las notas.
		"""
		os.mkdir(os.getcwd()+"/notas")
	#----------------------------------------------------------------------
	def crearFichero(self,nombre,carpeta, texto):
		"""
		Función que crea o sobrescribe un fichero añadiendo el texto indicado.
		Parámetros:
		nombre -- nombre del fichero.
		carpeta -- nombre de la carpeta.
		texto -- texto que se añadirá al fichero.
		"""
		f = open(self.__ruta+"/"+carpeta+"/"+nombre,'w')
		mensaje = texto
		f.write(mensaje)
		f.close()
	#----------------------------------------------------------------------
	def crearFicheroInial(self):
		"""
		Función que crea el fichero inicial de etiquetas.
		"""
		f = open(self.__ruta+"/"+"notas.txt",'w')
		f.close()
	#----------------------------------------------------------------------
	def volcar(self,cad):
		"""
		Función que vuelca la información de etiquetas ene l correspondiente fichero.
		Parámetros:
		cad -- información de etiquetas.
		"""
		f = open(self.__ruta+"/"+"notas.txt",'w')
		f.write(cad)
		f.close()
	#----------------------------------------------------------------------
	def crearFicheroU(self,fich, texto):
		"""
		Función que crea o sobrescribe un fichero añadiendo el texto indicado.
		Parámetros:
		fich -- ruta del fichero.
		texto -- texto que se añadirá al fichero.
		"""
		f = open(self.__ruta+fich,'w')
		mensaje = texto
		f.write(mensaje)
		f.close()
	#----------------------------------------------------------------------
	def crearFicheroUE(self,fich, texto):
		"""
		Función que crea o sobrescribe un fichero binario añadiendo el texto indicado.
		Parámetros:
		fich -- ruta del fichero.
		texto -- texto que se añadirá al fichero.
		"""
		f = open(self.__ruta+fich,'wb')
		mensaje = texto
		f.write(mensaje)
		f.close()
	#----------------------------------------------------------------------
	def leerFichero(self,entrada):
		"""
		Función que devuelve el contenido del fichero indicado.

		Parámetros:
		entrada -- ruta del fichero.

		Salida:
		x -- contenido del fichero.
		"""
		ObjFichero = open(self.__ruta+entrada)
		x=ObjFichero.read()
		ObjFichero.close()
		return x
	#----------------------------------------------------------------------
	def listar(self):
		"""
		Función lista la carpeta y ficheros existentes.

		Salida:
		a -- lista de tipo Padre que contiene las carpetas y ficheros.
		"""

		a=[]
		for carpeta in listdir(self.__ruta):
			print(bcolors.nuevo+carpeta+bcolors.ENDC)
			p=padre.Padre("/"+carpeta)
			if(not carpeta=="notas.txt"):
				for fichero in listdir(self.__ruta+"/"+carpeta):
					p.setHijo("/"+fichero)
					print("\t"+bcolors.morado+fichero+bcolors.ENDC)
				a.append(p)
		return a
	#----------------------------------------------------------------------
	def eliminarFichero(self,fic):
		"""
		Función que elimina el fichero indicado.

		Parámetros:
		fic -- ruta del fichero.

		"""
		os.remove(self.__ruta+fic)
	#----------------------------------------------------------------------
	def eliminarCarpeta(self, carpeta):
		"""
		Función que elimina la carpeta indicada.

		Parámetros:
		carpeta -- nombre de la carpeta.

		"""
		os.removedirs(self.__ruta+carpeta)
	#----------------------------------------------------------------------
	def leerFicheroL(self,entrada):
		"""
		Función que procesa el contenido el fichero de etiquetas.

		Parámetros:
		entrada -- texto que procesa.

		Salida:
		lista -- lista de cadenas filtradas.
		"""
		ObjFichero = open(self.__ruta+entrada)
		lista=[]
		for x in ObjFichero:
			if(x!="" or x!="+"):
				lista.append(x)
		ObjFichero.close()
		return lista
