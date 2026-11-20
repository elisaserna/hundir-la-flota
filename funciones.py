"""
Funciones auxiliares del juego Hundir la flota.

Aquí está la lógica que no pertenece a un tablero concreto: mostrar las
instrucciones, pedir y validar las coordenadas del jugador y elegir el
disparo de la máquina sin repetir casilla.
"""

import numpy as np

from variables import (
    AGUA,
    BIENVENIDA,
    ERROR_FORMATO,
    ERROR_RANGO,
    INSTRUCCIONES,
    PEDIR_COORDENADAS,
    TAMANO_TABLERO,
)


def mostrar_instrucciones():
    """Imprime el mensaje de bienvenida y las instrucciones del juego."""
    print(BIENVENIDA)
    print()
    print(INSTRUCCIONES)


def convertir_coordenadas(texto, tamano=TAMANO_TABLERO):
    """
    Convierte lo que escribe el jugador en una coordenada (fila, columna).

    Acepta los dos números separados por un espacio o por una coma:
    "3 7", "3,7" y "3, 7" dan (3, 7).

    Esta función no pide nada al jugador ni imprime nada: solo convierte
    o avisa del error. Así se puede probar por separado de input().

    Args:
        texto (str): Lo que ha escrito el jugador.
        tamano (int, optional): Lado del tablero. Por defecto, TAMANO_TABLERO.

    Returns:
        tuple[int, int]: La coordenada (fila, columna).

    Raises:
        ValueError: Si el texto no son dos números enteros o si alguno
            queda fuera del tablero. El mensaje del error es el que se
            enseña al jugador.
    """
    # Las comas se cambian por espacios y split() separa por espacios,
    # ignorando los que sobren: "  3 ,  7 " da ["3", "7"].
    partes = texto.replace(",", " ").split()
    if len(partes) != 2:
        raise ValueError(ERROR_FORMATO)

    # int() lanza ValueError si el texto no es un número entero ("a", "3.5").
    # Se captura y se lanza otro ValueError con un mensaje que entiende el
    # jugador, en vez del mensaje técnico de Python.
    try:
        fila = int(partes[0])
        columna = int(partes[1])
    except ValueError:
        raise ValueError(ERROR_FORMATO)

    if not (0 <= fila < tamano and 0 <= columna < tamano):
        raise ValueError(ERROR_RANGO)

    return fila, columna


def pedir_coordenadas(tamano=TAMANO_TABLERO):
    """
    Pide una coordenada al jugador hasta que escriba una válida.

    Si la entrada no es válida, enseña el motivo y vuelve a pedirla, así
    que el programa nunca se cierra por una entrada mal escrita. El
    disparo repetido no se comprueba aquí, sino en Tablero.recibir_disparo().

    Args:
        tamano (int, optional): Lado del tablero. Por defecto, TAMANO_TABLERO.

    Returns:
        tuple[int, int]: La coordenada (fila, columna) elegida.
    """
    while True:
        texto = input(PEDIR_COORDENADAS)
        try:
            return convertir_coordenadas(texto, tamano)
        except ValueError as error:
            # str(error) es el mensaje que se puso al lanzar el ValueError.
            print(error)


def disparo_maquina(tablero_rival):
    """
    Elige al azar una casilla del rival a la que la máquina no haya disparado.

    En lugar de probar casillas al azar hasta dar con una nueva, se buscan
    primero todas las que siguen sin disparar y se elige una de ellas. Así
    la máquina nunca repite casilla y no hace falta guardar una lista aparte.

    Args:
        tablero_rival (Tablero): Tablero del jugador al que dispara la máquina.

    Returns:
        tuple[int, int]: La coordenada (fila, columna) del disparo.
    """
    # En el array disparos, las casillas que siguen siendo AGUA son las que
    # aún no han recibido ningún disparo. np.argwhere devuelve sus
    # coordenadas, una por fila: [[0, 0], [0, 1], ...].
    casillas_libres = np.argwhere(tablero_rival.disparos == AGUA)

    # Se elige una fila de esa lista al azar.
    fila, columna = casillas_libres[np.random.randint(len(casillas_libres))]

    # int() convierte los enteros de NumPy en enteros normales de Python,
    # para que al imprimirlos salga (3, 7) y no (np.int64(3), np.int64(7)).
    return int(fila), int(columna)
