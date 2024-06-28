import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from UrbanRoutesPage import UrbanRoutesPage

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        # from selenium.webdriver import DesiredCapabilities
        #capabilities = DesiredCapabilities.CHROME
        #capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        #cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

        # desired_capabilities ya no es soportado por selenium
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.maximize_window()  # Modo de pantalla completa


    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_taxi_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_order_taxi_button()
        assert self.driver.find_element(*routes_page.confort_fee_button).get_property('alt') == "Comfort"

    def test_confort_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_confort_fee_button()
        element_showed = self.driver.find_element(By.XPATH,"//*[contains(text(), 'Manta y pañuelos')]")
        assert element_showed.get_attribute("class") == "r-sw-label"

    def test_fill_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.fill_phone_fild()
        assert self.driver.find_element(*routes_page.phone_field).text == data.phone_number


    def test_add_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
    #se cambia el nombre de la función según lo indicado
        routes_page.add_credit_card()
        assert self.driver.find_element(*routes_page.card_img).get_property('alt') == "card"

    def test_add_driver_comment(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_driver_comment()
        assert self.driver.find_element(*routes_page.driver_comment).get_property("value") == data.message_for_driver

    def test_add_blanket_handkerchiefs(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_blanket_handkerchiefs()
        assert self.driver.find_element(*routes_page.blanket_handkerchiefs_input).is_selected() == True

    def test_add_icecream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_icecream()
        assert self.driver.find_element(*routes_page.icecream_counter_value).text == '2'

    def test_click_taxi_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_taxi_button()
        assert self.driver.find_element(*routes_page.driver_img).get_property('alt') == "close"


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
