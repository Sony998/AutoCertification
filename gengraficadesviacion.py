import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo Excel
archivo_excel = "CUCAITA.xlsx"
df = pd.read_excel(archivo_excel)
def calcular_limites(errorpromedio):
    limite_inferior_ideal = errorpromedio * -2
    limite_superior_ideal = errorpromedio * 2
    return limite_inferior_ideal, limite_superior_ideal


nombrecertificado = df.iloc[4, 7]
datospatron = df.iloc[8, 1:7].astype(int)
datos_seleccionados = df.iloc[11, 1:7].astype(float)
errorpromedio = df.iloc[12, 1:7].astype(float)  # Obtener error promedio como una serie de datos para graficar puntos
limitemaximo = max(datos_seleccionados)
errores_promedio = [errorpromedio] * len(datospatron)
limiteminimo = min(datos_seleccionados)
limite_infe, limite_superior = calcular_limites(errorpromedio)

# Calcular los errores para las barras de error (distancia a los límites superior e inferior)
errores_superiores = limitemaximo - datos_seleccionados  # Distancia al límite máximo
errores_inferiores = datos_seleccionados - limiteminimo  # Distancia al límite mínimo
yerr = np.array([errores_inferiores, errores_superiores])  # Crear array de errores para yerr

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Graficar los datos solo con puntos, sin líneas
ax.scatter(datospatron, datos_seleccionados, color="blue", label="Datos obtenidos")

# Agregar barras de error que van desde el límite mínimo al límite máximo con remates
ax.errorbar(
    datospatron,
    datos_seleccionados,
    yerr=yerr,
    fmt="o",
    ecolor="#f0d16c",  # Color RGB(255, 170, 0) en formato de tupla normalizada
    capsize=15,               # Agregar remate a las barras de error
    elinewidth=20,
    label="Desviacion estandar",
)

# Crear una línea de puntos para el error promedio en color rojo
ax.plot(datospatron, errores_promedio, 'o-', color="red", markersize=5)

ax.set_ylim(limite_infe.min(), limite_superior.max())
ax.set_xticks(np.arange(min(datospatron), max(datospatron) + 1, 20))
ax.grid(True, which="both", linestyle="--", linewidth=0.5)
ax.set_xlabel("PATRON")
ax.set_ylabel("ERROR")
ax.set_title(
    "E.S.E CENTRO DE SALUD SANTA LUCIA \n" + nombrecertificado,
    fontsize=10,
    fontweight="bold",
)
ax.legend()

# Guardar la gráfica en un archivo PNG
plt.savefig("variacion_datos.png")
# Mostrar la gráfica
plt.show()
