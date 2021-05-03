from bot import Bot
from time import sleep
from datetime import date
import elementos_web as ew
import pandas as pd
import openpyxl as op
import manejo_datos as ld
import compra as compra


def bot_compra(datos_iphone, operador, apple_id, cantidad):      
    # inicio el bot
    bot = Bot(ew.url_apple)

    # datos que se utilizara
    nro_operador = '7868639220'
    cod_postal = '33178'

    # Usa diferentes botones la pagina si el celular es desbloqueado  
    compra.seleccion_producto(bot, datos_iphone[0], datos_iphone[1], datos_iphone[2], datos_iphone[3], operador)
    # Hace la verificacion del operador (solo si este no es unlocked)
    if operador != 'unlocked':
        compra.transpaso_operador(bot, nro_operador, cod_postal)
    # Realiza en bolsa la seleccion de cantidad del producto 
    compra.checkout(bot, cantidad, operador)
    # Realiza el logueo del usuario
    compra.logueo_appleid(bot, apple_id[0], apple_id[1])
    # Realiza los siguientes, que son seleccion de envio y seleccion de tarjeta
    compra.terminar_compra(bot) 
    # Guarada en el bot la orden de compra, caso contrario termina
    compra.obtener_orden(bot)
    
    bot.finalizar()

    return bot.get_estado(), bot.get_orden()

def lectura_excel():
    try: 
        print("         ---------- BOT APPLE -----------                ")
        print("SE NECESITA QUE SE INGRESE EL NOMBRE DE UN ARCHIVO EXCEL Y EL NOMBRE DE UNA HOJA DEL MISMO ARCHIVO ")
        print("Ingrese los siguientes datos. Nombre excel: BOT, Hoja: Compras")
        # nombre del archivo excel a leer
        archivo_excel = input("Ingrese el nombre del archivo (sin el .xlsx): ")
        hoja_calculo = input("Ingrese el nombre de la hoja donde se encuentra la tabla: ")   
        # Elimino los espacios en blanco que tengan  
        archivo_excel = archivo_excel.strip()
        hoja_calculo = hoja_calculo.strip()
        # Revisa si existe el archivo
        ld.existe_archivo(archivo_excel)
        # Abre el archivo con pandas para mejor manejo de los datos
        excel_celulares = pd.read_excel(f'{archivo_excel}.xlsx', sheet_name=hoja_calculo, engine='openpyxl')
    except:
        print("HAY UN ERROR EN EL NOMBRE DE LA HOJA DE CALCULO QUE SE INGRESO")
        exit(1)
    
    # Limpio la lista de datos vacios
    excel_celulares = ld.limpieza_datos(excel_celulares)
    
    # Abre archivo a modificar 
    excel_a_modificar = op.load_workbook(f'{archivo_excel}.xlsx')
    
    # Recorre cada fila del excel
    for i in excel_celulares.index:
        modelo = str(excel_celulares.loc[i,"MODELO"])
        apple_id = [str(excel_celulares.loc[i,"USER"]),str(excel_celulares.loc[i,"PASSWORD"])]
        operador = str(excel_celulares.loc[i,"OPERADOR"]).lower()
        cantidad = int(excel_celulares.loc[i,"CANTIDAD"])

        datos_iphone = ld.verificacion_modelo(modelo)

        print(f'SE ESTA COMPRANDO EL {modelo}')
        # Realiza la cantidad de veces que dice la variable cantidad (en este caso todos son verizon)     
        if operador != 'unlocked':   
            for rep in range(cantidad):
                try:
                    print(f'nrº{rep+1} de {cantidad}')

                    estado, orden = bot_compra(datos_iphone, operador, apple_id, cantidad)
                
                    if estado == 'Completado':
                        # Escribo el estado
                        ld.escribir_celda_excel(excel_a_modificar, hoja_calculo, i+2, 8, "Finalizado")
                        # Escribo el link de orden
                        ld.escribir_hipervinculo_excel(excel_a_modificar, hoja_calculo, i+2, 2, orden)
                        # Escribo la fecha
                        ld.escribir_celda_excel(excel_a_modificar, hoja_calculo, i+2, 1, str(date.today()))
                        print("---------------------------------------------------------------------------------------------------------")
                    elif estado == 'Fallido':
                        # Escribo el estado
                        ld.escribir_celda_excel(excel_a_modificar, hoja_calculo, i+2, 8, "Pendiente")
                        print(f'HA FALLADO LA COMPRA DEL {modelo}') 
                        print("---------------------------------------------------------------------------------------------------------")

                except:
                    # Escribo el estado
                    ld.escribir_celda_excel(excel_a_modificar, hoja_calculo, i+2, 8, "Pendiente")

                    print(f'HA FALLADO LA COMPRA DEL {modelo}')
                    print("---------------------------------------------------------------------------------------------------------")

        elif operador == 'unlocked':
            try:
                estado, orden = bot_compra(datos_iphone, operador, apple_id, cantidad)
                
                if estado == 'Completado':
                    # Escribo el estado
                    ld.escribir_celda_excel(excel_a_modificar, hoja_calculo, i+2, 8, "Finalizado")
                    # Escribo el link de orden
                    ld.escribir_hipervinculo_excel(excel_a_modificar, hoja_calculo, i+2, 2, orden)
                    # Escribo la fecha
                    ld.escribir_celda_excel(excel_a_modificar, hoja_calculo, i+2, 1, str(date.today()))
                    print("---------------------------------------------------------------------------------------------------------")
                elif estado == 'Fallido':
                    # Escribo el estado
                    ld.escribir_celda_excel(excel_a_modificar, hoja_calculo, i+2, 8, "Pendiente")

                    print(f'HA FALLADO LA COMPRA DEL {modelo}') 
                    print("---------------------------------------------------------------------------------------------------------")
            except:
                # Escribo el estado
                ld.escribir_celda_excel(excel_a_modificar, hoja_calculo, i+2, 8, "Pendiente")
        
                print(f'HA FALLADO LA COMPRA DEL {modelo}')
                print("---------------------------------------------------------------------------------------------------------")

    # Se guarda el archivo en cuestion
    excel_a_modificar.save(f'{archivo_excel}.xlsx')

    print("FINALIZANDO PROGRAMA")

if __name__ == "__main__":
    lectura_excel()
