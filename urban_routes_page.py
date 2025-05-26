from data import phone_number, card_number, card_code, message_for_driver, ice_cream_count
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.XPATH, "//button[contains(text(), 'Pedir un taxi')]")
    comfort_tariff_button = (By.XPATH,
                             "//div[contains(@class, 'tcard-title') and text()='Comfort']/parent::div")
    # Teléfono
    add_phone_number_button = (By.CLASS_NAME, "np-button")
    phone_input = (By.CSS_SELECTOR, 'input#phone[name="phone"]')
    phone_submit_button = (By.XPATH,"//button[contains(text(),'Siguiente')]")
    # Código SMS
    code_input = (By.ID, "code")
    confirm_code_button = (By.XPATH, "//button[contains(text(),'Confirmar')]")
    # Agregar tarjeta
    select_type_of_payment_button = (By.XPATH, "//div[contains(@class, 'pp-button') and .//div[text()='Método de pago']]")
    add_card_button = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
    card_number_input = (By.CSS_SELECTOR, 'input[name="number"]')
    card_code_input = (By.CSS_SELECTOR, 'input.card-input#code')
    link_card_button = (By.XPATH, "//button[contains(text(),'Agregar')]")
    close_button_add_payment_method = (By.XPATH, "(//div[contains(@class, 'payment-picker') and contains(@class, 'open')]//button[contains(@class, 'close-button') and contains(@class, 'section-close')])[1]")
    #Mensaje al conductor
    driver_message_button = (By.CSS_SELECTOR, "label[for='comment']")
    #Boton selector de mantas y pañuelos
    switch_blankest_and_handkerchiefs = (By.XPATH,
                                         "//div[contains(text(), 'Manta y pañuelos')]/following-sibling::div//span[contains(@class, 'slider') and contains(@class, 'round')]"
                                         )
    #Boton para pedir los helados
    add_ice_cream_button = (By.XPATH, "(//div[@class='r-counter-container']//div[@class='counter-plus'])[1]")
    #Boton para pedir el taxi
    search_a_taxi = (By.CLASS_NAME, "smart-button-wrapper")
    #modal
    confirmation_information_driver = (By.XPATH, '//*[contains(text(), "El conductor llegará en")]')




    def __init__(self, driver):
        self.driver = driver
        self.phone_number = phone_number
        self.card_number = card_number
        self.card_code = card_code
        self.message_for_driver = message_for_driver
        self.ice_cream_count = ice_cream_count

    def set_from(self, from_address):
        from_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.from_field)
        )
        from_input.clear()
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

    def select_comfort_tariff(self):
        # Esperar a que el modal de tarifas esté visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.comfort_tariff_button)
        )
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.comfort_tariff_button)
        ).click()

    def click_phone_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_phone_number_button)
        ).click()

    def set_phone_number(self, name):
        phone_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.phone_input))
        phone_field.clear()
        phone_field.send_keys(phone_number)

    def submit_phone_number(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.phone_submit_button)
        ).click()

    def enter_verification_code(self, code):
        code_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.code_input)
        )
        code_field.clear()
        code_field.send_keys(code)

    def confirm_code(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.confirm_code_button)
        ).click()

    def is_phone_number_displayed(self, phone_number):
        phone_element = self.driver.find_element(By.XPATH, f"//div[@class='np-text' and text()='{phone_number}']")
        return phone_element.is_displayed()

    def add_credit_card(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.select_type_of_payment_button)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_card_button)
        ).click()

        number_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.card_number_input)
        )
        number_input.click()
        number_input.send_keys(self.card_number)
        code_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.card_code_input)
        )
        code_input.click()
        code_input.send_keys(self.card_code)
        code_input.send_keys(Keys.TAB)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.link_card_button)
        ).click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.close_button_add_payment_method)).click()

    def driver_message(self):
        message_input = self.driver.find_element(By.ID, "comment")
        message_input.send_keys(message_for_driver)

    def ask_blanket_and_handkerchiefs(self):
        switch = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.switch_blankest_and_handkerchiefs)
        )
        switch.click()

    def order_ice_cream(self):
        for _ in range(self.ice_cream_count):
            add_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.add_ice_cream_button)
            )
            add_button.click()
            WebDriverWait(self.driver, 10).until(
                lambda driver: int(driver.find_element(By.XPATH,
                                                       "(//div[@class='r-counter-container']//div[@class='counter-value'])[1]").text) == _ + 1
            )

    def book_a_taxi(self):
        self.driver.find_element(*UrbanRoutesPage.search_a_taxi).click()

    def modal_to_search_taxi_appears(self):
        self.driver.find_element(*self.confirmation_information_driver)
