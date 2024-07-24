from behave import when, then, given
from selenium import webdriver
from pages.ContactListPage import ContactListPage
from pages.AddContactPage import AddContactPage


@when('click add a new contact')
def click_add_contact(context):
    ContactListPage(context.driver).click_add_contact_btn()

@when('fill out the contact details')
def add_contact_info(context):
    AddContactPage(context.driver).add_contact(
        "Bob",
        "Doe",
        "1980/01/12",
        "justatest@test.com",
        "9999999999",
        "123 Abc",
        " ",
        "Tulsa",
        "OK",
        "74135",
        "USA",
    )

@when('click submit button')
def click_btn(context):
    AddContactPage(context.driver).click_submit_btn()

@then('contact must have successfully added to contact list')
def verify_contact_added(context):
    ContactListPage(context.driver).verify_contact_add()
