from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

# Task 1 (Установка и чтение куки)

driver.get("https://www.freeconferencecall.com/en/us/login")

LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit']")

driver.get("https://www.freeconferencecall.com/en/us/login")
driver.find_element(*LOGIN_FIELD).send_keys("autocheck@ya.ru")
driver.find_element(*PASSWORD_FIELD).send_keys("123")
driver.find_element(*SUBMIT_BUTTON).click()

driver.add_cookie({
    'name': 'username',
    'value': 'user123'
})

print(driver.get_cookie("username"))

# Task 2 (Удаление куки)

driver.delete_cookie("username")
driver.refresh()

print(driver.get_cookie("username"))

input()


