import data
import helpers
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_taxi_button = (By.XPATH, "//button[@class='button round']")
    confort_fee_button = (By.XPATH, "//img[@alt='Comfort']")
    #llenado de teléfono
    phone_field = (By.CSS_SELECTOR, ".np-text")
    phone_field_popup = (By.ID, "phone")
    phone_button = (By.XPATH, "//button[@type='submit']")
    confirm_phone_button = (By.XPATH, "(//button[@type='submit'])[2]")
    validation_code_field = (By.ID, "code")
    #llenado tdc
    payment_method = (By.CSS_SELECTOR, ".pp-text")
    add_card = (By.CSS_SELECTOR, ".pp-plus")
    card_number_field = (By.ID, "number")
    card_code_field = (By.NAME, "code")
    add_card_button = (By.XPATH, "(//button[@type='submit'])[3]")
    close_add_card_modal = (By.CSS_SELECTOR, ".payment-picker .active > .close-button")
    #otros servicios
    driver_comment = (By.ID, "comment")
    blanket_handkerchiefs = (By.CSS_SELECTOR, ".r:nth-child(1) .slider")
    icecream_counter = (By.CSS_SELECTOR, ".r:nth-child(1) .counter-plus")
    get_taxi_button = (By.CSS_SELECTOR, ".smart-button-main")
    driver_img = (By.CSS_SELECTOR, ".order-button > img:nth-child(2)")

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(self.from_field))
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(self.to_field))
        self.set_from(address_from)
        self.set_to(address_to)

    def click_order_taxi_button(self):
        WebDriverWait(self.driver, 6).until(expected_conditions.presence_of_element_located(self.order_taxi_button))
        self.driver.find_element(*self.order_taxi_button).click()

    def click_confort_fee_button(self):
        WebDriverWait(self.driver, 6).until(expected_conditions.presence_of_element_located(self.confort_fee_button))
        self.driver.find_element(*self.confort_fee_button).click()

    def fill_phone_fild(self):
        self.driver.find_element(*self.phone_field).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(self.phone_field_popup))
        self.driver.find_element(*self.phone_field_popup).send_keys(data.phone_number)
        self.driver.find_element(*self.phone_button).click()
        validation_code = helpers.retrieve_phone_code(self.driver)
        self.driver.find_element(*self.validation_code_field).send_keys(validation_code)
        self.driver.find_element(*self.confirm_phone_button).click()

    def add_credit_card(self):
        self.driver.find_element(*self.payment_method).click()
        self.driver.find_element(*self.add_card).click()
        self.driver.find_element(*self.card_number_field).send_keys(data.card_number)
        self.driver.find_element(*self.card_code_field).send_keys(data.card_code)
        self.driver.find_element(*self.card_code_field).send_keys(Keys.TAB)
        self.driver.find_element(*self.add_card_button).click()
        self.driver.find_element(*self.close_add_card_modal).click()

    def add_aditional_data(self):
        self.driver.find_element(*self.driver_comment).send_keys(data.message_for_driver)
        self.driver.find_element(*self.blanket_handkerchiefs).click()
        self.driver.find_element(*self.icecream_counter).click()
        self.driver.find_element(*self.icecream_counter).click()
        self.driver.find_element(*self.get_taxi_button).click()
        WebDriverWait(self.driver, 60).until(expected_conditions.presence_of_element_located(self.driver_img))