import tkinter 
from tkinter import *
from tkinter import filedialog as fd
import xml.etree.ElementTree as ET
from ListaEncabezados import ListaEncabezados
from MatrizOrtogonal import MatrizOrtogonal
from Lista import *
from tkinter import ttk



class Window(Frame):

    def __init__(self, master=None):       
        Frame.__init__(self, master)      
        self.master = master
        self.inicio_window()
        
    def inicio_window(self):
        self.master.title("Proyecto 2")
        self.pack(fill=BOTH, expand=1)

        
        #menu
        menu = Menu(self.master)
        self.master.config(menu=menu)
       

        cargarArchivo = Menu(menu, tearoff=0)
        operaciones = Menu(menu, tearoff=0)
        reportes = Menu(menu, tearoff=0 )
        ayuda = Menu(menu, tearoff=0)



        menu.add_cascade(label="Cargar Archivo", menu=cargarArchivo)
        menu.add_cascade(label="Operaciones", menu=operaciones)
        menu.add_cascade(label="Reportes", menu=reportes)
        menu.add_cascade(label="Ayuda", menu=ayuda)


        #menu--comandos cargar archivo
        cargarArchivo.add_command(label="Abrir", command= self.fichero)
        cargarArchivo.add_separator()
        cargarArchivo.add_command(label="Salir", command=self.master.quit)


        #menu--comandos operaciones
        operaciones.add_command(label="1. Rotaciones horizontal")
        operaciones.add_command(label="2. Rotaciones vertical")
        operaciones.add_command(label="3. Transpuesta")
        operaciones.add_command(label="4. Limpiar")
        operaciones.add_command(label="5. Agregar linea horizontal")
        operaciones.add_command(label="6. Agragar linea vertical")
        operaciones.add_command(label="7. Agregar rectangulo")
        operaciones.add_command(label="8. Agregar triangulo rectangulo")

       
            
    def aceptar(self):
        global lista
        
        x = lista.buscar(self.NombreMatriz.get())
        y = lista.buscar("Matriz_2")
        x.matriz.recorrerFilas()
        matrizNueva = MatrizOrtogonal()
        matrizNuevaNueva = MatrizOrtogonal()
        matrizTranspuesta = MatrizOrtogonal()
        matrizBorrar = MatrizOrtogonal()
        matrizSuma = MatrizOrtogonal()
        matrizInterseccion = MatrizOrtogonal()
        matrizAgregarCuadrado = MatrizOrtogonal()



        print("\n ")
        filas = int(x.filas)
        columnas = int(x.columnas)
        for fila in range(filas):
            print("")
            for columna in range(columnas):
                matrizNueva.InsertarMatriz(fila+1, columna, str(x.matriz.obtenerPorFilaYColumna(fila+1, columnas-1 - columna)))
        
        for fila in range(filas):
            print("")
            for columna in range(columnas):
                matrizNuevaNueva.InsertarMatriz(fila+1, columna, str(x.matriz.obtenerPorFilaYColumna(filas - fila, columna)))
        
        for fila in range(filas):
            print("")
            for columna in range(columnas):
                matrizTranspuesta.InsertarMatriz(columna,fila+1 , str(x.matriz.obtenerPorFilaYColumna(fila+1, columna)))
        
        for fila in range(filas):
            print("")
            for columna in range(columnas):
                if(fila>=1 and fila<=3 and columna>=1 and columna<=3):
                    matrizBorrar.InsertarMatriz(fila+1,columna , " ")
                else:
                    matrizBorrar.InsertarMatriz(fila+1,columna , str(x.matriz.obtenerPorFilaYColumna(fila+1, columna)))

        for fila in range(filas):
            print("")
            for columna in range(columnas):
                val1 = str(x.matriz.obtenerPorFilaYColumna(fila+1, columna))
                val2 = str(y.matriz.obtenerPorFilaYColumna(fila+1, columna))
                if(val1 == "*" or val2 == "*"):
                    matrizSuma.InsertarMatriz(fila+1,columna , "*")
                else:
                    matrizSuma.InsertarMatriz(fila+1,columna , " ")

        for fila in range(filas):
            print("")
            for columna in range(columnas):
                val1 = str(x.matriz.obtenerPorFilaYColumna(fila+1, columna))
                val2 = str(y.matriz.obtenerPorFilaYColumna(fila+1, columna))
                if(val1 == "*" and val2 == "*"):
                    matrizInterseccion.InsertarMatriz(fila+1,columna , "*")
                else:
                    matrizInterseccion.InsertarMatriz(fila+1,columna , " ")
                    
        for fila in range(filas):
            print("")
            for columna in range(columnas):
                if((fila==1 or fila==1+8) or (columna==0 or columna==1+8)):
                    matrizAgregarCuadrado.InsertarMatriz(fila+1,columna , "*")
                else:
                    matrizAgregarCuadrado.InsertarMatriz(fila+1,columna , str(x.matriz.obtenerPorFilaYColumna(fila+1, columna)))

        print("")
        print("")
        print("Matriz nueva")
        matrizNueva.recorrerFilas()

        print("")
        print("")
        print("Matriz nueva nueva")
        matrizNuevaNueva.recorrerFilas()

        print("")
        print("")
        print("Matriz transpuesta")
        matrizTranspuesta.recorrerFilas()

        matrizBorrar.recorrerFilas()
        matrizSuma.recorrerFilas()
        matrizInterseccion.recorrerFilas()
        matrizAgregarCuadrado.recorrerFilas()

    def fichero(self):
        global lista
        
        self.archivo=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("Archivo xml","*.xml"),("todos los archivos","*.*")))
        print(self.archivo)
        self.tree = ET.parse(self.archivo)
        self.root = self.tree.getroot()

        
        lista = Lista()

        for valores in self.root:
            columna = 0
            fila = 0
            
            matriz = MatrizOrtogonal()

            for datos in valores:
                
                if datos.tag == "imagen":
                    for simbolo in datos.text:
                        if simbolo == "*":
                            
                            matriz.InsertarMatriz(fila,columna , simbolo)
                            columna +=1
                            
                            
                        elif simbolo == "-":
                            matriz.InsertarMatriz(fila,columna , " ")
                            columna +=1
                        elif simbolo == "\n":
                            columna = 0
                            fila += 1 
                elif datos.tag == "nombre":
                    nombre = datos.text
                elif datos.tag == "filas":
                    filas = datos.text
                elif datos.tag == "columnas":
                    columnas = datos.text
            lista.InsertarSimple(nombre,filas,columnas,matriz)

            
        

        #combo box

        self.NombreMatriz = StringVar()
        self.combo = ttk.Combobox(self, width = 15, textvariable= self.NombreMatriz)
        self.combo['values'] = lista.ObtenerMatriz()
        self.combo.place(x= 150, y = 20)
        self.label = ttk.Label(self, text = "selecciona la matriz: ")
        self.label.place(x= 125, y = 0)

        
        #botones
        Aceptar_Btn = Button(self, text= "Aceptar" ,command=self.aceptar)
        Aceptar_Btn.pack()
        Aceptar_Btn.place(x= 500, y= 350)

        
    




if __name__ == '__main__':
    ventana = Tk()
    ventana.geometry("500x700")
    app = Window(ventana)
    ventana.mainloop()  







