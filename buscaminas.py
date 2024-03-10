import random

# Constantes para los estados de las celdas
MINA = '*'
CASILLA_CERRADA = '-'
CASILLA_ABIERTA = ' '

# Clase para el tablero de Buscaminas
class TableroBuscaminas:
    def __init__(self, filas, columnas, minas):
        self.filas = filas
        self.columnas = columnas
        self.minas = minas
        self.tablero = self._inicializar_tablero()  # Método privado

    # Método estático para crear un tablero con dimensiones personalizadas
    @staticmethod
    def crear_tablero_personalizado(filas, columnas, minas):
        return TableroBuscaminas(filas, columnas, minas)

    def _inicializar_tablero(self):  # Método privado
        tablero = [[CASILLA_CERRADA for _ in range(self.columnas)] for _ in range(self.filas)]

        # Colocar minas aleatorias
        for _ in range(self.minas):
            fila, columna = random.randint(0, self.filas - 1), random.randint(0, self.columnas - 1)
            while tablero[fila][columna] == MINA:
                fila, columna = random.randint(0, self.filas - 1), random.randint(0, self.columnas - 1)
            tablero[fila][columna] = MINA

        return tablero

    def imprimir_tablero(self, mostrar_minas=False):
        for fila in self.tablero:
            for celda in fila:
                if celda == MINA and not mostrar_minas:
                    print(CASILLA_CERRADA, end=' ')
                else:
                    print(celda, end=' ')
            print()

    def contar_minas_alrededor(self, fila, columna):
        minas_cercanas = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                nueva_fila, nueva_columna = fila + i, columna + j
                if 0 <= nueva_fila < self.filas and 0 <= nueva_columna < self.columnas and self.tablero[nueva_fila][nueva_columna] == MINA:
                    minas_cercanas += 1
        return minas_cercanas

    def abrir_celda(self, fila, columna):
        if self.tablero[fila][columna] == MINA:
            return False  # Perdió
        elif self.tablero[fila][columna] == CASILLA_ABIERTA:
            return True  # Ya abierta
        else:
            minas_cercanas = self.contar_minas_alrededor(fila, columna)
            self.tablero[fila][columna] = CASILLA_ABIERTA if minas_cercanas == 0 else str(minas_cercanas)

            if minas_cercanas == 0:
                # Expandir en las direcciones si no hay minas cercanas
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        nueva_fila, nueva_columna = fila + i, columna + j
                        if 0 <= nueva_fila < self.filas and 0 <= nueva_columna < self.columnas:
                            self.abrir_celda(nueva_fila, nueva_columna)

            return True

# Clase heredada para agregar funcionalidades específicas de Buscaminas
class Buscaminas(TableroBuscaminas):
    def __init__(self, filas, columnas, minas):
        super().__init__(filas, columnas, minas)
        self.jugando = True

    def jugar(self):
        while self.jugando:
            self.imprimir_tablero()
            fila = int(input('Ingresa la fila (0 a {}): '.format(self.filas - 1)))
            columna = int(input('Ingresa la columna (0 a {}): '.format(self.columnas - 1)))

            if not (0 <= fila < self.filas) or not (0 <= columna < self.columnas):
                print('Coordenadas inválidas. Inténtalo de nuevo.')
                continue

            if not self.abrir_celda(fila, columna):
                self.imprimir_tablero(mostrar_minas=True)
                print('¡Perdiste! Se encontró una mina.')
                self.jugando = False

            if all(all(celda == MINA or celda == CASILLA_ABIERTA for celda in fila) for fila in self.tablero):
                self.imprimir_tablero(mostrar_minas=True)
                print('¡Ganaste! Has abierto todas las celdas sin encontrar minas.')
                self.jugando = False


    # Método de representación de cadena
    def __str__(self):
        return f"Buscaminas - Filas: {self.filas}, Columnas: {self.columnas}, Minas: {self.minas}"

if __name__ == '__main__':
    #Comprención de listas con condiciones
    filas = [f for f in range(6) if f % 1 == 0]
    
    #Comprención de diccionarios
    configuracion = {'filas': len(filas), 'columnas': 6, 'minas': 8}  # Se corrige aquí
    
    #Comprención de conjuntos
    conjunto_filas = {f for f in filas}
    
    #Empaquetamiento de variable
    dimensiones = (len(filas), 6)
    
    #Asignación múltiple
    filas, columnas = dimensiones
    
    #Desempaquetamiento en argumentos de funciones
    juego = Buscaminas(*dimensiones, 8)
    
    #Desempaquetamiento extendido
    juego_otro = Buscaminas(**configuracion)
    
    #Usar enumerate para comprención de listas
    lista_numerada = [f"{i}: {' '.join(map(str, fila))}" for i, fila in enumerate(juego.tablero) if i % 2 == 0]

    #Métodos estático
    tablero_personalizado = TableroBuscaminas.crear_tablero_personalizado(6, 6, 8)
    
    #Herencia múltiple
    juego.jugar()
    
    #Método de representación de cadenas
    print(juego)