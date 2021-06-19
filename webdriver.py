import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def opciones_chrome():
    opciones = Options()
    opciones.add_argument("--disable-gpu")
    opciones.add_argument("--log-level=3")
    opciones.add_argument("--no-sandbox")
    opciones.add_experimental_option("excludeSwitches", ['enable-automation','enable-logging'])
    return opciones

def instalar_webdriver():
    os.environ['WDM_LOCAL'] = '1'
    os.environ['WDM_LOG_LEVEL'] = '0'
    executableChrome = ChromeDriverManager().install()
    return executableChrome

def crear_webdriver(executableChrome):
    driver = webdriver.Chrome(executable_path=executableChrome, chrome_options=opciones_chrome())
    return driver
