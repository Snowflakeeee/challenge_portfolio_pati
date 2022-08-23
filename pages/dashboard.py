import time
from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = 'Scouts panel'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title
