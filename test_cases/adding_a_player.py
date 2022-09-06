import os
import time

import unittest
from selenium import webdriver

from pages.dashboard import Dashboard, TestDashboardPage
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestDashboardPageAddingPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_adding_a_player(self):
        user_login = LoginPage(self.driver)
        dashboard_page = Dashboard(self.driver)
        dashboard_page = TestDashboardPage(self.driver)
        user_login.type_in_email('user06@getnada.com')
        user_login.filling_in_the_password('Test-1234')
        user_login.clicking_on_sign_in_button()
        time.sleep(3)
        dashboard_page.clicking_on_add_players_button()
        dashboard_page.filling_in_email('snigana.pylypyuk@gmail.com')
        dashboard_page.filling_in_name('Sni')
        dashboard_page.filling_in_surname('Zhana')
        dashboard_page.filling_in_age('23.03.2004')
        dashboard_page.filling_in_main_position('goalkeeper')
        dashboard_page.clicking_on_add_players_submit_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()




    



