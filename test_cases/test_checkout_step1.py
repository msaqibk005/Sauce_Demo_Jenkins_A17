import pytest
from test_cases.test_inventory import login
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from time import sleep

def login_2(driver):
    login(driver)
    invent = InventoryPage(driver)
    invent.click_add_to_cart()
    sleep(2)
    invent.click_cart_link()
    sleep(2)
    cp = CartPage(driver)
    cp.click_checkout_btn()
    sleep(2)


from pages.checkout_step1_page import CheckoutStep1
from utilities.read_login import get_test3_data
from utilities.read_login import get_test4_data




# testcase 1:-
# open browser
# login
# click add to cart any item
# click to cart link
# click on checkout
# click on cancel
# expected result --> previous page should display (cart page)



@pytest.mark.order(9)

def test_click_cancel_step1_btn(driver):
    login_2(driver)
    check_step1 = CheckoutStep1(driver)
    check_step1.click_cancel_btn()
    sleep(2)

    assert driver.current_url=="https://www.saucedemo.com/cart.html",driver.save_screenshot("screenshots/click_cancel_btn not working.png")






# testcase 2:-
# open browser
# login
# click add to cart any item
# click to cart link
# click on checkout
# enter valid f_name,valid l_name,valid zipcode
# click on continue
# expected result --> checkout step 2 page should display





tc,fn,ln,zc = get_test3_data()

@pytest.mark.order(10)
def test_valid_login_credentials(driver):
    login_2(driver)
    check_step1 = CheckoutStep1(driver)
    check_step1.enter_first_name(fn)
    check_step1.enter_last_name(ln)
    check_step1.enter_zipcode(zc)
    check_step1.click_continue_btn()
    sleep(2)

    expected_url = "https://www.saucedemo.com/checkout-step-two.html"
    assert driver.current_url == expected_url,driver.save_screenshot(f"screenshots/valid_creds{tc}.png")



# testcase 3:-
# open browser
# login
# click add to cart any item
# click to cart link
# click on checkout
# enter empty f_name,valid l_name,valid zipcode
# click on continue
# expected result --> same page should display

# enter valid f_name,empty l_name,valid zipcode
# click on continue
# expected result --> same page should display

# enter empty f_name,empty l_name,empty zipcode
# click on continue
# expected result --> same page should display

@pytest.mark.skip

@pytest.mark.order(11)

@pytest.mark.parametrize("testcase,f_name,l_name,zipcode",get_test4_data())

def test_invalid_login_credentials(driver,testcase,f_name,l_name,zipcode):
    login_2(driver)
    check_step1 = CheckoutStep1(driver)
    check_step1.enter_first_name(f_name)
    check_step1.enter_last_name(l_name)
    check_step1.enter_zipcode(zipcode)
    check_step1.click_continue_btn()
    sleep(2)

    expected_url = "https://www.saucedemo.com/checkout-step-one.html"
    assert driver.current_url == expected_url,driver.save_screenshot(f"screenshots/invalid_creds{testcase}.png")






