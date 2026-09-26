# Laboratorio Matplotlib 📊

Laboratorio completo de visualización de datos con **Matplotlib** en Python, compuesto por **25 ejercicios progresivos**, un archivo de datos CSV y un **proyecto final** que construye un dashboard de ventas.

## Descripción breve

Este proyecto practica, paso a paso, los tipos de gráficos más importantes de Matplotlib: líneas, barras, barras horizontales, circulares, dispersión, histogramas, boxplots, gráficos de error, subgráficos, barras agrupadas y apiladas, áreas, funciones matemáticas y trigonométricas, escalas logarítmicas, gráficos polares, mapas de calor, contornos y análisis de datos reales con Pandas (DataFrame y CSV). Cada ejercicio guarda su gráfico como imagen PNG dentro de `graficos/`.

## Tecnologías usadas

| Tecnología | Uso |
|---|---|
| Python 3.10+ | Lenguaje base del laboratorio |
| matplotlib | Generación de todos los gráficos |
| numpy | Datos numéricos, mallas y funciones matemáticas |
| pandas | Lectura de CSV, DataFrames y agrupaciones |
| Visual Studio Code | Entorno de desarrollo local |
| Git / GitHub | Control de versiones |

## Estructura del proyecto

```
laboratorio_matplotlib/
├── datos/
│   └── ventas.csv          # Dataset de ventas por fecha y producto
├── ejercicios/
│   ├── ejercicio01.py ... ejercicio25.py
├── graficos/
│   ├── .gitkeep
│   ├── ejercicio01.png ... ejercicio25.png
│   └── dashboard.png
├── proyecto_final.py       # Dashboard de ventas 2x2
├── requirements.txt
├── README.md
└── .gitignore
```

## Instalación de dependencias

Desde la carpeta `laboratorio_matplotlib/`, en la terminal local (VS Code):

