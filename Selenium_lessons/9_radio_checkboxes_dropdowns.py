from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/selectable")

GRID_TAB = ("xpath", "//a[@id='demo-tab-grid']")
FOURTH_ELEMENT = ("xpath", "(//div[@id='demo-tabpane-grid']//li)[4]")
NINTH_ELEMENT = ("xpath", "(//div[@id='demo-tabpane-grid']//li)[9]")

driver.find_element(*GRID_TAB).click()
driver.find_element(*FOURTH_ELEMENT).click()
driver.find_element(*NINTH_ELEMENT).click()

assert "active" in driver.find_element(*FOURTH_ELEMENT).get_attribute("class"), "Чек-бокс 4 не выбран"
assert "active" in driver.find_element(*NINTH_ELEMENT).get_attribute("class"), "Чек-бокс 9 не выбран"

