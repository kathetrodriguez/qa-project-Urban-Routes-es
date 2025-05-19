import data
import pytest
from urban_routes_page import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # Crear opciones de Chrome
        options = Options()

        # Crear capacidades base
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}

        # Asignar capacidades a opciones
        options.capabilities.update(capabilities)

        # Crear driver con opciones
        cls.driver = webdriver.Chrome(options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_request_taxi(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        routes_page.click_request_taxi()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
