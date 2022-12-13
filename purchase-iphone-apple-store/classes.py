class ProductInformation:
    def __init__(self, **features):
        self.model = features['model']
        self.display = features['display']
        self.memory = features['memory']
        self.color = features['color']

class PurchaseInformation:
    def __init__(self, **information):
        self.username = information['username']
        self.password = information['password']
        self.carrier = information['carrier']
        self.quantify = information['quantify']
        self.store = information['store']
        self.storesList = information['storesList']
        self.newCard = information['newCard']

class CarrierInformation:
    def __init__(self, **information):
        self.number = information['number']
        self.postal = information['postal']

