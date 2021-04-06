from time import sleep
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, WebDriverException
import elementos_web as ew 

tiempo_espera = 15

def seleccion_producto(driver, modelo, pantalla, capacidad, color, operador):
    
    try:
        # Voy a la pagina del producto y selecciono 
        url_producto_especifico = f'{ew.url_producto}/{modelo}/{pantalla}-{capacidad}-{color}-{operador}'
        driver.cambiar_url(url_producto_especifico)
      
        if (operador == 'unlocked'):
            # Elementos que interactua cuando modelo es unlocked
            trade = driver.esperar_elemento(tiempo_espera, ew.btn_trade)
            trade.click()
            pay_full = driver.esperar_elemento(tiempo_espera, ew.btn_full_price_unlocked)
            pay_full.click()

            sleep(5)

            if (driver.stock_disponible() == True):
                add_bag = driver.esperar_elemento(tiempo_espera, ew.btn_continue_product)
                add_bag.click()
                print("SE ELEGIO SATISFACTORIAMENTE EL PRODUCTO")
            else: 
                print("EL PRODUCTO NO SE ENCUENTRA EN STOCK")
                exit(1)
        
        else: 
            # Elementos que interactua cuando modelo no es unlocked
            trade = driver.esperar_elemento(tiempo_espera, ew.btn_trade)
            trade.click()
            pay_full = driver.esperar_elemento(tiempo_espera, ew.btn_full_price)
            pay_full.click()
            sleep(5)

            if (driver.stock_disponible(tiempo_espera, ew.text_stock) == True):
                siguiente = driver.esperar_elemento(tiempo_espera, ew.btn_continue_product)
                siguiente.click()
                print("SE ELEGIO SATISFACTORIAMENTE EL PRODUCTO")
                sleep(5)
                if (modelo != 'iphone-12'):
                    activacion_now = driver.esperar_elemento(tiempo_espera, ew.btn_activation_carrier_now)
                    activacion_now.click()
            else: 
                print("EL PRODUCTO NO SE ENCUENTRA EN STOCK")
                exit(1)
    except:
        print("HA OCURRIDO UN ERROR EN LA SELECCION DEL PRODUCTO\n FINALIZANDO BOT...")
        exit(1)


def transpaso_operador(driver, nr_operador, cod_postal):
    try:
        # Rellena Textos
        operador = driver.esperar_elemento(tiempo_espera, ew.text_nr_operador)
        operador.send_keys(nr_operador)
        cod = driver.esperar_elemento(tiempo_espera, ew.text_cod_postal)
        cod.send_keys(cod_postal)
        # Clickea boton
        siguiente = driver.esperar_elemento(tiempo_espera, ew.btn_siguiente)
        siguiente.click()
        # Pagina de aviso 
        sleep(5)
        add_bag = driver.esperar_elemento(tiempo_espera, ew.btn_add_bag_2)
        add_bag.click()
    except:
        print('SE HIZO LA VERIFICACION DEL OPERADOR SATISFACTORIAMENTE')
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
        place_your_order = driver.esperar_elemento(tiempo_espera, ew.btn_place_your_order)
        place_your_order.click()
        
        sleep(5)
    
        if (driver.url_actual() == ew.url_billing):
            print('HA OCURRIDO UN ERROR CON LA TARJETA, INTENTE CON OTRA\n FINALIZANDO BOT...')
            exit(1)
        else:
            print('SE CONCRETO LA COMPRA SATISFACTORIAMENTE')
    except:
        print('HUBO UN ERROR EN MEDIO DE LA COMPRA\n FINALIZANDO BOT...')
        exit(1)

def rellenar_informacion(driver, nombre, apellido, direccion, edificio, cod_postal, email, telefono):
    try:
        # Relleno los textbox
        nom = driver.esperar_elemento(tiempo_espera, ew.text_name)
        print(nom)
        nom.send_keys(nombre)
        ape = driver.esperar_elemento(tiempo_espera, ew.text_last_name)
        ape.send_keys(apellido)
        direc = driver.esperar_elemento(tiempo_espera, ew.text_street)
        direc.send_keys(direccion)
        edif = driver.esperar_elemento(tiempo_espera, ew.text_home)
        edif.send_keys(edificio)
        zip_code = driver.esperar_elemento(tiempo_espera, ew.text_zip_code_ship)
        zip_code.send_keys(cod_postal + Keys.ENTER)
        mail = driver.esperar_elemento(tiempo_espera, ew.text_email)
        mail.send_keys(email)
        tel = driver.esperar_elemento(tiempo_espera, ew.text_phone_number)
        tel.send_keys(telefono)

        continue_pay = driver.esperar_elemento(tiempo_espera, ew.btn_continue_payment)
        continue_pay.click()
        print('SE RELLENO SATISFACTORIAMENTE LOS DATOS')
    except:
        print('HA OCURRIDO UN ERROR CON LOS DATOS DE DOMICILIO\n FINALIZANDO BOT...')
        exit(1)

    
def rellenar_datos_tarjeta(driver, nr_tarjeta, fec_exp, cvv):
    try:
        credit_card = driver.esperar_elemento(tiempo_espera, ew.btn_credit_card)
        credit_card.click()

        # Datos tarjeta
        card = driver.esperar_elemento(tiempo_espera, ew.text_card)
        card.send_keys(nr_tarjeta)
        exp = driver.esperar_elemento(tiempo_espera, ew.text_expired)
        exp.send_keys(fec_exp)
        codigo = driver.esperar_elemento(tiempo_espera, ew.text_cvv)
        codigo.send_keys(cvv)

        continue_review = driver.esperar_elemento(tiempo_espera, ew.btn_continue_to_review)
        continue_review.click()
        print('SE RELLENO SATISFACTORIAMENTE LOS DATOS')
    except:
        print('HA OCURRIDO UN ERROR CON LOS DATOS DE LA TARJETA\n FINALIZANDO BOT...')
        exit(1)



    




    
        


