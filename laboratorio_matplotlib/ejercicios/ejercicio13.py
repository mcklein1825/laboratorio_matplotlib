# -*- coding: utf-8 -*-
"""
EJERCICIO 13 — Barras apiladas
Objetivo: mostrar cómo se componen las ventas totales de cada producto
entre el canal online y el canal tienda, apilando la segunda serie sobre
la primera con el parámetro bottom.
Guarda el resultado en graficos/ejercicio13.png
"""
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    # Datos del ejercicio
    productos = ["Laptop", "Monitor", "Mouse"]
    online = [20, 30, 40]
    tienda = [15, 25, 30]

    fig, ax = plt.subplots(figsize=(8, 5))

    # Primero la base (online); encima se apila tienda con bottom=online
    ax.bar(productos, online, label="Online", color="tab:blue")
    ax.bar(productos, tienda, bottom=online, label="Tienda", color="tab:green")

    ax.set_title("Ventas por canal")
    ax.set_xlabel("Productos")
    ax.set_ylabel("Ventas")
    ax.grid(True, axis="y")
    ax.legend()

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio13.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
