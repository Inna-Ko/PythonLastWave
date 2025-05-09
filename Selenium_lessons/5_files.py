from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import requests

import os

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
preferences = {
    "download.default_directory": os.path.join(os.getcwd(), "lesson_6\\downloads"),
    "safebrowsing.enabled" : True,
    "download.prompt_for_download": False,
}
options.add_experimental_option("prefs", preferences)
driver = webdriver.Chrome(service=service, options=options)

# Task 1

driver.get("https://demoqa.com/upload-download")

file_upload_button = driver.find_element("xpath", "//input[@id='uploadFile']")
file_upload_button.send_keys(os.path.join(os.getcwd(), "raccon.jpg"))
input()

# Task 2

driver.get("http://the-internet.herokuapp.com/download")

files = driver.find_elements("xpath", "//div[@id='content']//a")
for file in files:
    file.click()
    response = requests.get(driver.current_url)
    if response.status_code == 404:
        print("404 ошибка")
        driver.back()
input()
