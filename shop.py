
from time import sleep
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchWindowException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import elementos_web as ew



def scroll_to(driver, elemento):
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", elemento)

def pagina_producto(driver, modelo, display, memoria, color, operador):
    try:
        driver.get(f'https://www.apple.com/shop/buy-iphone/{modelo}/{display}-{memoria}-{color}-{operador}')
        return True
    except (TimeoutException, WebDriverException):
        return False

def pagina_carrito(driver):
    try: 
        driver.get(ew.url_bag)
        return True
    except (TimeoutException, WebDriverException):
        return False

def seleccion_producto(driver, producto, tiempo_espera):
    
    pagina_producto(driver, producto.modelo, producto.display, producto.memoria, producto.color, producto.operador)

    print("Se esta seleccionando el producto")
    contenedor_producto = False
    intentos = 0
    while not contenedor_producto:
        try:
            WebDriverWait(driver, tiempo_espera).until(EC.presence_of_element_located((By.XPATH, ew.contenedor_botones_producto)))
            contenedor_producto = True
        except (NoSuchWindowException, WebDriverException):
            contenedor_producto = True
            raise Exception("Se cerro la ventana del navegador")                  
        except TimeoutException: 
            intentos+=1 
            if intentos > 3:
                contenedor_producto = True
                raise Exception ("No cargaron los elementos")

    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(ew.btn_trade))

    if producto.operador != 'unlocked':
        WebDriverWait(driver, tiempo_espera).until(EC.presence_of_element_located((By.XPATH, ew.btn_full_price)))
        driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(ew.btn_full_price))
    else:
        WebDriverWait(driver, tiempo_espera).until(EC.presence_of_element_located((By.XPATH, ew.btn_full_price_unlocked)))
        driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(ew.btn_full_price_unlocked))

    WebDriverWait(driver, tiempo_espera).until(EC.element_to_be_clickable((By.XPATH, ew.btn_continue_product)))
    scroll_to(driver, driver.find_element_by_xpath(ew.btn_continue_product))
    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(ew.btn_continue_product))

    print("Se selecciono el producto satisfactoriamente")

    if producto.modelo != 'iphone-12' and producto.operador != 'unlocked':
        WebDriverWait(driver, tiempo_espera).until(EC.element_to_be_clickable((By.XPATH, ew.btn_activation_carrier_now)))
        driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(ew.btn_activation_carrier_now))


def traspaso_operador(driver, producto, tiempo_espera):
    
    if producto.operador != 'unlocked':

        print("Se esta verificando el operador")

        contenedor_operador = False
        intentos = 0
        while not contenedor_operador:
            try:
                WebDriverWait(driver, tiempo_espera).until(EC.presence_of_element_located((By.XPATH, ew.contenedor_elementos_operador)))
                contenedor_operador = True
            except (NoSuchWindowException, WebDriverException):
                contenedor_operador = True
                raise Exception("Se cerro la ventana del navegador")                  
            except TimeoutException: 
                intentos+=1 
                if intentos > 3:
                    contenedor_operador = True
                    raise Exception ("No cargaron los elementos")

        driver.find_element_by_xpath(ew.text_nr_operador).send_keys("7868639220")

        driver.find_element_by_xpath(ew.text_cod_postal_operador).send_keys("33178")

        sleep(2)
     
        scroll_to(driver, driver.find_element_by_xpath(ew.btn_siguiente_operador))
        driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(ew.btn_siguiente_operador))

        print("Se ha completado los datos del operador")

        sleep(6)

        nueva_pagina = False 
        while not nueva_pagina:
            try:
                WebDriverWait(driver, tiempo_espera).until(EC.element_to_be_clickable((By.XPATH, ew.btn_add_bag_2)))
                scroll_to(driver, driver.find_element_by_xpath(ew.btn_add_bag_2))
                driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(ew.btn_add_bag_2))
                nueva_pagina = True

                print("Se ha verificado satisfactoriamente el operador")

            except (NoSuchWindowException, WebDriverException):
                nueva_pagina = True
                raise Exception("Se cerro la ventana del navegador")                  
            except TimeoutException: 
                intentos+=1 
                if intentos > 3:
                    nueva_pagina = True
                    raise Exception ("No cargo el elemento")

    # Espera a que la pagina de la descripcion se cargue el boton mas importante
    WebDriverWait(driver, (tiempo_espera + 2)).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="button button-block button-super"]')))


