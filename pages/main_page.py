from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.ui_element import UIElement

class MainPage(UIElement):
    LOADING_ID = "loading"
    URL = "https://todoist.com/app"
    ADD_TASK_BUTTON_XPATH = "//div[@id='editor']//button[contains (@class, 'plus_add_button')]"
    TASK_NAME_FIELD_XPATH = "//ul[@class='items']//div[contains (@class, 'DraftEditor-root')]" +\
                            "//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']"
    SUBMIT_BUTTON_TASK_XPATH = "//form//button[@type='submit']"
    CANCEL_BUTTON_XPATH = "//form//button[@class='cancel']"
    LIST_CREATE_TASK_XPATH = "//div[@id='editor']//ul[@class='items']//span[text()='CREATE-TASK-1']"

    TASK_DATE_FIELD_XPATH = "//div[@id='editor']//ul[@class='items']//div[@class='item_editor_assign']/button"
    DATE = "//div[@class='scheduler_popper popper']//div[@class='scheduler-preview-date']"
    DATE_MENU_XPATH = "//div[@class='scheduler_popper popper']"
    DATE_MENU_INPUT_XPATH = "//div[@class='scheduler_popper popper']//input"

    INBOX_ID = "filter_inbox"
    CREATED_TASK_WITH_DATE_XPATH = "//div[@id='editor']//ul[@class='items']//span[text()='CREATE-TASK-2']"


    CREATED_SUB_TASK = "//section//button[@class='plus_add_button']"
    SUB_TASK_FIELD_XPATH = "//section//div[contains (@class, 'editorContainer')]"
    SUB_TASK_SUBMIT_BUTTON_XPATH = "//section//button[@type='submit']"
    LIST_CREATE_SUB_TASK_XPATH = "//section//ul[@class='items']//span[text()='SUB-TASK']"
    CLOSE_BUTTON_XPATH = "//section//button[@class='item_detail_close']"

    PANEL_COMMENTS_TASK_XPATH = "//section//button[contains (@aria-controls, 'panel-comments')]"
    INPUT_FIELD_XPATH = "//section//textarea"
    SECTION_SUBMIT_BUTTON_XPATH = "//section//button[@type='submit']"
    TITLE_MESSAGE = "//section//h1"


    def navigate(self):
        self.driver.get(self.URL)
        self.wait_until_loaded()

    def wait_until_loaded(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.invisibility_of_element((By.ID, self.LOADING_ID)))
        wait.until(ec.url_contains(self.URL))

    def click_create_task(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, self.ADD_TASK_BUTTON_XPATH))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, self.TASK_NAME_FIELD_XPATH))).send_keys("CREATE-TASK-1")
        wait.until(ec.element_to_be_clickable((By.XPATH, self.SUBMIT_BUTTON_TASK_XPATH))).click()
        wait.until(ec.element_to_be_clickable((By.XPATH, self.CANCEL_BUTTON_XPATH))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, self.LIST_CREATE_TASK_XPATH)))
        wait.until(ec.text_to_be_present_in_element((By.XPATH, self.LIST_CREATE_TASK_XPATH), "CREATE-TASK-1"))

    def create_task_and_date(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, self.ADD_TASK_BUTTON_XPATH))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, self.TASK_NAME_FIELD_XPATH))).send_keys("CREATE-TASK-2")
        wait.until(ec.element_to_be_clickable((By.XPATH, self.TASK_DATE_FIELD_XPATH))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, self.DATE_MENU_XPATH)))
        wait.until(ec.visibility_of_element_located((By.XPATH, self.DATE_MENU_INPUT_XPATH))).send_keys("12 june 2021 12:55")
        wait.until(ec.visibility_of_element_located((By.XPATH, self.DATE))).click()
        wait.until(ec.element_to_be_clickable((By.XPATH, self.SUBMIT_BUTTON_TASK_XPATH))).click()

    def check_new_task(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.element_to_be_clickable((By.ID, self.INBOX_ID))).click()
        wait.until(ec.element_to_be_clickable((By.XPATH, self.CREATED_TASK_WITH_DATE_XPATH)))

    def create_sub_task(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, self.LIST_CREATE_TASK_XPATH))).click()
        wait.until(ec.element_to_be_clickable((By.XPATH, self.CREATED_SUB_TASK))).click()
        wait.until(ec.element_to_be_clickable((By.XPATH, self.TASK_NAME_FIELD_XPATH))).send_keys("SUB-TASK")
        wait.until(ec.element_to_be_clickable((By.XPATH, self.SUB_TASK_SUBMIT_BUTTON_XPATH))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, self.LIST_CREATE_SUB_TASK_XPATH)))
        wait.until(ec.visibility_of_element_located((By.XPATH, self.CLOSE_BUTTON_XPATH))).click()

    def create_comment(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(ec.visibility_of_element_located((By.XPATH, self.LIST_CREATE_TASK_XPATH))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, self.PANEL_COMMENTS_TASK_XPATH))).click()
        wait.until(ec.element_to_be_clickable((By.XPATH, self.INPUT_FIELD_XPATH))).send_keys("COMMENT")
        wait.until(ec.element_to_be_clickable((By.XPATH, self.SECTION_SUBMIT_BUTTON_XPATH))).click()
        return wait.until(ec.visibility_of_element_located((By.XPATH, self.TITLE_MESSAGE))).text