import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo Excel
archivo_excel = "CUCAITA.xlsx"
df = pd.read_excel(archivo_excel)

# Variables de datos
nombrecertificado = df.iloc[4, 7]
datospatron = df.iloc[8, 1:7].astype(int)
datos_seleccionados = df.iloc[11, 1:7].astype(float)
errorpromedio = (
    df.iloc[12, 1:7].astype(float).iloc[0]
)  # Tomar el primer valor de la serie
limitemaximo = max(datos_seleccionados)
limiteminimo = min(datos_seleccionados)
errores_promedio = [errorpromedio] * len(datospatron)
print(errorpromedio)
# Calcular los errores para las barras de error (distancia a los límites superior e inferior)
errores_superiores = limitemaximo - datos_seleccionados  # Distancia al límite máximo
errores_inferiores = datos_seleccionados - limiteminimo  # Distancia al límite mínimo
yerr = np.array(
    [errores_inferiores, errores_superiores]
)  # Crear array de errores para yerr


# Función para calcular límites idealmente
def calcular_limites(datos_seleccionados, errorpromedio):
    # Calcular el rango de los datos seleccionados
    limite_inferior_ideal = min(datos_seleccionados) - errorpromedio * 2
    limite_superior_ideal = max(datos_seleccionados) + errorpromedio * 2

    return limite_inferior_ideal, limite_superior_ideal


# Calcular límites usando el primer valor de errorpromedio
limite_infe, limite_superior = calcular_limites(
    datos_seleccionados, errorpromedio
)  # Usar el primer valor de la serie
print(limite_infe, limite_superior)
# Crear la figura y los ejes
fig, ax = plt.subplots()

# Graficar los datos solo con puntos, sin líneas
ax.scatter(datospatron, datos_seleccionados, color="blue", label="Datos seleccionados")

# Agregar barras de error que van desde el límite mínimo al límite máximo con remates
ax.errorbar(
    datospatron,
    datos_seleccionados,
    yerr=yerr,
    fmt="o",
    ecolor="#ffda8f",  # Color RGB(255, 170, 0) en formato de tupla normalizada
    capsize=15,  # Aumentar el tamaño del remate a las barras de error
    elinewidth=20,
    label="Desviacion estandar",
)

# Crear una línea de puntos para el error promedio en color rojo
ax.plot(datospatron, errores_promedio, "o-", color="red", markersize=5)

# Configuración de los ejes y otros elementos del gráfico
ax.set_ylim(limite_infe, limite_superior)
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
