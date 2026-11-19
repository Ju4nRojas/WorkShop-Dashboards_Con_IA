# Taller de 30 minutos · Tu primer dashboard con IA

Aprende a pasar de una pregunta de negocio a un dashboard **que puedas defender**, usando una IA en el navegador y **datos abiertos reales** de combustibles de Colombia. Lo haces **tú solo**, a tu ritmo y **sin instalar nada**.

> Los datos son **públicos** (Ministerio de Minas y Energía, SICOM, publicados en [datos.gov.co](https://www.datos.gov.co)). No uses datos internos ni confidenciales de tu organización en este taller.

## Lo que necesitas
- Un navegador y una **cuenta de Claude** ([claude.ai](https://claude.ai)). Sirve la cuenta gratuita, pero tiene un cupo de uso limitado: crear archivos gasta más cupo que un chat normal. Si tu cuenta se queda sin cupo, avísale al facilitador.
- La opción de **ejecución de código y creación de archivos** activada en tu cuenta (Configuración → Capacidades). El paso 0 del cuaderno te guía.
- 30 minutos, más 5 de preparación antes del taller.

## Cómo empezar (3 pasos)
1. **Descarga el material:** botón verde **Code → Download ZIP** y descomprímelo.
2. **Abre `cuaderno-30min.html`** con doble clic (se abre en tu navegador). Si prefieres texto, usa `cuaderno-30min.md`.
3. **Sigue el cuaderno paso a paso.** Cada pregunta tiene un botón **Copiar**; tus anotaciones y casillas se guardan en tu navegador. El facilitador pasará por tu puesto en distintos momentos para revisar tu avance.

## Qué vas a hacer
| Minuto | Paso |
|---|---|
| Antes | **Paso 0** · Preparación: cuenta, capacidad de código activada y datos a mano |
| 0–3 | **Paso 1** · Subes los datos y fijas las reglas de trabajo |
| 3–10 | **Pasos 2 y 3** · Calculas dos cifras con su cálculo a la vista y las **verificas contra un control** |
| 10–15 | **Pasos 4 y 5** · Una pregunta con matices y una **pregunta trampa** (que los datos no pueden responder) |
| 15–25 | **Paso 6** · Pides el dashboard y lo mejoras, un cambio por mensaje |
| 25–30 | **Paso 7** · Verificas con una lista de 4 preguntas y guardas una captura |

Los **controles** (las cifras correctas para comparar) te los entrega el facilitador durante el taller, en tarjetas, para que primero anotes **tus** resultados.

## Qué hay en este repositorio
| Archivo | Para qué |
|---|---|
| `cuaderno-30min.html` | **Empieza aquí.** El paso a paso interactivo: copiar prompts, casillas, campos para anotar y temporizador |
| `cuaderno-30min.md` | La misma guía en texto, por si no puedes abrir el HTML |
| `prompt-maestro.md` | El texto que pegas al inicio de tu chat para fijar las reglas de trabajo |
| `plantilla-pregunta.md` | Una página para convertir una necesidad de negocio en una pregunta verificable |
| `banco-de-preguntas.md` | Preguntas listas para pegar en cada paso previo al dashboard (la ruta rápida está marcada con ★) |
| `diccionario-datos.md` | Qué contiene cada archivo de datos y qué **no** dicen |
| `datos/` | Los dos archivos CSV que subes a Claude |

## Tres reglas para todo el taller
1. **Una cifra sin cálculo visible no se publica.** Pide siempre cómo se calculó: archivo, filtros y período.
2. **Compara períodos equivalentes:** enero–octubre contra enero–octubre, nunca un año parcial contra uno completo.
3. **Si los datos no pueden responder algo, la respuesta correcta es «no se puede con estos datos».** Las causas son hipótesis, no hechos.

## Preguntas frecuentes
- **No se abre el cuaderno HTML.** Ábrelo con otro navegador (Chrome, Edge, Firefox) o usa `cuaderno-30min.md`.
- **Claude no lee los CSV.** Revisa que la ejecución de código y la creación de archivos estén activadas, sube de nuevo los archivos o abre un chat nuevo.
- **Me quedé sin cupo de uso.** Avisa al facilitador; puedes esperar unos minutos o usar la cuenta de otra persona (solo con estos datos abiertos).
- **No terminé a tiempo.** Está bien: el cuaderno guarda tu avance en el navegador. Si te atrasas, salta las preguntas 3 y 4 y ve directo al dashboard (paso 6).

## Datos y licencia de los datos
- **Fuente:** Ministerio de Minas y Energía, Sistema de Información de Combustibles (SICOM), datos.gov.co. Conjuntos: `fbht-2fzd` (despacho a estaciones de servicio) y `he3q-86dn` (precios de gas natural vehicular).
- **Licencia de los datos de origen:** CC BY-SA 4.0. Si los reutilizas o publicas resultados, cita la fuente y la fecha de corte (**octubre de 2026**).
- Los archivos de `datos/` son **tablas agregadas por mes** a partir de esos conjuntos (los originales tienen millones de filas), con los valores numéricos y las fechas normalizados.
- **Límites que debes conocer:** un despacho es una compra de la estación al mayorista (indica demanda, no es la venta al consumidor final); los datos **no incluyen la marca** de la estación; y la unidad del precio del gas natural vehicular **no está documentada** (se asume COP por m³).
