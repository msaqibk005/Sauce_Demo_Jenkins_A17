
 # test case 1:-
 # open browser
 # enter correct credentials with username and password
 # username --> standard_user
 # pwd --> secret_sauce
 # expected result == " https://www.saucedemo.com/inventory.html"


# def test_valid_credentials(driver):
#    log = LoginPage(driver)
#    log.enter_username("standard_user")
#    log.enter_password("secret_sauce")
#    log.click_login_btn()

#    expected_url = 'https://www.saucedemo.com/inventory.html'
#    assert driver.current_url == expected_url,driver.save_screenshot("screenshots/test_case1.png")




# test case 2:-
# open browser
# enter invalid username and valid password
# username --> wrong_username
# pwd --> secret_sauce
# expected result == 'https://www.saucedemo.com/'



# def test_invalid_username(driver):
#    log = LoginPage(driver)
#    log.enter_username("wrong_username")
#    log.enter_password("secret_sauce")
#    log.click_login_btn()

#    expected_url = 'https://www.saucedemo.com/inventory.html'
#    assert driver.current_url == expected_url, driver.save_screenshot("screenshots/test_case2.png")






# test case 3:-
# open browser
# enter valid username and invalid password
# username --> standard_user
# pwd --> wrong_password
# expected result == 'https://www.saucedemo.com/'

# def test_invalid_password(driver):
#    log = LoginPage(driver)
#    log.enter_username("standard_user")
#    log.enter_password("wrong_password")
#    log.click_login_btn()

#    expected_url = 'https://www.saucedemo.com/'
#    assert driver.current_url == expected_url, driver.save_screenshot("screenshots/test_case3.png")



# test case 4:-
# open browser
# enter invalid username and invalid password
# username --> wrong_username
# password --> wrong_password
# expected result == 'https://www.saucedemo.com/'


# def test_invalid_credentials(driver):
#    log = LoginPage(driver)
#    log.enter_username("wrong_username")
#    log.enter_password("wrong_password")
#    log.click_login_btn()

#    expected_url = 'https://www.saucedemo.com/'
#    assert driver.current_url == expected_url, driver.save_screenshot("screenshots/test_case4.png")




# test case 5:-
# open browser
# enter empty username and empty password
# username --> "       "
# pwd --> "       "
# expected result == 'https://www.saucedemo.com/'

# def test_empty_credentials(driver):
#    log = LoginPage(driver)
#    log.enter_username("      ")
#    log.enter_password("      ")

#    expected_url = 'https://www.saucedemo.com/'
#    assert driver.current_url == expected_url, driver.save_screenshot("screenshots/test_case5.png")




########################################################################################################################





import pytest

from pages.login_page import LoginPage
from utilities.read_login import get_test1_data
from utilities.read_login import get_test2_data

tc,un,pwd = get_test1_data()

@pytest.mark.order(1)

def test_login_1(driver):
    log = LoginPage(driver)
    log.enter_username(un)
    log.enter_password(pwd)
    log.click_login_btn()
    
    
    expected_url = 'https://www.saucedemo.com/inventory.html'
    assert driver.current_url == expected_url,driver.save_screenshot(f"screenshots/test_case{tc}.png")



@pytest.mark.skip

@pytest.mark.order(2)
@pytest.mark.parametrize("testcase,username,password",get_test2_data())

def test_login_2(driver,testcase,username,password):
    log = LoginPage(driver)
    log.enter_username(username)
    log.enter_password(password)
    log.click_login_btn()
    
    
    expected_url = 'https://www.saucedemo.com/'
    assert driver.current_url == expected_url, driver.save_screenshot(f"screenshots/test_case{testcase}.png")



