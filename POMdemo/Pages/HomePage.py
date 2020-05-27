from POMdemo.Locators.Locators import Locators


class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_text_id = Locators.welcome_text_id
        self.logout_link_linkText = Locators.logout_link_linkText

    def click_welcome(self):
        # self.driver.find_element_by_link_text(self.welcome_link_text).click()
        self.driver.find_element_by_id(self.welcome_text_id).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_linkText).click()
