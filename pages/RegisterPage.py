from selenium.webdriver.common.by import By
import datetime

class RegisterPage:

    def __init__(self, driver):
        self.driver = driver
        self.signup_btn_xpath = '//button[@id="signup"]'
        self.fName_xpath = '//input[@id="firstName"]'
        self.lName_xpath = '//input[@id="lastName"]'
        self.email_xpath = '//input[@id="email"]'
        self.password_xpath = '//input[@id="password"]'
        self.submit_btn_xpath = '//button[@form="add-user"]'
        self.logout_btn_xpath = '//button[@id="logout"]'

    def goto_signup_page(self):
        self.driver.find_element(By.XPATH, self.signup_btn_xpath).click()

    def register_user_details(self, fName, lName, email, password):
        self.driver.find_element(By.XPATH, self.fName_xpath).clear()
        self.driver.find_element(By.XPATH, self.fName_xpath).send_keys(fName)

        self.driver.find_element(By.XPATH, self.lName_xpath).clear()
        self.driver.find_element(By.XPATH, self.lName_xpath).send_keys(lName)

        self.driver.find_element(By.XPATH, self.email_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

        self.driver.find_element(By.XPATH, self.password_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def click_register_btn(self):
        self.driver.find_element(By.XPATH, self.submit_btn_xpath).click()

    def verify_logged_in(self):
        logged_in = self.driver.find_element(By.XPATH, self.logout_btn_xpath).is_displayed()
        assert logged_in == True

        screenshot_timestamp = datetime.datetime.now()
        self.driver.save_screenshot(f'./screenshots/{screenshot_timestamp}.png')