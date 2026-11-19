# Diccionario de datos

Fuente: datos.gov.co · Ministerio de Minas y Energía (SICOM) · licencia **CC BY-SA 4.0** (cita siempre fuente y fecha de corte).
Corte de este kit: **octubre de 2026** (último mes completo). Todas las tablas están **agregadas por mes** y en UTF-8.

> Reglas que valen para todo: los despachos son **galones** (reporta en **Mgal** = millones de galones, `÷ 1.000.000`).
> Un despacho es una compra de una estación a un mayorista: indica demanda, **no es la venta al consumidor**.
> **No hay marca de estación** en estos datos.

## `despachos_eds_mensual.csv` · fbht-2fzd
Despacho de combustibles líquidos a estaciones de servicio (automotriz y fluvial). Misiones A, B y D.
| Columna | Significado |
|---|---|
| `anio`, `mes` | Año y mes (números) |
| `departamento` | Departamento de destino (la estación). `-` = sin dato (solo años 2022–2025, marginal) |
| `producto` | `GASOLINA MOTOR CORRIENTE`, `GASOLINA MOTOR EXTRA`, `BIODIESEL CON MEZCLA` (diésel/ACPM con biodiésel), `DIESEL MARINO` (marginal) |
| `zona_frontera` | `SI`/`NO`: el destino es zona de frontera |
| `volumen_gal` | Galones despachados en el mes |
| `n_registros` | Número de despachos agregados en la fila |

## `despachos_mayoristas_mensual.csv` · 339g-zjac
Despacho de los distribuidores mayoristas, por tipo de comprador. Reto extra (la fuente original tiene ~7,2 millones de filas).
Columnas: `anio`, `mes`, `tipo_comprador`, `subtipo_comprador`, `producto`, `volumen_gal`, `n_registros`.
Incluye además de las estaciones otros compradores (comercializadores industriales, aviación, grandes consumidores, quemadores industriales). Las compras de las estaciones aparecen **en esta tabla y en `despachos_eds_mensual.csv`**: no las sumes (doble conteo).

## `gnv_precios_mensual.csv` · he3q-86dn
Precios publicados por las estaciones de gas natural vehicular, agregados por municipio y mes. Misión C.
| Columna | Significado |
|---|---|
| `anio`, `mes`, `departamento`, `municipio` | Ubicación y período (Bogotá aparece como `BOGOTA, D.C.`) |
| `precio_promedio` | Promedio simple entre estaciones |
| `precio_min`, `precio_max`, `precio_mediana` | Mínimo, máximo y mediana entre estaciones |
| `n_registros` | Número de estaciones con precio ese mes |

**Unidad no documentada:** se asume COP por m³. Dilo como supuesto.

## `gnv_precios_estaciones_recientes.csv` · he3q-86dn
Precio por estación, **últimos 4 meses** (para ver la distribución, no solo el promedio).
Columnas: `anio`, `mes`, `departamento`, `municipio`, `estacion`, `precio`.

## `gnv_ventas_mensual.csv` · v8jr-kywh
Ventas de GNV por departamento y mes. Misión C.
Columnas: `anio`, `mes`, `departamento`, `volumen_m3` (m³ suministrados), `vehiculos_atendidos`, `numero_ventas`, `n_registros` (filas diarias agregadas).
**Cobertura:** la serie empieza en noviembre de 2022; 2022 es parcial, no lo compares con otros años.

## `frontera_beneficio_mensual.csv` · shbt-hqy9
Asignación (cupo/beneficio) máxima a despachar a estaciones de zona de frontera. Misión D.
Columnas: `anio`, `mes`, `departamento`, `tipo_agente`, `tipo_beneficio`, `beneficio`, `n_registros`.
Solo hay un `tipo_agente` (DISTRIBUIDOR MINORISTA) y un `tipo_beneficio` (CUPO UPME).
**Unidad no documentada:** el orden de magnitud se parece al de los galones despachados en frontera, pero es un **supuesto**: decláralo.

## Trampas de calidad que ya conocemos
- Año parcial: 2026 tiene 10 meses; 2022 en GNV ventas, solo 2.
- `departamento = "-"` en la tabla de estaciones (años anteriores).
- Bogotá D.C. y Cundinamarca son departamentos distintos.
- Un promedio puede esconder una distribución partida (mira mediana, mínimo, máximo y la tabla por estación).
- Un salto brusco en una serie puede ser un cambio en el reporte y no un cambio real: se describe, no se explica.
