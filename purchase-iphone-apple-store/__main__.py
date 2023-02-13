from .purchase import Purchase
from .filesManager import FilesHandler
from .classes import *
from .constants import DATA_PATH, EXCEL_PATH, NUMBER_ORDER_PATH, STORE_JSON, CONFIG_JSON, PRODUCT_JSON
from datetime import date
import os
import sys

fileHandler = FilesHandler()
dateFile = date.today()

def productVerification(selectedProduct, jsonFile):
    productList = fileHandler.readJson(DATA_PATH / jsonFile)
    for product in productList:
        if selectedProduct.lower() == product.lower():
            return productList[product]
    return False

def storeVerification(selectedStore, jsonFile):
    storesList = fileHandler.readJson(DATA_PATH / jsonFile)
    for store in storesList:
        if selectedStore.lower() == storesList[store]["nombre"].lower():
            return storesList[store] 
    return False 

def optionalStoreList(product, jsonFile):
    optionalStores = {}

    for i in range(1, 10):
        if str(product[f'OPCIONAL {i}']) != "nan":
            optionalStores[f'{i}'] = storeVerification(str(product[f'OPCIONAL {i}']), jsonFile)

    return optionalStores
    
def cardDataVerification(product):
    newCard = {}
    
    if str(product['NUMERO DE TARJETA CREDITO/DEBITO']) != "nan":
        cardData = {
            "numberCard": int(product['NUMERO DE TARJETA CREDITO/DEBITO']),
            "expiration": str(product['FECHA VENCIMIENTO']),
            "cvv": int(product['CVV'])
        }
    else:
        cardData = None

    if ((str(product['NOMBRE']) != "nan") and (str(product['APELLIDO']) != "nan")):
        billingInformation = {
            "firstName": str(product['NOMBRE']),
            "lastName": str(product['APELLIDO'])
        }
    else:
        billingInformation = None

    newCard["creditCard"] = cardData
    newCard["billingInformation"] = billingInformation
    return newCard


def getConfigUser(jsonFile):
    config = fileHandler.readJson(DATA_PATH / jsonFile)
    return config 

def showCompletedPurchase(listProductTotal):
    if (fileHandler.errorProduct):
        diffList = listProductTotal - len(fileHandler.errorProduct)

        print('+----------------------------------------------------------------------------+')
        print(f' Se ha completado exitosamente un total de {diffList} compras.')
        print(f' Se ha fallado un total de {len(fileHandler.errorProduct)} compras.')
        print(f' Por los siguiente errores:')
        for err in fileHandler.errorProduct:
            print(f' {err} ')
        print('+----------------------------------------------------------------------------+')


