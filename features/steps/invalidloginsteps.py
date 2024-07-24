from behave import given, when, then
from selenium import webdriver
from pages.LoginPage import LoginPage
from utils import utils


@when(u'enter invalid email and password')
def enter_invalid_credentails(context):
    LoginPage(context.driver).enter_user_login('invalidemail@test.com', 'abc123456')
@then(u'user must have received error message')
def verify_error_msg(context):
    LoginPage(context.driver).verify_not_logged_in()