# Demo 3 · Lista de ensayo paso a paso

**Para qué sirve:** que ensayes a mano, con casillas, lo único de la demo que no pude ejecutar: el recorrido **Power BI Desktop → MCP → medidas → skill de reportes**. Al final decides con un criterio claro si la haces **en vivo** o con **video**.

**Cómo usarla:** hazla completa dos veces. La primera es para descubrir problemas (calcula 60–75 minutos); la segunda, con cronómetro, para saber si cabe en 15. Los tiempos de cada bloque son **objetivos míos, no medidos**. Anota lo que ves en el registro del final.

> **Qué está verificado y qué no.** Verificado en este equipo: Windows, Power BI Desktop, Node, plugin `powerbi-authoring`, paquete del MCP en caché y CLI `powerbi-report-author` 0.5.0 (`scaffold` y `validate` funcionan sin red). **No verificado:** la conexión del MCP (timeout de 30 s sin causa confirmada), el DAX en Desktop, `preview --reload` y las capturas. Cada casilla de estos bloques es una prueba real.

---

## Bloque 0 · Punto de partida (5 min)
- [ ] Cierra todas las instancias de Power BI Desktop.
- [ ] Ejecuta `powershell -ExecutionPolicy Bypass -File verificar_requisitos.ps1`. **Esperado:** 0 faltan (el aviso de OneDrive es normal).
- [ ] Anota la hora de inicio: ______

## Bloque A · Proyecto PBIP en carpeta local (15 min)
- [ ] Crea `C:\Demo3PowerBI\datos` y copia allí `despachos_eds_mensual.csv` (la carpeta del repositorio está en OneDrive; Power Query y los archivos PBIP funcionan mejor fuera de ella).
- [ ] Power BI Desktop → obtener datos → Texto/CSV → ese archivo → **Cargar**. **Esperado:** 6.112 filas y 7 columnas (`anio`, `mes`, `departamento`, `producto`, `zona_frontera`, `volumen_gal`, `n_registros`).
- [ ] Renombra la tabla a `Despachos`.
- [ ] Guarda como **proyecto de Power BI (.pbip)** en `C:\Demo3PowerBI\Demo3.pbip`.
  - Si no aparece la opción, actívala en Opciones (características en vista previa). Los menús pueden variar según la versión.
  - Verifica que el reporte use el formato **PBIR** (el skill solo edita PBIR).
- [ ] Cierra Desktop y **ábrelo de nuevo desde el archivo `.pbip`**. **Esperado:** carga la tabla `Despachos` sin errores.
- [ ] Mira la carpeta: deben existir `Demo3.SemanticModel` y `Demo3.Report`, y dentro de `Demo3.Report` la carpeta `definition`.
- [ ] Haz una copia de seguridad de toda `C:\Demo3PowerBI` (por ejemplo `C:\Demo3PowerBI_respaldo_A`) y, si usas Git, un primer *commit*.

**Detente si:** Desktop no puede guardar como proyecto o el reporte no es PBIR. Sin eso el skill de reportes no funciona; usa el video en la demo.
Tiempo real del bloque: ______

## Bloque B · Conectar el MCP (10 min)
- [ ] Abre Claude Desktop → pestaña **Code** → carpeta `C:\Demo3PowerBI`.
- [ ] Comprueba que el plugin `powerbi-authoring` está activo y que el servidor `powerbi-modeling-mcp` aparece **conectado**.
- [ ] Si pide aceptar el **EULA**, acéptalo.
- [ ] **Si da *timeout*:** en una terminal ejecuta `npx -y @microsoft/powerbi-modeling-mcp@latest --start` y observa el mensaje (EULA, error, tiempo de arranque). Anótalo: es el dato que me falta para saber la causa. Cierra el proceso (Ctrl+C) y reinicia la sesión de Claude.
- [ ] Con Desktop abierto en `Demo3.pbip`, envía el **prompt 1** (solo lectura):
  > *Conéctate al modelo abierto en Power BI Desktop y lista sus tablas, columnas y medidas. No cambies nada todavía.*
  **Esperado:** una tabla `Despachos`, 7 columnas, ninguna medida. Si lista otra cosa o no encuentra el modelo, anótalo.
- [ ] Confirma que **no modificó nada** (el modelo sigue igual).

**Detente si:** el MCP no conecta tras dos intentos. Decisión provisional: video.
Tiempo real del bloque: ______

## Bloque C · Medidas con el MCP (15 min)
- [ ] Envía el **prompt 2**:
  > *Aplica las convenciones de nombres del skill de modelado y crea medidas para: volumen en Mgal, volumen enero–mes de corte del año actual y del anterior con los mismos meses, y la variación interanual en %. Usa VAR y DIVIDE. Valídalas con una consulta DAX y dime el resultado antes de tocar el reporte.*
