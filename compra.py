from time import sleep
from selenium import webdriver 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, WebDriverException
import elementos_web as ew 

tiempo_espera = 5

def seleccion_producto(driver, modelo, pantalla, capacidad, color, operador):
    # Direcciono a la pagina del producto
    url_producto_especifico = f'{ew.url_producto}/{modelo}/{pantalla}-{capacidad}-{color}-{operador}'
    driver.cambiar_url(url_producto_especifico)

    # Veo si cargo la pagina y contenedor de los botones:
    driver.elemento_cargado(tiempo_espera, ew.web_apple_producto)
    driver.elemento_cargado(tiempo_espera, ew.contenedor_botones_producto)
    
    # Cargo elementos a utilizar:
    trade = driver.encontrar_elemento(tiempo_espera, ew.btn_trade)

    try:
        if operador != 'unlocked':
            # Acciones
            accion = ActionChains(driver.get_driver())
            accion.move_to_element(trade)
            accion.click(trade)
            accion.pause(3)
            accion.perform()
            
            # Elemento con operador
            accion = ActionChains(driver.get_driver())
            pay_full_operador = driver.encontrar_elemento(tiempo_espera, ew.btn_full_price)
            accion.move_to_element(pay_full_operador)
            accion.click(pay_full_operador)
            accion.pause(3)
            accion.perform()

            # Acciones del Boton
            accion = ActionChains(driver.get_driver())
            btn_siguiente = driver.encontrar_elemento(tiempo_espera, ew.btn_continue_product)
            accion.click(btn_siguiente)
            accion.pause(3)
            accion.perform()

            print('SE SELECCIONO EL PRODUCTO SATISFACTORIAMENTE')
            if (modelo != 'iphone-12'):
                btn_carrier = driver.esperar_elemento(tiempo_espera, ew.btn_activation_carrier_now)
                btn_carrier.click()
        
        else: 
            # Acciones
            accion = ActionChains(driver.get_driver())
            accion.move_to_element(trade)
            accion.click(trade)
            accion.pause(3)
            accion.perform()

            # Elementos sin operador
            accion = ActionChains(driver.get_driver())
            pay_full_unlocked = driver.encontrar_elemento(tiempo_espera, ew.btn_full_price_unlocked)
            accion.move_to_element(pay_full_unlocked)
            accion.click(pay_full_unlocked)
            accion.pause(3)
            accion.perform() 

            accion = ActionChains(driver.get_driver())
            btn_siguiente = driver.encontrar_elemento(tiempo_espera, ew.btn_continue_product)
            accion.move_to_element(btn_siguiente)
            accion.click(btn_siguiente)
            accion.pause(3)
            accion.perform()
                
            print('SE SELECCIONO EL PRODUCTO SATISFACTORIAMENTE')
            
    except:
        print("HA OCURRIDO UN ERROR EN LA SELECCION DEL PRODUCTO")

def transpaso_operador(driver, nr_operador, cod_postal):
    # Veo si cargo el contenedor
    driver.elemento_cargado(tiempo_espera, ew.contenedor_operador) 

    # Elementos a usar
    operador = driver.encontrar_elemento(tiempo_espera, ew.text_nr_operador)
    cod = driver.encontrar_elemento(tiempo_espera, ew.text_cod_postal_operador)
    siguiente = driver.encontrar_elemento(tiempo_espera, ew.btn_siguiente_operador)

    try:
        # Acciones que sigue 
        accion = ActionChains(driver.get_driver())
        accion.move_to_element(siguiente)
        accion.send_keys_to_element(operador, nr_operador)
        accion.send_keys_to_element(cod, cod_postal)
        accion.click(siguiente)
        accion.pause(3)
        accion.perform()
        # Nueva pagina donde aparece un aviso y un boton para agregar el producto en carrito
        # Acciones
        accion = ActionChains(driver.get_driver())
        confirmar_operador = driver.esperar_elemento(tiempo_espera, ew.btn_add_bag_2)
        accion.move_to_element(confirmar_operador)
        accion.click(confirmar_operador)
        accion.pause(2)
        accion.perform()
        print('SE HIZO LA VERIFICACION DEL OPERADOR SATISFACTORIAMENTE')
    except:
        print('HUBO UN ERROR EN LA VERIFICACION DEL OPERADOR')
    
def completar_compra_appleid(driver, usuario, password):
    try:
        # Voy a la bolsa de apple para completar la compra
        driver.cambiar_url(ew.url_bag)

        btn_checkout = driver.esperar_elemento(tiempo_espera, ew.btn_checkout)
        btn_checkout.click()

        # Veo si cargo el contenedor
        driver.elemento_cargado(tiempo_espera, ew.contenedor_apple_id)

        driver.driver.switch_to_frame("aid-auth-widget")

        # Logue en AppleID
        # Inicio una cadena de acciones
        accion = ActionChains(driver.get_driver())

        # Elemento a usar
        username = driver.encontrar_elemento(tiempo_espera, ew.text_username)
        accion.send_keys_to_element(username, usuario + Keys.ENTER)
        accion.pause(2)

        # Elemento a usar
        password_id = driver.encontrar_elemento(tiempo_espera, ew.text_password)
        accion.send_keys_to_element(password_id, password + Keys.ENTER)
        accion.pause(5)
        accion.perform()

        terminar_compra(driver)
        
    except:
        print('HUBO UN ERROR EN MEDIO DE LA COMPRA')

def terminar_compra(driver):
    #  Pagina Fulfillment
    btn_continue_shipping = driver.esperar_elemento(tiempo_espera, ew.btn_continue_shipping)
    btn_continue_shipping.click()

    #  Pagina Shipping
    accion = ActionChains(driver.get_driver())
    btn_continue_payment = driver.esperar_elemento(tiempo_espera, ew.btn_continue_payment)
    accion.click(btn_continue_payment)
    accion.pause(3)
    accion.perform()

    # Pagina Billing 
    # Elementos a usar 
    accion = ActionChains(driver.get_driver())
    btn_card = driver.esperar_elemento(tiempo_espera, ew.btn_credit_card)
    accion.click(btn_card)
    accion.pause(2)
    accion.perform()
    
    btn_continue_review = driver.esperar_elemento(tiempo_espera, ew.btn_continue_to_review)
    btn_continue_review.click()

    # Pagina Review
    btn_place_your_order = driver.esperar_elemento(tiempo_espera, ew.btn_place_your_order)
    btn_place_your_order.click()
    sleep(6)

    if driver.url_actual() == ew.url_compra_realizada:
        print('LA COMPRA HA SIDO EXITOSA')
        nr_order = driver.esperar_elemento(tiempo_espera, ew.text_nr_orden)
        dato = str(nr_order.text)
        driver.escribir_texto(dato)
    else:
        print('HA FALLADO EL PROCESO DE PAGO, UTILIZAR OTRA TARJETA')
        sleep(3)
        
        


