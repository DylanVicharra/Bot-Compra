from .driver import Driver
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .constants import * 
from .errors import NumberOrderNoFound, NoStoreAvailable

class Purchase:

    timeOut = None
    frequency = None
    numberOrder = None
    status = None
    errorName = None
    carrierInformation = None
    productName = None

    def __init__(self, productInformation, purchaseInformation):
        self.productInformation = productInformation
        self.purchaseInformation = purchaseInformation
        self.driver = Driver()

    def run(self):
        purchaseSteps = [
            self.productSelection,
            self.carrierOption,
            self.carrierCheck,
            self.carrierNext,
            self.bag,
            self.loginAppleId,
            self.orderOptions,
            self.pickupOrDelivery,
            self.methodPayment,
            self.finishButton,
            self.getOrderNumber
        ]

        for step in purchaseSteps:
            try:
                if 'carrier' in str(step):
                    if (self.purchaseInformation.carrier != 'unlocked'):
                        step()
                else:
                    step()
            except Exception as ex: 
                if ((ex.__class__.__name__) in ['TimeoutException','ElementNotInteractableException']):
                    print(f'{ex.__class__.__name__}: Elemento no encontrado.')
                else:
                    print(f'{ex.__class__.__name__}: {ex}')
                self.status = "Incompleto"
                self.errorName = ex.__class__.__name__
                break
        # finish the instance of driver    
        self.driver.finishDriver()


    def favoriteStores(self):
        print("Se busca tiendas dentro de la lista de tiendas preferidas.")
        for appleStore in self.purchaseInformation.storesList:
            availableStore = self.driver.waitWebElement(elements = 'one', 
                                                        timeOut = self.timeOut, 
                                                        frequency = self.frequency, 
                                                        typeSearch = By.XPATH,
                                                        nameSearch = DEFINED_STORE_BUTTON.format(self.purchaseInformation.storesList[appleStore]["codigo"]))

            if (availableStore.get_property('disabled') == False):
                print(f'Se encontro una tienda disponible: {self.purchaseInformation.storesList[appleStore]["nombre"]}')
                self.purchaseInformation.store = self.purchaseInformation.storesList[appleStore]
                self.driver.scrollToWebElement(type = 'button',
                                                webElement = availableStore)
                
                try:
                    self.driver.waitWebElement(elements = 'one', 
                                                        timeOut = self.timeOut, 
                                                        frequency = self.frequency, 
                                                        typeSearch = By.XPATH,
                                                        nameSearch = '//li[@class="rt-storelocator-store-multipleavailability"]')
                    return True
                except:
                    print(f'La tienda {self.purchaseInformation.storesList[appleStore]["nombre"]} no tiene disponibles horarios, se buscara otro.')
        
        raise NoStoreAvailable("No hay tiendas disponibles. Se termina la compra del producto")

    def selectNoAppleCare(self):
        try:
            noAppleCareButton = self.driver.waitWebElement(elements = 'one',
                                                            timeOut = self.timeOut,
                                                            frequency = self.frequency,
                                                            typeSearch = By.XPATH,
                                                            nameSearch = NO_APPLE_CARE_BUTTON)

            self.driver.scrollToWebElement(type = 'buttonPanel',
                                            webElement = noAppleCareButton)
        except:
            noAppleCareButton = self.driver.waitWebElement(elements = 'one',
                                                        timeOut = self.timeOut,
                                                        frequency = self.frequency,
                                                        typeSearch = By.XPATH,
                                                        nameSearch = NO_APPLE_CARE_BUTTON_PLUS)

            self.driver.scrollToWebElement(type = 'buttonPanel',
                                        webElement = noAppleCareButton)

    def productSelection(self):

        print("Se esta seleccionando el producto")

        self.driver.website(PRODUCT_URL.format(self.productInformation.model, self.productInformation.display, self.productInformation.memory, self.productInformation.color, self.purchaseInformation.carrier))
        
        # Search first element
        tradeButton = self.driver.waitWebElement(elements = 'one', 
                                                timeOut = self.timeOut, 
                                                frequency = self.frequency, 
                                                typeSearch = By.XPATH,
                                                nameSearch = TRADE_BUTTON)

        self.driver.scrollToWebElement(type = 'loadElements', 
                                        webElement = tradeButton)

        fullPriceButton = self.driver.waitWebElement(elements = 'one',
                                                        timeOut = self.timeOut,
                                                        frequency = self.frequency,
                                                        typeSearch = By.XPATH,
                                                        nameSearch = FULLPRICE_BUTTON)

        self.driver.scrollToWebElement(type = 'buttonPanel', 
                                        webElement = fullPriceButton)

        carrierButton = self.driver.waitWebElement(elements = 'one',
                                                    timeOut = self.timeOut,
                                                    frequency = self.frequency,
                                                    typeSearch = By.XPATH,
                                                    nameSearch = CARRIER_BUTTON.format(self.purchaseInformation.carrier.upper()))
        
        self.driver.scrollToWebElement(type = 'loadElements',
                                        webElement = carrierButton)

        self.selectNoAppleCare()

        continueButton = self.driver.waitWebElement(elements = 'one',
                                                        timeOut = self.timeOut,
                                                        frequency = self.frequency,
                                                        typeSearch = By.XPATH,
                                                        nameSearch = CONTINUE_PRODUCT_BUTTON)
                                                
        self.driver.scrollToWebElement(type = 'button',
                                        webElement = continueButton)

    def carrierOption(self):
        try:
            activationCarrierButton = self.driver.waitWebElement(elements = 'one',
                                                        timeOut = self.timeOut,
                                                        frequency = self.frequency,
                                                        typeSearch = By.XPATH,
                                                        nameSearch = ACTIVATION_CARRIER_BUTTON)

            self.driver.scrollToWebElement(type = 'button',
                                            webElement = activationCarrierButton)
        except:
            pass
        
    def carrierCheck(self):
        print("Se esta verificando el operador")

        numberCarrierText = self.driver.waitWebElement(elements = 'one',
                                                        timeOut = self.timeOut,
                                                        frequency = self.frequency,
                                                        typeSearch = By.XPATH,
                                                        nameSearch = NUMBER_CARRIER_TEXT)

        self.driver.scrollToWebElement(type = 'text',
                                            webElement = numberCarrierText,
                                            textBox = self.carrierInformation.number)

        postalCarrierText = self.driver.waitWebElement(elements = 'one',
                                                        timeOut = self.timeOut,
                                                        frequency = self.frequency,
                                                        typeSearch = By.XPATH,
                                                        nameSearch = POSTAL_CARRIER_TEXT)

        self.driver.scrollToWebElement(type = 'text',
                                            webElement = postalCarrierText,
                                            textBox = self.carrierInformation.postal)


        continueCarrierButton = self.driver.waitWebElement(elements = 'one',
                                                            timeOut = self.timeOut,
                                                            frequency = self.frequency,
                                                            typeSearch = By.XPATH,
                                                            nameSearch = CONTINUE_CARRIER_BUTTON)

        self.driver.scrollToWebElement(type = 'button',
                                            webElement = continueCarrierButton)

    def carrierNext(self):
        carrierNextButton = self.driver.waitWebElement(elements = 'one',
                                                        timeOut = self.timeOut,
                                                        frequency = self.frequency,
                                                        typeSearch = By.XPATH,
                                                        nameSearch = NEXT_CARRIER_BUTTON)

        self.driver.scrollToWebElement(type = 'button',
                                            webElement = carrierNextButton)        

        addBagButton = self.driver.waitWebElement(elements = 'one',
                                                        timeOut = self.timeOut,
                                                        frequency = self.frequency,
                                                        typeSearch = By.XPATH,
                                                        nameSearch = '//button[@class="button button-block button-super"]')
        
        '''self.driver.scrollToWebElement(type = 'button',
                                            webElement = addBagButton)'''
    
    def bag(self):
        self.driver.website(BAG_URL)

        if (self.purchaseInformation.carrier == 'unlocked'): 
            quantityPicklist = self.driver.waitWebElement(elements = 'one',
                                                        timeOut = self.timeOut,
                                                        frequency = self.frequency,
                                                        typeSearch = By.XPATH,
                                                        nameSearch = QUANTIFY_PICKLIST)

            quantitySelect = Select(quantityPicklist)

            priceText = self.driver.waitWebElement(elements = 'one',
                                                        timeOut = self.timeOut,
                                                        frequency = self.frequency,
                                                        typeSearch = By.XPATH,
                                                        nameSearch = PRICE_LABEL)
            
            priceUnit = float((priceText.text).replace("$", "").replace(",","").strip())

            if (self.purchaseInformation.quantify < 10):
                quantitySelect.select_by_value(str(self.purchaseInformation.quantify))
            elif (self.purchaseInformation.quantify >= 10):
                quantitySelect.select_by_value(str(self.purchaseInformation.quantify))

                quantityText = self.driver.waitWebElement(elements = 'one',
                                                        timeOut = self.timeOut,
                                                        frequency = self.frequency,
                                                        typeSearch = By.XPATH,
                                                        nameSearch = QUANTIFY_TEXT)

                self.driver.scrollToWebElement(type = 'text',
                                            webElement = quantityText,
                                            textBox = str(self.purchaseInformation.quantify) + Keys.ENTER)
            
        checkoutButton = self.driver.waitWebElement(elements = 'one',
                                                    timeOut = self.timeOut,
                                                    frequency = self.frequency,
                                                    typeSearch = By.XPATH,
                                                    nameSearch = CHECKOUT_BUTTON)
        
        self.driver.scrollToWebElement(type = 'button',
                                        webElement = checkoutButton)

    def loginAppleId(self):

        print("Se esta iniciando sesion en Apple ID")

        loginIframe = self.driver.waitWebElement(elements = 'one',
                                                    timeOut = self.timeOut,
                                                    frequency = self.frequency,
                                                    typeSearch = By.XPATH,
                                                    nameSearch = APPLE_ID_IFRAME)

        self.driver.switchToFrame(loginIframe)

        usernameText = self.driver.waitWebElement(elements = 'one',
                                                    timeOut = self.timeOut,
                                                    frequency = self.frequency,
                                                    typeSearch = By.XPATH,
                                                    nameSearch = USERNAME_TEXT)

        self.driver.scrollToWebElement(type = 'text',
                                        webElement = usernameText,
                                        textBox = self.purchaseInformation.username + Keys.ENTER)

        passwordText = self.driver.waitWebElement(elements = 'one',
                                                    timeOut = self.timeOut,
                                                    frequency = self.frequency,
                                                    typeSearch = By.XPATH,
                                                    nameSearch = PASSWORD_TEXT)

        self.driver.scrollToWebElement(type = 'text',
                                        webElement = passwordText,
                                        textBox = self.purchaseInformation.password + Keys.ENTER) 

        '''signInButton = self.driver.waitWebElement(elements = 'one',
                                                    timeOut = self.timeOut,
                                                    frequency = self.frequency,
                                                    typeSearch = By.XPATH,
                                                    nameSearch = SIGNIN_BUTTON)

        self.driver.scrollToWebElement(type = 'button',
                                        webElement = signInButton) '''
        

    def pickupOrDelivery (self):

        print("Se rellena la informacion de contacto")
    
        if (self.purchaseInformation.store['nombre'].lower() == 'delivery'):
            continuePaymentButton = self.driver.waitWebElement(elements = 'one',
                                                                timeOut = self.timeOut,
                                                                frequency = self.frequency,
                                                                typeSearch = By.XPATH,
                                                                nameSearch = CONTINUE_PAYMENT_BUTTON)

            self.driver.scrollToWebElement(type = 'button',
                                            webElement = continuePaymentButton)
        
        else: 
    
            personPickupButton = self.driver.waitWebElement(elements = 'one',
                                                            timeOut = self.timeOut,
                                                            frequency = self.frequency,
                                                            typeSearch = By.XPATH,
                                                            nameSearch = PERSON_PICKUP_BUTTON.format(0))

            self.driver.scrollToWebElement(type = 'buttonPanel',
                                            webElement = personPickupButton)
                                            
            firstnameText = self.driver.waitWebElement(elements = 'one',
                                                        timeOut = self.timeOut,
                                                        frequency = self.frequency,
                                                        typeSearch = By.XPATH,
                                                        nameSearch = FIRSTNAME_TEXT)

            self.driver.sendKeysActions(webElement=firstnameText, keyDown = Keys.CONTROL, command = 'a', extra = Keys.DELETE, text = 'Esteban')
                                        
            '''self.driver.scrollToWebElement(type = 'text',
                                            webElement = firstnameText,
                                            textBox = 'Esteban')'''

            lastnameText = self.driver.waitWebElement(elements = 'one',
                                                        timeOut = self.timeOut,
                                                        frequency = self.frequency,
                                                        typeSearch = By.XPATH,
                                                        nameSearch = LASTNAME_TEXT)

            self.driver.sendKeysActions(webElement=lastnameText, keyDown = Keys.CONTROL, command = 'a', extra = Keys.DELETE, text = 'Iturrieta')
            
            '''self.driver.scrollToWebElement(type = 'text',
                                            webElement = lastnameText,
                                            textBox = 'Iturrieta')'''

            continueShippingButton = self.driver.waitWebElement(elements = 'one',
                                                            timeOut = self.timeOut,
                                                            frequency = self.frequency,
                                                            typeSearch = By.XPATH,
                                                            nameSearch = CONTINUE_SHIPPING_BUTTON)
            
            self.driver.scrollToWebElement(type = 'button',
                                            webElement = continueShippingButton)

    
    def orderOptions(self):
        print("Se selecciona el metodo de envio o retiro del producto")
        
        if (self.purchaseInformation.store['nombre'].lower() == 'delivery'):
            selectedOption = 0
        else: 
            selectedOption = 1
        
        fillmentButton = self.driver.waitWebElement(elements = 'one',
                                                            timeOut = self.timeOut,
                                                            frequency = self.frequency,
                                                            typeSearch = By.XPATH,
                                                            nameSearch = FILLMENT_OPTION_BUTTON.format(selectedOption))

        self.driver.scrollToWebElement(type = 'button', 
                                        webElement= fillmentButton)

        if (selectedOption == 0):
            deliveryOptionsButton = self.driver.waitWebElement(elements = 'many',
                                                                timeOut = self.timeOut,
                                                                frequency = self.frequency,
                                                                typeSearch = By.XPATH,
                                                                nameSearch = DELIVERY_OPTION_BUTTON)

            if (len(deliveryOptionsButton) != 0):
                
                count = 0

                for deliveryOption in deliveryOptionsButton:

                    deliveryInformationLeftCol = self.driver.findChildWebElement(elements = 'one',
                                                                                    webElementParent = deliveryOption,
                                                                                    typeSearch = By.XPATH,
                                                                                    nameSearch = DELIVERY_INFORMATION_LEFT_COL)

                    deliveryCharge = self.driver.findChildWebElement(elements = 'one',
                                                                        webElementParent = deliveryOption,
                                                                        typeSearch = By.XPATH,
                                                                        nameSearch = DELIVERY_CHARGE_LABEL)
                    
                    deliveryMethod = self.driver.findChildWebElement(elements = 'one',
                                                                        webElementParent = deliveryInformationLeftCol,
                                                                        typeSearch = By.XPATH,
                                                                        nameSearch = DELIVERY_METHOD_LABEL)

                    deliveryDate = self.driver.findChildWebElement(elements = 'one',
                                                                        webElementParent = deliveryInformationLeftCol,
                                                                        typeSearch = By.XPATH,
                                                                        nameSearch = DELIVERY_DATE_LABEL)

                    if ((deliveryCharge.text.find("FREE") != -1) and (deliveryMethod.text.find("Express Delivery") != -1)):
                        deliveryLabel = self.driver.findChildWebElement(elements = 'one',
                                                                        webElementParent = deliveryOption,
                                                                        typeSearch = By.XPATH,
                                                                        nameSearch = './/label')

                        self.driver.scrollToWebElement(type = 'buttonPanel', 
                                                        webElement= deliveryLabel)
                        
                        break
                    else: 
                        count +=1
                
                if len(deliveryOptionsButton) == count:
                # No se encontraron las opciones de envio mañana o el otro tipo de entrega
                    raise Exception("No se encontro alguna opcion de Express Delivery")

        if (selectedOption == 1):

            moreStoresButton = self.driver.waitWebElement(elements = 'one',
                                                            timeOut = self.timeOut,
                                                            frequency = self.frequency,
                                                            typeSearch = By.XPATH,
                                                            nameSearch = '//button[@data-autom="show-more-stores-button"]')
            
            self.driver.scrollToWebElement(type = 'button', 
                                            webElement= moreStoresButton)


            definedStoreButton = self.driver.waitWebElement(elements = 'one',
                                                            timeOut = self.timeOut,
                                                            frequency = self.frequency,
                                                            typeSearch = By.XPATH,
                                                            nameSearch = DEFINED_STORE_BUTTON.format(self.purchaseInformation.store["codigo"]))

            if (definedStoreButton.get_property('disabled') == True):
                print(f'La tienda no esta disponible se va buscar otra')
                self.favoriteStores()
            else:
                self.driver.scrollToWebElement(type = 'buttonPanel', 
                                                webElement= definedStoreButton)

                try:
                    self.driver.waitWebElement(elements = 'one', 
                                                timeOut = self.timeOut, 
                                                frequency = self.frequency, 
                                                typeSearch = By.XPATH,
                                                nameSearch = '//li[@class="rt-storelocator-store-multipleavailability"]')
                except:
                    self.favoriteStores()
            
            timePicklist = self.driver.waitWebElement(elements = 'one', 
                                                        timeOut = self.timeOut, 
                                                        frequency = self.frequency, 
                                                        typeSearch = By.XPATH,
                                                        nameSearch = TIME_PICKLIST)

            selectedHour = Select(timePicklist)

            selectedHour.select_by_index(2)

        continueShippingButton = self.driver.waitWebElement(elements = 'one', 
                                                            timeOut = self.timeOut, 
                                                            frequency = self.frequency, 
                                                            typeSearch = By.XPATH,
                                                            nameSearch = CONTINUE_SHIPPING_BUTTON)
        
        self.driver.scrollToWebElement(type = 'button',
                                        webElement= continueShippingButton)
    
    def methodPayment(self):
        print("Se selecciona el metodo de pago")

        if (self.purchaseInformation.newCard['creditCard'] is None):
            creditCardButton = self.driver.waitWebElement(elements = 'one', 
                                                            timeOut = self.timeOut, 
                                                            frequency = self.frequency, 
                                                            typeSearch = By.XPATH,
                                                            nameSearch = CREDIT_CARD_BUTTON)
            
            self.driver.scrollToWebElement(type = 'buttonPanel',
                                            webElement= creditCardButton)

        else: 
            newCreditCardButton = self.driver.waitWebElement(elements = 'one', 
                                                            timeOut = self.timeOut, 
                                                            frequency = self.frequency, 
                                                            typeSearch = By.XPATH,
                                                            nameSearch = NEW_CREDIT_CARD_BUTTON)

            self.driver.scrollToWebElement(type = 'button',
                                            webElement= newCreditCardButton)

            numberCardText = self.driver.waitWebElement(elements = 'one', 
                                                            timeOut = self.timeOut, 
                                                            frequency = self.frequency, 
                                                            typeSearch = By.XPATH,
                                                            nameSearch = NUMBER_CARD_TEXT)

            self.driver.scrollToWebElement(type = 'text',
                                            webElement= numberCardText,
                                            textBox = self.purchaseInformation.newCard['creditCard']["numberCard"])
            
            expirationText = self.driver.waitWebElement(elements = 'one', 
                                                            timeOut = self.timeOut, 
                                                            frequency = self.frequency, 
                                                            typeSearch = By.XPATH,
                                                            nameSearch = EXPIRATION_TEXT)

            self.driver.scrollToWebElement(type = 'text',
                                            webElement= expirationText,
                                            textBox = self.purchaseInformation.newCard['creditCard']['expiration'])

            cvvText = self.driver.waitWebElement(elements = 'one', 
                                                            timeOut = self.timeOut, 
                                                            frequency = self.frequency, 
                                                            typeSearch = By.XPATH,
                                                            nameSearch = CVV_TEXT)
            
            self.driver.scrollToWebElement(type = 'text',
                                            webElement= cvvText,
                                            textBox = self.purchaseInformation.newCard['creditCard']['cvv'])

            if (self.purchaseInformation.newCard['billingInformation'] is not None):
                firstNameText = self.driver.waitWebElement(elements = 'one', 
                                                            timeOut = self.timeOut, 
                                                            frequency = self.frequency, 
                                                            typeSearch = By.XPATH,
                                                            nameSearch = FIRSTNAME_BILL_TEXT)

                self.driver.sendKeysActions(webElement=firstNameText, keyDown = Keys.CONTROL, command = 'a', extra = Keys.DELETE, text = self.purchaseInformation.newCard['billingInformation']['firstName'])

                '''self.driver.scrollToWebElement(type = 'text',
                                                webElement= firstNameText,
                                                textBox = self.purchaseInformation.newCard['billingInformation']['firstName'])'''

                lastNameText = self.driver.waitWebElement(elements = 'one', 
                                                            timeOut = self.timeOut, 
                                                            frequency = self.frequency, 
                                                            typeSearch = By.XPATH,
                                                            nameSearch = LASTNAME_TEXT)
                
                self.driver.sendKeysActions(webElement=lastNameText, keyDown = Keys.CONTROL, command = 'a', extra = Keys.DELETE, text = self.purchaseInformation.newCard['billingInformation']['lastName'])

                '''self.driver.scrollToWebElement(type = 'text',
                                                webElement= lastNameText,
                                                textBox = self.purchaseInformation.newCard['billingInformation']['lastName'])'''

        continueReviewButton = self.driver.waitWebElement(elements = 'one', 
                                                            timeOut = self.timeOut, 
                                                            frequency = self.frequency, 
                                                            typeSearch = By.XPATH,
                                                            nameSearch = CONTINUE_REVIEW_BUTTON)
        
        self.driver.scrollToWebElement(type = 'button',
                                        webElement = continueReviewButton)

    def finishButton(self):
        placeOrderButton = self.driver.waitWebElement(elements = 'one', 
                                                            timeOut = self.timeOut, 
                                                            frequency = self.frequency, 
                                                            typeSearch = By.XPATH,
                                                            nameSearch = PLACE_ORDER_BUTTON)

        self.driver.scrollToWebElement(type = 'button',
                                        webElement = placeOrderButton)                                                   

    def getOrderNumber(self):
        try: 
            numberOrderText = self.driver.waitWebElement(elements = 'one', 
                                                            timeOut = self.timeOut, 
                                                            frequency = self.frequency, 
                                                            typeSearch = By.XPATH,
                                                            nameSearch = NUMBER_ORDER_TEXT)

            self.numberOrder = {
                "link":str(numberOrderText.get_attribute('href')),
                "number":str(numberOrderText.get_attribute('data-evar1').replace("OrderDetails", "").strip())
            }

            self.status = "Completado"
            
            print("La compra se realizo correctamente")
        except:
            if self.driver.driverChrome.title == "Order Options — Secure Checkout":
                raise NumberOrderNoFound("Error: El producto solo puede ser entregado por Delivery.")
            elif self.driver.driverChrome.title == "Rewiew Order — Secure Checkout":
                raise NumberOrderNoFound("Error: La fecha antes selecciona ya no se encuentra disponible.")
            elif self.driver.driverChrome.title == "Payment Details — Secure Checkout":
                raise NumberOrderNoFound("Error: Se debe ingresar otra tarjeta de credito para la compra del producto.")
            elif self.driver.driverChrome.title == "Sorry — Apple":
                raise NumberOrderNoFound("Error: Ha ocurrido un error con el proceso de la compra.")
            else: 
                raise NumberOrderNoFound("Error: Ha ocurrido algo inesperado.")


