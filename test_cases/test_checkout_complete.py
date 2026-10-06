
# testcase 1:-
# open browser
# login
# add to cart
# click cart link
#  click checkout
#  enter valid creds
#  click finish btn
# click back to home btn
# expected result --> inventory page

import pytest
from test_cases.test_checkout_step2 import login_3
from pages.checkout_step2_page import CheckoutStep2
from pages.checkout_complete_page import CheckoutComplete





@pytest.mark.order(15)
def test_click_back_home_btn(driver):
    login_3(driver)
    check_step2 = CheckoutStep2(driver)
    check_step2.click_finish_btn()
    check_complete = CheckoutComplete(driver)
    check_complete.click_back_home_btn()


    assert driver.current_url == "https://www.saucedemo.com/inventory.html",driver.save_screenshot("screenshots/back_home.png")

