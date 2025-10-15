# Automation Testing - Saucedemo.com (Page Object Model)

## Propósito del Proyecto
Este proyecto automatiza pruebas de funcionalidad para la aplicación web saucedemo.com aplicando el **patrón Page Object Model (POM)**, cubriendo:
- Login con credenciales válidas e inválidas
- Navegación y verificación del catálogo de productos
- Agregar y remover productos del carrito de compras

## Estructura del Proyecto
```
├── pages/                     # Page Objects (POM)
│   ├── __init__.py
│   ├── base_page.py          # Clase base con métodos comunes
│   ├── login_page.py         # Page Object para Login
│   ├── inventory_page.py     # Page Object para Inventario
│   └── cart_page.py          # Page Object para Carrito
├── tests/                     # Tests refactorizados
│   ├── test_login.py         # Tests de login
│   ├── test_catalogo.py      # Tests de catálogo
│   └── test_carrito.py       # Tests de carrito
├── screenshots/               # Capturas de pantalla
├── reports/                   # Reportes HTML
├── conftest.py               # Configuración de pytest y fixture driver()
└── requirements.txt          # Dependencias
```

## Tecnologías Utilizadas
- **Python 3.11** - Lenguaje de programación
- **Selenium WebDriver** - Automatización de navegador
- **Pytest** - Framework de testing
- **Page Object Model (POM)** - Patrón de diseño para tests
- **pytest-html** - Generación de reportes HTML

## Instalación de Dependencias

### Prerrequisitos
- Python 3.11 o superior
- Google Chrome instalado
- ChromeDriver en C:\chromedriver\
- Git

### Instalación
1. **Clonar el repositorio:**
```bash
git clone https://github.com/tu-usuario/pre-entrega-automation-testing.git
cd pre-entrega-automation-testing
```

2. **Crear entorno virtual (recomendado):**
```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
```

3. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

## Ejecución de Pruebas

### Ejecutar TODOS los tests con verbose
```bash
pytest -v
```

### Ejecutar tests SMOKE (críticos)
```bash
pytest -m smoke -v
```

### Ejecutar tests SMOKE con reporte HTML
```bash
pytest -m smoke --html=preentrega_pom.html --self-contained-html
```

### Ejecutar tests por módulo
```bash
# Solo tests de login
pytest tests/test_login.py -v

# Solo tests de catálogo
pytest tests/test_catalogo.py -v

# Solo tests de carrito
pytest tests/test_carrito.py -v
```

### Ejecutar un test específico
```bash
pytest tests/test_login.py::test_login_exitoso -v
```

### Generar reporte HTML completo
```bash
pytest -v --html=reports/reporte.html --self-contained-html
```

## Marcadores (Markers)
Los tests están marcados con `@pytest.mark.smoke` para identificar los casos críticos:
- `@pytest.mark.smoke` - Tests críticos que deben pasar siempre

## Page Objects
El proyecto implementa el patrón **Page Object Model (POM)** con las siguientes clases:

### BasePage
Clase base con métodos comunes:
- `find_element()` - Buscar elemento
- `click()` - Hacer clic
- `send_keys()` - Enviar texto
- `take_screenshot()` - Capturar pantalla

### LoginPage
Locators y métodos para la página de login:
- `login(username, password)` - Realizar login completo
- `is_error_message_displayed()` - Verificar errores

### InventoryPage
Locators y métodos para el catálogo:
- `get_products_count()` - Obtener cantidad de productos
- `add_product_to_cart()` - Agregar producto
- `get_cart_count()` - Obtener contador del carrito

### CartPage
Locators y métodos para el carrito:
- `get_cart_items_count()` - Obtener items en carrito
- `remove_item()` - Remover producto
- `click_checkout()` - Proceder al checkout

## Fixtures
### driver()
Fixture principal en `conftest.py` que:
- Configura ChromeDriver
- Inicializa el navegador
- Navega a la página inicial
- Limpia recursos al finalizar

## Tests Implementados

### test_login.py
- ✅ `test_login_exitoso` - Login con credenciales válidas (SMOKE)
- ✅ `test_login_usuario_bloqueado` - Usuario bloqueado (SMOKE)
- ✅ `test_login_credenciales_invalidas` - Credenciales inválidas

### test_catalogo.py
- ✅ `test_navegacion_catalogo` - Navegación del catálogo (SMOKE)
- ✅ `test_verificar_informacion_productos` - Info de productos (SMOKE)
- ✅ `test_validar_elementos_interfaz` - Elementos UI

### test_carrito.py
- ✅ `test_agregar_producto_carrito` - Agregar producto (SMOKE)
- ✅ `test_verificar_contenido_carrito` - Contenido del carrito (SMOKE)
- ✅ `test_agregar_multiples_productos` - Múltiples productos
- ✅ `test_remover_producto_carrito` - Remover producto

## Beneficios del POM
- ✅ **Mantenibilidad**: Los selectores están centralizados en los Page Objects
- ✅ **Reutilización**: Los métodos pueden ser usados por múltiples tests
- ✅ **Legibilidad**: Los tests son más claros y expresivos
- ✅ **Escalabilidad**: Fácil agregar nuevas páginas y tests

## Autor
Luciano Moliterno

## Licencia
Este proyecto es de uso educativo.
