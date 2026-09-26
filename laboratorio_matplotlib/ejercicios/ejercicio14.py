# -*- coding: utf-8 -*-
"""
EJERCICIO 14 — Gráfico de área
Objetivo: representar la evolución mensual de ventas rellenando el área
bajo la curva con ax.fill_between(), lo que enfatiza el volumen acumulado.
Guarda el resultado en graficos/ejercicio14.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    # Datos del ejercicio: meses 1..12 y sus ventas
    meses = np.arange(1, 13)
    ventas = [100, 120, 140, 130, 160, 180, 190, 200, 220, 210, 240, 260]

    fig, ax = plt.subplots(figsize=(9, 5))

    # Área sombreada bajo la curva (con transparencia) y línea superior
    ax.fill_between(meses, ventas, color="tab:cyan", alpha=0.4,
                    label="Área de ventas")
    ax.plot(meses, ventas, color="tab:blue", linewidth=2)

    ax.set_title("Evolución de ventas")
    ax.set_xlabel("Meses")
    ax.set_ylabel("Ventas")
    ax.grid(True)
    ax.legend()

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio14.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
