from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath ="//body[1]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/input[1]"
    sign_in_button_xpath ="//span[contains(text(),'Sign in')]"
    scouts_panel_xpath ="//h5[contains(text(),'Scouts Panel')]"
    remind_password_xpath ="//a[contains(text(),'Remind password')]"
    change_language_xpath ="//body[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
