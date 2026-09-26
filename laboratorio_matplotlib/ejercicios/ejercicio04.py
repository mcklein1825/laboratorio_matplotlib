# -*- coding: utf-8 -*-
"""
EJERCICIO 4 — Barras horizontales
Objetivo: repetir el gráfico de barras del ejercicio 3 pero en sentido
horizontal con ax.barh().

Preguntas respondidas en el README:
1. ¿Qué producto tiene mayor cantidad de ventas? -> Mouse, con 60 ventas.
2. ¿Cuál tiene menor cantidad?                    -> Impresora, con 20 ventas.
3. ¿Qué diferencia existe entre ambos?            -> 40 ventas.
Guarda el resultado en graficos/ejercicio04.png
"""
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    # Mismos datos del ejercicio 3
    productos = ["Laptop", "Monitor", "Teclado", "Mouse", "Impresora"]
    ventas = [35, 28, 45, 60, 20]

    fig, ax = plt.subplots(figsize=(8, 5))

    # Barras horizontales
    ax.barh(productos, ventas, color="tab:green")

    ax.set_title("Ventas de productos de forma horizontal")
    ax.set_xlabel("Ventas")
    ax.set_ylabel("Productos")
    ax.grid(True, axis="x")

    # Análisis rápido impreso en consola
    mayor = productos[ventas.index(max(ventas))]
    menor = productos[ventas.index(min(ventas))]
    print(f"Producto con mayor cantidad de ventas: {mayor} ({max(ventas)})")
    print(f"Producto con menor cantidad de ventas: {menor} ({min(ventas)})")
    print(f"Diferencia entre ambos: {max(ventas) - min(ventas)} ventas")

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio04.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
