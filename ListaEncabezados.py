from EncabezadoMatriz import Encabezado

class ListaEncabezados:
    def __init__(self):
        self.cabeza=None

    def Insertar(self, valor):

        if(self.cabeza == None):
            self.cabeza=valor
        else:
            if(valor.id < self.cabeza.id):
                valor.siguiente=self.cabeza
                self.cabeza.anterior=valor
                self.cabeza=valor
            else:
                actual=self.cabeza
                while(actual.siguiente != None):
                    if(valor.id < actual.siguiente.id):
                        valor.siguiente = actual.siguiente
                        actual.siguiente.anterior = valor
                        valor.anterior = actual
                        actual.siguiente = valor
                        break
                    actual=actual.siguiente

                if(actual.siguiente == None):
                    actual.siguiente=valor
                    valor.anterior=actual



    def getEncabezado(self, valor):
        auxiliar = self.cabeza
        while auxiliar != None:
            if auxiliar.id == valor:
                return auxiliar
            auxiliar = auxiliar.siguiente
        return None

