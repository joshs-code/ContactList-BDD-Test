from behave import given, then, when
from pages.EditContactPage import EditContactPage

@when(u'click delete contact')
def step_impl(context):
    EditContactPage(context.driver).click_delete_btn()
@when(u'click ok on alert box')
def step_impl(context):
    EditContactPage(context.driver).click_alert_accept()
@then(u'verify item is deleted')
def step_impl(context):
    EditContactPage(context.driver).verify_name_deleted()

