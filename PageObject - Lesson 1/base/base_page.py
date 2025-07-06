from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from metaclasses.meta_locator import MetaLocator
ё

class BasePage(metaclass=MetaLocator):

    _HOST_BUTTON = "//button[text()='Host']"
    _JOIN_BUTTON = "//button[text()='Join']"

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 10, 1)

    def open(self):
        self.driver.get(self._PAGE_URL)
        self.wait.until(EC.url_to_be(self._PAGE_URL))

    def is_opened(self):
        self.wait.until(EC.url_to_be(self._PAGE_URL))

    def click_host_button(self):
        button = self.driver.find_element(*self._HOST_BUTTON)
        button.click()

    def click_join_button(self):
        button = self.driver.find_element(*self._JOIN_BUTTON)
        button.click()