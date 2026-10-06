
#Testcase1:-
#Open browser
# login
# check whthr products are displayed or not
# expected result---> products should be displayed

import pytest


from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utilities.read_login import get_test1_data
from time import sleep


t,u,p=get_test1_data()


def login(driver):
    l=LoginPage(driver)
    l.enter_username(u)
    l.enter_password(p)
    l.click_login_btn()





@pytest.mark.order(3)


def test_products_displayed(driver):
    login(driver)
    invent = InventoryPage(driver)
    assert invent.get_products(),driver.save_screenshot("screenshots/product_not_displayed.png")







# Testcase2:-
# Open browser
#login
#verify add to cart button is working or not
# expected result ---> product added to cart


@pytest.mark.order(4)
def test_add_to_cart(driver):
    login(driver)
    invent = InventoryPage(driver)
    invent.click_add_to_cart()
    sleep(3)
    assert invent.get_text_cart()=='1',driver.save_screenshot("screenshots/add_to_cart.png")
    sleep(3)


# Testcase 3:-
# Open browser
# login
# click on cart link is working or not
# expected result ---> it should display in new page

@pytest.mark.order(5)
def test_click_on_cart_link(driver):
    login(driver)
    invent = InventoryPage(driver)
    invent.click_add_to_cart()
    sleep(2)
    invent.click_cart_link()
    sleep(3)
    expected_url = "https://www.saucedemo.com/cart.html"
    assert driver.current_url == expected_url,driver.save_scrrenshot("screenshots/cart_link.png")
    sleep(2)






