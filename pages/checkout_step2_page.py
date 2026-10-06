from time import sleep

class CheckoutStep2:

    prod_text = "xpath","//div[.='Sauce Labs Backpack']"
    cancel_btn = "id","cancel"
    finish_btn = "id","finish"


    def __init__(self,driver):
        self.driver = driver


    def click_product_text(self):
        self.driver.find_element(*CheckoutStep2.prod_text).click()
        sleep(2)

    def click_cancel_btn(self):
        self.driver.find_element(*CheckoutStep2.cancel_btn).click()
        sleep(2)

    def click_finish_btn(self):
        self.driver.find_element(*CheckoutStep2.finish_btn).click()
        sleep(2)

