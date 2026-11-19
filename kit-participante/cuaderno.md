# Cuaderno del participante · Dashboards con IA

**Material de extensión**, para después del taller de 30 minutos (`kit-taller-30min`). Duración sugerida: 38 minutos · **En parejas** · **Herramienta:** la que tengas (Claude, ChatGPT, Copilot…)

## Qué vas a entregar
Un dashboard de **hasta 5 tarjetas** para tu misión, con: título que dice la conclusión, cálculo visible, fuente y fecha de corte, y los límites del dato. Más: tu plantilla de pregunta llena.

## Antes de empezar (2 min)
- [ ] Tienes la carpeta del kit con los CSV de `datos/`.
- [ ] Elegiste tu **ruta**: **1** chat con archivos (todos) · **2** chat + skill · **3** agente con código (opcional).
- [ ] Elegiste tu **misión** (A, B, C o D) y la anotaste.
- [ ] Abriste `prompt-maestro.md` y `plantilla-pregunta.md`.

---

## Fase 1 · Calentamiento (8 min)
**Objetivo:** reproducir la cifra de control C1 y comprobar que tu IA compara períodos equivalentes.

1. Abre un chat nuevo. Sube `despachos_eds_mensual.csv`.
2. Pega el **prompt maestro** (completo) y, en "TU MISIÓN", escribe:
   > *Describe los datos. Luego calcula el volumen total (Mgal) de enero a octubre de 2025 y de 2026, muestra el cálculo y dime cuánto creció.*
3. Compara con el control del facilitador (lo proyecta). ¿Coincide?
   - **Sí:** pasa a la fase 2.
   - **No:** pregúntale *"¿qué meses incluiste en cada año?"*. Casi siempre el error es el período. Corrígelo y anota qué falló.

**Checkpoint (minuto 8):** todos con C1 verificada.

---

## Fase 2 · Construye (25 min)
1. **Llena la plantilla de pregunta** para tu misión (5 min). Usa las preguntas guía de abajo.
2. Pide **una cifra a la vez**, siempre con su cálculo. Compárala con tu "Control".
3. Cuando tengas 3–5 cifras verificadas, pide el dashboard:
   > *Con las preguntas que validamos, construye el dashboard siguiendo las reglas del prompt maestro. Una página HTML (o artifact), máximo 5 tarjetas, el título de cada tarjeta dice la conclusión, y con la fuente y la fecha de corte visibles.*
4. **Un cambio por mensaje** para ajustar (color, una tarjeta, un tooltip). Así sabes qué rompió qué.

**Checkpoint (minuto 33):** el facilitador pasa por las mesas y revisa un control por pareja.

### Misión A · Pulso nacional *(inicial)* · datos: `despachos_eds_mensual.csv`
Pregunta de negocio: ¿cómo evoluciona la demanda de gasolina y diésel y cuánto creció este año?
- ¿Cuánto creció el total y cada producto (corriente, extra, diésel) en ene–oct 2026 vs 2025?
- ¿Cómo se ve la serie mensual 2022–2026? ¿Qué producto pesa más?
- ¿Qué porcentaje del volumen es gasolina extra? (¡ojo con el denominador!)
- Gráficos sugeridos: KPI con referencia · línea mensual por producto · barras de crecimiento por producto.

### Misión B · Mapa de regiones *(inicial)* · datos: `despachos_eds_mensual.csv`
Pregunta de negocio: ¿qué departamentos concentran el volumen de diésel y cuáles crecen más?
- ¿Cuáles son los 10 departamentos con mayor volumen de diésel en ene–oct 2026 y qué % del total concentran?
- ¿Cuáles crecieron más frente a ene–oct 2025? (¿hay departamentos con muy poco volumen que distorsionan el %?)
- ¿Cómo tratas Bogotá D.C. frente a Cundinamarca y las filas con departamento "-"? Decláralo.
- Gráficos sugeridos: barras horizontales (top 10 + "otros" en el texto) · mapa de calor departamento × año.

