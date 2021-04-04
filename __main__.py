from bot import Bot
from time import sleep
import elementos_web as ew
from compra import seleccion_producto, transpaso_operador, completar_compra


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
    datos_domicilio = verificacion_datos(bot.leer_texto('datos_domicilio'))
    datos_tarjeta = verificacion_datos(bot.leer_texto('datos_tarjeta'))
    datos_iphone = verificacion_datos(bot.leer_texto('iphone'))
    operador = datos_iphone[4]
    print(operador)

    # Usa diferentes botones la pagina si el celular es desbloqueado  
    try:
        if operador == 'unlocked':
            seleccion_producto(bot, datos_iphone[0], datos_iphone[1], datos_iphone[2], datos_iphone[3], datos_iphone[4])
        else:
            seleccion_producto(bot, datos_iphone[0], datos_iphone[1], datos_iphone[2], datos_iphone[3], datos_iphone[4])
            transpaso_operador(bot, 7868639220, datos_domicilio[4])
    except:
        print('Se ha ingresado mal los datos del telefono a comprar')
        exit(1)

    completar_compra(bot, datos_domicilio, datos_tarjeta)

    sleep(10)

    del bot
        

if __name__ == "__main__":
    main()