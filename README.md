# Pre Entrega Automation Testing - Vicente Héctor Páez
 
## 📌 Propósito del proyecto
 
Este proyecto tiene como objetivo automatizar pruebas funcionales sobre el sitio web SauceDemo utilizando Selenium WebDriver y Pytest.
 
Las pruebas implementadas verifican:
 
- Inicio de sesión exitoso.
- Visualización del inventario de productos.
- Validación de productos visibles.
- Validación de nombre y precio de productos.
- Verificación de elementos de interfaz.
- Agregado de productos al carrito.
- Verificación del contador del carrito.
- Navegación a la página del carrito.
- Validación de productos agregados al carrito.
 
---
 
## 🛠 Tecnologías utilizadas
 
- Python 3
- Selenium WebDriver
- Pytest
- WebDriver Manager
- Google Chrome
- Git
- GitHub
 
---
 
## 📦 Instalación de dependencias
 
Clonar el repositorio:
 
```bash
git clone https://github.com/vicentehectorpaez/pre-entrega-automation-testing-vicente-hector-paez.git
```
 
Ingresar al directorio del proyecto:
 
```bash
cd pre-entrega-automation-testing-vicente-hector-paez
```
 
Instalar dependencias:
 
```bash
pip install selenium
pip install pytest
pip install webdriver-manager
pip install pytest-html
```
 
---
 
## ▶️ Ejecución de las pruebas
 
Ejecutar todas las pruebas:
 
```bash
py -m pytest
```
 
Ejecutar con salida detallada:
 
```bash
py -m pytest -v
```
 
Generar reporte HTML:
 
```bash
py -m pytest --html=reports/reporte_preentrega.html --self-contained-html
```
 
---
 
## ✅ Casos de prueba automatizados
 
- test_01_login
- test_02_verificar_inventario
- test_03_productos_visibles
- test_04_nombre_precio_producto
- test_05_validar_interfaz
- test_06_añadir_producto_al_carrito
- test_07_verificar_contador_carrito
- test_08_navegar_carrito
- test_09_comprobar_producto_en_carrito
 
---
 
## 📁 Estructura del proyecto
 
```text
pre-entrega-automation-testing-vicente-hector-paez
│
├── conftest.py
├── README.md
│
├── tests
│ └── test_saucedemo.py
│
└── utils
└── helpers.py
```
 
---
 
## 👨‍💻 Autor
 
Vicente Héctor Páez
