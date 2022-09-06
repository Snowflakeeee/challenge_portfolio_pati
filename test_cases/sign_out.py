import os
import time

import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestDashboardPagesignout(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_sign_out(self):
        user_login = LoginPage(self.driver)
        dashboard_page = Dashboard(self.driver)
        user_login.type_in_email('user06@getnada.com')
        user_login.filling_in_the_password('Test-1234')
        user_login.clicking_on_sign_in_button()
        time.sleep(3)
        dashboard_page.clicking_on_sign_out_button()
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()




