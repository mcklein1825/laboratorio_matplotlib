# -*- coding: utf-8 -*-
"""
EJERCICIO 20 — Gráfico de contorno
Objetivo: representar la función Z = X² + Y² sobre una malla bidimensional,
comparando contornos solo con líneas (contour) y contornos rellenos
(contourf) en dos subgráficos.
Guarda el resultado en graficos/ejercicio20.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    # Ejes y malla bidimensional
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)

    # Función paraboloide: Z = X² + Y²
    Z = X ** 2 + Y ** 2

    # Dos subgráficos lado a lado
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Izquierda: curvas de nivel trazadas con líneas
    curvas1 = ax1.contour(X, Y, Z)
    ax1.clabel(curvas1, inline=True, fontsize=8)  # etiquetas de nivel
    ax1.set_title("Contorno con líneas (contour)")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")

    # Derecha: regiones de nivel rellenas de color
    curvas2 = ax2.contourf(X, Y, Z, levels=15, cmap="viridis")
    fig.colorbar(curvas2, ax=ax2, label="Z")
    ax2.set_title("Contorno relleno (contourf)")
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")

    fig.suptitle("Gráficos de contorno")

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio20.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
