# -*- coding: utf-8 -*-
"""
EJERCICIO 5 — Gráfico circular
Objetivo: representar la participación porcentual de las ventas de cada
producto con ax.pie(), mostrando los porcentajes con autopct.
Guarda el resultado en graficos/ejercicio05.png
"""
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    # Datos del ejercicio
    productos = ["Laptop", "Monitor", "Teclado", "Mouse", "Impresora"]
    ventas = [35, 28, 45, 60, 20]

    fig, ax = plt.subplots(figsize=(7, 7))

    # Gráfico circular con porcentajes sobre cada porción
    ax.pie(
        ventas,
        labels=productos,
        autopct="%1.1f%%",  # muestra el porcentaje con un decimal
        startangle=90,      # primera porción comienza arriba
    )

    ax.set_title("Participación de ventas por producto")
    ax.axis("equal")  # fuerza que el pastel sea circular

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio05.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
