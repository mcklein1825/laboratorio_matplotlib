# -*- coding: utf-8 -*-
"""
EJERCICIO 9 — Gráfico de error
Objetivo: representar mediciones junto con su margen de error usando
ax.errorbar(), que dibuja barras verticales de error en cada punto.
Guarda el resultado en graficos/ejercicio09.png
"""
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    # Datos del ejercicio
    x = [1, 2, 3, 4, 5]
    valores = [20, 25, 28, 32, 35]
    errores = [2, 1, 3, 2, 4]

    fig, ax = plt.subplots(figsize=(8, 5))

    # Línea con marcadores y barras de error simétricas (fmt="-o")
    ax.errorbar(x, valores, yerr=errores, fmt="-o", capsize=5,
                ecolor="tab:red", elinewidth=2, color="tab:blue", label="Medición")

    ax.set_title("Mediciones con margen de error")
    ax.set_xlabel("Medición")
    ax.set_ylabel("Valor")
    ax.grid(True)
    ax.legend()

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio09.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
