# -*- coding: utf-8 -*-
"""
EJERCICIO 3 — Gráfico de barras
Objetivo: crear un gráfico de barras verticales con ax.bar() para
comparar las ventas de distintos productos.
Guarda el resultado en graficos/ejercicio03.png
"""
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    # Datos del ejercicio
    productos = ["Laptop", "Monitor", "Teclado", "Mouse", "Impresora"]
    ventas = [35, 28, 45, 60, 20]

    fig, ax = plt.subplots(figsize=(8, 5))

    # Barras verticales con colores distintos por producto
    ax.bar(productos, ventas, color=["tab:blue", "tab:orange", "tab:green",
                                     "tab:red", "tab:purple"])

    ax.set_title("Ventas de productos")
    ax.set_xlabel("Productos")
    ax.set_ylabel("Ventas")
    ax.grid(True, axis="y")  # cuadrícula solo en el eje Y para no confundir

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio03.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
