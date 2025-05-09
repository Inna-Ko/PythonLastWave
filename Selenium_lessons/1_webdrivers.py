# from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.chrome.service import Service
#
# service = Service(GeckoDriverManager().install())
# driver = webdriver.Firefox(service=service)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
input()
