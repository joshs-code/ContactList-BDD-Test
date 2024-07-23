from behave import given, when, then
from selenium import webdriver
from utils import utils
from pages.RegisterPage import RegisterPage
import names
import time


# Reusable WebDriver initialization
@given('launch chrome browser')
def openHomepage(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


# Open contact list homepage
@when('I open contact list homepage')
def openHomePage(context):
    context.driver.get(utils.URL)


# Click sign up button
@when('click sign up button')
def clickSignup(context):
    RegisterPage(context.driver).goto_signup_page()


# Enter user details
@when('enter first name and last name and email and password')
def enterInfo(context):
    rp = RegisterPage(context.driver)
    rp.register_user_details(names.get_first_name(), "a", names.get_first_name() + '@test.com', "meegy123abc")


# Click on submit button
@when('click on submit button')
def clickSubmit(context):
    RegisterPage(context.driver).click_register_btn()


# Verify account creation
@then('user must have successfully created account.')
def verifyCreated(context):
    RegisterPage(context.driver).verify_logged_in()


# Close the browser using context manager
@then('close the browser')
def closeBrowser(context):
    context.driver.quit()