from pathlib import Path

# Path
ROOT_PATH = Path(__file__).parent.parent
DATA_PATH = ROOT_PATH / 'data'
EXCEL_PATH = ROOT_PATH / 'excel'
NUMBER_ORDER_PATH = EXCEL_PATH / 'number-orders'

# Files Names
CONFIG_JSON = 'config.json'
PRODUCT_JSON = 'iphones.json'
STORE_JSON = 'stores.json'

# Direcciones 
APPLE_URL = 'https://www.apple.com'
PRODUCT_URL = 'https://www.apple.com/shop/buy-iphone/{}/{}-{}-{}-{}'
BAG_URL = f'{APPLE_URL}/shop/bag'
THANK_YOU_URL = "https://www.apple.com/shop/checkout/thankyou"


''' Pagina del producto '''
# Contenedores
contenedor_botones_producto = '//div[@id="root"]' 
# Botones
TRADE_BUTTON = '//input[@id="noTradeIn"][@value="noTradeIn"][@type="radio"]'  
# Seleccion 
FULLPRICE_BUTTON = '//input[@value="fullprice"][@type="radio"][@name="purchase_option_group"]' 
CARRIER_BUTTON = '//input[@class="form-selector-input"][@name="carrierModel"][contains(@value,"{}")]'
CONTINUE_PRODUCT_BUTTON = '//button[@type="submit"][@class="button button-block"]' 
NO_APPLE_CARE_BUTTON = '//input[@id="applecareplus_59_noapplecare"][@type="radio"]'
# aparece cuando no es un iphone 12, ventana de activacion
ACTIVATION_CARRIER_BUTTON = '//button[@type="submit"][@class="rf-carrier-fork-option-button form-selector-label"][@name="proceed"]'



''' Pagina de validadcion del operador  '''
# botones y textos para verificacion del operador
contenedor_elementos_operador = '//div[@class="page-body"]'
NUMBER_CARRIER_TEXT = '//input[@type="tel"][@name="wirelessNumber"][@class="form-textbox-input"]'
POSTAL_CARRIER_TEXT = '//input[@type="tel"][@name="postalcode"][@class="form-textbox-input"]'
CONTINUE_CARRIER_BUTTON = '//button[@type="submit"][@class="button"]'

# botones en aviso del operador y descripcion del dispositivo
NEXT_CARRIER_BUTTON = '//button[@type="submit"][@class="button"]'


''' Pagina del carrito '''
# botones en pagina bag
CHECKOUT_BUTTON = '//button[@id="shoppingCart.actions.navCheckout"][@class="button button-block"][@data-autom="checkout"]'
# Lista desplegable 
QUANTIFY_PICKLIST = '//div[@class="rs-quantity-wrapper form-dropdown"]/select' 
# Texto precio
PRICE_LABEL = '//div[@class="rs-iteminfo-price"]/p'
# texto si es una cantidad mayor a 10
QUANTIFY_TEXT = '//input[@type="tel"][@value="10"]'



''' Pagina de logueo de Apple ID '''
# textoBox de inicio sesion de AppleID:
APPLE_ID_IFRAME = '//iframe[@id="aid-auth-widget-iFrame"][@name="aid-auth-widget"]'
USERNAME_TEXT = '//input[@id="account_name_text_field"][@type="text"][@can-field="accountName"]'
PASSWORD_TEXT = '//input[@id="password_text_field"][@type="password"][@can-field="password"]'
SIGNIN_BUTTON = '//button[@id="sign-in"]'


