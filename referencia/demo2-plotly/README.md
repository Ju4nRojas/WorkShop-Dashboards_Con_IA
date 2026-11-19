# Demo 2 · Claude Desktop + Plotly

**Qué muestra:** que Claude escriba y ejecute código para generar un dashboard interactivo en **un solo archivo HTML que funciona sin internet**, y que el número del KPI salga del dato y no esté escrito a mano.

## Antes de la demo (hazlo con tiempo)
- Python 3.10 o superior y `pip install plotly pandas`. **En la red de las pruebas la instalación tardó casi 4 minutos**: no la dejes para el momento de la demo.
- Abre la carpeta `datos/` del proyecto en Claude Desktop, pestaña **Code**, para que Claude vea los CSV.
- Ten generado `dashboard-plotly.html` (este mismo directorio) como respaldo: `python build_plotly.py`.

## Prompt sugerido (pégalo en la pestaña Code)
```
Eres mi analista de datos de combustibles de Colombia. Responde en español.
En la carpeta datos/ están tablas agregadas por mes (SICOM, datos.gov.co, CC BY-SA 4.0).
Con pandas y Plotly genera UN archivo HTML autocontenido (include_plotlyjs=True) con:
1) un indicador con el volumen enero–octubre de 2026 frente a enero–octubre de 2025 (Mgal y variación %),
2) la serie mensual de gasolina corriente, diésel y gasolina extra,
3) los 10 mayores departamentos en diésel de enero a octubre de 2026.
Reglas: compara períodos equivalentes (nunca año parcial contra año completo); los valores salen del cálculo, nada escrito a mano;
excluye diésel marino y departamentos "-"; pon la fuente y el corte al pie; los despachos indican demanda, no venta al consumidor.
Antes de generar el HTML, dime las cifras que vas a mostrar y cómo las calculaste.
```

## Qué mirar durante la demo
1. ¿Comparó enero–octubre contra enero–octubre? El control revela **+3,16 %** (3.596,5 vs 3.486,4 Mgal).
2. ¿El script es legible y repetible (el mes que viene, un comando)?
3. ¿El HTML abre sin conexión? (ábrelo con el wifi apagado).
4. ¿Top 3 de diésel? Antioquia 251,7 · Cundinamarca 180,3 · Valle del Cauca 157,0 Mgal.

## Lo que ya se verificó
`build_plotly.py` genera el dashboard en unos 9 segundos (pandas y Plotly ya instalados) y comprueba con `assert` que el KPI y el top 3 coinciden con `facilitador/cifras_control.json`. No verifiqué qué script produce **tu** Claude con este prompt: ensáyalo y compara.
