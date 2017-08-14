import infoEt
import local
class ControlInfo:
    def __init__(self):
        self.__listaD=[]
        self.__listaL=[]

    def separar(self,cad):
        cad=cad.split("\n")
        for x in cad:
            t=infoEt.InfoEtiquetas(x)
            self.__listaD.append(t)

    def leeYSepara(self):
        x=local.Local()
        y=x.leerFicheroL("/notas.txt")
        for n in y:
            t=infoEt.InfoEtiquetas(n)
            self.__listaL.append(t)
            print(t.getHijo())
            print(t.getPadre())

    def buscarL(self, cad):
        final=[]
        for x in self.__listaL:
            if(x.buscar(cad)):
                final.append(x)
                print(x.getHijo(),"los pinguinos")
        return final

    def buscarD(self, cad):
        final=[]
        for x in self.__listaD:
            if(x.buscar(cad)):
                final.append(x)
        return final
    def crearCadenaL(self):
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
                print("tu puta madre")
                cad=cad+i
        return cad
    def nEtiquetaL(self,cad,et):
        for x in self.__listaL:
            print(x.getPadre()+"/"+x.getHijo()+" es igual a "+cad)
            if(x.getPadre()+"/"+x.getHijo()==cad):
                x.nuevaE(et)
    def nuevoL(self,nom,fich):
        t=infoEt.InfoEtiquetas("")
        t.setN(nom,fich)
        self.__listaL.append(t)
