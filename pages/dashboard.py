import time

from _pytest import unittest
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = 'Scouts panel'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'
    login_xpath = "//*[@id='login']"
    main_page_xpath = "//span[contains(text(),'Main page')]"
    players_xpath = "//*[text()='Players']"
    sign_out_button_xpath = "//*[text()='Sign out']"
    players_count_xpath = "//body[1]/div[1]//main[1]/div[2]//div[1]"
    dev_team_contact_xpath = "//span[contains(text(),'Dev team contact')]"
    shortcuts_xpath = "//h2[contains(text(),'Shortcuts')]"
    add_player_button_xpath = "//span[contains(text(),'Add player')]"
    scouts_panels_xpath = "//h6[contains(text(),'Scouts Panel')]"
    players_main_position_xpath = "//tbody/tr[@id='MUIDataTableBodyRow-9']/td[4]"
    events_count_xpath = "//div[contains(text(),'Events count')]"
    reports_count_xpath = "//div[contains(text(),'Reports count')]"
    players_rating_xpath = "//tbody/tr[@id='MUIDataTableBodyRow-9']/td[6]/div[1]"
    activity_xpath = "//h2[contains(text(),'Activity')]"
    tester_snizhana_button_xpath = "//span[contains(text(),'Tester')]"
    wait = WebDriverWait(driver, 10)


    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.add_player_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def clicking_on_sign_out_button(self):
        pass
        self.click_on_the_element(self.sign_out_button_xpath)




class TestDashboardPage(BasePage):
    add_players_xpath = "//span[contains(text(),'Add player')]"
    email_input_xpath = "//div[1]/div[1]/div[1]/input[1]"
    name_input_xpath = "//div[2]/div[1]/div[1]/input[1]"
    surname_input_xpath = "// div[3] // div[1] / input[1]"
    age_input_xpath = "//div[7]//div[1]/input[1]"
    main_position_xpath = "//div[11]//input[1]"
    add_players_submit_button_xpath = "//div[3]/button[1]"
    sign_out_button_xpath = "//ul[2]/div[2]"
    change_language_xpath ="//div[1]/ul[2]/div[1]"

    def clicking_on_add_players_button(self):
        self.click_on_the_element(self.add_players_xpath)

    def filling_in_email(self, password):
        self.field_send_keys(self.email_input_xpath, password)

    def filling_in_name(self, name):
        self.field_send_keys(self.name_input_xpath, name)

    def filling_in_surname(self, surname):
        self.field_send_keys(self.surname_input_xpath, surname)

    def filling_in_age(self, age):
        self.field_send_keys(self.age_input_xpath, age)

    def filling_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_xpath, main_position)

    def clicking_on_add_players_submit_button(self):
        self.click_on_the_element(self.add_players_submit_button_xpath)

    def clicking_on_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def clicking_on_changing_language_button(self):
        self.click_on_the_element(self.change_language_xpath)
