class Producto: 
    
    def __init__(self, modelo, display, memoria, color, operador, cantidad, username, password, order_option, lista_tiendas_opcionales):
        self.modelo = modelo 
        self.display = display
        self.memoria = memoria
        self.color = color
        self.operador = operador
        self.cantidad = cantidad
        self.username = username
        self.password = password
        self.order_option = order_option
        self.lista_tiendas_opcionales = lista_tiendas_opcionales
        self.producto_orden = None
        self.estado = None


