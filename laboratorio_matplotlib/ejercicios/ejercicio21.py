# -*- coding: utf-8 -*-
"""
EJERCICIO 21 — Crear un DataFrame
Objetivo: construir un DataFrame de Pandas a partir de un diccionario,
imprimirlo en consola y graficar una de sus columnas con un gráfico de
barras usando directamente df["Producto"] y df["Ventas"].
Guarda el resultado en graficos/ejercicio21.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    # Datos del ejercicio en forma de diccionario
    datos = {
        "Producto": ["Laptop", "Monitor", "Teclado", "Mouse", "Impresora"],
        "Ventas": [35, 28, 45, 60, 20],
        "Precio": [2500, 900, 120, 60, 800],
    }

    # Creación del DataFrame e impresión en consola
    df = pd.DataFrame(datos)
    print(df)

    fig, ax = plt.subplots(figsize=(8, 5))

    # Se usa directamente el DataFrame como fuente de las series
    ax.bar(df["Producto"], df["Ventas"], color="tab:blue")

    ax.set_title("Ventas por producto desde DataFrame")
    ax.set_xlabel("Productos")
    ax.set_ylabel("Ventas")
    ax.grid(True, axis="y")

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio21.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
