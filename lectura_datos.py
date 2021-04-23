from os import path

celulares = {'iphone 12 mini':['iphone-12', '5.4-inch-display'],
             'iphone 12 pro max':['iphone-12-pro', '6.7-inch-display'],
             'iphone 12 pro':['iphone-12-pro', '6.1-inch-display'],
             'iphone 12':['iphone-12', '6.1-inch-display'],
             'iphone 11':['iphone-11', '6.1-inch-display'],
             'iphone xr':['iphone-xr', '6.1-inch-display'],
             'iphone se':['iphone-se', '4.7-inch-display']
            }

def existe_archivo(nombre_archivo):
    if path.exists(f'{nombre_archivo}.xlsx'):
        pass 
    else: 
        print("NOMBRE ARCHIVO INCORRECTO")
        exit(1)

def verificacion_modelo(producto):
    for nombre_producto in celulares:
        if producto.find(nombre_producto)!=-1:
            producto = producto.replace(nombre_producto, "").strip()
            return celulares[nombre_producto], producto

def agrupacion_datos(descripcion):
    # Verifico si el modelo concuerdo y me devuelve el modelo y pantalla 
    modelo_iphone, datos = verificacion_modelo(descripcion.lower())
    # desgloso los otros datos que vienen en la descripcion
    nuevos_datos = datos.lower().split(' ')
    # Uno las dos listas en una sola
    modelo_iphone.extend(nuevos_datos)
    print(modelo_iphone)
    return modelo_iphone
