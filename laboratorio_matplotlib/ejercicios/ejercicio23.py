# -*- coding: utf-8 -*-
"""
EJERCICIO 23 — Ventas por producto
Objetivo: leer datos/ventas.csv, agrupar la suma de ventas por producto con
df.groupby("Producto")["Ventas"].sum() y representar el total con barras.
Guarda el resultado en graficos/ejercicio23.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    ruta_csv = ROOT / "datos" / "ventas.csv"

    if not ruta_csv.exists():
        print(f"ERROR: no se encontró el archivo {ruta_csv}.")
        print("Asegúrate de que exista datos/ventas.csv dentro del proyecto.")
        return

    # Lectura del CSV
    df = pd.read_csv(ruta_csv)

    # Suma total de ventas por producto
    resumen = df.groupby("Producto")["Ventas"].sum()
    print(resumen)

    fig, ax = plt.subplots(figsize=(8, 5))

    # Barras con los totales por producto
    ax.bar(resumen.index, resumen.values, color="tab:orange")

    ax.set_title("Total de ventas por producto")
    ax.set_xlabel("Producto")
    ax.set_ylabel("Ventas")
    ax.grid(True, axis="y")

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio23.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
