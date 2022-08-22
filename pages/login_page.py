from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath ="//input[@id='password']"
    sign_in_button_xpath ="//span[contains(text(),'Sign in')]"
    scouts_panel_xpath ="//h5[contains(text(),'Scouts Panel')]"
    remind_password_xpath ="//a[contains(text(),'Remind password')]"
    change_language_xpath ="//div[contains(text(),'English')]"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
