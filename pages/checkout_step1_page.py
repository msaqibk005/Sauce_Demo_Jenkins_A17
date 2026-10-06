
from time import sleep


class CheckoutStep1:

    FIRST_NAME = "id","first-name"
    LAST_NAME = "id","last-name"
    CODE = "id","postal-code"
    CONTINUE_BTN = "id","continue"
    CANCEL_BTN = "id","cancel"


    def __init__(self,driver):
        self.driver = driver


    def enter_first_name(self,f_name):
        self.driver.find_element(*CheckoutStep1.FIRST_NAME).send_keys(f_name)

    def enter_last_name(self,l_name):
        self.driver.find_element(*CheckoutStep1.LAST_NAME).send_keys(l_name)

    def enter_zipcode(self,zipcode):
        self.driver.find_element(*CheckoutStep1.CODE).send_keys(zipcode)

    def click_continue_btn(self):
        self.driver.find_element(*CheckoutStep1.CONTINUE_BTN).click()
        sleep(3)

    def click_cancel_btn(self):
        self.driver.find_element(*CheckoutStep1.CANCEL_BTN).click()
        sleep(2)





