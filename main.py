import tkinter 
from tkinter import *
from tkinter import filedialog as fd
import xml.etree.ElementTree as ET
from ListaEncabezados import ListaEncabezados
from Ortogonal import Ortogonal
from ListaSimple import *

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

       
            

    def fichero(self):
        
        self.archivo=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("Archivo xml","*.xml"),("todos los archivos","*.*")))
        print(self.archivo)
        self.tree = ET.parse(self.archivo)
        self.root = self.tree.getroot()

        
        self.lista = ListaSimple()

       



        for valores in self.root:
            self.columna = 0
            self.fila = -1
            
            matriz = Ortogonal()

            for datos in valores:
                
                if datos.tag == "imagen":
                    for self.simbolo in datos.text:
                        if self.simbolo == "*":
                            
                            matriz.InsertarMatriz(self.fila,self.columna , self.simbolo)
                            self.columna +=1
                            
                            
                        elif self.simbolo == "-":
                            self.columna +=1
                        elif self.simbolo == "\n":
                            self.columna = 0
                            self.fila += 1 
                elif datos.tag == "nombre":
                    nombre = datos.text
                elif datos.tag == "filas":
                    filas = datos.text
                elif datos.tag == "columnas":
                    columnas = datos.text
            self.lista.InsertarSimple(nombre,filas,columnas,matriz)

            
        self.lista.ImprimirSimple()
       
        
        






if __name__ == '__main__':
    ventana = Tk()
    ventana.geometry("400x300")
    app = Window(ventana)
    ventana.mainloop()  







