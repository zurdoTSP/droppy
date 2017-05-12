######################################################################## 
class Padre:
	"""Recipiente que recoge un fichero y su directorio padre"""
	def __init__(self,nomb):
		"""Constructor"""
		self.__nombre=nomb
		self.__hijo=[]
	#----------------------------------------------------------------------

	def setNombre(self,dir):
		"""
		Función que modifica el valor de la variable nombre, la cual es el hijo

		Parámetros:
		nombre -- nueva dirección
		
		"""
		self.__nombre=dir

	#----------------------------------------------------------------------
	def getNombre(self):
		"""
		Función que modifica el valor de la variable padre

		Devuelve:
		nombre 
		
		"""
		return self.__nombre

	#----------------------------------------------------------------------
	def setHijo(self,x):
		"""
		Función que añade etiquetas al final
		
		"""
		self.__hijo.append(x)		
	#----------------------------------------------------------------------	
	def getHijo(self):
		"""
		Función que devuelve las etiquetas
		
		"""
		return self.__hijo	
	#----------------------------------------------------------------------		
