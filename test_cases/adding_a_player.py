import os
import time

import unittest
from selenium import webdriver


from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestDashboardPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_adding_a_player(self):
        user_login = LoginPage(self.driver)
        user_adding_a_player = TestDashboardPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.filling_in_the_password('Test-1234')
        user_login.clicking_on_sign_in_button()
        time.sleep(5)
        user_adding_a_player.clicking_on_add_players_button()
        user_adding_a_player.filling_in_email('snigana.pylypyuk@gmail.com')
        user_adding_a_player.filling_in_name('Sni')
        user_adding_a_player.filling_in_surname('Zhana')
        user_adding_a_player.filling_in_age('23.03.2004')
        user_adding_a_player.filling_in_main_position('goalkeeper')
        user_adding_a_player.clicking_on_add_players_submit_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def clicking_on_add_players_button(self):
        pass

    def filling_in_email(self, param):
        pass

    def filling_in_name(self, param):
        pass

    def filling_in_surname(self, param):
        pass

    def filling_in_age(self, param):
        pass

    def filling_in_main_position(self, param):
        pass

    



