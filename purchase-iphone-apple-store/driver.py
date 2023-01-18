from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from . import EXECUTABLE_CHROME

class Driver:

    def website(self, website): 
        self.driverChrome.get(website)

    def __init__(self):
        self.driverChrome = webdriver.Chrome(executable_path=EXECUTABLE_CHROME, chrome_options=self.chromeOptions())

    def chromeOptions(self):
        options = Options()
        prefs = {
            "credentials_enable_service":False,
            "profile.password_manager_enabled":False
        }
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-popup-blocking")
        options.add_experimental_option("excludeSwitches", ['enable-automation','enable-logging'])
        options.add_experimental_option("prefs", prefs)
        return options

    def scrollToWebElement(self, **webElement):
        scrollOriginWebElement = ScrollOrigin.from_element(webElement['webElement'], 0, -20)
        if (webElement['type'] == 'buttonPanel'):
            ActionChains(self.driverChrome)\
                .move_to_element(webElement['webElement'])\
                .click(webElement['webElement'])\
                .pause(3)\
                .perform()
        elif (webElement['type'] == 'button'):
            ActionChains(self.driverChrome)\
                .move_to_element(webElement['webElement'])\
                .click(webElement['webElement'])\
                .pause(3)\
                .perform()
        elif (webElement['type'] == 'text'):
            ActionChains(self.driverChrome)\
                .move_to_element(webElement['webElement'])\
                .send_keys_to_element(webElement['webElement'], webElement['textBox'])\
                .pause(2)\
                .perform()
        elif (webElement['type'] == 'loadElements'):
            ActionChains(self.driverChrome)\
                .move_to_element(webElement['webElement'])\
                .click(webElement['webElement'])\
                .scroll_from_origin(scrollOriginWebElement, 0, 450)\
                .pause(2)\
                .perform()
    
    def forceClick(self, webElement):
        self.driverChrome.execute_script("arguments[0].click();", webElement)

    def sendKeysActions(self, webElement, **keys):
        ActionChains(self.driverChrome)\
            .key_down(keys['keyDown'])\
            .send_keys_to_element(webElement ,keys['command'])\
            .key_up(keys['keyDown'])\
            .send_keys_to_element(webElement ,keys['extra'])\
            .send_keys_to_element(webElement ,keys['text'])\
            .perform()

    def waitWebElement(self, **options):
        if (options['elements']=='one'):
            return WebDriverWait(self.driverChrome, options['timeOut'], options['frequency'],[TimeoutException, NoSuchElementException, ElementNotInteractableException]).until(lambda d: d.find_element(options['typeSearch'], options['nameSearch']))
        elif (options['elements']=='many'):
            return WebDriverWait(self.driverChrome, options['timeOut'], options['frequency'],[TimeoutException, NoSuchElementException, ElementNotInteractableException]).until(lambda d: d.find_elements(options['typeSearch'], options['nameSearch']))

    def findChildWebElement(self, **options):
        if (options['elements'] == 'one'):
            return options['webElementParent'].find_element(options['typeSearch'], options['nameSearch'])
        elif (options['elements'] == 'many'):
            return options['webElementParent'].find_elements(options['typeSearch'], options['nameSearch'])

    def switchToFrame(self, iframe):
        self.driverChrome.switch_to.frame(iframe)

    def finishDriver(self):
        self.driverChrome.quit()
    