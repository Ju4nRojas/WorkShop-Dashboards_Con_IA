# Diccionario de datos del taller

Fuente: datos.gov.co · Ministerio de Minas y Energía (SICOM) · licencia **CC BY-SA 4.0** (cita siempre fuente y fecha de corte). Corte: **octubre de 2026**. Tablas agregadas por mes, en UTF-8.

## `despachos_eds_mensual.csv` · conjunto fbht-2fzd
Despacho de combustibles líquidos a estaciones de servicio (automotriz y fluvial).
| Columna | Significado |
|---|---|
| `anio`, `mes` | Año y mes (números) |
| `departamento` | Departamento de destino (la estación). `-` = sin dato (solo años 2022–2025, volumen marginal) |
| `producto` | `GASOLINA MOTOR CORRIENTE`, `GASOLINA MOTOR EXTRA` (premium), `BIODIESEL CON MEZCLA` (diésel/ACPM), `DIESEL MARINO` (marginal) |
| `zona_frontera` | `SI`/`NO`: el destino es zona de frontera |
| `volumen_gal` | Galones despachados en el mes. Para reportar usa **Mgal** = millones de galones (÷ 1.000.000) |
| `n_registros` | Número de despachos agregados en la fila |

## `gnv_precios_mensual.csv` · conjunto he3q-86dn
Precio del gas natural vehicular (GNV) publicado por las estaciones, agregado por municipio y mes.
| Columna | Significado |
|---|---|
| `anio`, `mes`, `departamento`, `municipio` | Ubicación y período. Bogotá: `BOGOTA, D.C.`; Medellín: `MEDELLIN` (departamento ANTIOQUIA) |
| `precio_promedio` | Promedio simple entre estaciones |
| `precio_min`, `precio_max`, `precio_mediana` | Mínimo, máximo y mediana entre estaciones |
| `n_registros` | Número de estaciones con precio ese mes |

**Unidad no documentada:** se asume COP por m³. Dilo como supuesto.

## Lo que estos datos NO dicen
- Un despacho es una compra de la estación al mayorista: indica demanda, **no** es la venta al consumidor final.
- **No hay marca de estación**: no se puede calcular participación de mercado por empresa.
- No explican causas: un salto o una caída se describe; la causa es una hipótesis por verificar con otra fuente.
- Un promedio puede esconder la forma de los datos: mira también la mediana y el rango.
