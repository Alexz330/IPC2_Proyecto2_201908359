import tkinter 
from tkinter import *
from tkinter import filedialog as fd
import xml.etree.ElementTree as ET
from ListaEncabezados import ListaEncabezados
from MatrizOrtogonal import MatrizOrtogonal
from Lista import *
from tkinter import ttk
from datetime import datetime
import webbrowser
import time


reporte = ""

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
        operaciones.add_command(label="1. Rotaciones horizontal", command=self.rotacionH)
        operaciones.add_command(label="2. Rotaciones vertical", command=self.rotacionV)
        operaciones.add_command(label="3. Transpuesta" , command=self.transpuesta)
        operaciones.add_command(label="4. Limpiar", command = self.limpiar)
        operaciones.add_command(label="5. Agregar linea horizontal")
        operaciones.add_command(label="6. Agragar linea vertical")
        operaciones.add_command(label="7. Agregar rectangulo", command = self.agregarRectangulo)
        operaciones.add_command(label="8. Agregar triangulo rectangulo")
        operaciones.add_command(label="9. Union", command= self.Union)
        operaciones.add_command(label="10. interseccion", command= self.iterseccion)


        reportes.add_command(label="1. reporte", command= self.reporte)

        ayuda.add_command(label="1. datos estudiante", command=self.datospersonales)
        ayuda.add_command(label="2. documentacion", command=self.pdf)

        Graficar_btn = Button(self, text= "graficar" ,command=self.graficarMatriz)
        Graficar_btn.pack()
        Graficar_btn.place(x= 1000, y= 20)

    def fichero(self):
        global lista
        global espacios_llenos
        global espacios_vacios
        global reporte
        global f
        global vacias
        global llenas

        
        self.archivo=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("Archivo xml","*.xml"),("todos los archivos","*.*")))
        print(self.archivo)
        self.tree = ET.parse(self.archivo)
        self.root = self.tree.getroot()

        reporte = ""
        lista = Lista()
        vacias = []
        llenas = []        
        for valores in self.root:
            columna = 0
            fila = 0

            
            matriz = MatrizOrtogonal()
            espacios_llenos =0
            espacios_vacios = 0
            for datos in valores:
                
                if datos.tag == "imagen":
                    for simbolo in datos.text:
                        if simbolo == "*":
                            espacios_llenos +=1

                            matriz.InsertarMatriz(fila,columna , simbolo)
                            
                            columna +=1
                            
                            
                        elif simbolo == "-":
                            espacios_vacios +=1
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

            llenas.append(espacios_llenos)
            vacias.append(espacios_vacios)
        

        #combo box
        self.NombreMatriz = StringVar()
        self.combo = ttk.Combobox(self, width = 15, textvariable= self.NombreMatriz)
        self.combo['values'] = lista.ObtenerMatriz()  
          
        self.combo.place(x= 1000, y = 300)
        self.label = ttk.Label(self, text = "selecciona la matriz: ")
        self.label.place(x= 1000, y = 250)


        self.NombreMatriz1 = StringVar()
        self.combo1 = ttk.Combobox(self, width = 15, textvariable= self.NombreMatriz1)
        self.combo1['values'] = lista.ObtenerMatriz()  
          
        self.combo1.place(x= 1200, y = 300)
        self.label1 = ttk.Label(self, text = "selecciona la matriz: ")
        self.label1.place(x= 1200, y = 250)
        
    def rotacionH(self):
        global lista
        global reporte

        x = lista.buscar(self.NombreMatriz.get())
        matriz1 = MatrizOrtogonal()
        filas = int(x.filas)
        columnas = int(x.columnas)
        
        matriz1.GMatriz(columnas)
        for fila in range(filas):
            print("")
            for columna in range(columnas):
                matriz1.InsertarMatriz(fila+1, columna, str(x.matriz.obtenerPorFilaYColumna(fila+1, columnas-1 - columna)))
        print("Matriz nueva")
        matriz1.GMatriz(columnas)

        # self.Lmatrizh = ttk.Label(self, text = "Matriz Rotada horizontal")
        # self.Lmatrizh.place(x= 410, y = 4)
        self.imagenL1 = PhotoImage(file = "S.png")
        self.lblImagen1 = Label(self, image = self.imagenL1)
      
        self.lblImagen1.place(x=400, y=20)
        now=time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
        reporte = reporte + "<p>  Accion: rotacion horizontal: -" + x.nombre + " " + str(now) + " -</p>"

    def rotacionV(self):
        global lista
        global reporte

        x = lista.buscar(self.NombreMatriz.get())
        
        matrizV = MatrizOrtogonal()
        filas = int(x.filas)
        columnas = int(x.columnas)

        for fila in range(filas):
            print("")
            for columna in range(columnas):
                matrizV.InsertarMatriz(fila+1, columna, str(x.matriz.obtenerPorFilaYColumna(filas - fila, columna)))
        
        matrizV.GMatriz(columnas)
        
        # self.LmatrizV = ttk.Label(self, text = "Matriz Rotada vertical")
        # self.LmatrizV.place(x= 410, y = 4, width=100, height=10)
        self.imagenL2 = PhotoImage(file = "S.png")
        self.lblImagen2 = Label(self, image = self.imagenL2)
      
        self.lblImagen2.place(x=400, y=20)

        now=time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
        reporte = reporte + "<p>  Accion: rotacion vertical: -" + x.nombre + " " + str(now) + " -</p>"
    def transpuesta(self):
        global lista
        global reporte
        x = lista.buscar(self.NombreMatriz.get())
        x.matriz.recorrerFilas()
        matrizTranspuesta = MatrizOrtogonal()
        filas = int(x.filas)
        columnas = int(x.columnas)

        for fila in range(filas):
            print("")
            for columna in range(columnas):
                matrizTranspuesta.InsertarMatriz(columna,fila+1 , str(x.matriz.obtenerPorFilaYColumna(fila+1, columna)))

        matrizTranspuesta.GMatriz(columnas)

        # self.Lmatrizh = ttk.Label(self, text = "Matriz Transpuesta")
        # self.Lmatrizh.place(x= 410, y = 4,  width=100, height=10)
        self.imagenL3 = PhotoImage(file = "S.png")
        self.lblImagen3 = Label(self, image = self.imagenL3)
      
        self.lblImagen3.place(x=400, y=20)

        now=time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
        reporte = reporte + "<p>  Accion: Transpuesta: -" + x.nombre + " " + str(now) + " -</p>"
    def limpiar(self):
        
        global cordenadax1
        global cordenaday1
        global cordenadax2
        global cordenaday2 

        
       
        self.label2 = ttk.Label(self, text = "Introducir coordenadas")

        cordenadax1 = ttk.Entry(self, width=10)
        cordenadax1.place(x=50, y=600)

        cordenaday1 = ttk.Entry(self,width=10)
        cordenaday1.place(x=100, y=600)

        cordenadax2 = ttk.Entry(self, width=10)
        cordenadax2.place(x=200, y=600)

        cordenaday2 = ttk.Entry(self, width=10)
        cordenaday2.place(x=250, y=600)

        Aceptar_Btn = Button(self, text= "limpiar" ,command=self.btnLimpiar)
        Aceptar_Btn.pack()
        Aceptar_Btn.place(x= 300, y= 650)
        
    def btnLimpiar(self):
        global lista
        global cordenadax1
        global cordenaday1
        global cordenadax2
        global cordenaday2 
        global reporte


        x = lista.buscar(self.NombreMatriz.get())
        x.matriz.recorrerFilas()
        matrizBorrar = MatrizOrtogonal()
        filas = int(x.filas)
        columnas = int(x.columnas)

        for fila in range(filas):
            print("")
            for columna in range(columnas):
                if(fila>=int(cordenadax1.get()) and fila<=int(cordenadax2.get()) and columna>=int(cordenaday1.get()) and columna<=int(cordenaday2.get())):
                    matrizBorrar.InsertarMatriz(fila+1,columna , " ")
                else:
                    matrizBorrar.InsertarMatriz(fila+1,columna , str(x.matriz.obtenerPorFilaYColumna(fila+1, columna)))
        matrizBorrar.GMatriz(columnas)


        # self.Lmatrizl = ttk.Label(self, text = "Matriz Limpiar")
        # self.Lmatrizl.place(x= 410, y = 4)
        self.imagenL4 = PhotoImage(file = "S.png")
        self.lblImagen4 = Label(self, image = self.imagenL4)
      
        self.lblImagen4.place(x=400, y=20)

        now=time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
        reporte = reporte + "<p>  Accion: limpiar: -" + x.nombre + " " + str(now) + " -</p>"

    def agregarLineaH(self):
        pass

    def agregarLineaV(self):
        pass

    def agregarRectangulo(self):
         
        global cordenadaxx1
        global cordenadaxx2
        global cordenadayy1
        global cordenadayy2
        
       
        self.label3 = ttk.Label(self, text = "Introducir coordenadas")

        cordenadaxx1 = ttk.Entry(self, width=10)
        cordenadaxx1.place(x=50, y=50)

        cordenadayy1 = ttk.Entry(self,width=10)
        cordenadayy1.place(x=100, y=50)

        cordenadaxx2 = ttk.Entry(self, width=10)
        cordenadaxx2.place(x=200, y=50)

        cordenadayy2 = ttk.Entry(self,width=10)
        cordenadayy2.place(x=250, y=50)

        

        Aceptar_Btn = Button(self, text= "rectangulo" ,command=self.btnRectangulo)
        Aceptar_Btn.pack()
        Aceptar_Btn.place(x= 500, y= 350)
        
    def btnRectangulo(self):
        global lista
        global cordenadaxx1
        global cordenadaxx2
        global cordenadayy1
        global cordenadayy2
        global reporte


        x = lista.buscar(self.NombreMatriz.get())
        x.matriz.recorrerFilas()
        matrizAgregarCuadrado = MatrizOrtogonal()
        filas = int(x.filas)
        columnas = int(x.columnas)

        for fila in range(filas):
            print("")
            
            for columna in range(columnas):
                
                if(fila>int(cordenadaxx1.get()) and fila<int(cordenadaxx2.get()) and columna>int(cordenadayy1.get()) and columna<int(cordenadayy2.get())):
                    matrizAgregarCuadrado.InsertarMatriz(fila+1,columna , "*")
                else:
                    matrizAgregarCuadrado.InsertarMatriz(fila+1,columna , str(x.matriz.obtenerPorFilaYColumna(fila+1, columna)))
        matrizAgregarCuadrado.GMatriz() 

        now=time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
        reporte = reporte + "<p>  Accion: agregar rectangulo: -" + x.nombre + " " + str(now) + " -</p>"

    def agregarTringunlo(self):


        pass

    def graficarMatriz(self):
        x = lista.buscar(self.NombreMatriz.get())
        columnas = int(x.columnas)
        x.matriz.GMatriz(columnas)
        

        self.Lmatriz = ttk.Label(self, text = "Imagen seleccionada")
        self.Lmatriz.place(x= 25, y = 1)

        self.Lmatriz1 = ttk.Label(self, text = "Imagen Modificada")
        self.Lmatriz1.place(x= 410, y = 4)
        self.imagenL = PhotoImage(file = "S.png")
        self.lblImagen = Label(self, image = self.imagenL)
      
        self.lblImagen.place(x=20, y=20)

    def Union(self):
        global lista
        global reporte
        x = lista.buscar(self.NombreMatriz.get())
        y = lista.buscar(self.NombreMatriz1.get())
        filas = int(x.filas)
        columnas = int(x.columnas)
        matrizSuma = MatrizOrtogonal()

        for fila in range(filas):
            print("")
            for columna in range(columnas):
                val1 = str(x.matriz.obtenerPorFilaYColumna(fila+1, columna))
                val2 = str(y.matriz.obtenerPorFilaYColumna(fila+1, columna))
                if(val1 == "*" or val2 == "*"):
                    matrizSuma.InsertarMatriz(fila+1,columna , "*")
                else:
                    matrizSuma.InsertarMatriz(fila+1,columna , " ")

        matrizSuma.GMatriz(columnas)

        # self.Lmatriz1 = ttk.Label(self, text = "Matriz unida")
        # self.Lmatriz1.place(x= 410, y = 4)

        self.imagenL5 = PhotoImage(file = "S.png")
        self.lblImagen5 = Label(self, image = self.imagenL5)
      
        self.lblImagen5.place(x=400, y=20)

        now=time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
        reporte = reporte + "<p>  Accion: union: -" + x.nombre + " a " +y.nombre +" "+ str(now) + " -</p>"

    def iterseccion(self):
        global reporte
        global lista

        x = lista.buscar(self.NombreMatriz.get())
        y = lista.buscar(self.NombreMatriz1.get())
        filas = int(x.filas)
        columnas = int(x.columnas)
        matrizInterseccion= MatrizOrtogonal()


        for fila in range(filas):
            print("")
            for columna in range(columnas):
                val1 = str(x.matriz.obtenerPorFilaYColumna(fila+1, columna))
                val2 = str(y.matriz.obtenerPorFilaYColumna(fila+1, columna))
                if(val1 == "*" and val2 == "*"):
                    matrizInterseccion.InsertarMatriz(fila+1,columna , "*")
                else:
                    matrizInterseccion.InsertarMatriz(fila+1,columna , " ")
        
        matrizInterseccion.GMatriz(columnas)

        self.imagenL6 = PhotoImage(file = "S.png")
        self.lblImagen6 = Label(self, image = self.imagenL6)
      
        self.lblImagen6.place(x=400, y=20)

        now=time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
        reporte = reporte + "<p>  Accion: union: -" + x.nombre + " a " +y.nombre + " " + str(now) + " -</p>"

    def reporte(self):
        import time
        global lista
        global espacios_llenos
        global espacios_vacios
        global reporte
        global llenas
        global vacias
        global f

        f = open('reporte.html','w')
        f.write('<html>\n')
    
        f.write("""
        <head>
        <link rel="stylesheet" href="estilo.css">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
        <meta charset="utf-8"/>
        </head>
        """)
        f.write('<body>\n')
        f.write('<h1>logs</h1>\n')

        f.write('<h2>Matrices cargadas</h2>\n')
        f.write('<table class="table">\n' )
        f.write('<thead class="thead-light">\n')
        f.write('<tr>\n')
        th = """ 
            <th scope="col">nombre</th>
            <th scope="col">fecha</th>
            <th scope="col">espacios vacios</th>
            <th scope="col">espacios llenos</th>
            
            """
        f.write(th)
        f.write('</tr>\n')
        f.write('</thead>\n')       

        f.write('<tbody>')
        cont = 0
        for w in lista.ObtenerMatriz():
            
            f.write('<tr>\n')
            f.write('   <th>'+ str(w) +'</th>\n')
            now=time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
            f.write('<th>'+ now +'</th>\n')
            
            f.write('<th>'+ str(vacias[cont]) +'</th>\n')
            f.write('<th>'+ str(llenas[cont]) +'</th>\n')

            
            f.write('</tr>\n')
            cont += 1

        f.write('</tbody>')
        f.write('</table>\n' )



      
        f.write('<h2>Acciones</h2>')

        f.write(reporte)
        
        f.write('</body>\n')
        f.write('</html>\n')
        f.close()
       
        webbrowser.open_new_tab('reporte.html')

    def datospersonales(self):
        f = open('datos.html','w')
        f.write('<html>\n')
    
        f.write("""
        <head>
        <link rel="stylesheet" href="estilo.css">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
        <meta charset="utf-8"/>
        </head>
        """)
        f.write('<body>\n')
        f.write('<h1>Datos estudiante</h1>\n')

    
        f.write('<table class="table">\n' )
        f.write('<thead class="thead-light">\n')
        f.write('<tr>\n')
        th = """ 
            <th scope="col">nombre</th>
            <th scope="col">apellido</th>
            <th scope="col">carnet</th>
            <th scope="col">seccion</th>
            
            """
        f.write(th)
        f.write('</tr>\n')
        f.write('</thead>\n')       

        f.write('<tbody>')
       
       
            
        f.write('<tr>\n')
        f.write('<th>Alexis Marco Tulio </th>\n')
        f.write('<th>Lopez Cacoj</th>\n')
        f.write('<th>201908359</th>\n')
        f.write('<th>E</th>\n')
           
    
            
        f.write('</tr>\n')
            

        f.write('</tbody>')
        f.write('</table>\n' )


        
        f.write('</body>\n')
        f.write('</html>\n')
        f.close()
       
        webbrowser.open_new_tab('datos.html')

    def pdf(self):
         webbrowser.open_new_tab('documentacion.pdf')

        
if __name__ == '__main__':
    ventana = Tk()
    ventana.geometry("1500x720")
    app = Window(ventana)
    ventana.mainloop()  







