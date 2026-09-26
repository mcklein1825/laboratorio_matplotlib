# -*- coding: utf-8 -*-
"""
EJERCICIO 19 — Mapa de calor
Objetivo: visualizar una matriz de valores con plt.imshow() usando el mapa
de color "viridis" y una barra de color (colorbar) para interpretar los
valores. Se fija la semilla con np.random.seed(10) para reproducibilidad.

Interpretación incluida en el README:
Las zonas más claras/amarillas corresponden a los valores más altos y las
zonas más oscuras/violetas a los valores más bajos; el colorbar permite
asignar un valor numérico a cada color.
Guarda el resultado en graficos/ejercicio19.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    # Semilla fija para que el mapa de calor sea siempre idéntico
    np.random.seed(10)

    # Matriz de 10x10 con enteros aleatorios entre 0 y 99
    datos = np.random.randint(0, 100, (10, 10))

    print("Valor máximo:", datos.max(), "en posición", np.unravel_index(datos.argmax(), datos.shape))
    print("Valor mínimo:", datos.min(), "en posición", np.unravel_index(datos.argmin(), datos.shape))

    fig, ax = plt.subplots(figsize=(7, 6))

    # Cada celda se pinta según su valor usando el colormap viridis
    imagen = ax.imshow(datos, cmap="viridis")

    # Barra lateral que traduce colores a valores numéricos
    fig.colorbar(imagen, ax=ax, label="Valor")

    ax.set_title("Mapa de calor")
    ax.set_xlabel("Columna")
    ax.set_ylabel("Fila")

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio19.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
