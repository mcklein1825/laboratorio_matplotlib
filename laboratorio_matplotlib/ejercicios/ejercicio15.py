# -*- coding: utf-8 -*-
"""
EJERCICIO 15 — Funciones matemáticas
Objetivo: graficar tres funciones elementales sobre el mismo eje usando
una malla densa de puntos generada con np.linspace(-10, 10, 500):
y = x**2, y = x y y = -x.
Guarda el resultado en graficos/ejercicio15.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    # Malla de 500 puntos entre -10 y 10 para curvas suaves
    x = np.linspace(-10, 10, 500)

    # Las tres funciones pedidas
    y_parabola = x ** 2
    y_identidad = x
    y_opuesta = -x

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot(x, y_parabola, label="y = x²", color="tab:blue")
    ax.plot(x, y_identidad, label="y = x", color="tab:orange")
    ax.plot(x, y_opuesta, label="y = -x", color="tab:green")

    ax.set_title("Funciones matemáticas")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    ax.legend()

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio15.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
