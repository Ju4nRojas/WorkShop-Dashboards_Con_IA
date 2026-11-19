#!/usr/bin/env python3
"""Genera los snapshots (CSV) del taller desde datos.gov.co (API SODA, SoQL).

Uso:   python preparar_datos.py [--corte 2026-10]      (corte = ultimo mes COMPLETO a incluir)
Salida: CSV pequenos en esta carpeta + manifiesto.json (fuente, licencia, fecha de descarga).

Por que agregamos en el servidor: el dataset de despachos tiene millones de filas
(339g-zjac ~7,2 M). Nadie descarga eso en un taller: se pide SOLO lo agregado ($group).
Solo usa libreria estandar + pandas.
"""
import argparse, json, sys, time, urllib.parse, urllib.request
from datetime import date
from pathlib import Path
import pandas as pd

BASE = "https://www.datos.gov.co/resource/{id}.json"
AQUI = Path(__file__).resolve().parent

# nombre_salida -> (dataset, nombre legible, SoQL, prefijo de columnas de fecha, columnas de medida)
CONSULTAS = {
    "despachos_eds_mensual.csv": dict(
        id="fbht-2fzd",
        titulo="Estaciones de Servicio Automotriz y Fluvial: despacho de combustibles liquidos",
        select="anio_despacho AS anio, mes_despacho AS mes, departamento, producto, zona_frontera, "
               "sum(volumen_despachado) AS volumen_gal, count(*) AS n_registros",
        group="anio_despacho, mes_despacho, departamento, producto, zona_frontera"),
    "despachos_mayoristas_mensual.csv": dict(
        id="339g-zjac",
        titulo="Distribuidores Mayoristas: despacho de combustibles liquidos",
        select="anio_despacho AS anio, mes_despacho AS mes, tipo_comprador, subtipo_comprador, producto, "
               "sum(volumen_despachado) AS volumen_gal, count(*) AS n_registros",
        group="anio_despacho, mes_despacho, tipo_comprador, subtipo_comprador, producto"),
    "gnv_precios_mensual.csv": dict(
        id="he3q-86dn",
        titulo="Precios promedio de Gas Natural Comprimido Vehicular (GNCV)",
        select="anio_precio AS anio, mes_precio AS mes, departamento_eds AS departamento, municipio_eds AS municipio, "
               "avg(precio_promedio_publicado) AS precio_promedio, min(precio_promedio_publicado) AS precio_min, "
               "max(precio_promedio_publicado) AS precio_max, median(precio_promedio_publicado) AS precio_mediana, count(*) AS n_registros",
        group="anio_precio, mes_precio, departamento_eds, municipio_eds"),
    "gnv_ventas_mensual.csv": dict(
        id="v8jr-kywh",
        titulo="Ventas de Gas Natural Comprimido Vehicular (GNCV)",
        select="anio_venta AS anio, mes_venta AS mes, departamento, "
               "sum(cantidad_volumen_suministrado) AS volumen_m3, sum(vehiculos_atendidos) AS vehiculos_atendidos, "
               "sum(numero_de_ventas) AS numero_ventas, count(*) AS n_registros",
        group="anio_venta, mes_venta, departamento"),
    "frontera_beneficio_mensual.csv": dict(
        id="shbt-hqy9",
        titulo="Beneficio de estaciones de servicio en zona de frontera",
        select="anio_beneficio AS anio, mes_beneficio AS mes, departamento, tipo_agente, tipo_beneficio, "
               "sum(beneficio) AS beneficio, count(*) AS n_registros",
        group="anio_beneficio, mes_beneficio, departamento, tipo_agente, tipo_beneficio"),
}