- [ ] **Observa y anota:**
  - ¿Propuso renombrar tabla y columnas a nombres legibles con espacios? (las guías del skill lo piden) ______
  - ¿Usó `VAR` y `DIVIDE`? ¿Evitó usar una medida dentro de un filtro de `CALCULATE`? ______
  - ¿Ejecutó una consulta DAX de validación? ______
- [ ] **Control:** el resultado debe ser **3.596,45 · 3.486,41 · +3,16 %**. Compáralo con `medidas-referencia.dax` (otra redacción válida está bien; lo que importa es el resultado).
  - Si da otra cifra: pídele *«¿qué meses y qué filas incluiste en cada año?»*. Es el momento de mostrar cómo se encuentra el error.
- [ ] Mira las medidas en Desktop (recarga o reabre si no las ves): ¿existen y dan el mismo valor en una tarjeta de prueba?
- [ ] Copia de seguridad: `C:\Demo3PowerBI_respaldo_C`.

**Detente si:** las medidas no se crean o el resultado no coincide y no logras corregirlo en 5 minutos. Decisión provisional: mostrar solo hasta aquí en vivo y el resto con video.
Tiempo real del bloque: ______

## Bloque D · Visuales con el skill de reportes (15 min)
- [ ] En Desktop, **guarda** cualquier cambio manual antes de seguir (los archivos del disco son la fuente de verdad).
- [ ] Envía el **prompt 3** como **edición puntual** sobre el reporte existente:
  > *Con el skill de reportes, en el reporte existente agrega a la primera página dos tarjetas (volumen enero–corte y variación interanual) y un gráfico de líneas mensual por producto, sin diésel marino. Valida el PBIR, recarga en Power BI Desktop y revisa una captura.*
  - Si el skill responde con un **plan y pide aprobación**, aprueba: es su puerta de gobierno para reportes nuevos. Anota cuánto tiempo te costó.
- [ ] Para el gráfico mensual hace falta una fecha: si propone una columna `Fecha` (primer día de cada mes), déjalo crearla con el MCP.
- [ ] **Comprueba por tu cuenta** (no solo en el chat) en una terminal:
  - `powerbi-report-author validate C:\Demo3PowerBI\Demo3.Report` → **Esperado:** `errorCount: 0`. (Este comando sí lo probé en un esqueleto vacío.)
  - `powerbi-report-author preview-visuals C:\Demo3PowerBI\Demo3.Report` → resume los visuales creados (el comando existe en la CLI; no lo he ejecutado con un reporte real).
- [ ] Con el `.pbip` abierto en Desktop: `powerbi-report-author preview C:\Demo3PowerBI\Demo3.Report --host desktop --reload`. **Esperado:** Desktop recarga y muestra los visuales. Si responde `HOST_UNAVAILABLE`, falta abrir el `.pbip` en Desktop (lo comprobé: es el mensaje cuando no hay instancia).
- [ ] **Verifica los datos:** las tarjetas deben mostrar **3.596,45** y **+3,16 %**; el gráfico, tres líneas (corriente, diésel, extra).
- [ ] **Verifica que usan medidas del modelo** y no números fijos (abre un visual y mira el campo).
- [ ] Copia de seguridad del estado final bueno: `C:\Demo3PowerBI_respaldo_final`.

**Detente si:** el reporte no abre en Desktop tras el cambio. Restaura el respaldo anterior y anota el error exacto.
Tiempo real del bloque: ______

## Bloque E · Material de respaldo (10 min)
- [ ] **Graba el recorrido completo** (pantalla): bloques B, C y D en el orden de la demo.
- [ ] Toma una captura de: el modelo con las medidas, la consulta DAX con el resultado, y el reporte final.
- [ ] Guarda el respaldo final en una USB y en el equipo (no solo en la nube).

---

## Decisión: ¿en vivo o con video?
Rellénala tras la **segunda** pasada, con cronómetro.

| Criterio | ¿Se cumple? |
|---|---|
| El MCP conectó a la primera en las dos pasadas | |
| Las medidas dieron 3.596,45 · 3.486,41 · +3,16 % | |
| `validate` terminó con 0 errores y el reporte se recargó en Desktop | |
| Los bloques B, C y D caben en **menos de 15 minutos** | |
| Sabes explicar qué hizo el MCP (modelo) y qué el skill (reporte) | |

- **Todo "sí":** haz la demo en vivo y ten el video como red de seguridad.
- **Falla uno de los dos primeros o el tiempo:** haz en vivo solo conectar y la medida (valida el control), y muestra el resto con video.
- **Falla la conexión del MCP:** video completo, y usa los 15 minutos para explicar qué hace cada pieza y los límites (el MCP no crea visuales).

## Registro
| Pasada | Fecha | Bloque A | Bloque B | Bloque C | Bloque D | Total | ¿Conectó el MCP? | ¿Medidas = control? | Problemas |
|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | |
| 2 | | | | | | | | | |

**Si encuentras algo que no está en el runbook** (un mensaje de error, un paso distinto), anótalo en la última columna: es justo la información que falta para cerrar los puntos no verificados.
