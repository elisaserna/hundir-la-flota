# Clase Tablero del juego Hundir la flota.

import numpy as np

from variables import AGUA, BARCO, TOCADO, AGUA_DISPARADA, BARCOS, TAMANO_TABLERO, ORIENTACIONES

class Tablero:

    def __init__(self, id_jugador):
        self.id_jugador = id_jugador
        self.tamano = TAMANO_TABLERO
        self.barcos = BARCOS
        self.tablero = np.full((self.tamano, self.tamano), AGUA)
        self.disparos = np.full((self.tamano, self.tamano), AGUA)

    def colocar_barcos(self):
        for eslora in self.barcos.values():
            while True:
                fila = np.random.randint(self.tamano)
                columna = np.random.randint(self.tamano)
                orientacion = np.random.choice(list(ORIENTACIONES))
                paso_fila, paso_columna = ORIENTACIONES[orientacion]

                casillas = []
                for i in range(eslora):
                    casillas.append((fila + i * paso_fila, columna + i * paso_columna))

                cabe = True
                for f, c in casillas:
                    if not (0 <= f < self.tamano and 0 <= c < self.tamano):
                        cabe = False
                    elif self.tablero[f, c] == BARCO:
                        cabe = False

                if cabe:
                    break

            for f, c in casillas:
                self.tablero[f, c] = BARCO

    def recibir_disparo(self, fila, columna):
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
          return bool(np.any(self.tablero == BARCO))

    def mostrar(self, ocultar_barcos=False):
          if ocultar_barcos:
              casillas = self.disparos
          else:
              casillas = self.tablero

          print("Tablero de", self.id_jugador)
          print("  " + " ".join(str(n) for n in range(self.tamano)))
          for numero_fila, fila in enumerate(casillas):
              print(numero_fila, " ".join(fila))
          print()
