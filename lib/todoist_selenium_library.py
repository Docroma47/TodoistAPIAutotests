from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.application import Application


class RobotUILibrary():
    driver: WebDriver
    app: Application

    def set_up(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.maximize_window()
        self.app = Application(self.driver)
        self.app.login()
        self.app.main_page.navigate()

    def tear_down(self):
        self.driver.quit()

    def create_project(self, name_project: str):
        self.app.main_menu.click_create_project(name_project)

    def assert_project_with_name_exists(self, name_project: str):
        assert name_project == self.app.main_menu.get_created_project()

    def create_task(self, name_project: str, name_task: str):
        self.app.main_menu.click_create_project(name_project)
        self.app.main_page.click_create_task(name_task)

    def assert_task_with_name_exists(self, name_task: str):
        assert name_task == self.app.main_page.get_created_task()

    def create_task_with_date_and_time(self, name_project: str, name_task: str, date_task: str):
        self.app.main_menu.click_create_project(name_project)
        self.app.main_page.create_task_and_date(name_task, date_task)

    def assert_task_with_due_date_exist(self, name_task: str, date_task: str):
        assert name_task == self.app.main_page.get_created_task()
        assert date_task == self.app.main_page.get_date_task(), "Date is not correct"

