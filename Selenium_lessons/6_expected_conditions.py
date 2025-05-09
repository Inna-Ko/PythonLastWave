from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 45, poll_frequency=1)

driver.get("https://omayo.blogspot.com/")

# Task 1

TEXT_TO_DISAPPEAR = ("xpath", "//div[@id='deletesuccess']")
BUTTON_AFTER_TEXT_DISAPPEAR = ("xpath", "//input[@value='ClickAfterTextDissappears']")

# wait.until(EC.invisibility_of_element_located(TEXT_TO_DISAPPEAR)) # перестал исчезать текст через 25сек, поэтому строчка закомментирована
driver.find_element(*BUTTON_AFTER_TEXT_DISAPPEAR).click()
alert = driver.switch_to.alert
alert.accept()

# Task 2

TEXT_TO_DISPLAY = ("xpath", "//div[@id='delayedText']")
wait.until(EC.visibility_of_element_located(TEXT_TO_DISPLAY))

# Task 3

BUTTON_TO_ENABLE = ("xpath", "//input[@id='timerButton']")
wait.until(EC.element_to_be_clickable(BUTTON_TO_ENABLE))

# Task 4

BUTTON_TO_DISABLE = ("xpath", "//button[@id='myBtn']")
BUTTON_TRY_IT = ("xpath", "//button[text()='Try it']")

driver.find_element(*BUTTON_TRY_IT).click()
wait.until_not(EC.element_to_be_clickable(BUTTON_TO_DISABLE))

