# Pagina Apple 
url_apple = 'https://www.apple.com'
url_producto = f'{url_apple}/shop/buy-iphone'
url_bag = f'{url_apple}/shop/bag'
url_compra_realizada = "https://www.apple.com/shop/checkout/thankyou"


''' Pagina del producto '''
# Contenedores
contenedor_botones_producto = '//div[@id="root"]' 
# Botones
btn_trade = '//input[@id="noTradeIn"][@value="noTradeIn"][@type="radio"]'  
# Seleccion producto con operardor
btn_full_price = '//input[@type="radio"][@value="fullPrice"][@name="purchase_option_group"]' 
# Seleccion producto sin operador  
btn_full_price_unlocked = '//input[@value="fullPrice"][@type="radio"][@name="purchase_option"]' 
btn_continue_product = '//button[@type="submit"][@class="button button-block"]' 

# aparece cuando no es un iphone 12, ventana de activacion
btn_activation_carrier_now = '//button[@type="submit"][@class="rf-carrier-fork-option-button form-selector-label"][@name="proceed"]'



''' Pagina de validadcion del operador  '''
# botones y textos para verificacion del operador
contenedor_elementos_operador = '//div[@class="page-body"]'
text_nr_operador = '//input[@type="tel"][@name="wirelessNumber"][@class="form-textbox-input"]'
text_cod_postal_operador = '//input[@type="tel"][@name="postalcode"][@class="form-textbox-input"]'
btn_siguiente_operador = '//button[@type="submit"][@class="button"]'

# botones en aviso del operador y descripcion del dispositivo
btn_add_bag_2 = '//button[@type="submit"][@class="button"]'


''' Pagina del carrito '''
# botones en pagina bag
btn_checkout = '//button[@id="shoppingCart.actions.navCheckout"][@class="button button-block"][@data-autom="checkout"]'
# Lista desplegable 
select_cantidad = '//select[@class="rs-quantity-dropdown form-dropdown-select"]' 
# Texto precio
label_precio = '//div[@class="rs-iteminfo-price"]/p'
# texto si es una cantidad mayor a 10
text_cantidad = '//input[@type="tel"][@value="10"]'



''' Pagina de logueo de Apple ID '''
# textoBox de inicio sesion de AppleID:
contenedor_apple_id = '//iframe[@id="aid-auth-widget-iFrame"][@name="aid-auth-widget"]'
text_username = '//input[@id="account_name_text_field"][@type="text"][@can-field="accountName"]'
text_password = '//input[@id="password_text_field"][@type="password"][@can-field="password"]'
button_sign_in = '//button[@id="sign-in"]'


''' Pagina de seleccion de entrega '''
# fillmentOption 
#btn_fillmentOption = '//label[@for="fulfillmentOptionButtonGroup{}"]' #Se puede hacer una unica linea de codigo solo diciendo si es delivery (0) o pick-up (1)
btn_fillmentOption = '//input[@id="fulfillmentOptionButtonGroup{}"]'
# Pick up
# Seleccion lugar y dia
btn_lugar_definido_espera = '//label[@class="form-selector-label"]'
btn_lugar_definido = '//input[@value="{}"][@class="form-selector-input"]'
label_date = '//input[@id="bartPickupDateSelector{}"]'
# Seleccion de hora 
select_hora = '//select[@class="form-dropdown-select form-dropdown-selectnone"]'
# Delivery 
# Label Opciones
btn_delivery_option = '//div[@class="large-12 small-12 form-selector"]'
# Label cabeceras 
label_entrega_fecha = './/span[@class="form-selector-title"]'
label_metodo = './/span[@class="form-label-small"]'
label_entrega_costo = './/span[@class="column form-selector-right-col"]'
# Horarios
btn_setup_hora = '//div[@class="rs-time-window-slot rc-dimension-selector-row form-selector"]'
# Boton
btn_continue_shipping = '//button[@id="rs-checkout-continue-button-bottom"][@type="button"][@class="form-button"]' 


''' Pagina de seleccion de la persona que retira el producto '''
btn_persona_retiro = '//label[@for="pickupOptionButtonGroup{}"][@class="as-buttongroup-button"]' 
# Textos
text_firstName = '//input[@type="text"][@name="firstName"]'
text_lastName = '//input[@type="text"][@name="lastName"]'
text_email = '//input[@type="email"][@name="emailAddress"]'
text_phoneNumber = '//input[@type="tel"][@name="fullDaytimePhone"]'
# Boton 
btn_continue_payment = '//button[@id="rs-checkout-continue-button-bottom"][@type="button"][@class="form-button"][@data-autom="shipping-continue-button"]'


''' Pagina de forma de pago ''' 
# botones en la pagina billing 
contenedor_billling = '//fieldset[@class="rs-payment-section"]'
btn_credit_card = '//input[@id="checkout.billing.billingoptions.saved_card"][@name="checkout.billing.billingOptions.selectBillingOption"]' 
btn_continue_to_review = '//button[@id="rs-checkout-continue-button-bottom"][@type="button"][@class="form-button"]' 


''' Pagina confirmacion de compra ''' 
# boton para concretar la compra
btn_place_your_order = '//button[@id="rs-checkout-continue-button-bottom"][@type="button"][@class="form-button"][@data-autom="continue-button-label"][@aria-describedby="rs-checkout-continuedisclaimer-bottom"]'



# pagina de compra realizada
text_nr_orden = '//a[@class="as-buttonlink rs-thankyou-ordernumber"][@data-autom="order-number"]'


