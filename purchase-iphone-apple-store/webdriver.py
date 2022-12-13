from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from . import EXECUTABLE_CHROME

def chromeOptions():
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-popup-blocking")
    options.add_experimental_option("excludeSwitches", ['enable-automation','enable-logging'])
    return options

driverChrome = webdriver.Chrome(executable_path=EXECUTABLE_CHROME, chrome_options=chromeOptions())

