import os
from webdriver_manager.chrome import ChromeDriverManager

os.environ['WDM_LOCAL'] = '1'
os.environ['WDM_LOG_LEVEL'] = '0'

EXECUTABLE_CHROME = ChromeDriverManager().install()