from time import sleep

class LoginPage:

# declaration (separate locators)

    USERNAME = "id","user-name"
    PWD = "id","password"
    LOGIN_BTN = "id","login-button"


# create constructor
    def __init__(self,driver):
        self.driver = driver

# create main functions
    def enter_username(self,username):
        self.driver.find_element(*LoginPage.USERNAME).send_keys(username)


    def enter_password(self,password):
        self.driver.find_element(*LoginPage.PWD).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(*LoginPage.LOGIN_BTN).click()

        sleep(4)







