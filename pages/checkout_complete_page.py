from time import sleep
class CheckoutComplete:

    BACK_HOME_BTN = "xpath","//button[@class='btn btn_primary btn_small']"


    def __init__(self,driver):
        self.driver = driver


    def click_back_home_btn(self):
        self.driver.find_element(*CheckoutComplete.BACK_HOME_BTN).click()
        sleep(3)


