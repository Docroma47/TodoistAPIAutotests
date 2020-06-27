from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.ui_element import UIElement

class LandingPage(UIElement):
    URL = "https://todoist.com/"

    def navigate(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()

    def wait_until_loaded(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Начать")))

    def click_login(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Вход"))).click()