
import pytest

from selenium.webdriver import Chrome
from time import sleep




@pytest.fixture(scope='function')
def driver():
    driver = Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")
    sleep(3)
    yield driver
    driver.quit()



# collected 15 items
#
# test_cases/test_inventory.py::test_products_displayed PASSED
# test_cases/test_inventory.py::test_add_to_cart PASSED
# test_cases/test_inventory.py::test_click_on_cart_link PASSED
# test_cases/test_cart.py::test_cart_product PASSED
# test_cases/test_cart.py::test_click_continue_shopping_btn PASSED
# test_cases/test_cart.py::test_click_checkout_btn PASSED
# test_cases/test_checkout_step1.py::test_click_cancel_step1_btn PASSED
# test_cases/test_checkout_step1.py::test_valid_login_credentials PASSED
# test_cases/test_checkout_step1.py::test_invalid_login_credentials[2.0--Valid_Lastname-438549.0] PASSED
# test_cases/test_checkout_step1.py::test_invalid_login_credentials[3.0-Valid_Firstname--438549.0] PASSED
# test_cases/test_checkout_step1.py::test_invalid_login_credentials[4.0---] PASSED
# test_cases/test_checkout_step2.py::test_check_prod_text PASSED
# test_cases/test_checkout_step2.py::test_click_finish_btn PASSED
# test_cases/test_checkout_step2.py::test_click_cancel_btn PASSED
# test_cases/test_checkout_complete.py::test_click_back_home_btn PASSED
