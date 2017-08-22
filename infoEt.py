class InfoEtiquetas:
	"""
	Clase encargada de almacenar la información de los ficheros y sus etiquetas.
	"""
	def __init__(self,cad):
		"""
		constructor
		"""
		self.__lista=[]
		self.__padre=""
		self.__hijo=""
		if(cad!=""):
			self.procesar(cad)
	#----------------------------------------------------------------------
	def procesar(self,cad):
		"""
		Función que extrae la información necesaria de una cadena para su posterior trabajo.
		Encargada de extraer las etiquetas.
		Parámetros:
		cad --  cadena de la que se extrae información..
		"""
		cadena=cad.split("|")
		self.setRutas(cadena[0])
		for x in cadena[1:]:
			if(x.endswith("\n")):
				x=x.replace("\n","")
			self.__lista.append(x)
	#----------------------------------------------------------------------
	def setRutas(self,cadena):
		""""
		Función complementaria a la anterior, extrae la carpeta y el nombre del fichero.
		Parámetros:
		cadena -- cadena de la que se extrae información.
		"""
		cadena=cadena.split("+")
		if(len(cadena)>1):
			self.__padre=cadena[0]
			self.__hijo=cadena[1]
	#----------------------------------------------------------------------
	def getPadre(self):
		"""
		Función que devuelve la variable privada __padre.
		"""
		return self.__padre
	#----------------------------------------------------------------------
	def getHijo(self):
		"""
		Función que devuelve la variable privada __hijo.
		"""
		return self.__hijo
	#----------------------------------------------------------------------
	def getLista(self):
		"""
		Función que devuelve la variable privada __lista.
		"""
		return self.__lista
	#----------------------------------------------------------------------
	def setN(self,pa,fi):
		"""
		Función que crea un nuevo contenedor de etiquetas.

		Parámetros:
		pa -- carpeta contenedora.
		fi -- fichero al que se le relaciona la etiqueta.

		"""
		self.__padre=pa
		self.__hijo=fi
	#----------------------------------------------------------------------
	def buscar(self,elemento):
		"""
		Función que indica si la etiqueta entrante esta relacionada al fichero de la clase.

		Parámetros:
		elemento -- etiqueta que se va a buscar.

		"""
		if(elemento in self.__lista):
			return True
		else:
			return False
	#----------------------------------------------------------------------
	def nuevaE(self,et):
		"""
		Función que añade una nueva etiqueta.
		Parámetros:
		et -- etiqueta que se va a añadir.
		"""
		self.__lista.append(et)