''' Pagina de seleccion de entrega '''
# fillmentOption 
FILLMENT_OPTION_BUTTON = '//label[@for="fulfillmentOptionButtonGroup{}"]' #Se puede hacer una unica linea de codigo solo diciendo si es delivery (0) o pick-up (1)
#FILLMENT_OPTION_BUTTON = '//input[@id="fulfillmentOptionButtonGroup{}"]'
# Pick up
# Seleccion lugar y dia
btn_lugar_definido_espera = '//label[@class="form-selector-label"]'
DEFINED_STORE_BUTTON = '//input[@value="{}"][@class="form-selector-input"]' #btn_lugar_definido
label_date = '//input[@id="bartPickupDateSelector{}"]'
# Seleccion de hora 
TIME_PICKLIST = '//select[@class="form-dropdown-select form-dropdown-selectnone"]'
# Delivery 
# Label Opciones
DELIVERY_OPTION_BUTTON = '//div[@class="large-12 small-12 form-selector"]'
# Label cabeceras 
DELIVERY_INFORMATION_LEFT_COL = './/div[@class="column form-selector-left-col rs-fulfillment-delivery-label"]'
DELIVERY_DATE_LABEL = './/span[@class="form-selector-title"]'
DELIVERY_METHOD_LABEL = './/span[@class="form-label-small"]'
DELIVERY_CHARGE_LABEL = './/span[@class="column form-selector-right-col"]'
# Horarios
btn_setup_hora = '//div[@class="rs-time-window-slot rc-dimension-selector-row form-selector"]'
# Boton
CONTINUE_SHIPPING_BUTTON = '//button[@id="rs-checkout-continue-button-bottom"][@type="button"][@class="form-button"]' 


''' Pagina de seleccion de la persona que retira el producto '''
PERSON_PICKUP_BUTTON = '//label[@for="pickupOptionButtonGroup{}"][@class="as-buttongroup-button"]' 
# Textos
FIRSTNAME_TEXT = '//input[@type="text"][@name="firstName"]'
LASTNAME_TEXT = '//input[@type="text"][@name="lastName"]'
EMAIL_TEXT = '//input[@type="email"][@name="emailAddress"]'
PHONE_NUMBER_TEXT = '//input[@type="tel"][@name="fullDaytimePhone"]'
# Boton 
CONTINUE_PAYMENT_BUTTON = '//button[@id="rs-checkout-continue-button-bottom"][@type="button"][@class="form-button"][@data-autom="shipping-continue-button"]'


''' Pagina de forma de pago ''' 
# botones en la pagina billing 
contenedor_billling = '//fieldset[@class="rs-payment-section"]'
# boton tarjeta guardada
CREDIT_CARD_BUTTON = '//input[@id="checkout.billing.billingoptions.saved_card"][@name="checkout.billing.billingOptions.selectBillingOption"]' 
# boton de nueva tarjeta
NEW_CREDIT_CARD_BUTTON = '//input[@id="checkout.billing.billingoptions.credit"][@name="checkout.billing.billingOptions.selectBillingOption"]'
# textos de datos a completar
NUMBER_CARD_TEXT = '//input[@id="checkout.billing.billingOptions.selectedBillingOptions.creditCard.cardInputs.cardInput-0.cardNumber"]'
EXPIRATION_TEXT = '//input[@id="checkout.billing.billingOptions.selectedBillingOptions.creditCard.cardInputs.cardInput-0.expiration"]'
CVV_TEXT = '//input[@id="checkout.billing.billingOptions.selectedBillingOptions.creditCard.cardInputs.cardInput-0.securityCode"]'
FIRSTNAME_BILL_TEXT = '//input[@id="checkout.billing.billingOptions.selectedBillingOptions.creditCard.billingAddress.address.firstName"]'
LASTNAME_BILL_TEXT = '//input[@id="checkout.billing.billingOptions.selectedBillingOptions.creditCard.billingAddress.address.lastName"]'
# boton para confirmar el metodo de pago
CONTINUE_REVIEW_BUTTON = '//button[@id="rs-checkout-continue-button-bottom"][@type="button"][@class="form-button"]' 


''' Pagina confirmacion de compra ''' 
# boton para concretar la compra
PLACE_ORDER_BUTTON = '//button[@id="rs-checkout-continue-button-bottom"][@type="button"][@class="form-button"][@data-autom="continue-button-label"][@aria-describedby="rs-checkout-continuedisclaimer-bottom"]'



# pagina de compra realizada
NUMBER_ORDER_TEXT = '//a[@class="as-buttonlink rs-thankyou-ordernumber"][@data-autom="order-number"]'


