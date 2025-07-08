import time
from PageObject.base.base_test import BaseTest


class TestLoginPage(BaseTest):

    def test_login_in_account(self):
        self.login_page.open()
        self.login_page.enter_login("qaqatest@ya.ru")
        self.login_page.enter_password("123")
        self.login_page.click_agree_checkbox()
        self.login_page.click_submit_button()
        self.profile_page.is_opened()
        self.profile_page.click_host_meeting()
