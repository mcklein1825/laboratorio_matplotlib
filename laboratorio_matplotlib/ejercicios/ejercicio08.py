# -*- coding: utf-8 -*-
"""
EJERCICIO 8 — Boxplot
Objetivo: construir un diagrama de caja con ax.boxplot() y calcular en
consola los estadísticos principales: mínimo, Q1, mediana, Q3, máximo y
posibles valores atípicos.

Valores aproximados reportados en el README:
Mínimo: 10 | Q1: 14 | Mediana: 16 | Q3: 18 | Máximo: 20 | Atípicos: ninguno
Guarda el resultado en graficos/ejercicio08.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    # Mismas notas del ejercicio 7
    notas = [10, 12, 13, 14, 14, 15, 15, 15, 16, 16,
             17, 17, 18, 18, 18, 19, 19, 20]

    arreglo = np.array(notas)

    # Cálculo de estadísticos (percentil 25 = Q1, percentil 75 = Q3)
    minimo = np.min(arreglo)
    q1 = np.percentile(arreglo, 25)
    mediana = np.median(arreglo)
    q3 = np.percentile(arreglo, 75)
    maximo = np.max(arreglo)

    # Rango intercuartílico y límites para detectar valores atípicos
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    atipicos = arreglo[(arreglo < limite_inferior) | (arreglo > limite_superior)]

    # Impresión de resultados en consola
    print(f"Mínimo: {minimo}")
    print(f"Q1: {q1}")
    print(f"Mediana: {mediana}")
    print(f"Q3: {q3}")
    print(f"Máximo: {maximo}")
    print(f"Valores atípicos: {list(atipicos) if len(atipicos) else 'ninguno'}")

    fig, ax = plt.subplots(figsize=(6, 6))

    # Diagrama de caja vertical
    ax.boxplot(arreglo, patch_artist=True, boxprops=dict(facecolor="lightblue"))

    ax.set_title("Diagrama de caja de calificaciones")
    ax.set_ylabel("Calificaciones")
    ax.set_xticks([1])
    ax.set_xticklabels(["Notas"])
    ax.grid(True, axis="y")

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio08.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
