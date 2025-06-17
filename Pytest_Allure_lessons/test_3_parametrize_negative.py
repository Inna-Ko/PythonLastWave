import pytest
from selenium import webdriver


class TestExample:

    EMAIL_FIELD_LOCATOR = ("xpath", "//input[@id='login_email']")
    PASSWORD_FIELD_LOCATOR = ("xpath", "//input[@id='password']")
    SUBMIT_BUTTON_LOCATOR = ("xpath", "//button[@id='loginformsubmit']")
    TERMS_CHECKBOX = ("xpath", "//input[@id='gdpr_checkbox']")
    ERROR_LABEL = ("xpath", "//span[contains(@class, 'error')]//li")

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.freeconferencecall.com/login")

    @pytest.mark.parametrize(
        "email, password, error_message, expected_result", [
            ("demoqa@ya.ru", "123", None, True),
            ("gwrrfdsa.ru", "123", "This value should be a valid email", False),
            ("demoqa@ya.ru", "", "This value is required", False),
            ("", "123", "This value is required", False),
            ("", "", "This value is required", False),
        ]
    )
    def test_login(self, email, password, error_message, expected_result):
        self.driver.find_element(*self.EMAIL_FIELD_LOCATOR).send_keys(email)
        self.driver.find_element(*self.PASSWORD_FIELD_LOCATOR).send_keys(password)
        self.driver.find_element(*self.TERMS_CHECKBOX).click()
        self.driver.find_element(*self.SUBMIT_BUTTON_LOCATOR).click()

        if not expected_result:
            assert self.driver.find_element(*self.ERROR_LABEL).text == error_message

    def teardown_method(self):
        self.driver.quit()