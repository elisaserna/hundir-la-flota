"""
Clase Tablero del juego Hundir la flota.

Cada jugador (nosotros y la máquina) tiene su propio objeto Tablero.
Un tablero guarda dos arrays de NumPy del mismo tamaño:

- tablero: los barcos del jugador y los disparos que ha recibido.
  Es lo que ve el propio jugador al imprimir su tablero.
- disparos: solo los disparos recibidos, sin barcos.
  Es lo que ve el rival, para que no sepa dónde están los barcos.

Todas las constantes (tamaño, barcos, símbolos y orientaciones)
vienen de variables.py: en este archivo no hay ningún valor escrito a mano.
"""

import numpy as np

from variables import (
    AGUA,
    AGUA_DISPARADA,
    BARCO,
    BARCOS,
    ORIENTACIONES,
    TAMANO_TABLERO,
    TOCADO,
)


class Tablero:
    """
    Tablero de juego de un jugador.

    Attributes:
        id_jugador (str): Identificador del jugador, por ejemplo "jugador" o "máquina".
        tamano (int): Lado del tablero (tamano x tamano).
        barcos (dict): Nombre de cada barco y su eslora (número de casillas).
        tablero (np.ndarray): Barcos del jugador y disparos recibidos.
        disparos (np.ndarray): Solo los disparos recibidos, sin barcos.
    """

    def __init__(self, id_jugador, tamano=TAMANO_TABLERO, barcos=BARCOS):
        """
        Crea un tablero vacío: todas las casillas son agua.

        Los barcos no se colocan aquí, sino al llamar a colocar_barcos().
        Así main.py decide cuándo se colocan y se puede probar la clase
        con el tablero vacío.

        Args:
            id_jugador (str): Identificador del jugador.
            tamano (int, optional): Lado del tablero. Por defecto, TAMANO_TABLERO.
            barcos (dict, optional): Barcos que hay que colocar. Por defecto, BARCOS.
        """
        self.id_jugador = id_jugador
        self.tamano = tamano
        self.barcos = barcos

        # np.full crea un array de tamano x tamano con todas las casillas
        # rellenas con el mismo valor, en este caso el símbolo de agua.
        self.tablero = np.full((tamano, tamano), AGUA)
        self.disparos = np.full((tamano, tamano), AGUA)

    def _casillas_barco(self, fila, columna, orientacion, eslora):
        """
        Calcula las casillas que ocuparía un barco.

        Parte de la casilla de inicio y avanza en la dirección de la
        orientación tantas casillas como mide el barco. Ejemplo: un barco
        de eslora 3 que empieza en (5, 5) con orientación N ocupa
        (5, 5), (4, 5) y (3, 5).

        Este método solo calcula coordenadas: no comprueba si caben
        ni modifica el tablero.

        Args:
            fila (int): Fila de la casilla de inicio.
            columna (int): Columna de la casilla de inicio.
            orientacion (str): "N", "S", "E" u "O".
            eslora (int): Número de casillas del barco.

        Returns:
            list[tuple[int, int]]: Coordenadas (fila, columna) de cada casilla del barco.
        """
        # ORIENTACIONES dice cuánto se mueve la fila y la columna en cada paso.
        # Por ejemplo, N es (-1, 0): cada casilla está una fila más arriba.
        paso_fila, paso_columna = ORIENTACIONES[orientacion]

        casillas = []
        for i in range(eslora):
            casillas.append((fila + i * paso_fila, columna + i * paso_columna))
        return casillas

    def _cabe_barco(self, casillas):
        """
        Comprueba si un barco se puede colocar en esas casillas.

        Args:
            casillas (list[tuple[int, int]]): Casillas que ocuparía el barco.

        Returns:
            bool: True si todas las casillas están dentro del tablero y libres.
        """
        for fila, columna in casillas:
            # Primero se mira que la casilla esté dentro del tablero y solo
            # después se lee el array. El orden importa: en NumPy un índice
            # negativo no da error, sino que cuenta desde el final
            # (tablero[-1, 0] es la última fila). Sin esta comprobación,
            # un barco que se sale por arriba aparecería por abajo.
            if not (0 <= fila < self.tamano and 0 <= columna < self.tamano):
                return False

            # La casilla ya la ocupa otro barco.
            if self.tablero[fila, columna] == BARCO:
                return False

        return True

    def colocar_barcos(self):
        """
        Coloca todos los barcos en posiciones aleatorias.

        Para cada barco se elige al azar una casilla de inicio y una
        orientación (N, S, E u O). Si el barco se sale del tablero o pisa
        otro barco, se descarta ese intento y se prueba otra posición,
        hasta encontrar una en la que cabe. No hace falta dejar agua
        entre barcos.

        Usa np.random, así que llamando antes a np.random.seed() con el
        mismo número los barcos caen siempre en el mismo sitio (útil
        para la demo).
        """
        for eslora in self.barcos.values():
            # Se repite hasta encontrar una posición válida. En un tablero
            # de 10 x 10 con 20 casillas de barco siempre hay sitio, así
            # que el bucle termina en pocos intentos.
            while True:
                fila = np.random.randint(self.tamano)
                columna = np.random.randint(self.tamano)
                orientacion = np.random.choice(list(ORIENTACIONES))

                casillas = self._casillas_barco(fila, columna, orientacion, eslora)
                if self._cabe_barco(casillas):
                    break

            # Solo se escribe en el tablero cuando el barco entero cabe.
            # Si se marcaran las casillas una a una antes de comprobarlo,
            # un intento fallido dejaría trozos de barco sueltos.
            for fila_barco, columna_barco in casillas:
                self.tablero[fila_barco, columna_barco] = BARCO

    def recibir_disparo(self, fila, columna):
        """
        Procesa un disparo en la casilla (fila, columna).

        Marca el resultado en los dos arrays: en tablero, para que el
        jugador vea qué le han tocado, y en disparos, para que el rival
        vea dónde ha disparado ya.

        La coordenada tiene que llegar ya validada (dentro del tablero).
        Esa validación la hace funciones.py al pedir la coordenada.

        Args:
            fila (int): Fila del disparo, de 0 a tamano - 1.
            columna (int): Columna del disparo, de 0 a tamano - 1.

        Returns:
            str: "tocado", "agua" o "repetido".
        """
        # El array disparos solo cambia cuando se dispara, así que si la
        # casilla ya no es agua es que ya se había disparado ahí.
        # Se comprueba primero para que un disparo repetido no cuente.
        if self.disparos[fila, columna] != AGUA:
            return "repetido"

        if self.tablero[fila, columna] == BARCO:
            self.tablero[fila, columna] = TOCADO
            self.disparos[fila, columna] = TOCADO
            return "tocado"

        self.tablero[fila, columna] = AGUA_DISPARADA
        self.disparos[fila, columna] = AGUA_DISPARADA
        return "agua"

    def quedan_barcos(self):
        """
        Indica si al jugador le queda alguna casilla de barco sin tocar.

        Es la forma de saber si la partida ha terminado: con 20 casillas
        de barco es como tener 20 vidas, y cuando no queda ninguna el
        jugador ha perdido. No hace falta una clase Barco.

        Returns:
            bool: True si queda al menos una casilla de barco sin tocar.
        """
        # self.tablero == BARCO da un array de True/False del mismo tamaño;
        # np.any devuelve True si hay al menos un True.
        return bool(np.any(self.tablero == BARCO))

    def mostrar(self, ocultar_barcos=False):
        """
        Imprime el tablero con los números de fila y columna.

        Args:
            ocultar_barcos (bool, optional): Si es True, imprime el array
                disparos, que no tiene barcos. Es la opción que se usa con
                el tablero de la máquina. Por defecto, False.
        """
        casillas = self.disparos if ocultar_barcos else self.tablero

        print(f"Tablero de {self.id_jugador}")

        # Cabecera con los números de columna: "  0 1 2 3 ..."
        print("  " + " ".join(str(numero) for numero in range(self.tamano)))

        # Cada fila empieza por su número y sigue con sus símbolos.
        for numero_fila, fila in enumerate(casillas):
            print(f"{numero_fila} " + " ".join(fila))
        print()
