class Nodo:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.abajo = None
        self.arriba = None
        self.derecha = None
        self.izquierda = None