def bolsa(driver, producto, tiempo_espera):
    
    pagina_carrito(driver)

    if producto.operador == 'unlocked':
        WebDriverWait(driver, tiempo_espera).until(EC.visibility_of_element_located((By.XPATH, ew.select_cantidad)))
        desplegableCant = driver.find_element_by_xpath(ew.select_cantidad)
        selectCant = Select(desplegableCant)

        if (producto.cantidad <=10):
            selectCant.select_by_value(str(producto.cantidad))

        elif (producto.cantidad > 10 and producto.cantidad <= 99):
            selectCant.select_by_value('10')

            WebDriverWait(driver, tiempo_espera).until(EC.presence_of_element_located((By.XPATH, ew.text_cantidad)))
            driver.find_element_by_xpath(ew.text_cantidad).send_keys(str(producto.cantidad) + Keys.ENTER)
        else: 
            raise('la cantidad dada es mucho mayor a la permitida')
    else:
        tiempo_espera += 2

    # Espera a que los elementos seleccionados se vuelvan a cargar con la informacion cambiada
    sleep(2)

    WebDriverWait(driver, tiempo_espera).until(EC.element_to_be_clickable((By.XPATH, ew.btn_checkout)))
    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(ew.btn_checkout))


def login_appleId(driver, producto, tiempo_espera):

    print("Se esta iniciando sesion en Apple ID")

    procceded_login = False
    intentos = 0
    while not procceded_login:
        try:
            login_ready = EC.frame_to_be_available_and_switch_to_it((By.XPATH, ew.contenedor_apple_id))
            WebDriverWait(driver, tiempo_espera).until(login_ready)
            procceded_login = True  
        except (NoSuchWindowException, WebDriverException):
            procceded_login = True
            raise Exception("Se cerro la ventana del navegador")                  
        except TimeoutException: 
            intentos+=1 
            if intentos > 3:
                procceded_login = True
                raise Exception ("No cargo el elemento") 
    
    WebDriverWait(driver, tiempo_espera).until(EC.visibility_of_element_located((By.XPATH, ew.text_username)))
    driver.find_element_by_xpath(ew.text_username).send_keys(producto.username)
    driver.find_element_by_xpath(ew.text_username).send_keys(Keys.ENTER)

    WebDriverWait(driver, tiempo_espera).until(EC.visibility_of_element_located((By.XPATH, ew.text_password)))
    driver.find_element_by_xpath(ew.text_password).send_keys(producto.password)
    driver.find_element_by_xpath(ew.text_password).send_keys(Keys.ENTER)

    print("Apple ID ingresado correctamente")


def info_envio_o_retiro(driver, producto, tiempo_espera): # pensar otro nombre para el metodo 

    print("Se rellena la informacion de contacto")

    if (producto.order_option["nombre"] == 'DELIVERY'):
        WebDriverWait(driver, tiempo_espera).until(EC.element_to_be_clickable((By.XPATH, ew.btn_continue_payment)))
        driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(ew.btn_continue_payment))
    else:
        try:
            WebDriverWait(driver, tiempo_espera).until(EC.visibility_of_element_located((By.XPATH, ew.btn_persona_retiro.format("0"))))
            driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(ew.btn_persona_retiro.format("0")))
        except:
            pass 

        WebDriverWait(driver, tiempo_espera).until(EC.visibility_of_element_located((By.XPATH, ew.text_firstName)))
        textFirtsName = driver.find_element_by_xpath(ew.text_firstName)
        textFirtsName.clear()
        textFirtsName.send_keys('Esteban')

        textLastName = driver.find_element_by_xpath(ew.text_lastName)
        textLastName.clear()
        textLastName.send_keys('Iturrieta')

        scroll_to(driver, driver.find_element_by_xpath(ew.btn_continue_shipping))
        driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(ew.btn_continue_shipping))


