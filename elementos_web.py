# Pagina Apple 
url_apple = 'https://www.apple.com'
url_producto = f'{url_apple}/shop/buy-iphone'
url_bag = f'{url_apple}/shop/bag'
url_compra_realizada = "https://www.apple.com/shop/checkout/thankyou"


''' Pagina del producto '''
# Contenedores
contenedor_botones_producto = '//div[@id="root"]' #cambio 
# Botones
btn_trade = '//input[@id="noTradeIn"][@value="noTradeIn"][@type="radio"]'  
# Seleccion producto con operardor
btn_full_price = '//input[@type="radio"][@value="fullPrice"][@name="purchase_option_group"]' 
# Seleccion producto sin operador  
btn_full_price_unlocked = '//input[@value="fullPrice"][@type="radio"][@name="purchase_option"]' 
btn_continue_product = '//button[@type="submit"][@class="button button-block"]' #con este modelo de boton se puede usar en los dos caso

# aparece cuando no es un iphone 12, ventana de activacion
btn_activation_carrier_now = '//button[@type="submit"][@class="rf-carrier-fork-option-button form-selector-label"][@name="proceed"]'



''' Pagina de validadcion del operador  '''
# botones y textos para verificacion del operador
contenedor_elementos_operador = '//div[@id="primary"][@role="main"]'
text_nr_operador = '//input[@id="ctn"][@type="tel"][@name="ctn"][@placeholder="Wireless Number"]'
text_cod_postal_operador = '//input[@id="postalcode"][@type="number"][@name="postalcode"][@placeholder="Billing Zip Code"]'
btn_siguiente_operador = '//button[@id="preauth-button-next"][@type="submit"][@title="Continue"]'

# botones en aviso del operador y descripcion del dispositivo
btn_add_bag_2 = '//a[@id="preauth-button-next"][@class="button as-preauth-button-continue"]'



''' Pagina del carrito '''
# botones en pagina bag
btn_checkout = '//button[@id="shoppingCart.actions.navCheckout"][@class="button button-block"][@data-autom="checkout"]'
# Lista desplegable 
select_cantidad = '//select[@class="rs-quantity-dropdown form-dropdown-select"]' 
# texto si es una cantidad mayor a 10
text_cantidad = '//input[@type="tel"][@value="10"]'



''' Pagina de logueo de Apple ID '''
# textoBox de inicio sesion de AppleID:
contenedor_apple_id = '//iframe[@id="aid-auth-widget-iFrame"][@name="aid-auth-widget"]'
text_username = '//input[@id="account_name_text_field"][@type="text"][@can-field="accountName"]'
text_password = '//input[@id="password_text_field"][@type="password"][@can-field="password"]'


''' Pagina de seleccion de entrega '''
# fillmentOption 
#btn_fillmentOption = '//label[@for="fulfillmentOptionButtonGroup{}"]' #Se puede hacer una unica linea de codigo solo diciendo si es delivery (0) o pick-up (1)
btn_fillmentOption = '//input[@id="fulfillmentOptionButtonGroup{}"]'
# Pick up
# Seleccion lugar y dia
btn_lugar_definido_espera = '//label[@class="form-selector-label "][@for="checkout.fulfillment.pickupTab.pickup.storeLocator-{}"]'
btn_lugar_definido = '//input[@value="{}"][@id="checkout.fulfillment.pickupTab.pickup.storeLocator-{}"]'
label_date = '//input[@id="bartPickupDateSelector{}"]'
# Seleccion de hora 
select_hora = '//select[@aria-labelledby="timeWindows_label"][@class=" form-dropdown-select"]'
# Delivery 
# Boton
btn_continue_shipping = '//button[@id="rs-checkout-continue-button-bottom"][@type="button"][@class=" form-button "]' # Es el mismo boton, no cambia al igual que lo hace en producto


''' Pagina de seleccion de la persona que retira el producto '''
btn_persona_retiro = '//label[@for="pickupOptionButtonGroup{}"][@class="as-buttongroup-button"]' # 0 para el mismo, 1 para otra 
# Textos
text_firstName = '//input[@type="text"][@name="firstName"]'
text_lastName = '//input[@type="text"][@name="lastName"]'
text_email = '//input[@type="email"][@name="emailAddress"]'
text_phoneNumber = '//input[@type="tel"][@name="fullDaytimePhone"]'
# Boton 
btn_continue_payment = '//button[@id="addressVerification"][@type="button"][@class=" form-button "]' # los botones no son lo mismo, aca cuando va a pick up cambia, utiliza el mismo boton que btn_continue_shipping


''' Pagina de forma de pago ''' 
# botones en la pagina billing 
contenedor_billling = '//fieldset[@class="rs-payment-section"]'
btn_credit_card = '//input[@id="checkout.billing.billingOptions.options.1"][@name="checkout.billing.billingOptions.selectBillingOption"]' # Revisar en el otro codigo como esta
btn_continue_to_review = '//button[@id="rs-checkout-continue-button-bottom"][@type="button"][@class=" form-button "]' # Mismo boton que btn_continue_shipping


''' Pagina confirmacion de compra ''' 
# boton para concretar la compra
btn_place_your_order = '//button[@id="rs-checkout-continue-button-bottom"][@type="button"][@class=" form-button "]' # Mismo boton que btn_continue_shipping (nota 2: cambia en aria-described)



# pagina de compra realizada
text_nr_orden = '//*[@id="thankyou-container"]/div/div[2]/div[1]/div/div/a'



