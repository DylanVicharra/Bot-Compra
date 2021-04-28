from bot import Bot
from time import sleep
from datetime import datetime
import elementos_web as ew
import pandas as pd
import openpyxl as op
import lectura_datos as ld
from compra import seleccion_producto, transpaso_operador, completar_compra_appleid, obtener_orden


def verificacion_datos(lista_datos):
    if lista_datos == []:
        print('UNO DE LOS ARCHIVOS NO CONTIENE DATOS')
        exit(1)
    else: 
        return lista_datos

def bot_compra(datos_iphone, operador, apple_id):      
    
    # inicio el bot
    bot = Bot(ew.url_apple)

    # datos que se utilizara
    nro_operador = '7868639220'
    cod_postal = '33178'

    # Usa diferentes botones la pagina si el celular es desbloqueado  
    if operador == 'unlocked':
        seleccion_producto(bot, datos_iphone[0], datos_iphone[1], datos_iphone[2], datos_iphone[3], operador)
    else:
        seleccion_producto(bot, datos_iphone[0], datos_iphone[1], datos_iphone[2], datos_iphone[3], operador)
        transpaso_operador(bot, nro_operador, cod_postal)
    
    completar_compra_appleid(bot, apple_id[0], apple_id[1]) 
   
    return bot


def lectura_excel():
    # nombre del archivo excel a leer
    archivo_excel = input("Ingrese el nombre del archivo (sin el .xlsx): ")     
    # Revisa si existe el archivo
    ld.existe_archivo(archivo_excel)
    # Abre el archivo (camabiar la lista_celulares)
    excel_celulares = pd.read_excel(f'{archivo_excel}.xlsx', engine='openpyxl')

    # Recorre cada fila del excel
    for i in range(len(excel_celulares)):
        modelo = excel_celulares.loc[i,"MODELO"]
        apple_id = [excel_celulares.loc[i,"USUARIO"],excel_celulares.loc[i,"CONTRASEÑA"]]
        operador = excel_celulares.loc[i,"OPERADOR"]
        cantidad = excel_celulares.loc[i,"CANTIDAD"]

        datos_iphone = ld.agrupacion_datos(modelo)

        print(f'SE ESTA COMPRANDO EL {modelo}')
        # Realiza la cantidad de veces que dice la variable cantidad (en este caso todos son verizon)        
        for rep in range(cantidad):
            try:
                print(f'repeticion: {rep+1}')
                bot_auxiliar = bot_compra(datos_iphone, operador, apple_id)
                excel_celulares.loc[i,"ORDEN"] = bot_auxiliar.link_orden
                excel_celulares.loc[i,"ESTADO"] = "Finalizado"
                bot_auxiliar.finalizar()
                del bot_auxiliar
            except:
                excel_celulares.loc[i,"ORDEN"] = None
                excel_celulares.loc[i,"ESTADO"] = "Pendiente"
                print(f'HA FALLADO LA COMPRA DEL {modelo}')


    excel_celulares.to_excel(f'{str(datetime.today()).replace(":","")}_{archivo_excel}.xlsx', sheet_name = f'Ordenes',index = False)

    print("FINALIZANDO PROGRAMA")

if __name__ == "__main__":
    lectura_excel()
