from behave import given, then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
from selenium.common.exceptions import NoSuchElementException

class EditContactPage:

    def __init__(self, driver):
        self.driver = driver
        self.edit_first_el_xpath = '//tr[@class="contactTableBodyRow"]/td[2]'
        self.edit_contact_btn_xpath = '//button[@id="edit-contact"]'
        self.fName_xpath = '//input[@id="firstName"]'
        self.submit_xpath = '//button[@type="submit"]'
        self.fname_changed_xpath = '//span[@id="firstName"]'
        self.delete_btn_xpath = '//button[@id="delete"]'

    def click_1st_el(self):
        self.driver.find_element(By.XPATH, self.edit_first_el_xpath).click()

    def click_contact_edit_btn(self):
        self.driver.find_element(By.XPATH, self.edit_contact_btn_xpath).click()

    def edit_contact(self, fname):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.fName_xpath).clear()
        self.driver.find_element(By.XPATH, self.fName_xpath).send_keys(fname)

    def click_submit(self):
        self.driver.find_element(By.XPATH, self.submit_xpath).click()

    def verify_fname_changed(self):
        time.sleep(2)
        new_name = self.driver.find_element(By.XPATH, self.fname_changed_xpath).text
        print(new_name)
        assert new_name == "New First Name"

    def click_delete_btn(self):
        self.driver.find_element(By.XPATH, self.delete_btn_xpath).click()

    def click_alert_accept(self):
        alert = Alert(self.driver)
        alert.accept()

    def verify_name_deleted(self):
        time.sleep(2)
        try:
            new_name = self.driver.find_element(By.XPATH, self.fname_changed_xpath).text
            assert False
        except NoSuchElementException:
            assert True