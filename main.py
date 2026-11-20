"""
Partida de Hundir la flota contra la máquina.

Se ejecuta desde el terminal con:

    python main.py

Orden de la partida:
1. Bienvenida e instrucciones.
2. Se crean los dos tableros y se colocan los barcos, una sola vez.
3. Bucle de turnos: empieza el jugador. Quien acierta vuelve a disparar;
   quien da en agua pasa el turno al rival.
4. Cuando a un jugador no le quedan barcos, se anuncia el resultado y
   se sale del bucle.
"""

import numpy as np

from clases import Tablero
from funciones import disparo_maquina, mostrar_instrucciones, pedir_coordenadas
from variables import (
    ACERTADO,
    DISPARO_REPETIDO,
    FALLADO,
    GANADO,
    JUGADOR,
    MAQUINA,
    MAQUINA_ACIERTA,
    MAQUINA_FALLA,
    PARTIDA_INTERRUMPIDA,
    PERDIDO,
    SEMILLA,
)


def jugar():
    """Prepara los tableros y ejecuta la partida turno a turno hasta que alguien gana."""
    # Con una semilla fija, los barcos y los disparos de la máquina salen
    # siempre igual. Se usa para preparar la demo (ver SEMILLA en variables.py).
    if SEMILLA is not None:
        np.random.seed(SEMILLA)

    mostrar_instrucciones()

    # Los tableros y los barcos se preparan una sola vez, antes del bucle.
    tablero_jugador = Tablero(JUGADOR)
    tablero_maquina = Tablero(MAQUINA)
    tablero_jugador.colocar_barcos()
    tablero_maquina.colocar_barcos()

    # Indica de quién es el turno. Empieza el jugador.
    turno_del_jugador = True

    while True:
        if turno_del_jugador:
            # Al empezar cada disparo se enseña el tablero propio (para ver
            # qué ha tocado la máquina) y el de la máquina sin barcos (para
            # ver dónde se ha disparado ya).
            tablero_jugador.mostrar()
            tablero_maquina.mostrar(ocultar_barcos=True)

            fila, columna = pedir_coordenadas()
            resultado = tablero_maquina.recibir_disparo(fila, columna)

            if resultado == "repetido":
                # El disparo no cuenta: continue vuelve al principio del
                # bucle sin cambiar de turno y se pide otra coordenada.
                print(DISPARO_REPETIDO)
                continue

            if resultado == "tocado":
                print(ACERTADO)
                if not tablero_maquina.quedan_barcos():
                    tablero_maquina.mostrar()
                    print(GANADO)
                    break
                # Si acierta, el turno sigue siendo del jugador.
                continue

            # Ha dado en agua: pasa el turno a la máquina.
            print(FALLADO)
            turno_del_jugador = False

        else:
            fila, columna = disparo_maquina(tablero_jugador)
            resultado = tablero_jugador.recibir_disparo(fila, columna)

            # La máquina nunca repite casilla, así que el resultado solo
            # puede ser "tocado" o "agua".
            if resultado == "tocado":
                print(MAQUINA_ACIERTA.format(fila, columna))
                if not tablero_jugador.quedan_barcos():
                    tablero_jugador.mostrar()
                    print(PERDIDO)
                    break
                # Si acierta, la máquina sigue disparando.
            else:
                print(MAQUINA_FALLA.format(fila, columna))
                turno_del_jugador = True


if __name__ == "__main__":
    # Si el jugador cierra la partida con Ctrl+C (KeyboardInterrupt) o se
    # cierra la entrada (EOFError), se despide en vez de enseñar un error.
    try:
        jugar()
    except (KeyboardInterrupt, EOFError):
        print()
        print(PARTIDA_INTERRUMPIDA)
