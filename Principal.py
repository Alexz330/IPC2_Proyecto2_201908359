from ListaEncabezados import ListaEncabezados
from Ortogonal import Ortogonal
def Inicio():
    matriz = Ortogonal()
    matriz.InsertarMatriz(1, 0, "silla")
    matriz.InsertarMatriz(2, 1, "arbol")
    matriz.InsertarMatriz(0, 1, "casa")
    matriz.InsertarMatriz(1, 2, "zapato")
    matriz.InsertarMatriz(0, 2, "mesa")
    matriz.InsertarMatriz(0, 0, "avion")

                   
    matriz.recorrerFilas()


Inicio()