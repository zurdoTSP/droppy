import infoEt
import local
class ControlInfo:
    """
    Clase para el control de las etiquetas.
    """
    def __init__(self):
        """
        Constructor.
        """
        self.__listaD=[]
        self.__listaL=[]

    def separar(self,cad):
        """
	    Función separa las cadenas de etiquetas y las transforma en la información pertinente para trabajar con ellas.

		Parámetros:
		cad -- cadena a separar.

		"""
        cad=cad.split("\n")
        for x in cad:
            t=infoEt.InfoEtiquetas(x)
            self.__listaD.append(t)

    def leeYSepara(self,cad):
        """
		Función separa las cadenas de etiquetas y las transforma en la información pertinente para trabajar con ellas
        en modo local y de Dropbox.

		Parámetros:
		cad -- cadena de Dropbox.

		"""
        x=local.Local()
        y=x.leerFicheroL("/notas.txt")
        for n in y:
            t=infoEt.InfoEtiquetas(n)
            self.__listaL.append(t)
            print(t.getHijo())
            print(t.getPadre())
        z=cad
        print(cad)
        y=cad.split("\n")
        if(len(y)>0):
            print(y)
            for z in y:
                t=infoEt.InfoEtiquetas(z)
                self.__listaD.append(t)
                print(t.getHijo())
                print(t.getPadre())

    def buscarL(self, cad):
        """
		Función que busca las etiquetas indicadas en los ficheros y devuelve aquellos que la contienen.

		Parámetros:
		cad -- etiqueta a buscar

        Salida:
        final -- lista de ficheros que contienen la etiqueta.
		"""
        final=[]
        for x in self.__listaL:
            if(x.buscar(cad)):
                final.append(x)
        return final

    def buscarD(self, cad):
        """
		Función que busca las etiquetas indicadas en los ficheros y devuelve aquellos que la contienen.

		Parámetros:
		cad -- etiqueta a buscar

        Salida:
        final -- lista de ficheros que contienen la etiqueta.
		"""
        final=[]
        for x in self.__listaD:
            if(x.buscar(cad)):
                final.append(x)
        return final

    def crearCadenaL(self):
        """
		Función que crea la cadena de información que se almacenará en los ficheros.

        Salida:
        cad -- cadena resultante.
		"""
        cad=""
        cadH=""
        cadI=[]
        for x in self.__listaL:
            cad=cad+x.getPadre()+"+"+x.getHijo()
            for y in x.getLista():
                cadH=cadH+"|"+y
            cad=cad+cadH+"\n"
            cadI.append(cad)
            cadH=""
            cad=""
        for i in cadI:
            if(i!="+\n"and i!="\n"):
                cad=cad+i
        return cad

    def nEtiquetaL(self,cad,et):
        """
		Función añade una nueva etiqueta al lugar indicado.

		Parámetros:
		cad -- ruta del fichero.
        et -- etiqueta a añadir.
		"""
        for x in self.__listaL:
            if(x.getPadre()+"/"+x.getHijo()==cad):
                x.nuevaE(et)

    def nuevoL(self,nom,fich):
        """
		Función añade un nuevo fichero a la lista de etiquetas.

		Parámetros:
		nom -- carpeta que contiene el fichero.
        fich -- nombre del fichero.
		"""
        t=infoEt.InfoEtiquetas("")
        t.setN(nom,fich)
        self.__listaL.append(t)


#####################################################
    def nEtiquetaD(self,cad,et):
        """
		Función añade una nueva etiqueta al lugar indicado.

		Parámetros:
		cad -- ruta del fichero.
        et -- etiqueta a añadir.
		"""
        for x in self.__listaD:
            print(x.getPadre()+"/"+x.getHijo()+" es igual a "+cad)
            if(x.getPadre()+"/"+x.getHijo()==cad):
                x.nuevaE(et)

    def nuevoD(self,nom,fich):
        """
		Función añade un nuevo fichero a la lista de etiquetas.

		Parámetros:
		nom -- carpeta que contiene el fichero.
        fich -- nombre del fichero.
		"""
        t=infoEt.InfoEtiquetas("")
        t.setN(nom,fich)
        self.__listaD.append(t)

    def crearCadenaD(self):
        """
		Función que crea la cadena de información que se almacenará en los ficheros.

        Salida:
        cad -- cadena resultante.
		"""
        cad=""
        cadH=""
        cadI=[]
        for x in self.__listaD:
            cad=cad+x.getPadre()+"+"+x.getHijo()
            for y in x.getLista():
                cadH=cadH+"|"+y
            cad=cad+cadH+"\n"
            cadI.append(cad)
            cadH=""
            cad=""
        for i in cadI:
            if(i!="+\n"and i!="\n"):
                print("tu puta madre")
                cad=cad+i
        return cad
