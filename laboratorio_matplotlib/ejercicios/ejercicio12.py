# -*- coding: utf-8 -*-
"""
EJERCICIO 12 — Barras agrupadas
Objetivo: comparar las ventas de dos años por producto usando barras
agrupadas. Se calculan las posiciones con np.arange() y se desplaza un
grupo respecto al otro con un ancho width=0.35.
Guarda el resultado en graficos/ejercicio12.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    # Datos del ejercicio
    productos = ["Laptop", "Monitor", "Teclado", "Mouse"]
    ventas_2025 = [20, 30, 40, 50]
    ventas_2026 = [25, 35, 45, 65]

    # Posiciones base de cada grupo y ancho de cada barra
    x = np.arange(len(productos))
    width = 0.35

    fig, ax = plt.subplots(figsize=(8, 5))

    # Cada serie se desplaza medio ancho a izquierda/derecha del centro
    ax.bar(x - width / 2, ventas_2025, width, label="2025", color="tab:blue")
    ax.bar(x + width / 2, ventas_2026, width, label="2026", color="tab:orange")

    # Centrar las etiquetas del eje X en cada grupo de barras
    ax.set_xticks(x)
    ax.set_xticklabels(productos)

    ax.set_title("Comparación de ventas por producto")
    ax.set_xlabel("Productos")
    ax.set_ylabel("Ventas")
    ax.grid(True, axis="y")
    ax.legend()

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio12.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
