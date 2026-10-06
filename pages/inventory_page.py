

class InventoryPage:
    prod="xpath","//div[@class='inventory_item']"
    add_to_cart="xpath","//button[text()='Add to cart']"
    text_cart = "xpath","//span[@data-test='shopping-cart-badge']"  # text number on cart you have added on right corner
    cart = "xpath", "//a[@class='shopping_cart_link']"


    def __init__(self,driver):
        self.driver=driver



    def get_products(self):
       return self.driver.find_element(*InventoryPage.prod).is_displayed()


    def click_add_to_cart(self):
        self.driver.find_element(*InventoryPage.add_to_cart).click()


    def get_text_cart(self):
        a = self.driver.find_element(*InventoryPage.text_cart)
        b = a.text
        return b


    def click_cart_link(self):
        self.driver.find_element(*InventoryPage.cart).click()



