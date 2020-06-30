from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.ui_element import UIElement

class MainMenu(UIElement):
    NAME_PROJECT = "Test-Create-Project"
    ADD_BUTTON_XPATH = "//div[@id='projects_list_manager']//a[contains (@class, 'add_project')]"
    SUBMIT_BUTTON_XPATH = "//form//footer/button[@type='submit']"
    EDIT_PROJECT_FIELD_ID = "edit_project_modal_field_name"
    TITLE_PROJECTS_XPATH = "//div[@id='editor']//h1"

    def click_create_project(self, name_project: str = "Test-Create-Project"):
        LIST_PROJECTS_XPATH = "//ul[@id='projects_list']//li//td[@class='name']"

        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, self.ADD_BUTTON_XPATH))).click()
        self.driver.find_element_by_id(self.EDIT_PROJECT_FIELD_ID).send_keys(name_project)
        wait.until(ec.element_to_be_clickable((By.XPATH, self.SUBMIT_BUTTON_XPATH))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, LIST_PROJECTS_XPATH)))
        wait.until(ec.visibility_of_element_located((By.XPATH, self.TITLE_PROJECTS_XPATH)))

    def get_created_project(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(ec.visibility_of_element_located((By.XPATH, self.TITLE_PROJECTS_XPATH))).text
