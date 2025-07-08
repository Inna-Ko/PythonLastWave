from base.base_page import BasePage


class LoginPage(BasePage):

    _PAGE_URL = "https://www.freeconferencecall.com/global/pl/login"

    _LOGIN_FIELD = "//input[@id='login_email']"
    _PASSWORD_FIELD = "//input[@id='password']"
    _AGREE_CHECKBOX = "//input[@id='gdpr_checkbox']"
    _SUBMIT_BUTTON = "//button[@id='loginformsubmit']"

    def enter_login(self, login):
        login_field = self.driver.find_element(*self._LOGIN_FIELD)
        login_field.send_keys(login)

    def enter_password(self, password):
        password_field = self.driver.find_element(*self._PASSWORD_FIELD)
        password_field.send_keys(password)

    def click_agree_checkbox(self):
        checkbox = self.driver.find_element(*self._AGREE_CHECKBOX)
        checkbox.click()

    def click_submit_button(self):
        button = self.driver.find_element(*self._SUBMIT_BUTTON)
        button.click()

