# AI_LOG · Team Challenge Hundir la flota

Este registro no cuenta para la nota. Sirve para ver dónde vais solos y dónde os apoyáis. Si no habéis usado IA en una parte, dejad el nivel en 0: también es un dato útil.

**Grupo:** (nombres)

**Herramientas usadas:** Claude (Claude Code)

> El repositorio es público: no pongáis datos personales ni contraseñas en los prompts que copiéis aquí.

## Resumen por módulo

Niveles: **0** sin IA · **1** consulta puntual, el código es nuestro · **2** la IA escribe partes y las adaptamos · **3** casi todo lo escribe la IA

| Módulo | Quién lo ha llevado | Nivel de IA (0-3) | Nº de prompts | ¿Lo podríais repetir sin IA? (sí / en parte / no) |
|---|---|---|---|---|
| `variables.py` | Scrum Master (versión inicial) | 1 | 1 | |
| `clases.py` | Dev 1 | 2 | 5 | |
| `funciones.py` | Dev 1 | 3 | 1 | |
| `main.py` | Dev 1 | 3 | 1 | |
| `README.md` | Scrum Master | 1 | 1 | |

## Registro de prompts

### clases.py · Prompt 1

- **Objetivo:** reescribir a mano la clase `Tablero` del issue #2, que es la parte que me toca, en lugar de entregar la versión generada por la IA.
- **Prompt:** "Lo reescribimos a mano, es la parte que me toca a mí." Después, "No sé cómo hacerlo", y la IA lo explicó por trozos.
- **Respuesta relevante:** la clase dividida en cuatro pasos (constructor, `colocar_barcos()`, `recibir_disparo()`, y `quedan_barcos()` con `mostrar()`), cada uno con el código y la explicación de cada línea: por qué hay dos arrays, por qué se comprueba que la casilla está dentro del tablero antes de leer el array (en NumPy un índice negativo no da error) y por qué el disparo repetido se mira primero.
- **Cambios:** el código lo escribí yo en VS Code siguiendo la explicación. La IA corrigió la sangría (había métodos fuera de la clase y `cabe = True` dentro del bucle equivocado) y me explicó por qué estaba mal.
- **Comprobación:** 500 tableros aleatorios con exactamente 20 casillas de barco; disparos a las 100 casillas (20 tocados, 80 aguas, el repetido no cuenta); `mostrar(ocultar_barcos=True)` no enseña los barcos; `quedan_barcos()` pasa a `False` al tocarlo todo.
- **Decisión propia:** quedarme con `clases.py` como mi parte y escribirla yo para poder explicarla en la presentación.

### funciones.py, main.py · Prompt 1

- **Objetivo:** completar el resto del proyecto siguiendo el enunciado y la guía del equipo.
- **Prompt:** "Haz el trabajo entero y luego lo reviso yo todo."
- **Respuesta relevante:**
  - `variables.py`: barcos en un diccionario, constantes en mayúsculas, orientaciones, semilla para la demo y mensajes de validación y turnos.
  - `funciones.py`: `convertir_coordenadas()` valida formato y rango con `try/except`; `pedir_coordenadas()` repite hasta recibir una entrada válida; `disparo_maquina()` elige al azar entre las casillas sin disparar (`np.argwhere`), así que nunca repite.
  - `main.py`: bucle `while True` con turnos; quien acierta repite, el disparo repetido no cuenta (`continue`) y la partida acaba con `break`.
  - `README.md`: instalación, ejecución, reglas, símbolos, estructura y modo demo.
- **Cambios:** (pendiente)
- **Comprobación:** entradas no válidas (letras, un solo número, fuera de rango, decimales) y disparo repetido; 300 partidas completas con semillas distintas, todas terminan en victoria o derrota sin errores; `Ctrl+C` cierra sin enseñar un error.
- **Decisión propia:** (pendiente)

### Prompt 1 – variables.py

- **Objetivo:** revisar el archivo `variables.py` y mejorar los mensajes que aparecen durante el juego para comunicarse con el jugador.
- **Prompt:** "Revísame el archivo variables.py y ayúdame con los mensajes que se muestran al jugador durante la partida."
- **Respuesta relevante:**
  - Revisión de las constantes existentes.
  - Ayuda para redactar y organizar los mensajes de bienvenida e instrucciones.
  - Mensajes para solicitar coordenadas y avisar de errores de formato o rango.
  - Mensajes para indicar si un disparo ha acertado, ha fallado o si se ha repetido.
  - Mensajes para comunicar los turnos de la máquina y el resultado final de la partida.
- **Cambios:** revisión del archivo y mejora de los mensajes dirigidos al jugador.
- **Comprobación:** revisión de los textos y de su correspondencia con las distintas situaciones del juego.
- **Decisión propia:** seleccionar y adaptar los mensajes para que sean claros y fáciles de entender.

### Prompt 2 – README.md

- **Objetivo:** documentar el proyecto para explicar su funcionamiento y facilitar su instalación y ejecución.
- **Prompt:** "Hazme una descripción corta del juego Hundir la Flota para incluirla en el README.md."
- **Respuesta relevante:**
  - Se propuso una descripción breve del juego.
  - Se explicó el objetivo: hundir todos los barcos del rival mediante disparos estratégicos en un tablero de 10x10 casillas.
  - Se indicó que el proyecto está desarrollado en Python y utiliza NumPy.
  - También se recibió ayuda para crear el archivo README.md y conocer su estructura.
- **Cambios:** se incorporó una descripción del juego en el README.md.
- **Comprobación:** revisión del contenido y del formato Markdown.
- **Decisión propia:** elegir una descripción breve y adaptarla al estilo de documentación del equipo.