def soda(id_, select, group, intentos=4):
    q = {"$select": select, "$group": group, "$limit": "200000"}
    url = BASE.format(id=id_) + "?" + urllib.parse.urlencode(q)
    for i in range(intentos):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "taller-dashboards-ia"}), timeout=180) as r:
                return json.load(r)
        except Exception as e:  # reintento con espera creciente
            print(f"   intento {i+1} fallo: {e}", file=sys.stderr)
            time.sleep(5 * (i + 1))
    raise SystemExit(f"No se pudo consultar {id_}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corte", default="2026-10", help="ultimo mes completo (AAAA-MM)")
    ap.add_argument("--solo", help="regenerar solo este archivo de salida")
    a = ap.parse_args()
    ca, cm = (int(x) for x in a.corte.split("-"))
    manifiesto = {"descargado": date.today().isoformat(), "corte": a.corte, "licencia": "CC BY-SA 4.0",
                  "fuente": "datos.gov.co - Ministerio de Minas y Energia (SICOM)", "archivos": {}}
    for salida, c in CONSULTAS.items():
        if a.solo and a.solo != salida:
            continue
        print(f"-> {salida}  ({c['id']})", flush=True)
        t0 = time.time()
        df = pd.DataFrame(soda(c["id"], c["select"], c["group"]))
        # Normalizacion (las fechas llegan como texto: '9' vs '09', etc.)
        df["anio"] = pd.to_numeric(df["anio"], errors="coerce")
        df["mes"] = pd.to_numeric(df["mes"], errors="coerce")
        df = df.dropna(subset=["anio", "mes"]).astype({"anio": int, "mes": int})
        df = df[(df.anio < ca) | ((df.anio == ca) & (df.mes <= cm))]
        medidas = [x for x in df.columns if x.startswith(("volumen", "precio", "vehiculos", "numero", "beneficio", "n_registros"))]
        for m in medidas:
            df[m] = pd.to_numeric(df[m], errors="coerce")
        dims = [x for x in df.columns if x not in medidas]
        for d in dims:
            if df[d].dtype == object:
                df[d] = df[d].fillna("").astype(str).str.strip()
        df = df.sort_values(dims).reset_index(drop=True)
        for m in medidas:
            if m != "n_registros" and m.startswith(("precio", "volumen")):
                df[m] = df[m].round(2)
        df.to_csv(AQUI / salida, index=False, encoding="utf-8")
        manifiesto["archivos"][salida] = dict(dataset=c["id"], titulo=c["titulo"], filas=len(df),
                                              periodo=f"{int(df.anio.min())}-{int(df[df.anio==df.anio.min()].mes.min()):02d} a {a.corte}",
                                              url=f"https://www.datos.gov.co/d/{c['id']}")
        print(f"   {len(df):,} filas en {time.time()-t0:.0f}s", flush=True)
    # ---- Precios GNV por estacion, ultimos 4 meses (para ver la DISTRIBUCION, no solo el promedio) ----
    salida = "gnv_precios_estaciones_recientes.csv"
    if not a.solo or a.solo == salida:
        print(f"-> {salida}  (he3q-86dn, nivel estacion)", flush=True)
        q = {"$select": "anio_precio AS anio, mes_precio AS mes, departamento_eds AS departamento, municipio_eds AS municipio, "
                        "nombre_comercial_eds AS estacion, precio_promedio_publicado AS precio",
             "$where": f"anio_precio >= '{ca-1}'", "$limit": "50000"}
        url = BASE.format(id="he3q-86dn") + "?" + urllib.parse.urlencode(q)
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "taller-dashboards-ia"}), timeout=180) as r:
            est = pd.DataFrame(json.load(r))
        est["anio"] = pd.to_numeric(est["anio"]); est["mes"] = pd.to_numeric(est["mes"]); est["precio"] = pd.to_numeric(est["precio"])
        ini = (ca * 12 + cm - 1) - 3                                  # ventana de 4 meses terminando en el corte
        est = est[(est.anio * 12 + est.mes - 1 >= ini) & ((est.anio < ca) | ((est.anio == ca) & (est.mes <= cm)))]
        est = est.sort_values(["anio", "mes", "departamento", "municipio", "estacion"]).reset_index(drop=True)
        est.to_csv(AQUI / salida, index=False, encoding="utf-8")
        manifiesto["archivos"][salida] = dict(dataset="he3q-86dn", titulo="Precios de GNV por estacion (ultimos 4 meses)", filas=len(est),
                                              periodo=f"4 meses hasta {a.corte}", url="https://www.datos.gov.co/d/he3q-86dn")
        print(f"   {len(est):,} filas", flush=True)
    ruta = AQUI / "manifiesto.json"
    if a.solo and ruta.exists():  # conserva las entradas ya generadas
        previo = json.loads(ruta.read_text(encoding="utf-8"))
        previo["archivos"].update(manifiesto["archivos"])
        manifiesto = {**previo, "descargado": manifiesto["descargado"]}
    ruta.write_text(json.dumps(manifiesto, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Listo.")


if __name__ == "__main__":
    main()
