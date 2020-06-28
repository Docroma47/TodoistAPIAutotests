from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.ui_element import UIElement

class LoginPage(UIElement):
    URL = "https://todoist.com/users/showlogin"
    EMAIL_FIELD_XPATH = "//input [@id='email']"
    PASSWORD_FIELD_XPATH = "//input [@id='password']"
    SUBMIT_BUTTON_XPATH = "//form[@id='login_form']//button[contains(@class, 'submit_btn')]"

    def navigate(self):
        self.driver.get(self.URL)

    def wait_until_loaded(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located((By.XPATH, self.SUBMIT_BUTTON_XPATH)))

    def login(self, username: str = "ttrvuf0@lywenw.com", password: str = "Aj#%R*g54%u$x=Y"):
        self.driver.find_element_by_xpath(self.EMAIL_FIELD_XPATH).send_keys(username)
        self.driver.find_element_by_xpath(self.PASSWORD_FIELD_XPATH).send_keys(password)
        self.driver.find_element_by_xpath(self.SUBMIT_BUTTON_XPATH).click()