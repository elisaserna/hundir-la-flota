# hundir-la-flota
Team Challenge del Sprint 03

Equipo: Daniel Vaquerizo, Alvaro Urra, Elisa Serna

### Descripcion
El objetivo es localizar y hundir todos los barcos del tablero enemigo antes de que el rival consiga hundir los nuestros.

El juego cuenta con un tablero de 10x10 casillas en el que se distribuyen diferentes barcos de distintos tamaños. Los jugadores realizan disparos indicando las coordenadas y reciben información sobre si han acertado o fallado.

El proyecto utiliza Python y NumPy para gestionar los datos y el funcionamiento del tablero, aplicando conceptos de programación como variables, estructuras de datos, funciones y lógica de juego.

### Instalaciones
Mirar archivo requirements.txt

## Símbolos del tablero

| Símbolo | Significado |
|---|---|
| `~` | Agua sin disparar |
| `*` | Barco sin tocar (solo en tu tablero) |
| `·` | Disparo en agua |
| `X` | Barco tocado |

### Estructura

| Archivo | Qué contiene |
|---|---|
| `main.py` | Arranca la partida y lleva el bucle de turnos |
| `clases.py` | Clase `Tablero`: colocar barcos, recibir disparos y mostrar el tablero |
| `funciones.py` | Pedir y validar coordenadas y elegir el disparo de la máquina |
| `variables.py` | Constantes: tamaño, barcos, símbolos y mensajes |
| `requirements.txt` | Dependencias |
| `AI_LOG.md` | Registro del uso de IA |
