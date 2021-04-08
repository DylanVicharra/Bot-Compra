from bot import Bot
from time import sleep
import elementos_web as ew
from compra import seleccion_producto, transpaso_operador, completar_compra_appleid


def verificacion_datos(lista_datos):
    if lista_datos == []:
        print('El archivo no contiene datos')
        exit(1)
    else: 
        return lista_datos

def main():      
    # inicio el bot
    bot = Bot(ew.url_apple)

    # Lista de datos que se utilizara
    datos_iphone = verificacion_datos(bot.leer_texto('iphone'))
    apple_id = verificacion_datos(bot.leer_texto('apple_id'))
    operador = datos_iphone[4]
    nro_operador = '7868639220'
    cod_postal = '33178'

    # Usa diferentes botones la pagina si el celular es desbloqueado  
    if operador == 'unlocked':
        seleccion_producto(bot, datos_iphone[0], datos_iphone[1], datos_iphone[2], datos_iphone[3], datos_iphone[4])
    else:
        seleccion_producto(bot, datos_iphone[0], datos_iphone[1], datos_iphone[2], datos_iphone[3], datos_iphone[4])
        transpaso_operador(bot, nro_operador, cod_postal)
    
    completar_compra_appleid(bot, apple_id[0], apple_id[1])
    
    sleep(5)

    bot.finalizar()

    del bot
        

if __name__ == "__main__":
    main()