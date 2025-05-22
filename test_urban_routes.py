from phone_code import retrieve_phone_code
from  data import urban_routes_url, address_from, address_to, phone_number, message_for_driver
from urban_routes_page import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        # Configurar logging de performance correctamente
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.implicitly_wait(10)  # espera implícita útil para evitar fallos por carga lenta
        cls.driver.get(urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)

# Definir punto de partida y punto de llegada

    def test_set_route(self):
        self.routes_page.set_from(address_from)
        self.routes_page.set_to(address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

# Seleccionar la tarifa Comfort.

    def test_order_taxi_and_select_comfort_rate(self):
        self.routes_page.set_from(address_from)
        self.routes_page.set_to(address_to)
        self.routes_page.click_request_taxi()
        self.routes_page.select_comfort_tariff()

        comfort_tariff = self.driver.find_element(*self.routes_page.comfort_tariff_button)
        assert comfort_tariff.is_displayed()
        classes = comfort_tariff.get_attribute("class")
        assert "tcard" in classes and ("selected" in classes or "active" in classes)

# Rellenar el número de teléfono.

    def test_fill_phone_number(self):
        self.routes_page.set_from(address_from)
        self.routes_page.set_to(address_to)
        self.routes_page.click_request_taxi()
        self.routes_page.select_comfort_tariff()

        self.routes_page.click_phone_button()
        self.routes_page.set_phone_number(phone_number)

        phone_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.routes_page.phone_input))
        assert phone_number[-5:] in phone_field.get_attribute("value")

# Verificar Número de telefono

    def test_phone_verification(self):
        self.routes_page.set_from(address_from)
        self.routes_page.set_to(address_to)
        self.routes_page.click_request_taxi()
        self.routes_page.select_comfort_tariff()

        self.routes_page.click_phone_button()
        self.routes_page.set_phone_number(phone_number)
        self.routes_page.submit_phone_number()

        # Recuperar el código SMS desde los logs de red
        code = retrieve_phone_code(self.driver)
        self.routes_page.enter_verification_code(code)
        self.routes_page.confirm_code()

        assert self.routes_page.is_phone_number_displayed(
            "+1 123 123 12 12"), "El número de teléfono no se muestra correctamente en la pantalla."

# Agregar medio de mapo "tarjeta de credito"

    def test_add_credit_card(self):
        self.routes_page.set_from(address_from)
        self.routes_page.set_to(address_to)
        self.routes_page.click_request_taxi()
        self.routes_page.select_comfort_tariff()

        self.routes_page.click_phone_button()
        self.routes_page.set_phone_number(phone_number)
        self.routes_page.submit_phone_number()

        code = retrieve_phone_code(self.driver)
        self.routes_page.enter_verification_code(code)
        self.routes_page.confirm_code()

        self.routes_page.add_credit_card()

        payment_text = self.driver.find_element(By.CLASS_NAME, "pp-value-text").text
        assert "Tarjeta" in payment_text, "La tarjeta no se agregó correctamente"

# Escribir un mensaje para el controlador.
    def test_message_driver(self):
        self.routes_page.set_from(address_from)
        self.routes_page.set_to(address_to)
        self.routes_page.click_request_taxi()
        self.routes_page.select_comfort_tariff()

        self.routes_page.driver_message()

        message_input = self.driver.find_element(By.ID, "comment")
        assert message_input.get_attribute("value") == message_for_driver, \
            f"El mensaje no coincidió. Esperado: '{message_for_driver}', Actual: '{message_input.get_attribute('value')}'"

# Pedir una manta y pañuelos.
    def test_ask_for_blankets_and_handkerchiefs(self):
        self.routes_page.set_from(address_from)
        self.routes_page.set_to(address_to)
        self.routes_page.click_request_taxi()
        self.routes_page.select_comfort_tariff()
        self.routes_page.ask_blanket_and_handkerchiefs()

# Pedir 2 helados
    def test_order_two_ice_creams(self):
        self.routes_page.set_from(address_from)
        self.routes_page.set_to(address_to)
        self.routes_page.click_request_taxi()
        self.routes_page.select_comfort_tariff()

        self.routes_page.order_ice_cream()

        value = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "(//div[@class='r-counter-container']//div[@class='counter-value'])[1]"))
        ).text

        assert value == "2", f"Se esperaba 2 helados, pero se encontró: {value}"

# Llamar al taxi
    def test_call_taxi(self):
        self.routes_page.set_from(address_from)
        self.routes_page.set_to(address_to)
        self.routes_page.click_request_taxi()
        self.routes_page.select_comfort_tariff()
        self.routes_page.click_phone_button()
        self.routes_page.set_phone_number(phone_number)
        self.routes_page.submit_phone_number()
        code = retrieve_phone_code(self.driver)
        self.routes_page.enter_verification_code(code)
        self.routes_page.confirm_code()
        self.routes_page.add_credit_card()
        self.routes_page.driver_message()
        self.routes_page.ask_blanket_and_handkerchiefs()
        self.routes_page.order_ice_cream()
        self.routes_page.click_order_a_taxi()
        WebDriverWait(self.driver, 40).until(
            expected_conditions.visibility_of_element_located(self.routes_page.confirmation_information_driver)
        )
        assert self.driver.find_element(*self.routes_page.confirmation_information_driver).is_displayed()



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
