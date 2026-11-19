# Plantilla de pregunta (una por tarjeta del dashboard)

Complétala **antes** de pedirle nada a la IA. Si no puedes llenar "Control", todavía no tienes una pregunta.

```
Decisión     ¿Qué vas a decidir o a qué decisión ayuda esto?
             ______________________________________________
Pregunta     Una frase, con período, segmento y unidad.
             ______________________________________________
Métrica      ¿Qué se calcula exactamente? (suma, promedio, mediana, % de qué sobre qué)
             ______________________________________________
Período      ¿Mismos meses en ambos años? ¿Hasta qué mes?
             ______________________________________________
Dato         Archivo y columnas:
             ______________________________________________
Gráfico      ¿Cuál responde mejor? (indicador · línea · barras · tabla)
             ______________________________________________
Control      ¿Qué cifra esperas y por qué? ¿Con qué la vas a comparar?
             ______________________________________________
Límites      ¿Qué NO puede decir este dato? (marca, causa, venta final, unidad)
             ______________________________________________
Título       La conclusión en una frase (no el nombre de la tabla).
             ______________________________________________
```

## Ejemplo resuelto (distinto de las preguntas del taller)
```
Decisión     ¿Cuánto debe pesar el diésel en el plan de abastecimiento?
Pregunta     ¿Qué porcentaje del volumen total despachado en enero–octubre de 2026 es diésel?
Métrica      Suma de volumen_gal de BIODIESEL CON MEZCLA / suma de volumen_gal de todos los productos
Período      Enero a octubre de 2026
Dato         despachos_eds_mensual.csv (anio, mes, producto, volumen_gal)
Gráfico      Indicador con el porcentaje; barras con los productos
Control      Un poco menos de la mitad (casi la mitad del volumen es diésel)
Límites      Son despachos a estaciones: demanda, no venta al consumidor; no dice la causa
Título       "El diésel es casi la mitad del volumen despachado en 2026"
```
