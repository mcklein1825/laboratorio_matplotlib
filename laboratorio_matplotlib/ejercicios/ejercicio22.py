# -*- coding: utf-8 -*-
"""
EJERCICIO 22 — Gráfico desde un CSV
Objetivo: leer datos/ventas.csv con Pandas, convertir la columna de fechas,
agrupar las ventas por Fecha y Producto, y dibujar una línea por producto.
Guarda el resultado en graficos/ejercicio22.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    ruta_csv = ROOT / "datos" / "ventas.csv"

    # Verificación de la existencia del archivo de datos
    if not ruta_csv.exists():
        print(f"ERROR: no se encontró el archivo {ruta_csv}.")
        print("Asegúrate de que exista datos/ventas.csv dentro del proyecto.")
        return

    # Lectura del CSV y conversión de la columna de fechas
    df = pd.read_csv(ruta_csv)
    df["Fecha"] = pd.to_datetime(df["Fecha"])

    # Como hay varios productos por fecha, se agrupa por Fecha y Producto
    agrupado = df.groupby(["Fecha", "Producto"])["Ventas"].sum()

    # Reorganizar: filas = fechas, columnas = productos (una serie por producto)
    tabla = agrupado.unstack(level="Producto")

    fig, ax = plt.subplots(figsize=(10, 6))

    # Una línea con marcadores por cada producto
    for producto in tabla.columns:
        ax.plot(tabla.index, tabla[producto], marker="o", label=producto)

    ax.set_title("Ventas por fecha y producto")
    ax.set_xlabel("Fecha")
    ax.set_ylabel("Ventas")
    ax.grid(True)
    ax.legend()

    # Rotar las etiquetas de fecha para que no se solapen
    fig.autofmt_xdate()

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio22.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
