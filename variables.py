"""
Constantes del juego Hundir la flota.

Aquí está todo lo que no cambia durante la partida: el tamaño del tablero,
los barcos, los símbolos y los mensajes. El resto de archivos los importa
desde aquí, así que para cambiar algo (por ejemplo, un tablero de 12 x 12)
basta con tocar este archivo.
"""

# Tablero
TAMANO_TABLERO = 10

# Barcos: nombre y eslora (número de casillas que ocupa cada uno).
# 4 barcos de 1, 3 de 2, 2 de 3 y 1 de 4: en total, 20 casillas.
BARCOS = {
    "lancha_1": 1, "lancha_2": 1, "lancha_3": 1, "lancha_4": 1,
    "destructor_1": 2, "destructor_2": 2, "destructor_3": 2,
    "submarino_1": 3, "submarino_2": 3,
    "acorazado": 4,
}
TOTAL_CASILLAS_BARCOS = sum(BARCOS.values())

# Orientaciones para colocar los barcos: cuánto cambian la fila y la columna
# en cada paso. N sube una fila, S baja una, E avanza una columna a la
# derecha y O una a la izquierda.
ORIENTACIONES = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "O": (0, -1)}

# Semilla para los números aleatorios. Con None cada partida es distinta.
# Para la demo se puede poner un número (por ejemplo, 42) y los barcos
# caerán siempre en el mismo sitio.
SEMILLA = None

# Símbolos del tablero
AGUA = "~"
BARCO = "*"
AGUA_DISPARADA = "·"
TOCADO = "X"

# Nombres de los jugadores
JUGADOR = "jugador"
MAQUINA = "máquina"


# Mensajes para el jugador
INICIO = "¡Bienvenido/a a Hundir la Flota!"

INSTRUCCIONES = (
    "Los barcos se colocan al azar. Tienes 4 barcos de 1 casilla, "
    "3 de 2 casillas, 2 de 3 casillas y 1 de 4 casillas. "
    "En cada turno, escribe la fila y la columna (de 0 a 9) "
    "a la que quieres disparar."
)

ACERTADO = "¡Has acertado! Puedes volver a disparar."
FALLADO = "No has acertado. Le toca al otro jugador."
GANADO = "¡Enhorabuena, has ganado!"
PERDIDO = "Has perdido la partida. ¡Inténtalo de nuevo!"
