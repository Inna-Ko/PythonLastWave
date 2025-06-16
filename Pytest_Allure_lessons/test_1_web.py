import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestElements:

    WIKI_ICON = ("class name", "wikipedia-icon")
    SEARCH_BUTTON = ("css selector", ".wikipedia-search-button")

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com")

    def test_wiki_icon_is_displayed(self):
        wiki_icon = self.driver.find_element(*self.WIKI_ICON)
        assert wiki_icon.is_displayed() is True, "Элемент wiki не отображается на странице"

    def test_search_button_is_clickable(self):
        search_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        assert search_button.is_enabled() is True, "Кнопка поиска не кликабельна"

    def teardown_method(self):
        self.driver.close()


class TestLogin:

    USERNAME_LOCATOR = ("xpath", "//input[@name='username']")
    PASSWORD_LOCATOR = ("xpath", "//input[@name='password']")
    SUBMIT_BUTTON_LOCATOR = ("xpath", "//button[@type='submit']")

    def setup_method(self):
        self.driver = webdriver.Chrome()

    def test_open_login_page(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", "Неверный адрес страницы"

    def is_login_successful(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(*self.USERNAME_LOCATOR).send_keys("Admin")
        self.driver.find_element(*self.PASSWORD_LOCATOR).send_keys("admin123")
        self.driver.find_element(*self.SUBMIT_BUTTON_LOCATOR).click()
        time.sleep(3)
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index", "Неуспешный логин"

