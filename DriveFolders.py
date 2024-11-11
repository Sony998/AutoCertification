from googleapiclient.http import MediaFileUpload
from Google import Create_Service
import os
import pandas as pd
CLIENT_SECRET_FILE = "client_secrets.json"
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
folder_id = "1t2tsqNS901AlwhaONdqtsLZR_uU9_jrj"
archivo_excel = 'pulido.xlsx'   
excel_file = pd.ExcelFile(archivo_excel)
hojas = excel_file.sheet_names
print(hojas)
for hoja in hojas:
    file_metadata = {
        'name': hoja,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [folder_id]
    }
    folder = service.files().create(body=file_metadata, fields='id').execute()
    print(f'Folder created: {hoja}, ID: {folder.get("id")}')