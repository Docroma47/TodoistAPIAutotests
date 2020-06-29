import unittest

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.application import Application

class ProjectTest(unittest.TestCase):
    driver: WebDriver
    app: Application

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.app = Application(cls.driver)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    def test_create_project(self):
        self.app.login()
        self.app.main_page.navigate()
        self.app.main_menu.click_create_project()

    def test_create_task(self):
        self.app.login()
        self.app.main_page.navigate()
        self.app.main_page.click_create_task()

    def test_create_task_and_date(self):
        self.app.login()
        self.app.main_page.navigate()
        self.app.main_page.create_task_and_date()
        self.app.main_page.check_new_task()

    def test_create_sub_task(self):
        self.app.login()
        self.app.main_page.navigate()
        self.app.main_page.click_create_task()
        self.app.main_page.create_sub_task()

    def test_create_comment(self):
        self.app.login()
        self.app.main_page.navigate()
        message = self.app.main_page.create_comment()
        self.assertEqual(message, "Комментарии и загрузка файлов – функция Премиум")