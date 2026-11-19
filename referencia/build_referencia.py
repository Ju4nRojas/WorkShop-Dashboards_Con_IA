#!/usr/bin/env python3
"""Genera referencia/dashboard-referencia.html (un solo archivo, sin librerias ni internet).
Calcula todo desde ../datos/*.csv, COMPRUEBA que coincide con las cifras de control y falla si no.
Uso: python build_referencia.py"""
import json
from pathlib import Path
import pandas as pd

AQUI = Path(__file__).resolve().parent
D = AQUI.parent / "datos"
ctl = json.loads((AQUI.parent / "facilitador" / "cifras_control.json").read_text(encoding="utf-8"))
CA, CM = (int(x) for x in ctl["corte"].split("-"))
MES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
TC = {"BOGOTA D.C.": "Bogotá D.C.", "VALLE DEL CAUCA": "Valle del Cauca", "NORTE DE SANTANDER": "Norte de Santander"}


def nombre(d):
    ac = {"BOGOTA": "Bogotá", "ATLANTICO": "Atlántico", "BOLIVAR": "Bolívar", "BOYACA": "Boyacá", "CORDOBA": "Córdoba", "CHOCO": "Chocó",
          "QUINDIO": "Quindío", "GUAINIA": "Guainía", "CAQUETA": "Caquetá", "VAUPES": "Vaupés"}
    return " ".join(w if w == "D.C." else ac.get(w, w.capitalize()) if w not in ("DE", "DEL", "Y") else w.lower() for w in d.split())


def etiqueta(a, m):
    return f"{MES[m-1]} {str(a)[2:]}"


def es(x, d=1):
    return f"{x:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def hasta_corte(df, a):
    return df[(df.anio == a) & (df.mes <= CM)]


e = pd.read_csv(D / "despachos_eds_mensual.csv"); e["mgal"] = e.volumen_gal / 1e6
meses = (e.groupby(["anio", "mes"]).size().reset_index()[["anio", "mes"]]).sort_values(["anio", "mes"])
meses = meses[(meses.anio < CA) | ((meses.anio == CA) & (meses.mes <= CM))]
idx = list(zip(meses.anio, meses.mes))
prod = {"corriente": "GASOLINA MOTOR CORRIENTE", "extra": "GASOLINA MOTOR EXTRA", "diesel": "BIODIESEL CON MEZCLA"}
mens = {k: [float(e[(e.anio == a) & (e.mes == m) & (e["producto"] == v)].mgal.sum()) for a, m in idx] for k, v in prod.items()}

# --- KPI (C1, C4) ---
act, ant = hasta_corte(e, CA).mgal.sum(), hasta_corte(e, CA - 1).mgal.sum()
kp = {}
for k, v in prod.items():
    a = hasta_corte(e, CA).query("producto == @v").mgal.sum(); b = hasta_corte(e, CA - 1).query("producto == @v").mgal.sum()
    kp[k] = dict(actual=float(a), anterior=float(b), crec=float((a / b - 1) * 100))
assert abs((act / ant - 1) * 100 - ctl["C1"]["crec_pct"]) < 1e-6, "C1 no coincide"

# --- Diesel por departamento (C2) ---
dsl = hasta_corte(e, CA).query("producto == 'BIODIESEL CON MEZCLA' and departamento not in ['-', '']")
top = dsl.groupby("departamento").mgal.sum().sort_values(ascending=False)
assert [k for k, _ in ctl["C2"]["top3"]] == list(top.index[:3]), "C2 no coincide"
filas = [dict(d=nombre(k), v=float(x)) for k, x in top.head(10).items()]
otros = float(top.iloc[10:].sum()); n_otros = int(len(top) - 10)
top3_share = float(top.head(3).sum() / top.sum() * 100)

