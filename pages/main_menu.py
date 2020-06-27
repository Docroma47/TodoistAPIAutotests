from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.ui_element import UIElement

class MainMenu(UIElement):
    ADD_BUTTON_XPATH = "//div[@id='projects_list_manager']//a[contains (@class, 'add_project')]"

    def click_create_project(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, self.ADD_BUTTON_XPATH))).click()