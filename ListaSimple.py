from NodoSimple import NodoSimple

class ListaSimple:
    def __init__(self):
        self.cabeza=None

    def InsertarSimple(self, nombre, filas, columnas, relleno):
        nuevo = NodoSimple(nombre, filas, columnas, relleno)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            auxiliar = self.cabeza
            while auxiliar.siguiente is not None:
                auxiliar = auxiliar.siguiente
            auxiliar.siguiente = nuevo

    def ImprimirSimple(self):
        auxiliar = self.cabeza
        while auxiliar is not None:
            print(auxiliar.nombre)
            print(auxiliar.relleno.recorrerFilas())
            auxiliar=auxiliar.siguiente

