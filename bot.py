from sys import platform
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, WebDriverException


class Bot: 
    def __init__(self, url):
        os_confirm = self.ver_os()
        self.driver = webdriver.Chrome(executable_path=f"{os_confirm}")
        self.driver.get(url)

    def ver_os(self):
        if platform == 'win32':
            ruta = './Windows/chromedriver.exe'
            return ruta
        elif platform == 'darwin':
            ruta = './Mac/chromedriver.exe'
            return ruta     

    def cambiar_url(self,nueva_url):
        self.driver.get(nueva_url)

    def url_actual(self):
        url_actual = str(self.driver.current_url)
        return url_actual

    def esperar_elemento(self, tiempo_espera, elemento):
        espera_seleccion = False 
        while not espera_seleccion:
            try: 
                elemento_cargado = self.driver.find_element_by_xpath(elemento)
                return elemento_cargado
            except (ElementNotInteractableException, NoSuchElementException):
                wait = WebDriverWait(self.driver,tiempo_espera)
                wait.until(ec.visibility_of_element_located((By.XPATH, elemento)))
            except (TimeoutException):
                print("Posiblemente el elemento no se encuentra en la pagina")
                exit(1)

    def encontrar_elemento(self, tiempo_espera, elemento):
        espera_seleccion = False 
        while not espera_seleccion:
            try: 
                elemento_cargado = self.driver.find_element_by_xpath(elemento)
                return elemento_cargado
            except (ElementNotInteractableException, NoSuchElementException):
                wait = WebDriverWait(self.driver,tiempo_espera)
                wait.until(ec.visibility_of_element_located((By.XPATH, elemento)))
    
    def leer_texto(self, archivo):
        lista_datos = []
        if archivo == 'datos_domicilio' or archivo == 'datos_tarjeta' or archivo == 'iphone':
            lectura = open(f'{archivo}.txt','r')
            for linea in lectura:
                lista_datos.append(linea.strip('\n'))
            lectura.close()
            return lista_datos
        else: 
            print(f'El archivo {archivo}.text no admitido, renombrelo y vuelva intentar')
            return lista_datos

    def stock_disponible(self, tiempo_espera, elemento):
        # Reviso en el recuadro de informacion si hay stock
        stock = self.encontrar_elemento(tiempo_espera, elemento)
        if (str(stock.text) == 'In Stock'):
            return True
        else: 
            return False 

    def finalizar(self):
        self.driver.quit()

