from selenium.webdriver.remote.webdriver import WebDriver

class UIElement:
    driver: WebDriver

    def __init__(self, driver: WebDriver):
        super().__init__()
        self.driver = driver