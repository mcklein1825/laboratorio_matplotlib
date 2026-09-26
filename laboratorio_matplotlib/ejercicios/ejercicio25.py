# -*- coding: utf-8 -*-
"""
EJERCICIO 25 — Análisis estadístico
Objetivo: generar 100 notas aleatorias con NumPy (semilla fija), cargarlas
en un DataFrame de Pandas, calcular estadísticos básicos (media, mediana,
desviación estándar, mínimo y máximo) y visualizar la distribución con un
histograma y un boxplot en dos subgráficos.
Guarda el resultado en graficos/ejercicio25.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    # Semilla fija para reproducibilidad y generación de 100 notas 0..20
    np.random.seed(10)
    notas = np.random.randint(0, 21, 100)

    # Carga de las notas en un DataFrame
    df = pd.DataFrame({
        "Nota": notas
    })

    # Cálculo e impresión de estadísticos descriptivos
    print(f"Media:                 {df['Nota'].mean()}")
    print(f"Mediana:               {df['Nota'].median()}")
    print(f"Desviación estándar:   {df['Nota'].std()}")
    print(f"Mínimo:                {df['Nota'].min()}")
    print(f"Máximo:                {df['Nota'].max()}")

    # Dos subgráficos: histograma (izquierda) y boxplot (derecha)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # 1. Histograma de la distribución de notas
    ax1.hist(df["Nota"], bins=10, color="tab:blue", edgecolor="black")
    ax1.set_title("Histograma de notas")
    ax1.set_xlabel("Nota")
    ax1.set_ylabel("Frecuencia")
    ax1.grid(True, axis="y")

    # 2. Diagrama de caja de las mismas notas
    ax2.boxplot(df["Nota"], patch_artist=True,
                boxprops=dict(facecolor="lightgreen"))
    ax2.set_title("Boxplot de notas")
    ax2.set_ylabel("Nota")
    ax2.set_xticks([1])
    ax2.set_xticklabels(["Notas"])
    ax2.grid(True, axis="y")

    fig.suptitle("Análisis estadístico de notas")

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio25.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