def stores_preferencias(driver, producto):
    # Buscar todas las opciones 
    lista_stores_preferencias = producto.lista_tiendas_opcionales

    for apple_store in lista_stores_preferencias:
        tienda_pos_disponible = driver.find_element_by_xpath(ew.btn_lugar_definido.format(lista_stores_preferencias[apple_store]["codigo"], lista_stores_preferencias[apple_store]["codigo"]))
        if tienda_pos_disponible.get_property('disabled') == False: 
            print(f'Se encontro una tienda disponible: {lista_stores_preferencias[apple_store]["nombre"]}')
            producto.order_option = lista_stores_preferencias[apple_store]
            driver.execute_script("arguments[0].click();", tienda_pos_disponible)
            return True

    raise Exception("No se encontro ninguna tienda disponible dentro de las preferencias. Se termina la compra")


def order_options(driver, producto, tiempo_espera):
    print("Se selecciona el metodo de envio o retiro del producto")
    
    if (producto.order_option["nombre"] == "DELIVERY"):
        selectOption = 0
    else: 
        selectOption = 1

    WebDriverWait(driver, tiempo_espera).until(EC.presence_of_element_located((By.XPATH, ew.btn_fillmentOption.format(selectOption))))
    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(ew.btn_fillmentOption.format(selectOption)))


    if selectOption == 1:
        WebDriverWait(driver, tiempo_espera).until(EC.visibility_of_element_located((By.XPATH, '//button[@data-autom="show-more-stores-button"]')))
        driver.execute_script("arguments[0].click();", driver.find_element_by_xpath('//button[@data-autom="show-more-stores-button"]'))
        #try:
        WebDriverWait(driver, tiempo_espera).until(EC.visibility_of_element_located((By.XPATH, ew.btn_lugar_definido_espera.format(producto.order_option["codigo"]))))

        boton = driver.find_element_by_xpath(ew.btn_lugar_definido.format(producto.order_option["codigo"], producto.order_option["codigo"]))    
        
        if boton.get_property('disabled')==True:
            print(f'La tienda {producto.order_option["nombre"]} no esta disponible se va encontrar otro')
            stores_preferencias(driver, producto)
        else: 
            driver.execute_script("arguments[0].click();", boton)
        #except:

        WebDriverWait(driver, tiempo_espera).until(EC.visibility_of_element_located((By.XPATH, ew.select_hora)))
        desplegableHora = driver.find_element_by_xpath(ew.select_hora)
        selectHora = Select(desplegableHora)

        selectHora.select_by_index(2)

        # Para ver algo
        sleep(6)


    scroll_to(driver, driver.find_element_by_xpath(ew.btn_continue_shipping))
    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(ew.btn_continue_shipping))


def metodo_pago(driver, tiempo_espera):  
    
    print("Se selecciona el metodo de pago")

    WebDriverWait(driver, tiempo_espera).until(EC.presence_of_element_located((By.XPATH, ew.contenedor_billling)))
    
    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(ew.btn_credit_card))

    scroll_to(driver, driver.find_element_by_xpath(ew.btn_continue_to_review))
    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(ew.btn_continue_to_review))

    print("Metodo de pago seleccionado correctamente")

def obtener_orden(driver, producto, tiempo_espera):
    
    WebDriverWait(driver, tiempo_espera).until(EC.element_to_be_clickable((By.XPATH, ew.btn_place_your_order)))
    scroll_to(driver, driver.find_element_by_xpath(ew.btn_place_your_order))
    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(ew.btn_place_your_order))
    
    driver.implicitly_wait(8)
    
    try:
        orden = driver.find_element_by_xpath(ew.text_nr_orden)

        producto.producto_orden = {
                                    "link":str(orden.get_attribute('href')),
                                    "nombre":str(orden.get_attribute('data-evar1').replace("OrderDetails", "").strip())
                                  }
        
        producto.estado = "Completado"
        
        print("La compra se realizo correctamente")

        # Para ver algo de la informacion de compra: puede ser eliminado a futuro
        sleep(4)
        return True
    except:
        pass 

    try:
        WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.XPATH, '//div[@role="alert"]')))
        print("Hubo un error con la tarjeta seleccionada, utilizar otro usuario para esta compra")
    except:
        raise Exception ("El producto no se puede retirar en tienda, solo delivery")

    
    
