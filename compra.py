from time import sleep

from selenium import webdriver 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, WebDriverException
import elementos_web as ew 

tiempo_espera = 10

def seleccion_producto(driver, modelo, pantalla, capacidad, color, operador):
    # Direcciono a la pagina del producto
    url_producto_especifico = f'{ew.url_producto}/{modelo}/{pantalla}-{capacidad}-{color}-{operador}'
    driver.cambiar_url(url_producto_especifico)

    # Veo si cargo la pagina y contenedor:
    driver.elemento_cargado(tiempo_espera, ew.web_apple_producto)
    driver.elemento_cargado(tiempo_espera, ew.contenedor_botones_producto)

    # Inicio una cadena de accciones
    accion = ActionChains(driver.driver)
    
    # Cargo elementos a utilizar:
    trade = driver.encontrar_elemento(tiempo_espera, ew.btn_trade)

    try:
        if operador != 'unlocked':
            # Acciones 
            accion.move_to_element(trade)
            accion.click(trade)
            accion.pause(5)
            accion.perform()

            # Elemento con operador
            pay_full_operador = driver.encontrar_elemento(tiempo_espera, ew.btn_full_price)

            accion.move_to_element(pay_full_operador)
            accion.click(pay_full_operador)
            accion.pause(5)
            accion.perform()
            if (driver.stock_disponible(tiempo_espera, ew.text_stock)==True):
                btn_siguiente = driver.encontrar_elemento(tiempo_espera, ew.btn_continue_product)
                accion.move_to_element(btn_siguiente)
                accion.click(btn_siguiente)
                accion.pause(5)
                accion.perform()

                if (modelo != 'iphone-12'):
                    btn_carrier = driver.esperar_elemento(tiempo_espera, ew.btn_activation_carrier_now)
                    btn_carrier.click()

            else: 
                print('NO HAY STOCK DISPONIBLE DEL PRODUCTO')
                exit(1)
        else: 
            # Acciones
            accion.move_to_element(trade)
            accion.click(trade)
            accion.pause(5)
            accion.perform()

            # Elementos sin operador
            pay_full_unlocked = driver.encontrar_elemento(tiempo_espera, ew.btn_full_price_unlocked)

            accion.move_to_element(pay_full_unlocked)
            accion.click(pay_full_unlocked)
            accion.pause(5)
            accion.perform() 
            if (driver.stock_disponible(tiempo_espera, ew.text_stock)==True):
                btn_siguiente = driver.encontrar_elemento(tiempo_espera, ew.btn_continue_product)
                accion.move_to_element(btn_siguiente)
                accion.click(btn_siguiente)
                accion.pause(5)
                accion.perform()

                if (modelo != 'iphone-12'):
                    btn_carrier = driver.esperar_elemento(tiempo_espera, ew.btn_activation_carrier_now)
                    btn_carrier.click()

            else: 
                print('NO HAY STOCK DISPONIBLE DEL PRODUCTO')
                exit(1)
    except:
        print("HA OCURRIDO UN ERROR EN LA SELECCION DEL PRODUCTO\n FINALIZANDO BOT...")
        exit(1)


def transpaso_operador(driver, nr_operador, cod_postal):
    # Veo si cargo el contenedor
    driver.elemento_cargado(tiempo_espera, ew.contenedor_operador) 

    # Inicio una cadena de acciones
    accion = ActionChains(driver.driver)

    # Elementos a usar
    operador = driver.encontrar_elemento(tiempo_espera, ew.text_nr_operador)
    cod = driver.encontrar_elemento(tiempo_espera, ew.text_cod_postal_operador)
    siguiente = driver.encontrar_elemento(tiempo_espera, ew.btn_siguiente_operador)

    try:
        # Acciones que sigue 
        accion.move_to_element(siguiente)
        accion.send_keys_to_element(operador, nr_operador)
        accion.send_keys_to_element(cod, cod_postal)
        accion.click(siguiente)
        accion.pause(5)
        accion.perform()
        # Nueva pagina donde aparece un aviso y un boton para agregar el producto en carrito
        confirmar_operador = driver.esperar_elemento(tiempo_espera, ew.btn_add_bag_2)
        confirmar_operador.click()
        print('SE HIZO LA VERIFICACION DEL OPERADOR SATISFACTORIAMENTE')
    except:
        print('HUBO UN ERROR EN LA VERIFICACION DEL OPERADOR')
        exit(1)
    
    
