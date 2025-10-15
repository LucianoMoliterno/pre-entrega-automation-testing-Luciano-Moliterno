import pytest
from py.xml import html
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def pytest_configure(config):
    """Configuración de marcadores personalizados"""
    config.addinivalue_line(
        "markers", "smoke: Marca los tests críticos de tipo smoke"
    )


def pytest_html_report_title(report):
    report.title = "Reporte de Pruebas - Saucedemo Automation (POM)"


def pytest_html_results_table_header(cells):
    cells.insert(2, html.th("Description"))
    cells.insert(1, html.th("Time", class_="sortable time", col="time"))


def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.datetime.now(), class_="col-time"))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)


@pytest.fixture
def driver():
    """Fixture para configurar el WebDriver"""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # Ruta del ChromeDriver
    CHROME_DRIVER_PATH = r"C:\chromedriver\chromedriver.exe"

    print("\n[OK] Iniciando ChromeDriver...")
    # Inicializar el WebDriver
    driver = webdriver.Chrome(
        service=Service(CHROME_DRIVER_PATH),
        options=chrome_options
    )
    driver.implicitly_wait(10)

    # Navegar a la página inicial
    print("[OK] Navegando a saucedemo.com...")
    driver.get("https://www.saucedemo.com/")

    yield driver

    # Cleanup después de cada test
    print("\n[OK] Cerrando navegador...")
    driver.quit()
