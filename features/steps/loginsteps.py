from behave import given, when, then
from selenium import webdriver
from utils import utils
from pages.LoginPage import LoginPage

@when('enter email and password')
def enterCredentials(context):
    lp = LoginPage(context.driver)
    lp.enter_user_login("josh1988@gmail.com", "password123")

@when('click on the submit button')
def clickLogin(context):
    LoginPage(context.driver).click_login_btn()


@then('user must have successfully logged in.')
def verifyLogin(context):
    LoginPage(context.driver).verify_logged_in()