import time
from selenium import webdriver
from table_handler import TableHandler
import os

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
preferences = {
    "download.default_directory": os.path.join(os.getcwd(), "13_tables\\downloads"),
    "safebrowsing.enabled" : True,
    "download.prompt_for_download": False,
}
options.add_experimental_option("prefs", preferences)
driver = webdriver.Chrome(options=options)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
# Login
USERNAME_LOCATOR = ("xpath", "//input[@name='username']")
PASSWORD_LOCATOR = ("xpath", "//input[@name='password']")
SUBMIT_BUTTON_LOCATOR = ("xpath", "//button[@type='submit']")

driver.find_element(*USERNAME_LOCATOR).send_keys("Admin")
driver.find_element(*PASSWORD_LOCATOR).send_keys("admin123")
driver.find_element(*SUBMIT_BUTTON_LOCATOR).click()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
time.sleep(3)
table = TableHandler(driver)
print(table.get_cell_content(2, 3))
print(table.get_row_content(8))
table.download_by_first_value("Senior QA Lead")
table.delete_row_by_value("Senior QA Lead")   # без подтверждения удаления

time.sleep(5)