def main():
    os.system('cls')
    print("                 ============ BOT APPLE ============                 ")
    print("SE NECESITA QUE SE INGRESE EL NOMBRE DE UN ARCHIVO EXCEL Y EL NOMBRE DE UNA HOJA DEL MISMO ARCHIVO ")
    print("Se usara como archivo predeterminado el 'BOT.xlsx' y la hoja 'Compras' del mismo")

    try:
        config = getConfigUser(CONFIG_JSON)
        excelSheet = config['sheetNameBot']

        # Config system
        timeOut = config['timeOut']
        frequency = config['frequency']
        acceptedNames = config['acceptedNames']
        carriers = config['carrier']
        #userDriverInfo = config['userDriver']

        fileHandler.acceptedColumnsNames = acceptedNames
        fileHandler.sheetName = 'Compras'

        # Find an excel file in the excel folder
        mainFile = fileHandler.getExcelFile(EXCEL_PATH)
        mainFileName = mainFile.replace(f'{EXCEL_PATH}',"").strip()
        mainFileName = "".join(filter(str.isalnum, mainFileName))
        mainFileName = mainFileName.replace("xlsx",".xlsx")
        print(f"Lectura del archivo {mainFileName}")
        
        # Get information of purchase excel
        sheetNameDriver = 'Information'
        userDriverInfo = fileHandler.getDriverPurchase(mainFile, sheetNameDriver)

        # Name the file to be saved
        saveFileName = f'{dateFile}-{mainFileName}'

        # Backup file name 
        backupFileName = f'{dateFile}-{mainFileName.replace(".xlsx","").strip()}-backup.xlsx'

        purchaseList = fileHandler.readExcelFile(mainFile, excelSheet)
        
        # Open or create a excel file where the order numbers will be stored
        numberOrdersFile = fileHandler.openOrCreateExcelFile(NUMBER_ORDER_PATH, saveFileName) 

        # Instance of int variable
        listProductTotal = 0
    except Exception as ex:
        print(f'{ex.__class__.__name__}: {ex}')
        print("Ha ocurrido un error inesperado.")
        print("Finalizando BOT APPLE...")
        sys.exit(1)

    try:
        # Start shopping list
        for product in purchaseList:
            # 
            modelProduct = productVerification(product['MODELO'], PRODUCT_JSON)
            storeProduct = storeVerification(product['STORE'], STORE_JSON)
            optionalStoreProduct = optionalStoreList(product, STORE_JSON)
            newCardProduct = cardDataVerification(product)
            carrierProduct = product['OPERADOR'].lower()

            if (modelProduct!=False):
                # Error variable
                errProduct = {}
                # Important information is completed
                if (carrierProduct != 'unlocked'):
                    carrierInformation =  CarrierInformation(
                        number = carriers[carrierProduct]['number'],
                        postal = carriers[carrierProduct]['postal']
                    )
                else:
                    carrierInformation = None

                productInformation = ProductInformation(
                    model = modelProduct[0],
                    display = modelProduct[1],
                    memory = modelProduct[2],
                    color = modelProduct[3]
                )

                purchaseInformation = PurchaseInformation(
                    username = product['USER'],
                    password = product['PASSWORD'],
                    carrier = product['OPERADOR'].lower(),
                    quantify = int(product['CANTIDAD']),
                    store = storeProduct,
                    storesList = optionalStoreProduct,
                    newCard = newCardProduct,
                    userDriver = userDriverInfo
                )

                purchaseProduct = Purchase(productInformation, purchaseInformation)
                purchaseProduct.timeOut = timeOut
                purchaseProduct.frequency = frequency
                purchaseProduct.carrierInformation = carrierInformation
                purchaseProduct.productName = str(product['MODELO']).lower()

                # Conteo de cantidad total de productos
                listProductTotal+=purchaseProduct.purchaseInformation.quantify

                print('=======================================================================================')
                print(f'Se inicia la compra del producto: {purchaseProduct.productName}')

                if purchaseProduct.purchaseInformation.carrier != 'unlocked':
                    # Se tiene que comprar la cantidad dicha
                    for repeat in range(purchaseProduct.purchaseInformation.quantify):
                        
                        print('---------------------------------------------------------------------------------------')
                        print(f'Cant: {repeat+1} de {purchaseProduct.purchaseInformation.quantify}')

                        if ((repeat+1)>1):
                            repeatPurchaseProduct = Purchase(productInformation, purchaseInformation)
                            repeatPurchaseProduct.timeOut = timeOut
                            repeatPurchaseProduct.frequency = frequency
                            repeatPurchaseProduct.carrierInformation = carrierInformation
                            repeatPurchaseProduct.productName = str(product['MODELO']).lower()
                            purchaseProduct = repeatPurchaseProduct  
                            
                        purchaseProduct.run()

                        if purchaseProduct.status ==  "Completado":
                            fileHandler.writeExcelFile(numberOrdersFile, purchaseProduct)
                        else:
                            print(f'Ha fallado la compra del producto: {purchaseProduct.productName}')
                            errProduct['errorName'] = purchaseProduct.errorName
                            errProduct['product'] = purchaseProduct.productName
                            fileHandler.errorProduct.append(errProduct)
                    
                elif purchaseProduct.purchaseInformation.carrier == 'unlocked':
                    
                    print('---------------------------------------------------------------------------------------')
                    
                    purchaseProduct.run()

                    if purchaseProduct.status ==  "Completado":
                        fileHandler.writeExcelFile(numberOrdersFile, purchaseProduct)
                    else:
                        print(f'Ha fallado la compra del producto: {purchaseProduct.productName}')
                        errProduct['errorName'] = purchaseProduct.errorName
                        errProduct['product'] = purchaseProduct.productName
                        fileHandler.errorProduct.append(errProduct)
            else:
                errProduct['errorName'] = 'ModelNotFound'
                errProduct['product'] = product['MODELO'].lower()
                fileHandler.errorProduct.append(errProduct)
        
        #showCompletedPurchase(listProductTotal)

        fileHandler.saveExcelFile(numberOrdersFile, saveFileName, NUMBER_ORDER_PATH)
        
        print("Finalizando BOT APPLE...")

    except PermissionError:
        print(f"Ha ocurrido un error al guardar el archivo {saveFileName} .")
        print(f"Posiblemente el archivo existente este siendo usado por otro programa o no tenga los permisos necesarios para modificarlo.\nSe guardara la informacion en un nuevo archivo nombrado {backupFileName}") 
        fileHandler.saveExcelFile(numberOrdersFile, backupFileName, NUMBER_ORDER_PATH) 
        print("Finalizando BOT APPLE...")
        sys.exit(1)
    except KeyboardInterrupt:
        fileHandler.saveExcelFile(numberOrdersFile, saveFileName, NUMBER_ORDER_PATH) 
        print("Finalizando BOT APPLE...")
        sys.exit(1)
    except Exception as ex:
        print(f'{ex.__class__.__name__}: {ex}')
        fileHandler.saveExcelFile(numberOrdersFile, saveFileName, NUMBER_ORDER_PATH) 
        print("Finalizando BOT APPLE...")
        sys.exit(1)

if __name__ == "__main__":
    main()