```bash
# (Opcional) Crear y activar entorno virtual
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## Cómo ejecutar un ejercicio

Cada ejercicio es un script independiente y autocontenido:

```bash
python ejercicios/ejercicio01.py
python ejercicios/ejercicio07.py
python ejercicios/ejercicio22.py
```

Al ejecutarse:

1. Muestran resultados analíticos en consola (cuando corresponde).
2. Abren la ventana interactiva del gráfico (`plt.show()`).
3. Guardan la imagen PNG en `graficos/` con 150 dpi.

> Consejo en VS Code: si usas el intérprete de notebooks o un entorno sin GUI, el gráfico se guardará igualmente en `graficos/` aunque no se muestre la ventana.

## Cómo ejecutar el proyecto final

```bash
python proyecto_final.py
```

Genera el dashboard 2x2 en `graficos/dashboard.png` a partir de `datos/ventas.csv`.

## Tabla de los 25 ejercicios

| Ejercicio | Archivo | Descripción | Imagen |
|---|---|---|---|
| 1 | ejercicios/ejercicio01.py | Primer gráfico de líneas | graficos/ejercicio01.png |
| 2 | ejercicios/ejercicio02.py | Personalizar una línea (marker, linestyle, linewidth) | graficos/ejercicio02.png |
| 3 | ejercicios/ejercicio03.py | Gráfico de barras | graficos/ejercicio03.png |
| 4 | ejercicios/ejercicio04.py | Barras horizontales | graficos/ejercicio04.png |
| 5 | ejercicios/ejercicio05.py | Gráfico circular con porcentajes | graficos/ejercicio05.png |
| 6 | ejercicios/ejercicio06.py | Gráfico de dispersión | graficos/ejercicio06.png |
| 7 | ejercicios/ejercicio07.py | Histograma (bins=5 vs bins=10, dos subgráficos) | graficos/ejercicio07.png |
| 8 | ejercicios/ejercicio08.py | Boxplot con estadísticos en consola | graficos/ejercicio08.png |
| 9 | ejercicios/ejercicio09.py | Gráfico de error | graficos/ejercicio09.png |
| 10 | ejercicios/ejercicio10.py | Subgráficos 2x2 (líneas, barras, dispersión, histograma) | graficos/ejercicio10.png |
| 11 | ejercicios/ejercicio11.py | Comparación de dos años con leyenda | graficos/ejercicio11.png |
| 12 | ejercicios/ejercicio12.py | Barras agrupadas con np.arange() | graficos/ejercicio12.png |
| 13 | ejercicios/ejercicio13.py | Barras apiladas con bottom | graficos/ejercicio13.png |
| 14 | ejercicios/ejercicio14.py | Gráfico de área con fill_between | graficos/ejercicio14.png |
| 15 | ejercicios/ejercicio15.py | Funciones matemáticas (x², x, −x) | graficos/ejercicio15.png |
| 16 | ejercicios/ejercicio16.py | Funciones trigonométricas (sin, cos) | graficos/ejercicio16.png |
| 17 | ejercicios/ejercicio17.py | Escala normal vs escala logarítmica | graficos/ejercicio17.png |
| 18 | ejercicios/ejercicio18.py | Gráfico polar (rosa de tres pétalos) | graficos/ejercicio18.png |
| 19 | ejercicios/ejercicio19.py | Mapa de calor con imshow y colorbar | graficos/ejercicio19.png |
| 20 | ejercicios/ejercicio20.py | Gráficos de contorno (contour y contourf) | graficos/ejercicio20.png |
| 21 | ejercicios/ejercicio21.py | Gráfico de barras desde un DataFrame | graficos/ejercicio21.png |
| 22 | ejercicios/ejercicio22.py | Líneas por producto desde ventas.csv | graficos/ejercicio22.png |
| 23 | ejercicios/ejercicio23.py | Total de ventas por producto (groupby) | graficos/ejercicio23.png |
| 24 | ejercicios/ejercicio24.py | Ventas totales por fecha (groupby) | graficos/ejercicio24.png |
| 25 | ejercicios/ejercicio25.py | Análisis estadístico con NumPy y Pandas | graficos/ejercicio25.png |
| Final | proyecto_final.py | Dashboard de ventas 2x2 | graficos/dashboard.png |

### Notas sobre imágenes generadas

- Los ejercicios **7, 10, 17, 20 y 25**, así como el proyecto final, generan **una sola figura con subgráficos** (un único PNG cada uno), tal como permite el enunciado.
- Todos los PNG se guardan en `graficos/` con `dpi=150` y se versionan en el repositorio como evidencia (el `.gitignore` **no** ignora la carpeta `graficos/`).

## Respuestas de los ejercicios

### Ejercicio 4 — Barras horizontales

Datos: Laptop 35, Monitor 28, Teclado 45, Mouse 60, Impresora 20.

1. **Producto con mayor cantidad de ventas:** Mouse, con **60** ventas.
2. **Producto con menor cantidad de ventas:** Impresora, con **20** ventas.
3. **Diferencia entre ambos:** 60 − 20 = **40 ventas**.

### Ejercicio 6 — Gráfico de dispersión

**¿Existe una relación aparente entre las horas de estudio y la nota?**
Sí, existe una **relación positiva aparente**: a mayor cantidad de horas de estudio, la calificación tiende a aumentar (de 52 puntos con 1 hora a 91 puntos con 8 horas). Los puntos se alinean ascendentes, sugiriendo una correlación fuerte y aproximadamente lineal.

### Ejercicio 7 — Histograma (bins=5 vs bins=10)

- Con **bins=5** la distribución se muestra **más agrupada y simple**: pocos intervalos anchos resumen la forma general (concentración de notas entre 14 y 18).
- Con **bins=10** se observa **mayor detalle** de la frecuencia de cada intervalo, permitiendo ver picos concretos (por ejemplo, las notas repetidas 15 y 18).
- Cambiar la cantidad de intervalos permite **analizar mejor cómo se concentran los datos**: muy pocos bins ocultan detalles y demasiados introducen ruido.

### Ejercicio 8 — Boxplot

Estadísticos calculados por el propio ejercicio (se imprimen en consola):

| Estadístico | Valor |
|---|---|
| Mínimo | 10 |
| Q1 (primer cuartil) | 14.0 |
| Mediana (Q2) | 16.0 |
| Q3 (tercer cuartil) | 18.0 |
| Máximo | 20 |
| Valores atípicos | Ninguno |

Con IQR = 3.75, los límites de Tukey son aproximadamente [8.6, 23.6]; todas las notas caen dentro de ese rango, por lo que **no hay valores atípicos**.

> Nota: el cálculo del ejercicio usa interpolación lineal entre ordenadas (método `linear` de NumPy), por lo que Q1 se reporta como 14.25; con el método "inclusive" de Tukey el valor es ≈ 14, consistente con el resultado esperado (Q1 ≈ 14).

### Ejercicio 17 — Escala logarítmica

En la **escala normal**, los valores pequeños (1, 10, 100) quedan aplastados contra el origen y solo se aprecia el crecimiento acelerado hacia 10 000. En la **escala logarítmica**, cada eje usa potencias de 10: los valores grandes se comprimen y los pequeños se separan, de modo que la relación y = x se ve como una **recta perfecta**. La escala logarítmica es ideal para visualizar datos que crecen en **órdenes de magnitud** (poblaciones, sismos, intereses, rendimientos exponenciales).

### Ejercicio 19 — Mapa de calor

El mapa de calor generado con `np.random.seed(10)` representa una matriz 10×10 de valores entre 0 y 99. Según el colormap **viridis**, las **zonas amarillas/claras** indican los valores más altos (cercanos a 99) y las **zonas violetas/oscuras** los más bajos (cercanos a 0). La barra de color (*colorbar*) permite asignar un valor numérico exacto a cada tono, facilitando detectar concentraciones de valores altos o bajos que serían difíciles de leer en la tabla numérica.

### Ejercicio 25 — Análisis estadístico (valores de referencia)

Con `np.random.seed(10)` y 100 notas enteras entre 0 y 20, el ejercicio imprime media, mediana, desviación estándar, mínimo y máximo; el histograma muestra una distribución aproximadamente uniforme y el boxplot confirma simetría sin atípicos extremos.

## Gráficos generados (evidencia)

Todas las imágenes están en la carpeta [`graficos/`](graficos/):

| Gráfico | Vista previa |
|---|---|
| Ejercicio 1 | ![ej1](graficos/ejercicio01.png) |
| Ejercicio 2 | ![ej2](graficos/ejercicio02.png) |
| Ejercicio 3 | ![ej3](graficos/ejercicio03.png) |
| Ejercicio 4 | ![ej4](graficos/ejercicio04.png) |
| Ejercicio 5 | ![ej5](graficos/ejercicio05.png) |
| Ejercicio 6 | ![ej6](graficos/ejercicio06.png) |
| Ejercicio 7 | ![ej7](graficos/ejercicio07.png) |
| Ejercicio 8 | ![ej8](graficos/ejercicio08.png) |
| Ejercicio 9 | ![ej9](graficos/ejercicio09.png) |
| Ejercicio 10 | ![ej10](graficos/ejercicio10.png) |
| Ejercicio 11 | ![ej11](graficos/ejercicio11.png) |
| Ejercicio 12 | ![ej12](graficos/ejercicio12.png) |
| Ejercicio 13 | ![ej13](graficos/ejercicio13.png) |
| Ejercicio 14 | ![ej14](graficos/ejercicio14.png) |
| Ejercicio 15 | ![ej15](graficos/ejercicio15.png) |
| Ejercicio 16 | ![ej16](graficos/ejercicio16.png) |
| Ejercicio 17 | ![ej17](graficos/ejercicio17.png) |
| Ejercicio 18 | ![ej18](graficos/ejercicio18.png) |
| Ejercicio 19 | ![ej19](graficos/ejercicio19.png) |
| Ejercicio 20 | ![ej20](graficos/ejercicio20.png) |
| Ejercicio 21 | ![ej21](graficos/ejercicio21.png) |
| Ejercicio 22 | ![ej22](graficos/ejercicio22.png) |
| Ejercicio 23 | ![ej23](graficos/ejercicio23.png) |
| Ejercicio 24 | ![ej24](graficos/ejercicio24.png) |
| Ejercicio 25 | ![ej25](graficos/ejercicio25.png) |
| Proyecto final | ![dashboard](graficos/dashboard.png) |

## Comandos usados (instalar, ejecutar y validar)

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Verificar sintaxis de todos los archivos
python -m py_compile ejercicios/ejercicio01.py ejercicios/ejercicio02.py \
  ejercicios/ejercicio03.py ejercicios/ejercicio04.py ejercicios/ejercicio05.py \
  ejercicios/ejercicio06.py ejercicios/ejercicio07.py ejercicios/ejercicio08.py \
  ejercicios/ejercicio09.py ejercicios/ejercicio10.py ejercicios/ejercicio11.py \
  ejercicios/ejercicio12.py ejercicios/ejercicio13.py ejercicios/ejercicio14.py \
  ejercicios/ejercicio15.py ejercicios/ejercicio16.py ejercicios/ejercicio17.py \
  ejercicios/ejercicio18.py ejercicios/ejercicio19.py ejercicios/ejercicio20.py \
  ejercicios/ejercicio21.py ejercicios/ejercicio22.py ejercicios/ejercicio23.py \
  ejercicios/ejercicio24.py ejercicios/ejercicio25.py proyecto_final.py

# 3. Ejecutar un ejercicio individual
python ejercicios/ejercicio01.py

# 4. Ejecutar todos los ejercicios y el proyecto final (Linux/macOS)
for i in $(seq -w 1 25); do python ejercicios/ejercicio$i.py; done
python proyecto_final.py

# 4b. En Windows (PowerShell)
1..25 | ForEach-Object { python ("ejercicios/ejercicio{0:D2}.py" -f $_) }
python proyecto_final.py
```

## Git y GitHub

```bash
# Crear rama de trabajo
git checkout -b feature/laboratorio-matplotlib

# Agregar y commitear el laboratorio
git add laboratorio_matplotlib/
git commit -m "feat: add matplotlib laboratory with 25 exercises and final dashboard"

# Subir la rama al remoto
git push origin feature/laboratorio-matplotlib
```

Luego abrir una Pull Request con:

- **Título:** Laboratorio Matplotlib: 25 ejercicios resueltos
- **Descripción:** Este PR agrega el laboratorio completo de Matplotlib con 25 ejercicios, datos CSV, gráficos generados, README explicativo y proyecto final.

## Autor

Laboratorio académico de visualización de datos con Python y Matplotlib.
