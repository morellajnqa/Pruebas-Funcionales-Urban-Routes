[![Tripleten](https://id.tripleten.com/resources/2jrb4/login/practicum-keycloakify/build/favicon-32x32.png)]()
# Comprobar la funcionalidad de Urban Routes
#### Por: Morella Jiménez 

## Descripción del proyecto
Este proyecto se desarrollo para probar la aplicación Urban Routes, de forma automatizada, específicamente para probar la funcionalidad de solicitar un taxi, con las siguientes características:

- Se incluye los datos de origen y destino suministradas desde el archivo data.py
- Se selecciona la tarifa "Confort"
- Se incluye un número telefónico suministrado desde el archivo data.py
- Se incluyen los datos del método de pago con tarjeta de crédito desde el archivo data.py
- Se incluye un comentario para el conductor.
- Se le solicitan dos servicios adicionales como "Mantas y Helado".


## Requisitos

- python3
- librerias 
  - sellenium
  - pytest
- Ajustes en data.py
  - urban_routes_url debe tener una url válida

## Archivos

- data.py: aquí se almacenan los datos necesarios para completar las pruebas.
- main.py: aquí se encuentra el código de automatización junto a los casos de pruebas.
- UrbanRoutesPage.py: Contiene la pagina para la clase del webdriver para selenium 
- helpers.py: Tiene unas funciones de espera y de obtención de codigo telefónico.

## Ejecución del programa
```sh
pytest .\main.py
