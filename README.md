# 🚕 Urban Routes - Automated Testing Suite

Welcome! This repository contains an end-to-end automated testing project for the **Urban Routes** web app — GITfocused on browser automation with Selenium.

These tests simulate a full taxi ordering experience, including UI interactions, service selection, credit card form handling, and driver assignment validation.

---
urban-routes/
├── data.py # Test data and helper utilities
├── test_urban_routes.py # Main test suite
├── urban_routes_page.py # Page Object Model (POM) for Urban Routes
├── phone_code.py # Code interception utility for phone verification
└── README.md # This file

## ✅ Features Covered

This test suite walks through a real-world user scenario:

- From set pickup and destination addresses to  observe transition from search state to trip details.

🛠 Requirements

Python 3.8+

Selenium

Pytest

Happy testing! 💻🧪
---
# 🚕 Urban Routes - Pruebas Automatizadas 

## 📁 Project Structure

Este repositorio contiene pruebas automatizadas para la aplicación Urban Routes. Las pruebas están diseñadas usando Selenium y validan el proceso completo de solicitud de un taxi, incluyendo la selección de servicios adicionales y la verificación del conductor asignado.

📂 Estructura del Repositorio

urban-routes/
│
├── data.py             # Contiene datos de entrada y utilidades para las pruebas
├── test_urban_routes.py             # Archivo principal con las pruebas automatizadas
├── urban_routes_page.py   # Page Object Model para la página Urban Routes
├── phone_code.py    # Herramienta necesaria para la ejecución
└── README.md           # Este archivo

🚕 Funcionalidad Probada

Las pruebas cubren el proceso completo de pedir un taxi en la app Urban Routes, incluyendo:

Configurar la dirección.

Seleccionar la tarifa Comfort.

Ingresar el número de teléfono.

Agregar una tarjeta de crédito:

Llenar campos de tarjeta.

Simular pérdida de enfoque en el campo CVV para activar el botón de enlace.

Utilizar la función retrieve_phone_code() para interceptar el código de confirmación.

Escribir un mensaje para el conductor.

Solicitar servicios adicionales:

Manta y pañuelos.

2 helados.

Confirmar la solicitud del taxi.

Verificar la aparición del conductor:

Esperar la transición del modal de búsqueda a la información del viaje.

🚀 Cómo Ejecutar

Clona este repositorio:

git clone https://github.com/tu_usuario/urban-routes.git
cd urban-routes

Instala las dependencias:

pip install -r requirements.txt

Ejecuta las pruebas:

pytest main.py

🛠 Requisitos

Python 3.8+

Selenium

Pytest

Webdriver (ChromeDriver, GeckoDriver, etc., según el navegador)

📌 Notas

Asegúrate de que el navegador y el WebDriver estén correctamente instalados y configurados.

La función retrieve_phone_code() está diseñada para interceptar el código de confirmación necesario al agregar una tarjeta de crédito.

En algunos elementos del formulario (como el CVV), es necesario simular el cambio de enfoque con TAB o un clic para activar botones relacionados.