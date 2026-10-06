class CartPage:

    cart_prod = "xpath","//div[@class='cart_item_label']"
    cont_shop_btn = "id","continue-shopping"
    CHECKOUT  = "id","checkout"

    def __init__(self,driver):
        self.driver = driver



    def get_cart_product(self):
        return self.driver.find_element(*CartPage.cart_prod).is_displayed()


    def click_continue_shopping(self):
        self.driver.find_element(*CartPage.cont_shop_btn).click()


    def click_checkout_btn(self):
        self.driver.find_element(*CartPage.CHECKOUT).click()