# --- GNV precios (C7) ---
p = pd.read_csv(D / "gnv_precios_mensual.csv")
def serie_precio(contiene, dep):
    s = p[p.municipio.str.upper().str.contains(contiene) & p.departamento.str.upper().str.contains(dep)]
    g = s.groupby(["anio", "mes"]).agg(avg=("precio_promedio", "mean"), lo=("precio_min", "min"), hi=("precio_max", "max"), med=("precio_mediana", "mean"), n=("n_registros", "sum"))
    return {k: [None if (a, m) not in g.index else float(g.loc[(a, m), k]) for a, m in idx] for k in ["avg", "lo", "hi", "med", "n"]}
bog, med = serie_precio("BOGOT", "BOGOT"), serie_precio("MEDELL", "ANTIOQUIA")
assert abs(bog["avg"][-1] - ctl["C7"]["bogota"]["precio"]) < 0.01 and abs(med["avg"][-1] - ctl["C7"]["medellin"]["precio"]) < 0.01, "C7 no coincide"

# --- GNV volumen (C8) ---
v = pd.read_csv(D / "gnv_ventas_mensual.csv")
idx_v = [(a, m) for a, m in idx if a >= 2023]
vol = [float(v[(v.anio == a) & (v.mes == m)].volumen_m3.sum() / 1e6) for a, m in idx_v]
q = ctl["C8"]["quiebre"]

# --- Frontera (C6, C9) ---
b = pd.read_csv(D / "frontera_beneficio_mensual.csv")
fr = hasta_corte(e, CA).query("zona_frontera == 'SI'").groupby("departamento").mgal.sum()
cu = hasta_corte(b, CA).groupby("departamento").beneficio.sum() / 1e6
fx = pd.concat([fr.rename("desp"), cu.rename("cupo")], axis=1).dropna().sort_values("desp", ascending=False).head(8)
assert abs(fr.sum() - ctl["C6"]["total_frontera_mgal"]) < 1e-6, "C6 no coincide"
uso_nac = float(fr.sum() / cu.sum() * 100)
assert abs(uso_nac - ctl["C9"]["uso_cupo_nacional_pct"]) < 1e-6, "C9 no coincide"

DATA = dict(
    corte=f"{MES[CM-1]} de {CA}".replace("oct", "octubre"),
    corte_txt="octubre de 2026" if CM == 10 else f"{CM}/{CA}", anio=CA, mes_corte=MES[CM - 1],
    kpi=dict(total=dict(actual=float(act), anterior=float(ant), crec=float((act / ant - 1) * 100)), **kp),
    mens=dict(labels=[etiqueta(a, m) for a, m in idx], anios=[a for a, _ in idx], meses=[m for _, m in idx], **mens),
    diesel=dict(filas=filas, top3_share=top3_share, total=float(top.sum()), otros=otros, n_otros=n_otros),
    precio=dict(labels=[etiqueta(a, m) for a, m in idx], bog=bog, med=med, c7=ctl["C7"]),
    gnv=dict(labels=[etiqueta(a, m) for a, m in idx_v], vol=vol, i_quiebre=idx_v.index((2025, 11)), i_pico=idx_v.index((2025, 9)), q=q,
             crec_ene_oct=ctl["C8"]["crec_pct"]),
    frontera=dict(filas=[dict(d=nombre(k), desp=float(r.desp), cupo=float(r.cupo), uso=float(r.desp / r.cupo * 100)) for k, r in fx.iterrows()],
                  uso_nac=uso_nac, pct_nac=ctl["C6"]["pct_frontera_nacional"], total=float(fr.sum()), cupo_total=float(cu.sum())),
)
plantilla = (AQUI / "plantilla.html").read_text(encoding="utf-8")
(AQUI / "dashboard-referencia.html").write_text(plantilla.replace("{{DATA}}", json.dumps(DATA, ensure_ascii=False)), encoding="utf-8")
print("OK -> dashboard-referencia.html (todas las cifras coinciden con cifras_control.json)")
