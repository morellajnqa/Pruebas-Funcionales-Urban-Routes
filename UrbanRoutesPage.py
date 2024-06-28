import data
import helpers
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

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
    # agrego este elemento para el assert
    card_img = (By.XPATH , "//img[@alt='card']")
    #otros servicios
    driver_comment = (By.ID, "comment")
    blanket_handkerchiefs = (By.CSS_SELECTOR, ".r:nth-child(1) .slider")
    # Agregar elemento para assert
    blanket_handkerchiefs_input = (By.CSS_SELECTOR, ".r:nth-child(1) .switch-input")
    # Agregar elemento para assert
    icecream_counter_value = (By.CSS_SELECTOR, ".r:nth-child(1) .counter-value")
    icecream_counter = (By.CSS_SELECTOR, ".r:nth-child(1) .counter-plus")
    get_taxi_button = (By.CSS_SELECTOR, ".smart-button-main")
    # Para verificar que este en busquedo en el pop up
    order_header_title = (By.CSS_SELECTOR, ".order-header-title")
    driver_img = (By.CSS_SELECTOR, ".order-button > img:nth-child(2)")

    # < div class ="order-header-title" > Buscar automóvil < / div >

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
        helpers.wait_elements (self.driver, self.from_field)
        helpers.wait_elements(self.driver, self.to_field)
        self.set_from(address_from)
        self.set_to(address_to)

    def click_order_taxi_button(self):
        #WebDriverWait(self.driver, 6).until(expected_conditions.presence_of_element_located(self.order_taxi_button))
        helpers.wait_elements(self.driver, self.order_taxi_button)
        self.driver.find_element(*self.order_taxi_button).click()


    def click_confort_fee_button(self):
        helpers.wait_elements(self.driver, self.confort_fee_button)
        #WebDriverWait(self.driver, 6).until(expected_conditions.presence_of_element_located(self.confort_fee_button))
        self.driver.find_element(*self.confort_fee_button).click()

    def fill_phone_fild(self):
        self.driver.find_element(*self.phone_field).click()
        helpers.wait_elements(self.driver, self.phone_field_popup)
        #WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(self.phone_field_popup))
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

    def add_driver_comment(self):
        self.driver.find_element(*self.driver_comment).send_keys(data.message_for_driver)

    def add_blanket_handkerchiefs(self):
        self.driver.find_element(*self.blanket_handkerchiefs).click()

    def add_icecream(self):
        self.driver.find_element(*self.icecream_counter).click()
        self.driver.find_element(*self.icecream_counter).click()

    def click_taxi_button(self):
        self.driver.find_element(*self.get_taxi_button).click()
        #helpers.wait_elements(self.driver, self.driver_img, 60)
        #WebDriverWait(self.driver, 60).until(expected_conditions.presence_of_element_located(self.driver_img))