# Banco de preguntas para la IA · antes de crear el dashboard

Un dashboard confiable se construye **antes** de pedir el gráfico. Estas son las preguntas que puedes hacerle a la IA, en el orden del método:

**Entender los datos → Calidad → Decisión y pregunta → Cálculo → Comparar → Verificar → Límites → Preparar el dashboard**

Cópialas tal cual y cambia lo que está entre `[corchetes]`. Se escribieron para los dos archivos del taller (`despachos_eds_mensual.csv` y `gnv_precios_mensual.csv`), pero sirven con cualquier dato.
**★ = ruta rápida** para el taller de 30 minutos: si vas justo, haz solo estas.

## Cómo preguntar bien
- **Una pregunta por mensaje.** Así sabes qué respuesta corresponde a qué.
- **Pide siempre el cálculo:** qué archivo, qué filas, qué filtros, qué período.
- **Escribe lo que esperas antes de ver la respuesta** (orden de magnitud, sube o baja): te permite detectar un error.
- **Pide tablas** cuando la respuesta sea larga o tenga varias cifras.
- **Si una respuesta te suena demasiado buena, desconfía:** pídele que la audite (sección F).

| En vez de… | Pregunta… |
|---|---|
| ¿Cómo vamos en combustibles? | ¿Cuánto creció el volumen total despachado entre enero y [mes de corte] de [año] frente al mismo período del año anterior, en millones de galones? |
| ¿Quién vende más? | ¿Qué 10 departamentos concentran más [producto] entre enero y [mes de corte]? |
| ¿Subió el gas? | ¿Cómo evolucionó mes a mes el precio promedio y la mediana del GNV en [ciudad] desde [año]? |

---

## A · Entender los datos (¿qué tengo?)
- **A1 ★** Describe cada archivo: número de filas y columnas, tipo de dato de cada columna, rango de fechas y valores vacíos. No analices todavía.
- **A2** Explícame qué significa cada columna con un ejemplo de fila real. Marca cuáles son medidas (se suman o se promedian) y cuáles son dimensiones (se agrupan o se filtran).
- **A3** Dime los valores distintos de `producto`, `zona_frontera` y `departamento`, y cuántos hay de cada uno.
- **A4** ¿Qué representa una fila de cada archivo? ¿Qué combinación de columnas identifica una fila de forma única?
- **A5** ¿Qué unidad tiene cada medida? Separa lo que dice el archivo de lo que estás asumiendo, y dime qué supuestos son arriesgados.
- **A6** ¿Qué períodos están completos y cuáles no? ¿Faltan meses en alguna serie?

## B · Calidad de los datos
- **B1 ★** Revisa nulos, vacíos, duplicados, ceros, negativos y categorías raras (por ejemplo `-`). Dame un conteo de cada hallazgo.
- **B2** ¿Hay nombres de departamento o municipio escritos de formas distintas o que se puedan confundir (por ejemplo Bogotá D.C. y Cundinamarca)? ¿Cómo los trataríamos?
- **B3** Cuenta cuántas filas y qué volumen representan las filas con departamento `-`. ¿Las excluirías de un ranking? ¿Por qué?
- **B4** ¿El último año está completo? ¿Cuál es el último mes con datos? ¿Qué comparaciones son válidas y cuáles no?
- **B5** En el archivo de precios, ¿cuántos municipios tienen una sola estación en el último mes? ¿Qué problema tiene calcular un promedio con una sola estación?
- **B6** ¿Qué valores te parecen atípicos en volumen o en precio? Muéstrame las filas sin eliminarlas.

## C · De la decisión a la pregunta
- **C1** Tengo que decidir `[la decisión]`. Propón 5 preguntas de negocio que estos datos puedan responder; cada una con período, segmento y unidad.
- **C2 ★** Reescribe esta pregunta para que se pueda responder con estos datos: «`[pregunta vaga]`».
- **C3** Para esta pregunta: «`[pregunta]`», dime qué archivo, columnas y filtros necesito y si los datos alcanzan. Si no alcanzan, ¿qué dato faltaría?
- **C4** ¿Qué decisión concreta apoyaría la respuesta a «`[pregunta]`» y quién la tomaría?
- **C5 ★** Antes de calcular: ¿qué orden de magnitud o qué dirección (sube o baja) esperarías para «`[pregunta]`» y por qué? Voy a comparar tu expectativa con el cálculo.
- **C6** Ordena estas preguntas de mayor a menor valor para la decisión y de menor a mayor esfuerzo: `[lista]`.

