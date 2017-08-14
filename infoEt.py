class InfoEtiquetas:
    def __init__(self,cad):
        self.__lista=[]
        self.__padre=""
        self.__hijo=""
        if(cad!=""):
            self.procesar(cad)


    def procesar(self,cad):
        cadena=cad.split("|")
        self.setRutas(cadena[0])
        for x in cadena[1:]:
            if(x.endswith("\n")):
                x=x.replace("\n","")
            self.__lista.append(x)

    def setRutas(self,cadena):
        cadena=cadena.split("+")
        if(len(cadena)>1):
            self.__padre=cadena[0]
            self.__hijo=cadena[1]

    def getPadre(self):
        return self.__padre

    def getHijo(self):
        return self.__hijo

    def getLista(self):
        return self.__lista
    def setN(self,pa,fi):
        self.__padre=pa
        self.__hijo=fi
    def buscar(self,elemento):
        if(elemento in self.__lista):
            return True
        else:
            return False

    def nuevaE(self,et):
        self.__lista.append(et)
