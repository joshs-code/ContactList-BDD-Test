from selenium.webdriver.common.by import By


class AddContactPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_contact_btn_xpath = '//button[@id="add-contact"]'
        self.fName_xpath = ''
        self.lName_xpath = ''
        self.dob_xpath = ''
        self.email_xpath = ''
        self.phone_xpath = ''
        self.addr_one_xpath = ''
        self.addr_two_xpath = ''
        self.city_xpath = ''
        self.state_xpath = ''
        self.postal_code_xpath = ''
        self.country_xpath = ''
        self.submit_xpath = ''

    def click_add_contact(self):
        self.driver.find_element(By.XPATH, self.add_contact_btn_xpath).click()

    def add_contact(self, fname, lname, dob, email, phone, addrone, addrtwo, city, state, postcode, country):
        self.driver.find_element(By.XPATH, self.fName_xpath).clear()
        self.driver.find_element(By.XPATH, self.fName_xpath).send_keys(fname)

        self.driver.find_element(By.XPATH, self.lName_xpath).clear()
        self.driver.find_element(By.XPATH, self.lName_xpath).send_keys(lname)

        self.driver.find_element(By.XPATH, self.phone_xpath).clear()
        self.driver.find_element(By.XPATH, self.phone_xpath).send_keys(phone)

        self.driver.find_element(By.XPATH, self.addr_one_xpath).clear()
        self.driver.find_element(By.XPATH, self.addr_one_xpath).send_keys(addrone)

        self.driver.find_element(By.XPATH, self.addr_two_xpath).clear()
        self.driver.find_element(By.XPATH, self.addr_two_xpath).send_keys(addrtwo)

        self.driver.find_element(By.XPATH, self.city_xpath).clear()
        self.driver.find_element(By.XPATH, self.city_xpath).send_keys(city)

        self.driver.find_element(By.XPATH, self.state_xpath).clear()
        self.driver.find_element(By.XPATH, self.state_xpath).send_keys(state)

        self.driver.find_element(By.XPATH, self.postal_code_xpath).clear()
        self.driver.find_element(By.XPATH, self.postal_code_xpath).send_keys(postcode)

        self.driver.find_element(By.XPATH, self.country_xpath).clear()
        self.driver.find_element(By.XPATH, self.country_xpath).send_keys(country)

        self.driver.find_element(By.XPATH, self.submit_xpath).click()