from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://todoist.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 4000)

class CreateProject:

    XpathButtonAdd = "//div[@id='projects_list_manager']//a[contains (@class, 'add_project')]"
    XpathInputField = "//input[@id='edit_project_modal_field_name']"
    XpathSubmitButton = "//form//footer/button[@type='submit']"
    XpathAddProject = "//div[@id='projects_list_manager']//a[contains (@class, 'add_project')]"

    def create(self):
        wait.until(ec.invisibility_of_element((By.ID, "loading")))
        wait.until(ec.element_to_be_clickable((By.XPATH, self.XpathButtonAdd)))
        driver.find_element_by_xpath(self.XpathButtonAdd).click()
        driver.find_element_by_xpath(self.XpathInputField).send_keys("Test")
        driver.find_element_by_xpath(self.XpathSubmitButton).click()
        driver.find_element_by_xpath(self.XpathAddProject).click()

class LoginProfile:

    XpathLogin = "//ul[@class='_1QHsb']//a[@href='/users/showlogin']"
    XpathEmail = "//input [@id='email']"
    XpathPassword = "//input [@id='password']"
    XpathSubmitButton = "//form[@id='login_form']//button[contains(@class, 'submit_btn')]"

    def Login(self):
        driver.find_element_by_xpath(self.XpathLogin).click()
        driver.find_element_by_xpath(self.XpathEmail).send_keys("ttrvuf0@lywenw.com")
        driver.find_element_by_xpath(self.XpathPassword).send_keys("Aj#%R*g54%u$x=Y")
        driver.find_element_by_xpath(self.XpathSubmitButton).click()

class CreateTask:

    XpathButtonAdd = "//div[@id='editor']//button[contains (@class, 'plus_add_button')]"
    XpathInputField = "//input[@id='edit_project_modal_field_name']"
    XpathSubmitButton = "//form//footer/button[@type='submit']"

    def createTask(self):
        driver.find_element_by_xpath(self.XpathButtonAdd).click()
        driver.find_element_by_xpath(self.XpathInputField).send_keys("TestTask")
        driver.find_element_by_xpath(self.XpathSubmitButton).click()

class CreateTaskWithDate:

    XpathButtonAdd = "//div[@id='editor']//button[contains (@class, 'plus_add_button')]"
    XpathInputField = "//input[@id='edit_project_modal_field_name']"
    XpathInputTime = "//div[@id='editor']//button[contains (@class, 'item_editor_assign_due')]"
    XpathSubmitButton = "//form//footer/button[@type='submit']"

    def createTaskWithDate(self):
        driver.find_element_by_xpath(self.XpathButtonAdd).click()
        driver.find_element_by_xpath(self.XpathInputField).send_keys("TestTask")
        driver.find_element_by_xpath(self.XpathInputTime).send_keys("12 june 2020 12:12")
        driver.find_element_by_xpath(self.XpathSubmitButton).click()

class CreateSubtask:

    XpathButtonAdd = "//section//button[@class='plus_add_button']"
    XpathInputField = "//section//div[contains (@class, 'editorContainer')]"
    XpathInputTime = "//section//button[contains (@class, 'item_editor_assign_due')]"

    def createSubtask(self):
        driver.find_element_by_xpath(self.XpathButtonAdd).click()
        driver.find_element_by_xpath(self.XpathInputField).send_keys("TestSubtask")
        driver.find_element_by_xpath(self.XpathInputTime).send_keys("12 june 2020 12:12")

class AddComment:

    XpathButtonAdd = "//div[@id='editor']//button[@class='clickable note_icon']"
    XpathInputField = "//section//textarea"
    XpathInputTime = "//section//button[contains (@class, 'item_editor_assign_due')]"
    XpathSectionSubmitButton = "//section//button[@type='submit']"
    XpathSubmitButton = "//div[@id='editor']//button[@type='submit']"

    def createSubtask(self):
        driver.find_element_by_xpath(self.XpathButtonAdd).click()
        driver.find_element_by_xpath(self.XpathInputField).send_keys("Test")
        driver.find_element_by_xpath(self.XpathInputTime).send_keys("12 june 2020 12:12")
        driver.find_element_by_xpath(self.XpathSectionSubmitButton).click()
        driver.find_element_by_xpath(self.XpathSubmitButton).click()