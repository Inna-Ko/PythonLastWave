from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(service=service, options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("https://hyperskill.org/login")
driver.execute_script('window.open("https://www.avito.ru/", "_blank");')
driver.execute_script('window.open("https://www.ozon.ru/", "_blank");')

windows = driver.window_handles
window_1_title = driver.title
driver.switch_to.window(windows[1])
window_2_title = driver.title
driver.switch_to.window(windows[2])
window_3_title = driver.title

print(f"Первая вкладка: {window_1_title}")
print(f"Вторая вкладка: {window_2_title}")
print(f"Третья вкладка: {window_3_title}")

HYPERSKILL_SIGN_IN_BUTTON = ("xpath", "//button[normalize-space()='Sign in']")
OZON_ELECTRONICS = ("xpath", "//a[text()='Электроника']")
AVITO_CART = ("xpath", "//a[@title='Корзина']")

driver.switch_to.window(windows[0])
driver.find_element(*HYPERSKILL_SIGN_IN_BUTTON).click()

driver.switch_to.window(windows[1])
driver.find_element(*OZON_ELECTRONICS).click()

driver.switch_to.window(windows[2])
driver.find_element(*AVITO_CART).click()

input()
