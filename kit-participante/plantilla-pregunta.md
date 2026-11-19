# Plantilla de pregunta (una por tarjeta del dashboard)

Complétala **antes** de pedirle nada a la IA. Si no puedes llenar "Control", todavía no tienes una pregunta.

```
MISIÓN: ____
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
Gráfico      ¿Cuál responde mejor a la pregunta? (KPI · línea · barras · calor · tabla)
             ______________________________________________
Control      ¿Qué cifra esperas y por qué? ¿Con qué la vas a comparar?
             ______________________________________________
Límites      ¿Qué NO puede decir este dato? (marca, causa, venta final, unidad)
             ______________________________________________
Título       La conclusión en una frase (no el nombre de la tabla).
             ______________________________________________
```

## Ejemplo resuelto (el del gancho)
```
Decisión     ¿Ajustamos el abastecimiento del próximo año?
Pregunta     ¿Cuánto creció el volumen despachado ene–oct 2026 frente a ene–oct 2025?
Métrica      Suma de volumen_gal, en Mgal; variación % = actual / anterior − 1
Período      Enero a octubre en ambos años
Dato         despachos_eds_mensual.csv (anio, mes, volumen_gal)
Gráfico      KPI con referencia + línea mensual
Control      Alrededor de +3 % (lo confirma el facilitador)
Límites      Es demanda de estaciones, no venta al consumidor; no dice la causa
Título       "El consumo creció 3,2 % en ene–oct 2026 frente al mismo período de 2025"
```
