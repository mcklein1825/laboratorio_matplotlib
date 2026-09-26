# -*- coding: utf-8 -*-
"""
EJERCICIO 10 — Primer conjunto de subgráficos
Objetivo: crear una figura 2x2 con plt.subplots(2, 2) que combine cuatro
tipos de gráfico básicos: líneas, barras, dispersión e histograma.
Guarda el resultado en graficos/ejercicio10.png
"""
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    # Datos reutilizados de ejercicios anteriores
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
    ventas = [120, 150, 180, 160, 210, 250]

    productos = ["Laptop", "Monitor", "Teclado", "Mouse", "Impresora"]
    ventas_prod = [35, 28, 45, 60, 20]

    horas = [1, 2, 3, 4, 5, 6, 7, 8]
    notas = [52, 55, 60, 65, 70, 76, 84, 91]

    notas_hist = [10, 12, 13, 14, 14, 15, 15, 15, 16, 16,
                  17, 17, 18, 18, 18, 19, 19, 20]

    # Figura de 2 filas x 2 columnas compartiendo tamaño
    fig, ejes = plt.subplots(2, 2, figsize=(11, 8))

    # Desempaquetar los cuatro ejes para mayor claridad
    ax_lineas = ejes[0, 0]
    ax_barras = ejes[0, 1]
    ax_dispersion = ejes[1, 0]
    ax_histograma = ejes[1, 1]

    # 1. Gráfico de líneas
    ax_lineas.plot(meses, ventas, color="tab:blue")
    ax_lineas.set_title("Ventas mensuales (líneas)")
    ax_lineas.grid(True)

    # 2. Gráfico de barras
    ax_barras.bar(productos, ventas_prod, color="tab:orange")
    ax_barras.set_title("Ventas por producto (barras)")
    ax_barras.grid(True, axis="y")

    # 3. Gráfico de dispersión
    ax_dispersion.scatter(horas, notas, color="tab:green")
    ax_dispersion.set_title("Horas vs nota (dispersión)")
    ax_dispersion.set_xlabel("Horas de estudio")
    ax_dispersion.set_ylabel("Calificación")
    ax_dispersion.grid(True)

    # 4. Histograma
    ax_histograma.hist(notas_hist, bins=5, color="tab:purple", edgecolor="black")
    ax_histograma.set_title("Distribución de notas (histograma)")
    ax_histograma.grid(True, axis="y")

    # Super título general de la figura
    fig.suptitle("Combinación de gráficos básicos en subgráficos 2x2")

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio10.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
