from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://vk.com")
vk_title = driver.title
print(vk_title)

driver.get("https://ya.ru")
ya_title = driver.title
print(ya_title)

driver.back()
assert driver.title == vk_title, "Мы попали куда-то не туда"

driver.refresh()
first_url = driver.current_url
print(first_url)

driver.forward()
assert driver.current_url != first_url, "Ссылки совпадают"