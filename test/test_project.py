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
        self.app.main_menu.wait_until_created_project()
