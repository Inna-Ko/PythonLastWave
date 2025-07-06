from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


class BaseTest:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)
        self.profile_page = ProfilePage(self.driver)