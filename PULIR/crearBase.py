import os 
import json

nombretipo = input("Ingrese el nombre del tipo de equipo:")
directorios = ["Certificados", "Completos", "Graficos", "partesReporte/1","partesReporte/2","partesReporte/3", "partesReporte/4",  "QRS", "Reportes"]
archivo_json = 'enlaces.json'
links = []

if not os.path.exists(nombretipo):
    for directorio in directorios:
        os.makedirs(nombretipo + "/" + directorio)
        print("Directorio " + directorio + " creado")

def obtener_urls():
    with open(archivo_json) as json_file:
        data = json.load(json_file)
        for p in data['links']:
            link = {'url': p['url'], 'name': p['name']}
            links.append(link)
        return data

def download_files():
    for link in links:
        os.system( "wget " + link['url'])
        os.system("mv " + link['name'] + " " + nombretipo + "/")
        print("Archivo descargado")

obtener_urls()
download_files()
