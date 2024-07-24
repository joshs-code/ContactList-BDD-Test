from selenium.webdriver.common.by import By
import datetime

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.email_xpath = '//input[@id="email"]'
        self.password_xpath = '//input[@id="password"]'
        self.submit_btn_xpath = '//button[@id="submit"]'
        self.logout_btn_xpath = '//button[@id="logout"]'
        self.login_error_msg_xpath = '//span[contains(text(), "Incorrect username or password")]'

    def enter_user_login(self, email, password):
        self.driver.find_element(By.XPATH, self.email_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

        self.driver.find_element(By.XPATH, self.password_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(By.XPATH, self.submit_btn_xpath).click()

    def verify_logged_in(self):
        logout_btn = self.driver.find_element(By.XPATH, self.logout_btn_xpath)
        assert logout_btn

        screenshot_timestamp = datetime.datetime.now()
        self.driver.save_screenshot(f"./screenshots/verified-valid-login{screenshot_timestamp}.png")

    def verify_not_logged_in(self):
        err_msg= self.driver.find_element(By.XPATH, self.login_error_msg_xpath).text
        assert err_msg

        screenshot_timestamp = datetime.datetime.now()
        self.driver.save_screenshot(f"./screenshots/verified-invalid-login-{screenshot_timestamp}.png")
