# Hundir la flota

Versión de Hundir la flota en Python para jugar contra la máquina desde el terminal. Team Challenge del Sprint 3 del bootcamp de Data Science de The Bridge.

## Instalación

Hace falta Python 3 y NumPy. Desde la carpeta del proyecto:

```bash
python -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Cómo se ejecuta

```bash
python main.py
```

## Cómo se juega

- Cada jugador (tú y la máquina) tiene un tablero de 10 x 10.
- Los barcos se colocan al azar: 4 de 1 casilla, 3 de 2, 2 de 3 y 1 de 4. En total, 20 casillas con barco.
- Empiezas tú. En cada turno escribes la fila y la columna a la que disparas, de 0 a 9, separadas por un espacio (por ejemplo, `3 7`).
- Si aciertas, vuelves a disparar. Si das en agua, dispara la máquina, que también repite mientras acierta.
- Gana quien toque primero las 20 casillas de barco del rival.
- Si disparas a una casilla repetida o escribes algo que no es una coordenada, el juego te avisa y te la vuelve a pedir.
- Para salir a mitad de partida, pulsa `Ctrl+C`.

En cada turno ves dos tableros: el tuyo, con tus barcos y los disparos de la máquina, y el de la máquina, solo con tus disparos.

## Símbolos del tablero

| Símbolo | Significado |
|---|---|
| `~` | Agua sin disparar |
| `*` | Barco sin tocar (solo en tu tablero) |
| `·` | Disparo en agua |
| `X` | Barco tocado |

## Estructura

| Archivo | Qué contiene |
|---|---|
| `main.py` | Arranca la partida y lleva el bucle de turnos |
| `clases.py` | Clase `Tablero`: colocar barcos, recibir disparos y mostrar el tablero |
| `funciones.py` | Pedir y validar coordenadas y elegir el disparo de la máquina |
| `variables.py` | Constantes: tamaño, barcos, símbolos y mensajes |
| `requirements.txt` | Dependencias |
| `AI_LOG.md` | Registro del uso de IA |

Todas las constantes están en `variables.py`. Para cambiar el tamaño del tablero o los barcos solo hay que tocar ese archivo.

## Modo demo

Para enseñar una partida completa en poco tiempo, en `variables.py`:

- `SEMILLA = 42` (o cualquier número): los barcos y los disparos de la máquina salen siempre igual.
- Dejar menos barcos en `BARCOS`, por ejemplo solo `"acorazado": 4`.

Antes de subir cambios, hay que volver a dejar `SEMILLA = None` y los barcos originales.
