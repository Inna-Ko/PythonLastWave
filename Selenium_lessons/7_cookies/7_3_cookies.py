from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import json

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(service=service, options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# Task 3 (Автоматизация корзины покупок)

driver.get("https://www.kufar.by/l?rgn=all&b2c=1&cmp=1&cnd=2&sort=lst.d")

ACCEPT_COOKIES_BUTTON = ("xpath", "//button[text()='Принять']")
driver.find_element(*ACCEPT_COOKIES_BUTTON).click()

# Добавляем два первых элемента в корзину

ADD_TO_CART_BUTTON_FIRST = ("xpath", "(//button[@data-cy='add_to_cart_button'])[1]")
ADD_TO_CART_BUTTON_SECOND = ("xpath", "(//button[@data-cy='add_to_cart_button'])[2]")
driver.find_element(*ADD_TO_CART_BUTTON_FIRST).click()
driver.find_element(*ADD_TO_CART_BUTTON_SECOND).click()

# Сохраняем куки в файл

cookies = driver.get_cookies()
with open("cookies.json", "w") as f:
    json.dump(cookies, f, indent=4)

# Удаляем куки и обновляем страницу

driver.delete_all_cookies()
driver.refresh()

# Считываем куки из файла

with open("cookies.json", "r") as f:
    cookies = json.load(f)

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()

input()
