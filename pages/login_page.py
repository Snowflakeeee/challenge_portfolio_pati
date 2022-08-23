from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//input[@id='password']"
    sign_in_button_xpath = "//span[contains(text(),'Sign in')]"
    scouts_panel_xpath = "//h5[contains(text(),'Scouts Panel')]"
    remind_password_xpath = "//a[contains(text(),'Remind password')]"
    change_language_xpath = "//div[contains(text(),'English')]"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en'
    expected_title = 'Scouts panel - sign in'
    password_field_xpath = "//input[@id='password']"
    sign_in_button_xpath = "//span[contains(text(),'Sign in')]"
    scouts_panel_xpath = "//h5[contains(text(),'Scouts Panel')]"
    remind_password_xpath = "//a[contains(text(),'Remind password')]"
    change_language_xpath = "//div[contains(text(),'English')]"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def filling_in_the_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def clicking_on_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title


