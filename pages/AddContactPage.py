from selenium.webdriver.common.by import By


class AddContactPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_contact_btn_xpath = '//button[@id="add-contact"]'
        self.fName_xpath = '//input[@id="firstName"]'
        self.lName_xpath = '//input[@id="lastName"]'
        self.dob_xpath = '//input[@id="birthdate"]'
        self.email_xpath = '//input[@id="email"]'
        self.phone_xpath = '//input[@id="phone"]'
        self.addr_one_xpath = '//input[@id="street1"]'
        self.addr_two_xpath = '//input[@id="street2"]'
        self.city_xpath = '//input[@id="city"]'
        self.state_xpath = '//input[@id="stateProvince"]'
        self.postal_code_xpath = '//input[@id="postalCode"]'
        self.country_xpath = '//input[@id="country"]'
        self.submit_xpath = '//button[@type="submit"]'

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

    def click_submit_btn(self):
        self.driver.find_element(By.XPATH, self.submit_xpath).click()