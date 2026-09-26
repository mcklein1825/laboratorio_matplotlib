# -*- coding: utf-8 -*-
"""
EJERCICIO 11 — Comparación de dos años
Objetivo: dibujar dos líneas en el mismo gráfico (ventas 2025 vs 2026),
etiquetándolas con label y mostrándolas mediante una leyenda.
Guarda el resultado en graficos/ejercicio11.png
"""
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    # Datos del ejercicio
    meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
    ventas_2025 = [100, 120, 150, 140, 180, 200]
    ventas_2026 = [110, 130, 170, 160, 210, 240]

    fig, ax = plt.subplots(figsize=(8, 5))

    # Dos series en el mismo eje; label alimenta la leyenda
    ax.plot(meses, ventas_2025, marker="o", linestyle="-", color="tab:blue",
            label="2025")
    ax.plot(meses, ventas_2026, marker="s", linestyle="--", color="tab:orange",
            label="2026")

    ax.set_title("Comparación de ventas 2025 vs 2026")
    ax.set_xlabel("Meses")
    ax.set_ylabel("Ventas")
    ax.grid(True)
    ax.legend()  # mostrar la leyenda con ambas series

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio11.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
