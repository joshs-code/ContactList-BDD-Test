from behave import given, then, when
from selenium import webdriver
from pages.EditContactPage import EditContactPage

@when('click first element')
def click_first_el(context):
    EditContactPage(context.driver).click_1st_el()

@when('click edit contact button')
def click_edit_btn(context):
    EditContactPage(context.driver).click_contact_edit_btn()

@when('edit the contact entry')
def edit_info(context):
    EditContactPage(context.driver).edit_contact("New First Name")
@when('click changes submit button')
def click_submit(context):
    EditContactPage.click_submit()
@then('verify details changes made')
def verify_changes(context):
    EditContactPage(context.driver).verify_fname_changed()