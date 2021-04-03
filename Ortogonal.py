from ListaEncabezados import ListaEncabezados
from NodoMatriz import Nodo
from EncabezadoMatriz import Encabezado


class Ortogonal:
    def __init__(self):
        self.encaFilas = ListaEncabezados()
        self.encaColumnas = ListaEncabezados()

    def InsertarMatriz(self, fila, columna, valor):
        nuevo = Nodo(fila, columna, valor)

        eFila = self.encaFilas.getEncabezado(fila) #Filas
        if(eFila == None):
            eFila = Encabezado(fila)
            self.encaFilas.Insertar(eFila)
            eFila.acceso = nuevo
        else:
            if(nuevo.columna < eFila.acceso.columna):
                nuevo.derecha = eFila.acceso
                eFila.acceso.izquierda = nuevo
                eFila.acceso = nuevo
            else:
                actual=eFila.acceso
                while(actual.derecha != None):
                    if(nuevo.columna < actual.derecha.columna):
                        nuevo.derecha=actual.derecha
                        actual.derecha.izquierda=nuevo
                        nuevo.izquierda=actual
                        actual.derecha=nuevo
                        break
                    actual=actual.derecha

                if(actual.derecha == None):
                    actual.derecha=nuevo
                    nuevo.izquierda=actual

        eColumna = self.encaColumnas.getEncabezado(columna)  # Columnas
        if (eColumna == None):
            eColumna = Encabezado(columna)
            self.encaColumnas.Insertar(eColumna)
            eColumna.acceso = nuevo
        else:
            if (nuevo.fila < eColumna.acceso.fila):
                nuevo.abajo = eColumna.acceso
                eColumna.acceso.arriba = nuevo
                eColumna.acceso = nuevo
            else:
                actual = eColumna.acceso
                while (actual.abajo != None):
                    if (nuevo.fila < actual.abajo.fila):
                        nuevo.abajo = actual.abajo
                        actual.abajo.arriba = nuevo
                        nuevo.arriba = actual
                        actual.abajo = nuevo
                        break
                    actual = actual.abajo

                if (actual.abajo == None):
                    actual.abajo = nuevo
                    nuevo.arriba = actual

    def recorrerFilas(self):
        eFila=self.encaFilas.cabeza
        print("\nRecorrido por filas: ")

        while(eFila != None):
            actual = eFila.acceso
            while(actual != None):
                print(actual.valor + " en ",end=" ")
                print("Fila: " + str(actual.fila),end="")
                print("| Columna: " + str(actual.columna),end=" ")

                if(eFila.siguiente != None or actual.derecha != None):
                    print("->",end=" ")

                actual=actual.derecha

            eFila=eFila.siguiente

    def recorrerColumnas(self):
        eColumna = self.encaColumnas.cabeza
        print("Recorrido por columnas: ")

        while (eColumna != None):
            actual = eColumna.acceso
            while (actual != None):
                print(actual.valor,end="")

                if (eColumna.siguiente != None or actual.abajo != None):
                    print("->",end="")

                actual = actual.abajo

            eColumna = eColumna.siguiente




