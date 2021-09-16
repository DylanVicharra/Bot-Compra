import os

try:
    print("Instalando las librerias:") 
    # Librerias ha instalar
    os.system('pip install webdriver-manager')
    os.system('pip install openpyxl')
    os.system('pip install pandas')
    os.system('pip install selenium')
    print("Instalacion completa")
except:
    print("Error al instalar los paquetes")