import os
from selenium.common.exceptions import TimeoutException, NoSuchWindowException, SessionNotCreatedException
import manejo_datos as md
import webdriver as bot
import shop as shop


def secuencia_compra(ejecutableChrome, producto, tiempo_espera):

    try:
        driver = bot.crear_webdriver(ejecutableChrome)
    except SessionNotCreatedException:
        print("La version de Chrome no corresponde con el webdriver que se utiliza." + "\n" +
              "Actualice su navegador Chrome a la ultima version disponible.")
        exit(1)
    
    funciones_compra = {shop.seleccion_producto:[driver, producto, tiempo_espera], shop.traspaso_operador:[driver, producto, tiempo_espera], shop.bolsa:[driver, producto, tiempo_espera], shop.login_appleId:[driver, producto, tiempo_espera], shop.order_options:[driver, producto, tiempo_espera], shop.info_envio_o_retiro:[driver, producto, tiempo_espera], shop.metodo_pago:[driver, tiempo_espera], shop.obtener_orden:[driver, producto, tiempo_espera]}
    
    for funcion in funciones_compra:
        try:
            funcion(*funciones_compra[funcion])
        except NoSuchWindowException:
            print("Ocurrio un error con la ventana del navegador.")
            producto.estado = "Incompleto"
            break    
        except TimeoutException:
            print(f'Ocurrio un errror en: {funcion.__name__.replace("_", " ")}')
            print('Se demoro en encontrar el boton o texto.')    
            producto.estado = "Incompleto"    
            break
        except Exception as ex : 
            error_message = '\n'.join(map(str, ex.args)).rstrip()
            print(f"{error_message}")
            producto.estado = "Incompleto"
            break

    driver.quit()
    
    return producto

def main():
    os.system('cls')
    print("                 ============ BOT APPLE ============                 ")
    print("SE NECESITA QUE SE INGRESE EL NOMBRE DE UN ARCHIVO EXCEL Y EL NOMBRE DE UNA HOJA DEL MISMO ARCHIVO ")
    print("Se usara como archivo predeterminado el 'BOT.xlsx' y la hoja 'Compras' del mismo")
    
    # Nombres del archivo y hoja (para modificar mas facil)
    archivo_excel = 'BOT'.rstrip()
    hoja_excel = 'Compras'.rstrip()
    # Tiempo maximo de espera 
    tiempo_espera = 8
    # Instalacion del ejecutable 
    print("Instalacion del Webdriver de Chrome")
    
    try:
        ejecutableChrome = bot.instalar_webdriver()
    except:
        print("Archivo posiblemente dañado. Borrar la carpeta .wdm y volver a iniciar el programa")
        exit(1)

    print(f'Ruta: {ejecutableChrome}')
    # Lectura del archivo
    print(f"Lectura del archivo {archivo_excel}.xlsx")
    # Veo si existe el archivo
    try: 
        md.existe_archivo_excel(archivo_excel)
    except Exception as ex: 
        print(f'{ex}' + '\n' + "Finalizando..." + '\n')
        exit(1)

    lista_compra = md.lectura_lista_compra(archivo_excel, hoja_excel)
    
    # archivo que tiene que modificarse 
    archivo_ordenes = md.crear_archivo(archivo_excel) 

    # Se comienza la compra de la lista.
    for producto in lista_compra:
        
        atributosProducto = lista_compra[producto]["objeto"]
        print('=======================================================================================')
        print(f'Se inicia la compra del {lista_compra[producto]["nombre"]}')

        if atributosProducto.operador != 'unlocked':
            # Se tiene que comprar la cantidad dicha
            for repeticion in range(atributosProducto.cantidad):
                
                print('---------------------------------------------------------------------------------------')
                print(f'Compra {repeticion+1} de {atributosProducto.cantidad}')

                atributosProducto = secuencia_compra(ejecutableChrome , atributosProducto, tiempo_espera)

                if atributosProducto.estado ==  "Completado":
                    md.escribir_fila_excel(archivo_ordenes, "Ordenes", atributosProducto.producto_orden, lista_compra[producto]["nombre"], atributosProducto.order_option["nombre"])
                else:
                    print(f'Ha fallado la compra del {lista_compra[producto]["nombre"]}')
            
        elif atributosProducto.operador == 'unlocked':

            atributosProducto = secuencia_compra(ejecutableChrome, atributosProducto, tiempo_espera)

            if atributosProducto.estado ==  "Completado":
                md.escribir_fila_excel(archivo_ordenes, "Ordenes", atributosProducto.producto_orden, lista_compra[producto]["nombre"], atributosProducto.order_option["nombre"])
            else:
                print(f'Ha fallado la compra del {lista_compra[producto]["nombre"]}')

    archivo_ordenes.save(f'{md.date.today()}-{archivo_excel}.xlsx')

    print("Finalizando BOT APPLE...")

if __name__ == "__main__":
    main()