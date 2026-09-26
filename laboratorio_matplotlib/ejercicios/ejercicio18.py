# -*- coding: utf-8 -*-
"""
EJERCICIO 18 — Gráfico polar
Objetivo: dibujar una curva en coordenadas polares con plt.polar().
La ecuación r = 1 + sin(3θ) produce una rosa de tres pétalos.
Guarda el resultado en graficos/ejercicio18.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    # Ángulo entre 0 y 2π; radio dado por la ecuación pedida
    theta = np.linspace(0, 2 * np.pi, 500)
    r = 1 + np.sin(3 * theta)

    # Figura con proyección polar
    fig = plt.figure(figsize=(7, 7))
    ax = plt.subplot(111, projection="polar")

    # Equivalente al uso de plt.polar(theta, r)
    ax.plot(theta, r, color="tab:green", linewidth=2)
    ax.fill(theta, r, alpha=0.2, color="tab:green")

    ax.set_title("Gráfico polar", pad=20)

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio18.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
