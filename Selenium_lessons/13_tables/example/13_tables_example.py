import time
from selenium import webdriver
from table_handler import TableHandler

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
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

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
time.sleep(3)
table = TableHandler(driver)
print(table.get_cell_content(2, 3))
print(table.get_row_content(2))
print(table.get_column_content(3))
table.select_row(2)
table.delete_by_username("ANNa3160")
time.sleep(3)
