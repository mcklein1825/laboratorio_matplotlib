# -*- coding: utf-8 -*-
"""
PROYECTO FINAL — Dashboard de ventas
Objetivo: construir un dashboard 2x2 a partir de datos/ventas.csv con:
  1. Ventas totales por fecha (línea).
  2. Total de ventas por producto (barras).
  3. Distribución porcentual de ventas por producto (gráfico circular).
  4. Distribución de las ventas (histograma + boxplot combinados).
Ejecución:  python proyecto_final.py
Guarda el resultado en graficos/dashboard.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# El archivo está en la raíz del laboratorio, por lo que ROOT es su propio directorio
ROOT = Path(__file__).resolve().parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    ruta_csv = ROOT / "datos" / "ventas.csv"

    # Verificación del archivo de datos
    if not ruta_csv.exists():
        print(f"ERROR: no se encontró el archivo {ruta_csv}.")
        print("Asegúrate de que exista datos/ventas.csv dentro del proyecto.")
        return

    # Lectura y preparación de los datos con Pandas
    df = pd.read_csv(ruta_csv)
    df["Fecha"] = pd.to_datetime(df["Fecha"])

    # Agrupaciones necesarias para el dashboard
    ventas_fecha = df.groupby("Fecha")["Ventas"].sum()
    ventas_producto = df.groupby("Producto")["Ventas"].sum()

    # Figura 2x2 con tamaño amplio para el dashboard
    fig, ejes = plt.subplots(2, 2, figsize=(14, 9))
    ax_fecha = ejes[0, 0]
    ax_barras = ejes[0, 1]
    ax_pastel = ejes[1, 0]
    ax_dist = ejes[1, 1]

    # 1. Ventas totales por fecha (línea con marcadores)
    ax_fecha.plot(ventas_fecha.index, ventas_fecha.values, marker="o",
                  color="tab:blue", linewidth=2)
    ax_fecha.set_title("Ventas totales por fecha")
    ax_fecha.set_xlabel("Fecha")
    ax_fecha.set_ylabel("Ventas")
    ax_fecha.grid(True)
    plt.setp(ax_fecha.get_xticklabels(), rotation=30, ha="right")

    # 2. Total de ventas por producto (barras)
    ax_barras.bar(ventas_producto.index, ventas_producto.values,
                  color="tab:orange")
    ax_barras.set_title("Total de ventas por producto")
    ax_barras.set_xlabel("Producto")
    ax_barras.set_ylabel("Ventas")
    ax_barras.grid(True, axis="y")

    # 3. Distribución de ventas por producto (gráfico circular)
    ax_pastel.pie(ventas_producto.values, labels=ventas_producto.index,
                  autopct="%1.1f%%", startangle=90)
    ax_pastel.set_title("Distribución de ventas por producto")
    ax_pastel.axis("equal")

    # 4. Distribución de las ventas: histograma y boxplot apilados
    ax_dist.hist(df["Ventas"], bins=6, color="tab:green",
                 edgecolor="black", alpha=0.7)
    ax_dist.set_title("Distribución de ventas (histograma)")
    ax_dist.set_xlabel("Ventas")
    ax_dist.set_ylabel("Frecuencia")
    ax_dist.grid(True, axis="y")

    # Boxplot horizontal superpuesto en la parte inferior del eje
    caja_eje = ax_dist.twiny()
    caja_eje.boxplot(df["Ventas"], vert=False, positions=[0.5],
                     patch_artist=True, boxprops=dict(facecolor="lightyellow"))
    caja_eje.set_ylim(-1, 1.5)   # recorta el espacio para ver solo la caja
    caja_eje.set_yticks([])      # oculta etiquetas del eje del boxplot

    # Super título general del dashboard
    fig.suptitle("Dashboard de ventas", fontsize=16, fontweight="bold")

    plt.tight_layout()
    plt.savefig(GRAFICOS / "dashboard.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
