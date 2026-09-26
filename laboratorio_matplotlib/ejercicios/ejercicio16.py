# -*- coding: utf-8 -*-
"""
EJERCICIO 16 — Funciones trigonométricas
Objetivo: graficar sen(x) y cos(x) sobre un periodo completo [0, 2π]
usando una malla densa generada con np.linspace.
Guarda el resultado en graficos/ejercicio16.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    # 500 puntos entre 0 y 2π (un periodo completo)
    x = np.linspace(0, 2 * np.pi, 500)

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(x, np.sin(x), label="sin(x)", color="tab:blue")
    ax.plot(x, np.cos(x), label="cos(x)", color="tab:red")

    ax.set_title("Funciones trigonométricas")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    ax.legend()

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio16.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