## D · Cálculo con el cálculo a la vista
- **D1 ★** Calcula `[métrica]` y muéstrame el código o los pasos, las filas que usaste y los filtros aplicados.
- **D2** Dame el resultado en una tabla con unidades visibles (millones de galones) y formato colombiano: punto para miles y coma para decimales.
- **D3** Lista los meses exactos que incluiste en cada año del cálculo.
- **D4** ¿Cuántas filas entraron al cálculo y cuántas excluiste? Explica cada exclusión.
- **D5** Para este porcentaje: dime el numerador y el denominador, y por qué es ese denominador.
- **D6** Calcula la misma cifra de dos maneras distintas y compáralas.
- **D7** Para los precios: dame promedio, mediana, mínimo, máximo y número de estaciones por ciudad y mes. ¿Por qué difieren el promedio y la mediana?

## E · Comparar y entender la serie
- **E1 ★** Compara enero–`[mes de corte]` del año actual con el mismo período del año anterior. Explícame por qué no conviene compararlo con el año anterior completo.
- **E2** ¿Qué meses tuvieron el mayor y el menor volumen total? ¿Hay estacionalidad?
- **E3** ¿Hay saltos o quiebres bruscos en la serie? Descríbelos con fechas y magnitud, sin explicar la causa.
- **E4** ¿Qué producto o departamento crece más y cuál menos? ¿El volumen pequeño distorsiona los porcentajes?
- **E5** Si ves un cambio brusco, propón hipótesis y dime qué dato adicional las confirmaría o las descartaría.
- **E6** Compara `[ciudad 1]` y `[ciudad 2]` mes a mes y dime qué conclusión es segura y cuál no.

## F · Verificar (auditar a la IA)
- **F1 ★** Audita tu respuesta anterior: busca períodos no comparables, filas excluidas sin avisar, unidades equivocadas y categorías mal tratadas.
- **F2** ¿Qué supuestos hiciste? ¿Qué tan segura estás de cada cifra y por qué?
- **F3** Reproduce la cifra con un método independiente (por ejemplo, sumar por producto y luego el total) y dime si coincide.
- **F4** Dame tres pruebas de sensatez para esta cifra (por ejemplo: debe ser menor que el total; la suma de las partes debe dar el total).
- **F5** Tengo este control de otra fuente: `[cifra]`. Si no coincide con la tuya, encuentra dónde está la diferencia.
- **F6** ¿Qué parte de tu respuesta sale de los datos y cuál de conocimiento general? Márcalas por separado.

## G · Límites y trampas (lo que NO se puede afirmar)
- **G1 ★** ¿Puedo calcular con estos datos la participación de mercado de una marca de estaciones? Si no, explica por qué y qué puedo calcular en su lugar.
- **G2** ¿Estos datos dicen por qué subió o bajó `[algo]`? ¿Qué puedo afirmar y qué es solo una hipótesis?
- **G3** ¿Un despacho es lo mismo que una venta al consumidor final? ¿Qué implica eso para mis conclusiones?
- **G4** Redacta tres conclusiones sobre `[tema]` que NO debería escribir en un dashboard con estos datos, y por qué.
- **G5** ¿Qué advertencias y supuestos deben ir visibles junto a cada cifra?

## H · Preparar el dashboard (último paso antes de pedirlo)
- **H1 ★** Resume las preguntas que validamos en una tabla: pregunta, cifra, cálculo, período, límite y decisión que apoya.
- **H2** Para cada pregunta, ¿qué gráfico recomiendas y por qué? ¿Cuál no usarías?
- **H3** Propón un título que diga la conclusión para cada tarjeta, sin exagerar lo que los datos permiten.
- **H4** ¿Qué filtros (por producto, departamento o año) serían útiles y cuáles confundirían?
- **H5** ¿En qué orden pondrías las tarjetas para que se lea de la decisión al detalle? Máximo 4.
- **H6** Escribe el pie de página: fuente, fecha de corte y supuestos.

Cuando tengas H1 revisada, pide el dashboard con el prompt del **paso 6** del cuaderno (`cuaderno-30min.html`).

---

## Si trabajas con Power BI (modelo semántico)
Para quien use el MCP de Power BI y los skills de Microsoft (Demo 3). Son los mismos pasos, aplicados al modelo:
- **I1** Conéctate al modelo abierto y lista tablas, columnas, medidas y relaciones. No cambies nada.
- **I2** Evalúa el modelo frente a buenas prácticas de modelado y dime qué incumple, sin aplicar cambios todavía.
- **I3** ¿Qué medidas necesito para responder estas preguntas: `[lista]`? Propón nombres según las convenciones y explica la lógica en palabras antes de escribir DAX.
- **I4** Valida la medida `[nombre]` con una consulta DAX y dime el resultado; compáralo con este control: `[cifra]`.
- **I5** Agrega descripciones a tablas, columnas y medidas en lenguaje de negocio.
