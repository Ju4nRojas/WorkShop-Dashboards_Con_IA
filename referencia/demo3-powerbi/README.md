# Demo 3 · MCP + skills de Power BI (runbook)

**Qué muestra:** Claude edita un **modelo semántico** con el MCP de autoría de Power BI (medidas validadas con DAX) y agrega visuales al **reporte** con el skill `powerbi-report-cli`, todo sobre un proyecto PBIP que se ve en Power BI Desktop. El hilo: la misma pregunta de las otras demos (¿cuánto creció ene–oct 2026 frente a ene–oct 2025?) y el mismo control (**+3,16 %**).

**Quién hace qué (dilo en la demo):** el **MCP** modifica el modelo (tablas, columnas, medidas, DAX) y **no** crea páginas ni visuales; el **skill de reportes**, con su CLI `powerbi-report-author`, crea y valida el reporte (PBIR) y lo previsualiza.

> **Estado de verificación (19-nov-2026):** esta demo **no se ejecutó de punta a punta**. Lo verificado: requisitos del equipo (abajo), contenido del plugin, guías oficiales y, con la CLI ya instalada (0.5.0, 19-nov-2026), que `scaffold` y `validate` funcionan **sin red y sin Desktop** (esqueleto de reporte con 0 errores y 0 advertencias) y que `preview` exige tener el `.pbip` abierto en Power BI Desktop. Lo no verificado: la conexión del MCP (dio *timeout* de 30 s en mi sesión sin causa confirmada), el DAX en Desktop y la creación de visuales con vista previa. **Ensáyala dos veces antes del evento.**

## 1 · Requisitos y estado en el equipo donde se preparó
Ejecuta `powershell -ExecutionPolicy Bypass -File verificar_requisitos.ps1` (solo lectura). Resultado del 19-nov-2026:

| Requisito | Estado | Qué hacer |
|---|---|---|
| Windows | OK | El MCP local no soporta macOS |
| Power BI Desktop | OK (Tienda 2.159) | — |
| Node.js 20+ | OK (v24.20) | La CLI de reportes pide 20+; el MCP, 18+ |
| Plugin `powerbi-authoring` | OK (0.3.22) | — |
| Paquete del MCP en caché de npx | OK | Ya descargado: el timeout **no** fue por una primera descarga |
| CSV de la demo | OK | — |
| CLI `powerbi-report-author` | OK (0.5.0, instalada el 19-nov-2026) | En otro equipo: `npm install -g @microsoft/powerbi-report-authoring-cli@latest`. Sin ella el skill no puede crear, validar ni previsualizar el reporte |
| Ubicación del proyecto | Aviso | El repositorio está en OneDrive: crea el PBIP en una carpeta local (p. ej. `C:\Demo3PowerBI`) y copia allí el CSV |

## 2 · Preparación
> **Para ensayar paso a paso, con casillas, tiempos y un criterio para decidir entre vivo y video: [`ensayo-paso-a-paso.md`](ensayo-paso-a-paso.md).**

1. **La CLI ya está instalada en este equipo** (0.5.0). En otro equipo instálala con el comando de arriba. Comprueba `powerbi-report-author --version`.
2. **Conecta el MCP con tiempo.** Abre una sesión con el plugin y confirma que el servidor `powerbi-modeling-mcp` conecta; **acepta el EULA** cuando lo pida. Si da *timeout*, ejecuta en una terminal `npx -y @microsoft/powerbi-modeling-mcp@latest --start` para ver el mensaje de arranque (EULA, errores) y cuánto tarda; la causa del timeout que vi no está confirmada.
3. **Crea el proyecto en Power BI Desktop** (en la carpeta local):
   - Obtener datos → Texto/CSV → `despachos_eds_mensual.csv` → Cargar. Renombra la tabla a `Despachos`.
   - Guardar como **proyecto de Power BI (.pbip)**. Si no ves la opción, actívala en Opciones (características en vista previa) y verifica que el reporte use el formato **PBIR**: el skill solo edita PBIR. Los nombres exactos de menús pueden variar según la versión.
   - Cierra y vuelve a abrir desde el archivo `.pbip` para comprobar que carga.
4. **Copia de seguridad** de la carpeta del proyecto y, si puedes, `git init` + un primer *commit*: Microsoft recomienda un punto de partida para revisar o revertir los cambios del agente.
5. **Graba el video de respaldo** del recorrido completo.

