import os
import sys
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POMdemo.Pages.LoginPage import LoginPage
from POMdemo.Pages.HomePage import HomePage
import HtmlTestRunner


class LoginTests(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        # self.driver.get("https://opensource-demo.orangehrmlive.com/")
        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()

        # driver.find_element_by_id('welcome').click()
        # self.driver.find_element_by_link_text("Welcome Admin").click()
        # self.driver.find_element_by_link_text('Logout').click()
        # self.time.sleep(2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="/Users/yatin/Desktop/webdriver-manager/PracticeProjects/POMdemo/Reports"))
