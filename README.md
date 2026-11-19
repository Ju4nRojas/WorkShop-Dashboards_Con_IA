# Dashboards con IA: de datos abiertos a decisiones

Dos sesiones con datos reales de combustibles de Colombia (datos.gov.co, SICOM, MinEnergía):

1. **Charla con tres demos · 90 minutos** (`presentacion/`, `facilitador/`).
2. **Taller práctico · 30 minutos, en sesión aparte, sin instalar nada** (`taller-30min/`, `kit-taller-30min.zip`).

Hilo conductor: **decisión → pregunta → datos → cálculo → gráfico → verificación**.

## Sesión 1 · Charla y demos (90 min)
| Min | Bloque |
|---|---|
| 0–3 | Apertura |
| 3–12 | Por qué ahora: señales de Microsoft y Anthropic, brecha adopción–confianza, cuatro razones |
| 12–32 | La caja de herramientas: de un HTML con Plotly a Power BI (skills, MCP, plugins), método, datos y sus límites |
| 32–77 | Tres demos de 15 min: **Claude web** · **Claude Desktop + Plotly** · **MCP + skills de Power BI** |
| 77–82 | Verificación y comparación |
| 82–90 | Invitación al taller de 30 minutos y cierre |

## Sesión 2 · Taller de 30 minutos
Prepara (3) → Verifica (7) → Pregunta con trampa (5) → Dashboard (10) → Verifica y comparte (5). En Claude web con dos CSV, en parejas si el cupo es poco. Incluye verificación previa de acceso, controles para el facilitador y kit sin respuestas.

## Qué hay aquí
| Carpeta | Contenido | ¿Se reparte? |
|---|---|---|
| `presentacion/` | `index.html`: 29 diapositivas estilo Periferia con notas (N) y control oculto en las demos (C) | Se proyecta |
| `referencia/` | `dashboard-referencia.html` (sin internet), `demo2-plotly/` (script, README y HTML de respaldo) y `demo3-powerbi/` (runbook, verificador de requisitos, DAX de referencia) | Se muestran |
| `facilitador/` | Guion de la charla y las 3 demos, plan B, preparación, cifras de control | **No** |
| `taller-30min/` | Guion del facilitador (generado, con controles) y fuentes del kit | Guion: **no** |
| `kit-taller-30min.zip` | Kit del taller de 30 minutos (2 CSV, prompt maestro, cuaderno, plantilla, diccionario) | Sí |
| `participante/` y `kit-participante.zip` | Kit completo con 4 misiones avanzadas (extensión después del taller) | Opcional |
| `datos/` | CSV agregados, `preparar_datos.py` (consultas SoQL), manifiesto | Los CSV, sí |

## Fuentes (datos.gov.co · MinEnergía · CC BY-SA 4.0)
`fbht-2fzd` despacho a estaciones · `339g-zjac` despacho de mayoristas (~7,2 M de filas) · `he3q-86dn` precios de GNV · `v8jr-kywh` ventas de GNV · `shbt-hqy9` beneficio en zona de frontera.

## Regenerar con otro corte
```bash
python datos/preparar_datos.py --corte 2026-10
python facilitador/calcular_cifras_control.py
python presentacion/build_deck.py
python referencia/build_referencia.py
python taller-30min/build_taller.py
python empaquetar_kit.py
```
Las cifras de la presentación, los dashboards y la guía del taller salen de los CSV y se contrastan con las cifras de control: si algo no coincide, el script falla. Para el dashboard Plotly: `pip install plotly pandas` y `python referencia/demo2-plotly/build_plotly.py`.

## Estado de la verificación
- **Verificado:** cifras de control (contra otro taller y contra la API en vivo), dashboards de referencia, kit sin filtración de respuestas, contenido de Microsoft contrastado con la documentación oficial de noviembre de 2026.
- **Pendiente de ensayo:** respuestas de tu herramienta y modelo en las demos 1 y 2, y la Demo 3 completa (MCP + skill de reportes), que no se ejecutó. Verificación de acceso a claude.ai y de cupo con cuentas reales antes del taller.

## Empieza por
`facilitador/preparacion.md` y `facilitador/guion-90min.md`; para el taller, `taller-30min/facilitador/guion-30min.md`.
