from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.ui_element import UIElement

class MainPage(UIElement):
    LOADING_ID = "loading"
    URL = "https://todoist.com/app"

    def navigate(self):
        self.driver.get(self.URL)
        self.wait_until_loaded()

    def wait_until_loaded(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.invisibility_of_element((By.ID, self.LOADING_ID)))
        wait.until(ec.url_contains(self.URL))