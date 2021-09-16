from sys import platform
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.chrome.options import Options


class Bot: 
    def __init__(self, url):
        os_confirm = self.ver_os()
        options = self.opciones()
        self.estado = None
        self.link_orden = None
        self.etapa = None 
        self.driver = webdriver.Chrome(executable_path=f"{os_confirm}", chrome_options=options)
        self.driver.get(url)

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

    # Selecciona al elemento que este cargado y visible 
    def esperar_elemento(self, tiempo_espera, elemento):
        espera_seleccion = False 
        while not espera_seleccion:
            try: 
                WebDriverWait(self.driver,tiempo_espera).until(ec.presence_of_element_located((By.XPATH, elemento)))
                elemento_cargado = self.driver.find_element_by_xpath(elemento)
                espera_seleccion = True
                return elemento_cargado
            except (ElementNotInteractableException, NoSuchElementException, TimeoutException):
                pass
                '''wait = WebDriverWait(self.driver,tiempo_espera)
                wait.until(ec.visibility_of_element_located((By.XPATH, elemento)))'''
               

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
    
    def get_etapa(self):
        return self.etapa

    def opciones(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--log-level=3")
        return chrome_options

    def set_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def set_orden(self, nuevo_orden):
        self.link_orden = nuevo_orden

    def set_etapa(self, nueva_etapa):
        self.etapa = nueva_etapa