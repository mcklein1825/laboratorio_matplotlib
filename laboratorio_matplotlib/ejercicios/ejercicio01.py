# -*- coding: utf-8 -*-
"""
EJERCICIO 1 — Primer gráfico de líneas
Objetivo: crear un gráfico de líneas simple con plt.plot()/ax.plot(),
mostrando las ventas de una empresa durante seis meses.
Guarda el resultado en graficos/ejercicio01.png
"""
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    # Datos del ejercicio
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
    ventas = [120, 150, 180, 160, 210, 250]

    # Crear la figura y el eje
    fig, ax = plt.subplots(figsize=(8, 5))

    # Graficar la línea de ventas
    ax.plot(meses, ventas, color="tab:blue")

    # Títulos y etiquetas en español
    ax.set_title("Ventas de una empresa durante seis meses")
    ax.set_xlabel("Meses")
    ax.set_ylabel("Ventas")

    # Mostrar cuadrícula
    ax.grid(True)

    # Ajustar, guardar, mostrar y liberar memoria
    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio01.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
