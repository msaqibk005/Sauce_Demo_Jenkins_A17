
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from test_cases.test_inventory import login
from time import sleep




# testcase 1:-
# open browser
# login the site
# click add to cart
# click on cart link
# cart page should open
# expected result --> cart product is displaying or not

@pytest.mark.order(6)

def test_cart_product(driver):
    login(driver)
    invent = InventoryPage(driver)
    invent.click_add_to_cart()
    sleep(2)
    invent.click_cart_link()
    sleep(3)
    cp = CartPage(driver)

    assert cp.get_cart_product(),driver.save_screenshot("screenshots/cart_product_not_displaying.png")
    sleep(3)




# testcase 2:-
# open browser
# login the site
# click add to cart
# click on cart link
# cart page should open
# click on continue shopping
# expected result ----> previous page or inventory page should be open

@pytest.mark.order(7)

def test_click_continue_shopping_btn(driver):
    login(driver)
    invent = InventoryPage(driver)
    invent.click_add_to_cart()
    sleep(2)
    invent.click_cart_link()
    sleep(3)
    cp = CartPage(driver)
    cp.click_continue_shopping()
    sleep(3)

    assert driver.current_url=="https://www.saucedemo.com/inventory.html",driver.save_screenshot("screenshots/continue_shopping_btn not working.png")





# testcase 3:-
# open browser
# login the site
# click add to cart
# click on cart link
# cart page should open
# click on checkout btn
# expected result ---> next page should open


@pytest.mark.order(8)
def test_click_checkout_btn(driver):
    login(driver)
    invent = InventoryPage(driver)
    invent.click_add_to_cart()
    sleep(2)
    invent.click_cart_link()
    sleep(3)
    cp = CartPage(driver)
    cp.click_checkout_btn()
    sleep(3)

    assert driver.current_url=="https://www.saucedemo.com/checkout-step-one.html",driver.save_screenshot("screenshots/checkout_btn not working.png")


