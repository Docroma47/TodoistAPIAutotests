from selenium.webdriver.remote.webdriver import WebDriver

from pages.landing_page import LandingPage
from pages.main_menu import MainMenu
from pages.main_page import MainPage
from pages.login_page import LoginPage

class Application:
    landing_page: LandingPage
    login_page: LoginPage
    main_menu: MainMenu
    main_page: MainPage

    def __init__(self, driver: WebDriver):
        super().__init__()
        self.landing_page = LandingPage(driver)
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        self.main_menu = MainMenu(driver)

    def login(self):
        self.landing_page.navigate()
        self.landing_page.wait_until_loaded()
        self.landing_page.click_login()
        self.login_page.wait_until_loaded()
        self.login_page.login()
        self.main_page.wait_until_loaded()