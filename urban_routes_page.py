from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.XPATH, "//button[contains(text(), 'Pedir un taxi')]")


    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        # Esperar a que el campo "from" esté presente en el DOM
        from_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.from_field)
        )
        # Limpiar el campo por si tiene texto previo
        from_input.clear()
        # Escribir la nueva dirección
        from_input.send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def click_request_taxi(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.request_taxi_button)
        ).click()
