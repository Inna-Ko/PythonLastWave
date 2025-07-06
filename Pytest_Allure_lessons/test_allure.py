import pytest
import allure
from selenium import webdriver


@allure.suite("Набор тестов для примера - Урок 1")  # Красиво отобразит название тестового набора
class TestExample:

    @allure.title("Переход по ссылке")  # Отобразит название теста
    @allure.description("Переход по любой ссылке после открытия страницы")  # Отобразит описание теста
    @allure.severity("Critical")  # Отобразит северети теста
    @allure.link(url="https://vk.com", name="Переход по ссылке")  # Отобразит ссылку на ручной кейс
    def test_1(self):

        self.driver = webdriver.Chrome()
        with allure.step("Открыть страницу Яндекса"):
            self.driver.get("https://ya.ru")
            assert "https://ya.ru" in self.driver.current_url, "Страница не была открыта"

        with allure.step("Нажать на любую ссылку"):
            self.driver.find_element("xpath", "//a").click()
