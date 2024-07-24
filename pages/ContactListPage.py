from selenium.webdriver.common.by import By
import datetime

class ContactListPage:

    def __init__(self, driver):
        self.driver = driver
        self.add_contact_btn_xpath = '//button[@id="add-contact"]'
        self.test_add_contact_xpath = '//td[contains(text(), "Bob")]'

    def click_add_contact_btn(self):
        self.driver.find_element(By.XPATH, self.add_contact_btn_xpath).click()

    def verify_contact_add(self):
        contact_shown = self.driver.find_element(By.XPATH, self.test_add_contact_xpath).is_displayed()
        assert contact_shown
        screenshot_timestamp = datetime.datetime.now()
        self.driver.save_screenshot(f"./screenshots/added-contact-{screenshot_timestamp}.png")
