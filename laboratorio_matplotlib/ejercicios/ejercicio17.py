# -*- coding: utf-8 -*-
"""
EJERCICIO 17 — Escala logarítmica
Objetivo: comparar la misma serie de datos (que crece por órdenes de
magnitud) en escala normal y en escala logarítmica en ambos ejes.

Explicación incluida en el README:
En escala normal los valores pequeños quedan comprimidos contra el origen;
la escala logarítmica comprime los valores grandes y permite visualizar
mejor datos que crecen en órdenes de magnitud (una recta indica crecimiento
multiplicativo/potencial).
Guarda el resultado en graficos/ejercicio17.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    # Datos del ejercicio: potencias de 10
    x = np.array([1, 10, 100, 1000, 10000])
    y = np.array([1, 10, 100, 1000, 10000])

    # Dos subgráficos lado a lado
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Subgráfico 1: escala normal (lineal)
    ax1.plot(x, y, marker="o", color="tab:blue")
    ax1.set_title("Escala normal")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.grid(True)

    # Subgráfico 2: escala logarítmica en ambos ejes
    ax2.plot(x, y, marker="o", color="tab:red")
    ax2.set_xscale("log")  # equivalente funcional a plt.xscale("log")
    ax2.set_yscale("log")  # equivalente funcional a plt.yscale("log")
    ax2.set_title("Escala logarítmica")
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    ax2.grid(True, which="both")

    fig.suptitle("Comparación entre escala normal y escala logarítmica")

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio17.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
