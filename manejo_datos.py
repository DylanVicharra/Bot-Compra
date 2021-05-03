from os import path
import openpyxl as op

iphone_disponibles = {'IPHONE 11 128GB BLACK':['iphone-11','6.1-inch-display','128gb','black'], 'IPHONE 11 128GB GREEN':['iphone-11','6.1-inch-display','128gb','green'], 'IPHONE 11 128GB PURPLE':['iphone-11','6.1-inch-display','128gb','purple'], 'IPHONE 11 128GB RED':['iphone-11','6.1-inch-display','128gb','red'], 'IPHONE 11 128GB WHITE':['iphone-11','6.1-inch-display','128gb','white'], 'IPHONE 11 128GB YELLOW':['iphone-11','6.1-inch-display','128gb','yellow'],
                      'IPHONE 11 256GB BLACK':['iphone-11','6.1-inch-display','256gb','black'], 'IPHONE 11 256GB GREEN':['iphone-11','6.1-inch-display','256gb','green'], 'IPHONE 11 256GB PURPLE':['iphone-11','6.1-inch-display','256gb','purple'], 'IPHONE 11 256GB RED':['iphone-11','6.1-inch-display','256gb','red'], 'IPHONE 11 256GB WHITE':['iphone-11','6.1-inch-display','256gb','white'], 'IPHONE 11 256GB YELLOW':['iphone-11','6.1-inch-display','256gb','yellow'],
                      'IPHONE 11 64GB BLACK':['iphone-11','6.1-inch-display','64gb','black'], 'IPHONE 11 64GB GREEN':['iphone-11','6.1-inch-display','64gb','green'], 'IPHONE 11 64GB PURPLE':['iphone-11','6.1-inch-display','64gb','purple'], 'IPHONE 11 64GB RED':['iphone-11','6.1-inch-display','64gb','red'], 'IPHONE 11 64GB WHITE':['iphone-11','6.1-inch-display','64gb','white'], 'IPHONE 11 64GB YELLOW':['iphone-11','6.1-inch-display','64gb','yellow'],
                      'IPHONE 12 128GB BLACK':['iphone-12','6.1-inch-display','128gb','black'], 'IPHONE 12 128GB BLUE':['iphone-12','6.1-inch-display','128gb','blue'], 'IPHONE 12 128GB GREEN':['iphone-12','6.1-inch-display','128gb','green'], 'IPHONE 12 128GB RED':['iphone-12','6.1-inch-display','128gb','red'], 'IPHONE 12 128GB WHITE':['iphone-12','6.1-inch-display','128gb','white'],
                      'IPHONE 12 256GB BLACK':['iphone-12','6.1-inch-display','256gb','black'], 'IPHONE 12 256GB BLUE':['iphone-12','6.1-inch-display','256gb','blue'], 'IPHONE 12 256GB GREEN':['iphone-12','6.1-inch-display','256gb','green'], 'IPHONE 12 256GB RED':['iphone-12','6.1-inch-display','256gb','red'], 'IPHONE 12 256GB WHITE':['iphone-12','6.1-inch-display','256gb','white'],
                      'IPHONE 12 64GB BLACK':['iphone-12','6.1-inch-display','64gb','black'], 'IPHONE 12 64GB BLUE':['iphone-12','6.1-inch-display','64gb','blue'], 'IPHONE 12 64GB GREEN':['iphone-12','6.1-inch-display','64gb','green'], 'IPHONE 12 64GB RED':['iphone-12','6.1-inch-display','64gb','red'], 'IPHONE 12 64GB WHITE':['iphone-12','6.1-inch-display','64gb','white'],
                      'IPHONE 12 MINI 128GB BLACK':['iphone-12','5.4-inch-display','128gb','black'], 'IPHONE 12 MINI 128GB BLUE':['iphone-12','5.4-inch-display','128gb','blue'], 'IPHONE 12 MINI 128GB GREEN':['iphone-12','5.4-inch-display','128gb','green'], 'IPHONE 12 MINI 128GB RED':['iphone-12','5.4-inch-display','128gb','red'], 'IPHONE 12 MINI 128GB WHITE':['iphone-12','5.4-inch-display','128gb','white'],
                      'IPHONE 12 MINI 256GB BLACK':['iphone-12','5.4-inch-display','256gb','black'], 'IPHONE 12 MINI 256GB BLUE':['iphone-12','5.4-inch-display','256gb','blue'], 'IPHONE 12 MINI 256GB GREEN':['iphone-12','5.4-inch-display','256gb','green'], 'IPHONE 12 MINI 256GB RED':['iphone-12','5.4-inch-display','256gb','red'], 'IPHONE 12 MINI 256GB WHITE':['iphone-12','5.4-inch-display','256gb','white'],
                      'IPHONE 12 MINI 64GB BLACK':['iphone-12','5.4-inch-display','64gb','black'], 'IPHONE 12 MINI 64GB BLUE':['iphone-12','5.4-inch-display','64gb','blue'], 'IPHONE 12 MINI 64GB GREEN':['iphone-12','5.4-inch-display','64gb','green'], 'IPHONE 12 MINI 64GB RED':['iphone-12','5.4-inch-display','64gb','red'], 'IPHONE 12 MINI 64GB WHITE':['iphone-12','5.4-inch-display','64gb','white'],
                      'IPHONE 12 PRO 128GB PACIFIC BLUE':['iphone-12-pro','6.1-inch-display','128gb','pacific-blue'], 'IPHONE 12 PRO 128GB GOLD':['iphone-12-pro','6.1-inch-display','128gb','gold'], 'IPHONE 12 PRO 128GB GRAPHITE':['iphone-12-pro','6.1-inch-display','128gb','graphite'], 'IPHONE 12 PRO 128GB SILVER':['iphone-12-pro','6.1-inch-display','128gb','silver'],
                      'IPHONE 12 PRO 256GB PACIFIC BLUE':['iphone-12-pro','6.1-inch-display','256gb','pacific-blue'], 'IPHONE 12 PRO 256GB GOLD':['iphone-12-pro','6.1-inch-display','256gb','gold'], 'IPHONE 12 PRO 256GB GRAPHITE':['iphone-12-pro','6.1-inch-display','256gb','graphite'], 'IPHONE 12 PRO 256GB SILVER':['iphone-12-pro','6.1-inch-display','256gb','silver'],
                      'IPHONE 12 PRO 512GB PACIFIC BLUE':['iphone-12-pro','6.1-inch-display','512gb','pacific-blue'], 'IPHONE 12 PRO 512GB GOLD':['iphone-12-pro','6.1-inch-display','512gb','gold'], 'IPHONE 12 PRO 512GB GRAPHITE':['iphone-12-pro','6.1-inch-display','512gb','graphite'], 'IPHONE 12 PRO 512GB SILVER':['iphone-12-pro','6.1-inch-display','512gb','silver'],
                      'IPHONE 12 PRO MAX 128GB PACIFIC BLUE':['iphone-12-pro','6.7-inch-display','128gb','pacific-blue'], 'IPHONE 12 PRO MAX 128GB GOLD':['iphone-12-pro','6.7-inch-display','128gb','gold'], 'IPHONE 12 PRO MAX 128GB GRAPHITE':['iphone-12-pro','6.7-inch-display','128gb','graphite'], 'IPHONE 12 PRO MAX 128GB SILVER':['iphone-12-pro','6.7-inch-display','128gb','silver'],
                      'IPHONE 12 PRO MAX 256GB PACIFIC BLUE':['iphone-12-pro','6.7-inch-display','256gb','pacific-blue'], 'IPHONE 12 PRO MAX 256GB GOLD':['iphone-12-pro','6.7-inch-display','256gb','gold'], 'IPHONE 12 PRO MAX 256GB GRAPHITE':['iphone-12-pro','6.7-inch-display','256gb','graphite'], 'IPHONE 12 PRO MAX 256GB SILVER':['iphone-12-pro','6.7-inch-display','256gb','silver'],
                      'IPHONE 12 PRO MAX 512GB PACIFIC BLUE':['iphone-12-pro','6.7-inch-display','512gb','pacific-blue'], 'IPHONE 12 PRO MAX 512GB GOLD':['iphone-12-pro','6.7-inch-display','512gb','gold'], 'IPHONE 12 PRO MAX 512GB GRAPHITE':['iphone-12-pro','6.7-inch-display','512gb','graphite'], 'IPHONE 12 PRO MAX 512GB SILVER':['iphone-12-pro','6.7-inch-display','512gb','silver'],
                      'IPHONE SE 128GB BLACK':['iphone-se','4.7-inch-display','128gb','black'], 'IPHONE SE 128GB RED':['iphone-se','4.7-inch-display','128gb','red'], 'IPHONE SE 128GB WHITE':['iphone-se','4.7-inch-display','128gb','white'],
                      'IPHONE SE 256GB BLACK':['iphone-se','4.7-inch-display','256gb','black'], 'IPHONE SE 256GB RED':['iphone-se','4.7-inch-display','256gb','red'], 'IPHONE SE 256GB WHITE':['iphone-se','4.7-inch-display','256gb','white'],
                      'IPHONE SE 64GB BLACK':['iphone-se','4.7-inch-display','64gb','black'], 'IPHONE SE 64GB RED':['iphone-se','4.7-inch-display','64gb','red'], 'IPHONE SE 64GB WHITE':['iphone-se','4.7-inch-display','64gb','white'],
                      'IPHONE XR 128GB BLACK':['iphone-xr','6.1-inch-display','128gb','black'], 'IPHONE XR 128GB BLUE':['iphone-xr','6.1-inch-display','128gb','blue'], 'IPHONE XR 128GB CORAL':['iphone-xr','6.1-inch-display','128gb','coral'], 'IPHONE XR 128GB RED':['iphone-xr','6.1-inch-display','128gb','red'], 'IPHONE XR 128GB WHITE':['iphone-xr','6.1-inch-display','128gb','white'], 'IPHONE XR 128GB YELLOW':['iphone-xr','6.1-inch-display','128gb','yellow'],
                      'IPHONE XR 64GB BLACK':['iphone-xr','6.1-inch-display','64gb','black'], 'IPHONE XR 64GB BLUE':['iphone-xr','6.1-inch-display','64gb','blue'], 'IPHONE XR 64GB CORAL':['iphone-xr','6.1-inch-display','64gb','coral'], 'IPHONE XR 64GB RED':['iphone-xr','6.1-inch-display','64gb','red'], 'IPHONE XR 64GB WHITE':['iphone-xr','6.1-inch-display','64gb','white'], 'IPHONE XR 64GB YELLOW':['iphone-xr','6.1-inch-display','64gb','yellow']
                     }