def completar_compra(driver, info_domicilio, info_tarjeta):
    try:
        # Voy a la bolsa de apple para completar la compra
        driver.cambiar_url(ew.url_bag)

        # Botones
        btn_checkout = driver.esperar_elemento(tiempo_espera, ew.btn_checkout)
        btn_checkout.click()
        guest = driver.esperar_elemento(tiempo_espera, ew.btn_continue_as_guest)
        guest.click()
        delivery = driver.esperar_elemento(tiempo_espera, ew.btn_delivery)
        delivery.click()

        # Texto ingreso el cod postal
        cod_postal = driver.esperar_elemento(tiempo_espera, ew.text_zip_code)
        cod_postal.send_keys(info_domicilio[4] + Keys.ENTER)
        
        shipping = driver.esperar_elemento(tiempo_espera, ew.btn_continue_shipping)
        shipping.click()

        # inicio los rellenos de formularios necesarios
        rellenar_informacion(driver, info_domicilio[0], info_domicilio[1], info_domicilio[2], info_domicilio[3],info_domicilio[4],info_domicilio[5],info_domicilio[6])
        rellenar_datos_tarjeta(driver, info_tarjeta[0], info_tarjeta[1], info_tarjeta[2])

        # Concretar la compra
        #place_your_order = driver.esperar_elemento(tiempo_espera, ew.btn_place_your_order)
        #place_your_order.click()

    except:
        print('HUBO UN ERROR EN MEDIO DE LA COMPRA\n FINALIZANDO BOT...')
        exit(1)

def rellenar_informacion(driver, nombre, apellido, direccion, edificio, cod_postal, email, telefono):
    # Veo si cargo el contenedor
    driver.elemento_cargado(tiempo_espera, ew.contenedor_shipping)
    driver.elemento_cargado(tiempo_espera, ew.contenedor_shipping_adresscontact)

    # Inicio una cadena de accciones
    accion = ActionChains(driver.driver)

    # Elemento a usar
    nom = driver.encontrar_elemento(tiempo_espera, ew.text_name)
    ape = driver.encontrar_elemento(tiempo_espera, ew.text_last_name)
    direc = driver.encontrar_elemento(tiempo_espera, ew.text_street)
    edif = driver.encontrar_elemento(tiempo_espera, ew.text_home)
    zip_code = driver.encontrar_elemento(tiempo_espera, ew.text_zip_code_ship)
    mail = driver.encontrar_elemento(tiempo_espera, ew.text_email)
    tel = driver.encontrar_elemento(tiempo_espera, ew.text_phone_number)
    continue_pay = driver.encontrar_elemento(tiempo_espera, ew.btn_continue_payment)

    try:
        # Relleno los textbox
        accion.pause(3)
        accion.send_keys_to_element(nom, nombre)
        accion.send_keys_to_element(ape, apellido)
        accion.send_keys_to_element(direc, direccion)
        accion.send_keys_to_element(edif, edificio)
        accion.move_to_element(zip_code)
        accion.send_keys_to_element(zip_code, cod_postal + Keys.ENTER)
        accion.move_to_element(continue_pay)
        accion.send_keys_to_element(mail, email)
        accion.send_keys_to_element(tel, telefono)
        accion.click(continue_pay)
        accion.pause(5)
        accion.perform()
        print('SE RELLENO SATISFACTORIAMENTE LOS DATOS')
    except:
        print('HA OCURRIDO UN ERROR CON LOS DATOS DE DOMICILIO\n FINALIZANDO BOT...')
        exit(1)

    
def rellenar_datos_tarjeta(driver, nr_tarjeta, fec_exp, cvv):
    # Inicio una cadena de accciones
    accion = ActionChains(driver.driver)

    # Elementos a usar
    opc_credit_card = driver.esperar_elemento(tiempo_espera, ew.btn_credit_card)
    opc_credit_card.click()
    btn_continue_review = driver.encontrar_elemento(tiempo_espera, ew.btn_continue_to_review)

    try:
        # Cargo los textos
        card = driver.encontrar_elemento(tiempo_espera, ew.text_card)
        exp = driver.encontrar_elemento(tiempo_espera, ew.text_expired)
        codigo = driver.encontrar_elemento(tiempo_espera, ew.text_cvv)

        accion.pause(5)
        accion.send_keys_to_element(card, nr_tarjeta)
        accion.send_keys_to_element(exp, fec_exp)
        accion.send_keys_to_element(codigo, cvv)
        accion.move_to_element(btn_continue_review)
        accion.click(btn_continue_review)
        accion.pause(5)
        accion.perform()

        print('SE RELLENO SATISFACTORIAMENTE LOS DATOS')
    except:
        print('HA OCURRIDO UN ERROR CON LOS DATOS DE LA TARJETA\n FINALIZANDO BOT...')
        exit(1)




    
        


