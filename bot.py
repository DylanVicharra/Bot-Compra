import os.path as path
from sys import platform
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException


class Bot: 
    def __init__(self, url):
        os_confirm = self.ver_os()
        self.driver = webdriver.Chrome(executable_path=f"{os_confirm}")
        self.driver.get(url)
        self.estado = None
        self.link_orden = None

    def get_driver(self):
        driver = self.driver
        return driver

    def ver_os(self):
        if platform == 'win32':
            ruta = './Windows/chromedriver.exe'
            return ruta
        elif platform == 'darwin':
            ruta = './Mac/chromedriver.exe'
            return ruta     

    def cambiar_url(self,nueva_url):
        self.driver.get(nueva_url)
    
    # Solo espera que el elemento este cargado en DOM
    def elemento_cargado(self, tiempo_espera, elemento):
        # Espera que cargue un pagina y contenedores
        try: 
            elemento = ec.presence_of_element_located((By.XPATH,elemento))
            WebDriverWait(self.driver,tiempo_espera).until(elemento)      
        except (TimeoutException):
            print("TARDA EN CARGAR LA PAGINA")

    # Selecciona al elemento que este cargado y visible 
    def esperar_elemento(self, tiempo_espera, elemento):
        espera_seleccion = False 
        while not espera_seleccion:
            try: 
                elemento_cargado = self.driver.find_element_by_xpath(elemento)
                return elemento_cargado
            except (ElementNotInteractableException, NoSuchElementException):
                wait = WebDriverWait(self.driver,tiempo_espera)
                wait.until(ec.visibility_of_element_located((By.XPATH, elemento)))
               

    # Selecciona al elemento que solo este presente en el DOM 
    def encontrar_elemento(self, tiempo_espera, elemento):
        espera_seleccion = False 
        while not espera_seleccion:
            try: 
                elemento_encontrado = self.driver.find_element_by_xpath(elemento)
                return elemento_encontrado
            except (NoSuchElementException):
                wait = WebDriverWait(self.driver,tiempo_espera)
                wait.until(ec.presence_of_element_located((By.XPATH, elemento)))

    def finalizar(self):
        self.driver.quit()

    def get_estado(self):
        return self.estado

    def get_orden(self):
        return self.link_orden


