from base.base_page import BasePage


class ProfilePage(BasePage):

    _PAGE_URL = "https://www.freeconferencecall.com/profile/account-info-login"

    _HOST_MEETING = "//button[@data-test-id='launch-button']"
    _INVITE_BUTTON = "//button[@title='Invite']"

    def click_host_meeting(self):
        button = self.driver.find_element(*self._HOST_MEETING)
        button.click()

    def click_invite(self):
        button = self.driver.find_element(*self._INVITE_BUTTON)
        button.click()