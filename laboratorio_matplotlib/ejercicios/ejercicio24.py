# -*- coding: utf-8 -*-
"""
EJERCICIO 24 — Ventas por fecha
Objetivo: leer datos/ventas.csv, agrupar la suma de ventas por fecha con
df.groupby("Fecha")["Ventas"].sum() y mostrar la evolución temporal con una
línea con marcadores.
Guarda el resultado en graficos/ejercicio24.png
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

    # Lectura del CSV y conversión de la columna de fechas
    df = pd.read_csv(ruta_csv)
    df["Fecha"] = pd.to_datetime(df["Fecha"])

    # Suma de ventas por fecha
    ventas_fecha = df.groupby("Fecha")["Ventas"].sum()
    print(ventas_fecha)

    fig, ax = plt.subplots(figsize=(9, 5))

    # Línea temporal con marcadores circulares
    ax.plot(ventas_fecha.index, ventas_fecha.values, marker="o",
            color="tab:blue", linewidth=2)

    ax.set_title("Ventas totales por fecha")
    ax.set_xlabel("Fecha")
    ax.set_ylabel("Ventas")
    ax.grid(True)

    # Rotar etiquetas del eje X para mejorar la legibilidad
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio24.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
