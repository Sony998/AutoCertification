import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo Excel
archivo_excel = 'CUCAITAPUNTO.xlsx'
df = pd.read_excel(archivo_excel, sheet_name='TERMOMETRO')

# Definir el índice de inicio
fila_actual = 4

# Bucle para generar las gráficas
while True:
    # Leer nombre del certificado y verificar si está vacío
    nombrecertificado = df.iat[fila_actual, 7]
    print(nombrecertificado)
    if pd.isna(nombrecertificado):
        break  # Salir del bucle si no hay más nombres de certificados

    # Leer los datos patrón y seleccionados
    datospatron = df.iloc[fila_actual + 4, 1:7].astype(int)  # Fila de los datos patrón
    datos_seleccionados = df.iloc[fila_actual + 6, 1:7].astype(float)  # Fila de los datos seleccionados

    # Crear la figura y los ejes
    fig, ax = plt.subplots()

    # Graficar los datos solo con puntos, sin líneas
    ax.scatter(datospatron, datos_seleccionados, color='blue')
    ax.set_ylim(-6, 3)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.set_xlabel('PATRON')
    ax.set_ylabel('ERROR')
    ax.set_title(f'E.S.E CENTRO DE SALUD SANTA LUCIA \n{nombrecertificado}', fontsize=10, fontweight='bold')

    # Guardar la gráfica en un archivo PNG con el nombre del certificado
    plt.savefig(f'{nombrecertificado}.png')

    # Cerrar la figura para liberar memoria
    plt.close(fig)

    # Avanzar 22 filas para la próxima iteración
    fila_actual += 16