## 3 · Guion (15 min)
Modo **interactivo**, nunca automático. Recuerda al público: los metadatos y resultados viajan al proveedor del modelo.

| Min | Paso | Prompt (cópialo) | Qué esperas ver |
|---|---|---|---|
| 0–2 | Contexto | — | Qué es el MCP (hacer) y qué un skill (cómo); el MCP no hace visuales |
| 2–4 | **Conectar (solo lectura)** | *Conéctate al modelo abierto en Power BI Desktop y lista sus tablas, columnas y medidas. No cambies nada todavía.* | Una tabla `Despachos` con 7 columnas y sin medidas |
| 4–9 | **Medidas con el MCP** | *Aplica las convenciones de nombres del skill de modelado y crea medidas para: volumen en Mgal, volumen enero–mes de corte del año actual y del anterior con los mismos meses, y la variación interanual en %. Usa VAR y DIVIDE. Valídalas con una consulta DAX y dime el resultado antes de tocar el reporte.* | Medidas creadas y una consulta DAX con **3.596,45 · 3.486,41 · +3,16 %**. Pulsa **C** en la diapositiva y compara con el control |
| 9–13 | **Visuales con el skill** | *Con el skill de reportes, en el reporte existente agrega a la primera página dos tarjetas (volumen enero–corte y variación interanual) y un gráfico de líneas mensual por producto, sin diésel marino. Valida el PBIR, recarga en Power BI Desktop y revisa una captura.* | Los visuales usan **medidas del modelo** (no números fijos); validación sin errores; página recargada |
| 13–15 | Comparar y cerrar | — | Qué hizo el MCP, qué el skill, qué verificaste |

**Detalles del skill que debes saber:**
- Pide una **edición puntual** sobre el reporte existente: va directo a *authoring*. Si pides un reporte **nuevo y completo**, el skill entra en *planning*, escribe `_brief/report-spec.md` y **se detiene a pedir tu aprobación** antes de construir (es una puerta intencional; en 15 minutos conviene evitarla o aprovecharla como ejemplo de gobierno).
- Para el gráfico mensual hace falta una fecha: si el agente propone una columna `Fecha` (primer día de cada mes) a partir de `anio` y `mes`, es correcto; deja que la cree con el MCP.
- Los archivos del disco son la fuente de verdad: **guarda en Desktop** cualquier cambio manual antes de pedir cambios al agente.

## 4 · DAX de referencia
`medidas-referencia.dax` trae las medidas y la consulta de validación con los resultados esperados. Sirven para **comparar**, no para pegar: el agente puede escribir otra versión válida; lo que importa es que dé **+3,16 %**. Están sin probar en Desktop.

## 5 · Si algo falla
| Síntoma | Qué hacer |
|---|---|
| El servidor MCP no conecta o da *timeout* | Verifica EULA, Node y la conexión de npm; ejecútalo en terminal para ver el error. Si no se arregla: video de respaldo |
| El agente dice que no encuentra el archivo | El MCP local trabaja con el archivo abierto en Desktop o con la carpeta PBIP; abre el `.pbip` y repite la conexión |
| `preview` responde `HOST_UNAVAILABLE` («No Power BI Desktop instance is running») | Es lo esperado si Desktop no tiene el reporte abierto: abre el `.pbip` en Power BI Desktop antes de previsualizar o recargar |
| Cambios sin efecto en Desktop | Recarga el modelo/reporte desde el agente (`preview ... --reload`) o cierra y reabre el `.pbip` |
| El skill no genera el visual | Muestra el modelo y la consulta DAX (el valor del MCP) y pasa al video del visual |
| La CLI no está en el PATH | Cierra y abre la terminal tras instalarla; `powerbi-report-author --version` |
| Error de versión de esquema al abrir el reporte | No edites los archivos a mano: pide al skill que haga `scaffold --offline`/`validate`, o usa el video |

## 6 · Registro del ensayo
| Fecha | ¿Conectó el MCP? | ¿Medidas = control? | ¿Visuales válidos y recargados? | Problemas | Minutos |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |

## Fuentes
Microsoft Learn: Power BI Authoring MCP server · Power BI Report skill · Power BI agentic overview · Skills for Fabric (consultadas en noviembre de 2026), y las guías del plugin `powerbi-authoring` 0.3.22 (`SKILL.md` del skill de reportes y referencias de modelado y DAX).
