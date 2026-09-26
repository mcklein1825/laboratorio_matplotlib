# -*- coding: utf-8 -*-
"""
EJERCICIO 2 — Personalizar una línea
Objetivo: personalizar el gráfico de líneas del ejercicio 1 usando
marker (marcadores), linestyle (línea discontinua) y linewidth (grosor).
Guarda el resultado en graficos/ejercicio02.png
"""
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    # Mismos datos del ejercicio 1
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
    ventas = [120, 150, 180, 160, 210, 250]

    fig, ax = plt.subplots(figsize=(8, 5))

    # Línea personalizada: marcadores circulares, trazo discontinuo y grosor 3
    ax.plot(
        meses,
        ventas,
        marker="o",          # marcadores circulares en cada punto
        linestyle="--",      # línea discontinua
        linewidth=3,         # grosor de línea
        color="tab:red",     # color de la línea
        markersize=8,        # tamaño de los marcadores
    )

    ax.set_title("Ventas de una empresa durante seis meses (línea personalizada)")
    ax.set_xlabel("Meses")
    ax.set_ylabel("Ventas")
    ax.grid(True)

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio02.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
