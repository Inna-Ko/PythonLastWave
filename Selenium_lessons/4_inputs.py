import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Task 1

driver.get("https://demoqa.com/text-box")

full_name = driver.find_element("xpath", "//input[@id='userName']")
full_name.clear()
full_name.send_keys("Тестовое Имя")
assert "Тестовое Имя" in full_name.get_attribute("value")

email = driver.find_element("xpath", "//input[@id='userEmail']")
email.clear()
email.send_keys("test@email.com")
assert "test@email.com" in email.get_attribute("value")

current_address = driver.find_element("xpath", "//textarea[@id='currentAddress']")
current_address.clear()
current_address.send_keys("Адрес проживания")
assert "Адрес проживания" in current_address.get_attribute("value")

permanent_address = driver.find_element("xpath", "//textarea[@id='permanentAddress']")
permanent_address.clear()
permanent_address.send_keys("Адрес регистрации")
assert "Адрес регистрации" in permanent_address.get_attribute("value")

# Task 2

driver.get("https://the-internet.herokuapp.com/login")

username = driver.find_element("xpath", "//input[@id='username']")
username.clear()
username.send_keys("tomsmith")

password = driver.find_element("xpath", "//input[@id='password']")
password.clear()
password.send_keys("SuperSecretPassword!")

login_button = driver.find_element("xpath", "//button[@type='submit']")
login_button.click()

logout_button = driver.find_element("xpath", "//a[i[normalize-space()='Logout']]")
assert logout_button.is_displayed(), "Кнопка Logout не отображается на странице"

login_buttons = driver.find_elements("xpath", "//button[@type='submit']")
if len(login_buttons) == 0:
    print("Кнопка Login отсутствует на странице.")
else:
    print(f"На странице найдена кнопка Login!")

input()