def existe_archivo(nombre_archivo):
    if path.exists(f'{nombre_archivo}.xlsx'):
        pass 
    else: 
        print("NOMBRE ARCHIVO INCORRECTO")
        exit(1)

def verificacion_modelo(producto):
    for iphone in iphone_disponibles:
        if producto == iphone:
            return iphone_disponibles[iphone]
    return None 

def limpieza_datos(archivo_excel):
    # Se elimina las filas vacias que no contengan la informacion requerida, ademas de los iphone que ya aparecen como finalizado
    archivo_excel = archivo_excel.dropna(axis=0, subset=['MODELO'])
    archivo_excel = archivo_excel.dropna(axis=0, subset=['OPERADOR'])
    archivo_excel = archivo_excel.dropna(axis=0, subset=['PASSWORD'])
    archivo_excel = archivo_excel.dropna(axis=0, subset=['USER'])
    archivo_excel = archivo_excel.dropna(axis=0, subset=['CANTIDAD'])
    archivo_excel = archivo_excel.drop(archivo_excel[archivo_excel['STATUS']=='Finalizado'].index)
    return archivo_excel

def escribir_excel(archivo_a_modificar, hoja, fila, columna, dato):
    #Busco la hoja donde tengo que modificar 
    hoja_a_modificar = archivo_a_modificar.get_sheet_by_name(hoja)
    #Escribo la celda
    hoja_a_modificar.cell(row = fila, column = columna).value = dato
    
