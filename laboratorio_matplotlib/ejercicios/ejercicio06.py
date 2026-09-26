# -*- coding: utf-8 -*-
"""
EJERCICIO 6 — Gráfico de dispersión
Objetivo: analizar la relación entre las horas de estudio y la calificación
obtenida usando ax.scatter().

Pregunta respondida en el README:
¿Existe una relación aparente entre las horas de estudio y la nota?
-> Sí, existe una relación positiva aparente: a mayor cantidad de horas
   de estudio, la calificación tiende a aumentar.
Guarda el resultado en graficos/ejercicio06.png
"""
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
GRAFICOS = ROOT / "graficos"
GRAFICOS.mkdir(parents=True, exist_ok=True)


def main():
    # Datos del ejercicio
    horas = [1, 2, 3, 4, 5, 6, 7, 8]
    notas = [52, 55, 60, 65, 70, 76, 84, 91]

    fig, ax = plt.subplots(figsize=(8, 5))

    # Nube de puntos: cada punto es (hora de estudio, calificación)
    ax.scatter(horas, notas, color="tab:purple", s=80)

    ax.set_title("Relación entre horas de estudio y calificación")
    ax.set_xlabel("Horas de estudio")
    ax.set_ylabel("Calificación")
    ax.grid(True)

    plt.tight_layout()
    plt.savefig(GRAFICOS / "ejercicio06.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
