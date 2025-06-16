from seleniumwire import webdriver

driver = webdriver.Chrome()


class TestLogin:   # Название тестового класса

    def setup_method(self):
        print("Выполняюсь до теста")
        self.driver = webdriver.Chrome()

    def test_open_login_page(self):
        self.driver.get("https://demoqa.com/login")
        assert self.driver.current_url == "https://demoqa.com/login", "Ошибка"

    def teardown_method(self):
        self.driver.close()
        print("Выполняюсь после теста")