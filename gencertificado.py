import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos desde el archivo de Excel
# Asegúrate de reemplazar 'ruta_del_archivo.xlsx' con la ruta real de tu archivo de Excel
ruta_archivo = 'CUCAITA.xlsx'
df = pd.read_excel(ruta_archivo)

# Definir los datos de referencia (patrones) y los valores medidos
patron = df.columns[1:].astype(float)  # Convierte los nombres de las columnas a números
primera = df.iloc[0, 1:].values.astype(float)  # Datos de la primera fila
segunda = df.iloc[1, 1:].values.astype(float)  # Datos de la segunda fila

# Calcular el error en cada medida
errores_primera = np.abs(primera - patron)
errores_segunda = np.abs(segunda - patron)

# Crear la gráfica de error
plt.figure(figsize=(10, 6))
plt.errorbar(patron, primera, yerr=errores_primera, fmt='o-', label='Primera Medición', capsize=5)
plt.errorbar(patron, segunda, yerr=errores_segunda, fmt='s-', label='Segunda Medición', capsize=5)

# Personalizar la gráfica
plt.title('Gráfica de Error de Mediciones')
plt.xlabel('Patrón (mmHg)')
plt.ylabel('Mediciones (mmHg)')
plt.legend()
plt.grid(True)

# Guardar la gráfica como PNG
plt.savefig('grafica_error.png')
plt.show()
