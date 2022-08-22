from pages.base_page import BasePage


class Dashboard(BasePage):
    button_xpath = "//*[@id='login']"
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
    reports_count_xpath ="//div[contains(text(),'Reports count')]"
    players_rating_xpath = "//tbody/tr[@id='MUIDataTableBodyRow-9']/td[6]/div[1]"
    activity_xpath = "//h2[contains(text(),'Activity')]"
    tester_snizhana_button_xpath = "//span[contains(text(),'Tester')]"

