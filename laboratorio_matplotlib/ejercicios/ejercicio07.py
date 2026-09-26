# -*- coding: utf-8 -*-
"""
EJERCICIO 7 — Histograma
Objetivo: comparar cómo cambia la apariencia de un histograma al variar la
cantidad de intervalos (bins). Se crean dos subgráficos: bins=5 y bins=10.

Análisis incluido en el README:
- Con bins=5 la distribución se muestra más agrupada y simple.
- Con bins=10 se observa mayor detalle de la frecuencia de cada intervalo.
Guarda el resultado en graficos/ejercicio07.png
"""
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    # Datos del ejercicio
    notas = [10, 12, 13, 14, 14, 15, 15, 15, 16, 16,
             17, 17, 18, 18, 18, 19, 19, 20]

    # Figura con dos subgráficos lado a lado
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Izquierda: histograma con pocos intervalos (más agrupado)
    ax1.hist(notas, bins=5, color="tab:blue", edgecolor="black")
    ax1.set_title("Histograma con bins=5")
    ax1.set_xlabel("Nota")
    ax1.set_ylabel("Frecuencia")
    ax1.grid(True)

    # Derecha: histograma con más intervalos (mayor detalle)
    ax2.hist(notas, bins=10, color="tab:orange", edgecolor="black")
    ax2.set_title("Histograma con bins=10")
    ax2.set_xlabel("Nota")
    ax2.set_ylabel("Frecuencia")
    ax2.grid(True)

    # Super título de la figura
    fig.suptitle("Histograma de calificaciones")

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio07.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
