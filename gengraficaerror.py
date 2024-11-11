import pandas as pd
import matplotlib.pyplot as plt
# Cargar el archivo Excel
archivo_excel = 'CUCAITA3.xlsx'
df = pd.read_excel(archivo_excel, sheet_name='TERMOHIGROMETRO')
# Cargar el archivo Excel
nombrecertificado = df.iat[4, 7]  # Usar índice entero iat para evitar problemas de etiquetas
datospatron = df.iloc[8, 1:7].astype(int)  # Fila 9 (índice 9) y columnas 1 a 6 (excluyendo la última)
datos_seleccionados = df.iloc[10, 1:7]
print(nombrecertificado)
print(datos_seleccionados)
print(datospatron)

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Graficar los datos solo con puntos, sin líneas
ax.scatter(datospatron, datos_seleccionados, color='blue')
ax.set_ylim(-6, 3)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.set_xlabel('PATRON')
ax.set_ylabel('ERROR')
ax.set_title('E.S.E CENTRO DE SALUD SANTA LUCIA \n' + nombrecertificado , fontsize=10, fontweight='bold')

# Guardar la gráfica en un archivo PNG
plt.savefig('variacion_datos.png')

# Mostrar la gráfica
plt.show()
