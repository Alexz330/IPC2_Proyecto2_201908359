from NodoSimple import NodoSimple

class Lista:
    def __init__(self):
        self.cabeza=None

    def InsertarSimple(self, nombre, filas, columnas, matriz):
        nuevo = NodoSimple(nombre, filas, columnas, matriz)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            tmp = self.cabeza
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

    def ImprimirSimple(self):
        tmp = self.cabeza
        while tmp is not None:
            print(tmp.nombre)
            print(tmp.matriz.recorrerFilas())
            tmp=tmp.siguiente
    
    def ObtenerMatriz(self):
        nombres =[]
        tmp = self.cabeza 
        while tmp is not None:

            nombres.append(tmp.nombre)
            tmp = tmp.siguiente
        return nombres 

    def buscar(self,nombre):
        
        tmp = self.cabeza 
        while tmp is not None:
            
            if tmp.nombre == nombre:
                return tmp
            tmp = tmp.siguiente
        return None