### Misión C · GNV: precio y demanda *(medio)* · datos: `gnv_precios_mensual.csv`, `gnv_precios_estaciones_recientes.csv`, `gnv_ventas_mensual.csv`
Pregunta de negocio: ¿el GNV es más caro en Bogotá que en Medellín y qué pasó con su volumen desde 2025?
- ¿Cuál es el precio de Bogotá y de Medellín mes a mes? ¿Siempre fue más caro en Bogotá?
- ¿Cómo se distribuyen los precios por estación en el último mes? ¿Promedio o mediana?
- ¿Cómo evoluciona el volumen mensual de GNV? ¿Hay quiebres? ¿Qué NO puedes afirmar sobre su causa?
- Gráficos sugeridos: dos paneles alineados (precio y volumen), no doble eje · rango mín–máx.

### Misión D · Zona de frontera *(avanzado)* · datos: `despachos_eds_mensual.csv`, `frontera_beneficio_mensual.csv`
Pregunta de negocio: ¿cuánto pesa la zona de frontera en el volumen y se está usando el cupo asignado?
- ¿Qué % del volumen nacional ene–oct 2026 va a zonas de frontera y qué departamentos pesan más?
- ¿Cuánto cupo (beneficio) se asignó por departamento y cuánto se despachó realmente? ¿Cuál es el uso del cupo?
- ¿Qué supuesto estás haciendo sobre la unidad del cupo?
- Gráficos sugeridos: barras de volumen vs cupo por departamento · KPI de uso del cupo.

---

## Fase 3 · Verifica y congela (5 min)
Pasa esta lista con tu pareja. Una casilla sin marcar es una corrección pendiente.

- [ ] **Cálculo a la vista:** cada cifra clave muestra de dónde sale (columnas, filtro, operación).
- [ ] **Períodos comparables:** mismos meses; sin año parcial contra año completo.
- [ ] **Control:** comparaste con el control de tu misión. ¿Coincide o explicas por qué no?
- [ ] **Límites:** fuente, corte (octubre de 2026) y supuestos visibles; nada sobre marcas ni causas como hecho.
- [ ] **Títulos:** cada tarjeta dice la conclusión.
- [ ] **Todas las tarjetas muestran su gráfico** (nada vacío).
- [ ] **Decisión:** el dashboard dice qué decisión apoya.

**Congela:** guarda el HTML (o el enlace del artifact) y una captura. Eso es lo que muestras.

---

## Si te atascas (3 minutos máximo, luego levanta la mano)
| Síntoma | Qué probar |
|---|---|
| La cifra no coincide con el control | Pregunta *"¿qué meses y qué filas incluiste?"*. Casi siempre es el período o el producto |
| La IA responde algo que los datos no pueden decir | Recuérdale la regla 7 del prompt maestro: si no se puede, dilo |
| El dashboard sale vacío o roto | *"Revisa que cada tarjeta tenga datos y que el script cargue; corrige solo eso."* Si no, pide la versión sin librerías externas |
| El gráfico es ilegible (30 categorías) | *"Muestra solo las 10 mayores y el resto en una nota."* |
| Los números salen con puntos y comas mezclados | *"Formato colombiano: miles con punto, decimales con coma."* |
| No tienes cuenta o herramienta | Trabaja con tu pareja y haz tú la plantilla y la verificación |

## Reto extra (si terminaste antes)
Añade una tarjeta con una pregunta que los datos **no puedan responder** (por ejemplo: participación de una marca en un departamento, o la causa de una caída) y explica en la tarjeta **por qué no se puede** y qué dato haría falta.

## Rúbrica del show & tell (máx. 10 puntos)
| Criterio | 0 | 1 | 2 |
|---|---|---|---|
| Cifra de control | No la comparó | La comparó y no coincidía | Coincide, o explica por qué difiere |
| Cálculo a la vista | Ninguna cifra lo muestra | Algunas | Todas las cifras clave |
| Límites del dato | Afirma lo que no puede | Menciona algún límite | Fuente, corte y supuestos visibles |
| Claridad visual | Confuso o sobrecargado | Se entiende con esfuerzo | Títulos que dicen la conclusión |
| Decisión | No se ve para qué sirve | Se infiere | Dice qué decisión apoya |
