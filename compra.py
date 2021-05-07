from time import sleep
from selenium import webdriver 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as ec 
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, WebDriverException
import elementos_web as ew 

tiempo_espera = 10

def seleccion_producto(driver, modelo, pantalla, capacidad, color, operador):
    driver.set_etapa('SELECCION PRODUCTO')
    # Direcciono a la pagina del producto
    url_producto_especifico = f'{ew.url_producto}/{modelo}/{pantalla}-{capacidad}-{color}-{operador}'
    driver.cambiar_url(url_producto_especifico)
    
    # Cargo elementos a utilizar:
    trade = driver.encontrar_elemento(tiempo_espera, ew.btn_trade)

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


def transpaso_operador(driver, nr_operador, cod_postal, operador):
    driver.set_etapa('VERIFICACION OPERADOR')
    if operador != 'unlocked':
        # Veo si cargo el contenedor
        driver.elemento_cargado(tiempo_espera, ew.contenedor_operador) 

        # Elementos a usar
        operador = driver.encontrar_elemento(tiempo_espera, ew.text_nr_operador)
        cod = driver.encontrar_elemento(tiempo_espera, ew.text_cod_postal_operador)
        siguiente = driver.encontrar_elemento(tiempo_espera, ew.btn_siguiente_operador)

        
        # Acciones que sigue 
        accion = ActionChains(driver.get_driver())
        accion.move_to_element(siguiente)
        accion.send_keys_to_element(operador, nr_operador)
        accion.send_keys_to_element(cod, cod_postal)
        accion.click(siguiente)
        accion.pause(5)
        accion.perform()
        # Nueva pagina donde aparece un aviso y un boton para agregar el producto en carrito
        # Acciones
        accion = ActionChains(driver.get_driver())
        confirmar_operador = driver.esperar_elemento(tiempo_espera, ew.btn_add_bag_2)
        accion.move_to_element(confirmar_operador)
        accion.click(confirmar_operador)
        accion.pause(5)
        accion.perform()
        print('SE HIZO LA VERIFICACION DEL OPERADOR SATISFACTORIAMENTE')
        

def logueo_appleid(driver, usuario, password):
    driver.set_etapa('INICIANDO SESION EN APPLE ID')
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
    accion.pause(6)
    accion.perform()
    print("SE INICIO SESION EN APPLE ID CORRECTAMENTE")
    

def checkout(driver, cantidad, operador):
    driver.set_etapa('CHECKOUT')
    # Voy a la bolsa de apple para completar la compra
    driver.cambiar_url(ew.url_bag)
    
    
    # Elijo la cantidad del producto que deseeo comprar (solo si este es unlocked)
    if operador == 'unlocked':
        driver_aux = driver.get_driver()
        # Selecciono la lista desplegable
        driver_aux.find_element(By.TAG_NAME,'select')
        select_cantidad = driver_aux.find_element_by_tag_name('select')
        seleccion_cant = Select(select_cantidad)
        if cantidad < 10:
            # Selecciona la cantidad que deseo
            seleccion_cant.select_by_value(str(cantidad))
            sleep(3)
        else:
            seleccion_cant.select_by_value('10+')
            sleep(3)
            driver_aux.find_element(By.XPATH,"//input[@type='tel'][@value='10']")
            texto_cant = driver_aux.find_element_by_xpath("//input[@type='tel'][@value='10']")
            texto_cant.send_keys(str(cantidad) + Keys.ENTER)

    # Presiono el boton de checkout para pasar al logueo
    btn_checkout = driver.esperar_elemento(tiempo_espera, ew.btn_checkout)
    btn_checkout.click()
        


def terminar_compra(driver):
    driver.set_etapa('SELECCION DE ENVIO Y TARJETA')
    
    #  Pagina Fulfillment
    accion = ActionChains(driver.get_driver())
    btn_delivery = driver.esperar_elemento(tiempo_espera, ew.btn_delivery)
    accion.move_to_element(btn_delivery)
    accion.click(btn_delivery)
    btn_continue_shipping = driver.esperar_elemento(tiempo_espera, ew.btn_continue_shipping)
    accion.move_to_element(btn_continue_shipping)
    accion.click(btn_continue_shipping)
    accion.pause(5)
    accion.perform()

    #  Pagina Shipping
    accion = ActionChains(driver.get_driver())
    btn_continue_payment = driver.esperar_elemento(tiempo_espera, ew.btn_continue_payment)
    accion.click(btn_continue_payment)
    accion.pause(5)
    accion.perform()

    # Pagina Billing 
    # Elementos a usar 
    accion = ActionChains(driver.get_driver())
    btn_card = driver.esperar_elemento(tiempo_espera, ew.btn_credit_card)
    accion.click(btn_card)
    accion.pause(3)
    accion.perform()
        
    btn_continue_review = driver.esperar_elemento(tiempo_espera, ew.btn_continue_to_review)
    btn_continue_review.click()

    # Pagina Review
    btn_place_your_order = driver.esperar_elemento(tiempo_espera, ew.btn_place_your_order)
    btn_place_your_order.click()
    sleep(5)
    print("SE SELECCIONO TIPO DE ENTREGA Y TARJETA CORRECTAMENTE")
    
        
def obtener_orden(driver):
    driver.set_etapa('OBTENCION DE LA ORDEN')
    
    nr_orden = driver.esperar_elemento(tiempo_espera, ew.text_nr_orden)
    link_orden = nr_orden.get_attribute('href')
    nombre = nr_orden.text
    driver.set_estado('Completado')
    driver.set_orden([str(link_orden), str(nombre)])
    print('LA COMPRA HA SIDO EXITOSA')
    sleep(3)

        

