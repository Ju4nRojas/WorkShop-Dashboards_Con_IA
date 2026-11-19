#!/usr/bin/env python3
"""Demo 2 · referencia reproducible: dashboard Plotly (HTML autocontenido, funciona sin internet).

Es el resultado al que se espera llegar cuando Claude Desktop (pestaña Code) recibe el prompt de README.md.
Lee los CSV de ../../datos, calcula con pandas y COMPRUEBA que las cifras coinciden con las de control.

Requisitos:  pip install plotly pandas      (instálalos ANTES de la demo: en una red lenta tarda varios minutos)
Uso:         python build_plotly.py          -> dashboard-plotly.html
"""
import json
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

AQUI = Path(__file__).resolve().parent
DATOS = AQUI.parent.parent / "datos"
ctl = json.loads((AQUI.parent.parent / "facilitador" / "cifras_control.json").read_text(encoding="utf-8"))
CA, CM = (int(x) for x in ctl["corte"].split("-"))          # último mes completo
MES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"][CM - 1]


def nombre_depto(d):
    return " ".join(w.lower() if w in ("DE", "DEL", "Y") else w if w == "D.C." else w.capitalize() for w in d.split())


e = pd.read_csv(DATOS / "despachos_eds_mensual.csv")
e["mgal"] = e.volumen_gal / 1e6


def ene_a_corte(df, anio):
    return df[(df.anio == anio) & (df.mes <= CM)]


# 1) KPI: mismos meses en ambos años (nunca año parcial contra año completo)
actual, anterior = ene_a_corte(e, CA).mgal.sum(), ene_a_corte(e, CA - 1).mgal.sum()
crec = (actual / anterior - 1) * 100
assert abs(crec - ctl["C1"]["crec_pct"]) < 1e-6, "El KPI no coincide con la cifra de control C1"

# 2) Serie mensual por producto (sin diésel marino: marginal)
productos = {"GASOLINA MOTOR CORRIENTE": "Gasolina corriente", "BIODIESEL CON MEZCLA": "Diésel", "GASOLINA MOTOR EXTRA": "Gasolina extra"}
mensual = e[e["producto"].isin(productos)].groupby(["anio", "mes", "producto"]).mgal.sum().reset_index()
mensual["fecha"] = pd.to_datetime(dict(year=mensual.anio, month=mensual.mes, day=1))

# 3) Top 10 departamentos en diésel, enero a corte (sin filas "-")
dsl = ene_a_corte(e, CA).query("producto == 'BIODIESEL CON MEZCLA' and departamento not in ['-', '']")
top = dsl.groupby("departamento").mgal.sum().sort_values(ascending=False)
assert [k for k, _ in ctl["C2"]["top3"]] == list(top.index[:3]), "El top 3 no coincide con la cifra de control C2"
top10 = top.head(10)[::-1]

fig = make_subplots(rows=2, cols=2, specs=[[{"type": "indicator", "colspan": 2}, None], [{"type": "xy"}, {"type": "xy"}]],
                    row_heights=[0.24, 0.76], vertical_spacing=0.14,
                    subplot_titles=("", "Volumen mensual por producto (Mgal)", f"Diésel: 10 mayores departamentos, ene–{MES} {CA} (Mgal)"))
fig.add_trace(go.Indicator(mode="number+delta", value=actual, number={"suffix": " Mgal", "valueformat": ",.1f"},
                           delta={"reference": anterior, "relative": True, "valueformat": "+.1%"},
                           title={"text": f"Volumen ene–{MES} de {CA} frente al mismo período de {CA-1}"}), row=1, col=1)
for (p, nombre), color in zip(productos.items(), ["#2a78d6", "#eb6834", "#1baf7a"]):
    s = mensual[mensual["producto"] == p]
    fig.add_trace(go.Scatter(x=s.fecha, y=s.mgal, name=nombre, mode="lines", line=dict(width=2, color=color),
                             hovertemplate=nombre + ": %{y:,.1f} Mgal<extra>%{x|%b %Y}</extra>"), row=2, col=1)
fig.add_trace(go.Bar(x=top10.values, y=[nombre_depto(d) for d in top10.index], orientation="h", marker_color="#2a78d6", showlegend=False,
                     hovertemplate="%{y}: %{x:,.1f} Mgal<extra></extra>"), row=2, col=2)
fig.update_yaxes(automargin=True, row=2, col=2)
fig.update_layout(template="plotly_white", height=680, width=1240, separators=",.",
                  title=f"Combustibles en Colombia · corte {MES} de {CA}",
                  legend=dict(orientation="h", y=-0.1, x=0), margin=dict(t=90, b=150),
                  annotations=list(fig.layout.annotations) + [dict(
                      text="Fuente: MinEnergía – SICOM, datos.gov.co (CC BY-SA 4.0). Despachos a estaciones de servicio: indican demanda, no venta al consumidor final.",
                      x=0, y=-0.26, xref="paper", yref="paper", showarrow=False, xanchor="left", font=dict(size=11, color="#74736e"))])
salida = AQUI / "dashboard-plotly.html"
fig.write_html(salida, include_plotlyjs=True, full_html=True)   # JS embebido: sin internet
print(f"OK -> {salida.name} ({salida.stat().st_size/1024/1024:.1f} MB) · KPI {crec:+.2f} % · top diésel: {', '.join(top.index[:3])}")
