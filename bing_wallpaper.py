import requests
import os
from datetime import datetime

def descargar_foto_bing(resolucion="1920x1080", carpeta="BingWallpapers"):
    # Endpoint oficial de Bing para la foto del día
    url_api = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=es-AR"
    r = requests.get(url_api)
    data = r.json()

    # Construir URL base de la imagen
    url_base = "https://www.bing.com" + data["images"][0]["urlbase"]

    # Intentar primero con UHD
    url_img = f"{url_base}_UHD.jpg" if resolucion == "UHD" else f"{url_base}_1920x1080.jpg"
    img = requests.get(url_img)

    # Si no existe UHD, caer a 1920x1080
    if img.status_code != 200 and resolucion == "UHD":
        url_img = f"{url_base}_1920x1080.jpg"
        img = requests.get(url_img)

    # Crear carpeta si no existe
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    # Nombre del archivo con fecha
    fecha = datetime.now().strftime("%Y-%m-%d")
    archivo = os.path.join(carpeta, f"bing_{fecha}.jpg")

    # Guardar imagen
    with open(archivo, "wb") as f:
        f.write(img.content)

    print(f"✅ Foto descargada: {archivo}")

# Ejemplo de uso
descargar_foto_bing(resolucion="UHD")  # Cambiar a "1920x1080" si preferís
