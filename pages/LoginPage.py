from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.email_xpath = '//input[@id="email"]'
        self.password_xpath = '//input[@id="password"]'
        self.submit_btn_xpath = '//button[@id="submit"]'

    def register_user_details(self, fName, lName, email, password):
        self.driver.find_element(By.XPATH, self.email_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

        self.driver.find_element(By.XPATH, self.password_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

        self.driver.find_element(By.XPATH, self.submit_btn_xpath).click()

