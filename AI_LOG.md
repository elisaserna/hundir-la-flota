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
| `clases.py` | Dev 1 | 3 | 1 | |
| `funciones.py` | Dev 1 | 3 | 1 | |
| `main.py` | Dev 1 | 3 | 1 | |
| `README.md` | Scrum Master | 1 | 1 | |

## Registro de prompts

### clases.py · Prompt 1

- **Objetivo:** implementar la clase `Tablero` del issue #2 con todo el código explicado.
- **Prompt:** "Sí, hazlo, pero quiero que todo quede explicado."
- **Respuesta relevante:** clase `Tablero` con los arrays `tablero` y `disparos`, `colocar_barcos()` con casilla de inicio y orientación N/S/E/O al azar, `recibir_disparo()` que devuelve tocado, agua o repetido, `quedan_barcos()` y `mostrar()` con opción para ocultar los barcos. Docstrings en formato Google y comentarios en los pasos menos obvios.
- **Cambios:** (pendiente)
- **Comprobación:** 2.000 colocaciones aleatorias con exactamente 20 casillas de barco; disparos a las 100 casillas (20 tocados, 80 aguas, el repetido no cuenta); tablero de 12 x 12 sin cambiar `clases.py`.
- **Decisión propia:** (pendiente)

### variables.py, funciones.py, main.py y README.md · Prompt 1

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
