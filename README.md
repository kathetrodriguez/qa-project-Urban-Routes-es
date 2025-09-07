🚕 Urban Routes – Proyecto de Pruebas Automatizadas

Este proyecto contiene un conjunto de pruebas automáticas que validan cómo funciona la aplicación web Urban Routes, desde el momento en que un usuario pide un taxi hasta que se confirma el conductor asignado.

El objetivo es simular la experiencia de un cliente real y verificar que todas las funciones clave de la app funcionan correctamente.

🎯 Objetivos del Proyecto

General: Garantizar que la aplicación Urban Routes permita pedir un taxi sin errores y con una experiencia fluida para el usuario.

Específicos:

Validar que se puedan ingresar direcciones y elegir un tipo de servicio (ejemplo: tarifa Comfort).

Verificar el proceso de agregar y confirmar una tarjeta de crédito.

Confirmar que los servicios adicionales (manta, pañuelos, helados) se soliciten correctamente.

Asegurar que la app muestre la información del conductor una vez asignado.

📂 Estructura del Proyecto

data.py → Datos de entrada usados en las pruebas.

test_urban_routes.py → Archivo principal con las pruebas.

urban_routes_page.py → Implementación del Page Object Model (estructura que organiza las pruebas).

phone_code.py → Función para simular el código de confirmación al agregar una tarjeta.

README.md → Este documento explicativo.

✅ Funcionalidades Probadas

Las pruebas simulan todo el proceso que haría un usuario real:

Configurar dirección de inicio y destino.

Seleccionar la tarifa Comfort.

Ingresar número de teléfono.

Agregar tarjeta de crédito y confirmar con código.

Escribir un mensaje para el conductor.

Solicitar servicios adicionales (manta, pañuelos, helados).

Confirmar el viaje.

Verificar que aparece la información del conductor asignado.

🚀 Cómo Ejecutar las Pruebas

Clonar el repositorio:

git clone https://github.com/tu_usuario/urban-routes.git  
cd urban-routes


Instalar dependencias:

pip install -r requirements.txt


Ejecutar las pruebas:

pytest main.py

🛠 Requisitos

Python 3.8+

Selenium

Pytest

WebDriver (ChromeDriver o GeckoDriver, según tu navegador)

✍️ Autor

Proyecto desarrollado por Katherine Torres Rodríguez.
