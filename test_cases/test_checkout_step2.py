
from test_cases.test_checkout_step1 import login_2
from test_cases.test_checkout_step1 import CheckoutStep1
from pages.checkout_step2_page import CheckoutStep2
import pytest

from utilities.read_login import get_test3_data

tc,fn,ln,zip = get_test3_data()

def login_3(driver):
    login_2(driver)
    check_step1 = CheckoutStep1(driver)
    check_step1.enter_first_name(fn)
    check_step1.enter_last_name(ln)
    check_step1.enter_zipcode(zip)
    check_step1.click_continue_btn()


# testcase 1:-
# open browser
# login
# add to cart
# click cart link
# click checkout
# enter valid creds
# click continue
# click prod text
# expected ---> new html prod page should display



@pytest.mark.order(12)
def test_check_prod_text(driver):
    login_3(driver)

    check_step2 = CheckoutStep2(driver)
    check_step2.click_product_text()

    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=4",driver.save_screenshot("screenshots/step2_prod_text.png")



# testcase 2:-
# open browser
# login
# add to cart
# click cart link
# click checkout
# enter valid creds
# click finish btn
# expected result --> next page should be open

@pytest.mark.order(13)
def test_click_finish_btn(driver):

    login_3(driver)
    check_step2 = CheckoutStep2(driver)
    check_step2.click_finish_btn()



    assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html",driver.save_screenshot("screenshots/step2_finish_btn.png")






# testcase 3:-
# open browser
# login
# add to cart
# click cart link
# click checkout
# enter valid creds
# click prod cancel btn
# expected result --> inventory page should display

@pytest.mark.order(14)
def test_click_cancel_btn(driver):

    login_3(driver)
    check_step2 = CheckoutStep2(driver)
    check_step2.click_cancel_btn()


    assert driver.current_url == "https://www.saucedemo.com/inventory.html",driver.save_screenshot("screenshots/step2_cancel_btn.png")



