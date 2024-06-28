import data
import helpers
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
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

    def test_confort_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_confort_fee_button()

    def test_fill_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.fill_phone_fild()

    def test_add_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
    #se cambia el nombre de la función según lo indicado
        routes_page.add_credit_card()

    def test_add_driver_comment(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_driver_comment()

    def add_blanket_handkerchiefs(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_blanket_handkerchiefs()

    def add_icecream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_icecream()

    def click_taxi_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_taxi_button()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
