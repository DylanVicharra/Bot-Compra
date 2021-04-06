# Pagina Apple 

url_apple = 'https://www.apple.com'
url_producto = f'{url_apple}/shop/buy-iphone'
url_bag = f'{url_apple}/shop/bag'
url_billing = str('https://secure2.store.apple.com/shop/checkout?_s=Billing')

# botones y textos para seleccion producto con operardor

text_stock = '//*[@id="primary"]/summary-builder/div[2]/div[1]/materializer/div[1]/div/div/ul/li[1]/span'
btn_trade = '//*[@id="tradeup-inline-heroselector"]/div/div/fieldset/div/div[1]/div/div' 
btn_full_price = '/html/body/div[2]/div[7]/div[2]/div/store-provider/step1-flagship/div/div[3]/materializer[2]/purchase-options/fieldset/materializer[1]/div/div[1]/div/div/label'
btn_continue_product = '/html/body/div[2]/div[7]/div[2]/div/store-provider/step1-flagship/div/div[3]/summary-builder/div[2]/div[1]/div/div[1]/div[2]/div/div/form/div/span/button'

# botones y textos para seleccion producto sin operador  
btn_full_price_unlocked = '//*[@id="primary"]/materializer[2]/purchase-options/fieldset/materializer[2]/div/div[2]'
btn_add_bag = '/html/body/div[2]/div[7]/div[2]/div/store-provider/step1-flagship/div/div[3]/summary-builder/div[2]/div[1]/div/div[1]/div[2]/div/div/form/div/span/button'

# aparece cuando no es un iphone 12, ventana que activacion
btn_activation_carrier_now = '/html/body/div[2]/div[7]/div/div/div[2]/div[1]/form/div[1]/span/button'

# botones y textos para verificacion del operador
text_nr_operador = '//*[@id="ctn"]'
text_cod_postal = '//*[@id="postalcode"]'
btn_siguiente = '//*[@id="preauth-button-next"]'

# botones en aviso del operador y descripcion del dispositivo
btn_add_bag_2 = '/html/body/div[1]/div[6]/div/div[2]/a'

# botones en pagina bag
btn_checkout = '//*[@id="shoppingCart.actions.navCheckout"]'

# botones en ventana sign-in faster 
btn_continue_as_guest = '//*[@id="signIn.guestLogin.guestLogin"]'

# botones y textos de la ventana checkout
btn_delivery = '//*[@id="checkout-container"]/div/div[6]/div[1]/div[2]/div/div/div[1]/div/div/div/fieldset/div[1]/div[1]/label'
text_zip_code= '/html/body/div[2]/div[4]/div/div[6]/div[1]/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div/input'
btn_continue_shipping = '//*[@id="rs-checkout-continue-button-bottom"]'

# botones y textos de informacion del delivery 
text_name = '/html/body/div[2]/div[4]/div/div[6]/div[1]/div[2]/div/div/div/div[1]/div[3]/fieldset/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/input'
text_last_name = '/html/body/div[2]/div[4]/div/div[6]/div[1]/div[2]/div/div/div/div[1]/div[3]/fieldset/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/input'
text_street = '/html/body/div[2]/div[4]/div/div[6]/div[1]/div[2]/div/div/div/div[1]/div[3]/fieldset/div/div/div/div/div/div/div/div/div/div[3]/div/div/div/div/input'
text_home = '/html/body/div[2]/div[4]/div/div[6]/div[1]/div[2]/div/div/div/div[1]/div[3]/fieldset/div/div/div/div/div/div/div/div/div/div[4]/div/div/div/div/input'
text_zip_code_ship = '/html/body/div[2]/div[4]/div/div[6]/div[1]/div[2]/div/div/div/div[1]/div[3]/fieldset/div/div/div/div/div/div/div/div/div/div[5]/div/fieldset/div/div/div[1]/div/div/div/input'

# texto de informacion de contacto /
text_email = '/html/body/div[2]/div[4]/div/div[6]/div[1]/div[2]/div/div/div/div[1]/fieldset/div[1]/div/div/div/div/div[1]/div/div/div/input'
text_phone_number = '/html/body/div[2]/div[4]/div/div[6]/div[1]/div[2]/div/div/div/div[1]/fieldset/div[2]/div/div/div/div/div[1]/div/div/div/div/input'
btn_continue_payment = '//*[@id="addressVerification"]'

# botones en la pagina billing 
btn_credit_card = '//*[@id="checkout.billing.billingOptions.options.0-selector"]/label'
text_card = '/html/body/div[2]/div[4]/div/div[7]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/fieldset/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div/div/input'
text_expired = '/html/body/div[2]/div[4]/div/div[7]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/fieldset/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div/div/input'
text_cvv = '/html/body/div[2]/div[4]/div/div[7]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/fieldset/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[1]/input'
btn_continue_to_review = '/html/body/div[2]/div[4]/div/div[7]/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div/div/button'

# boton para concretar la compra

btn_place_your_order = '/html/body/div[2]/div[4]/div/div[5]/div[1]/div[1]/div/div/div[2]/div[5]/div/div/div/div[1]/button'

