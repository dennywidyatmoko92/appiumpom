from SampleProjects.LocatorElement.locators import Locators

class LoginPage():
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.username_textbox_id = Locators.txt_username
        self.password_textbox_id = Locators.txt_password
        self.login_button_id = Locators.button_sign_in
        self.login_button_masuk = Locators.button_masuk

    def enter_username(self, username):
        self.webdriver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.webdriver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_signin(self):
        self.webdriver.find_element_by_id(self.login_button_id).click()

    def click_masuk(self):
        self.webdriver.find_element_by_id(self.login_button_masuk).click()
