"""
Utilidades para pruebas de API
"""
import requests


class APIClient:
    """Cliente base para interactuar con APIs"""

    def __init__(self, base_url):
        """
        Inicializa el cliente de API
        :param base_url: URL base de la API
        """
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint, params=None, headers=None):
        """
        Realiza una petición GET
        :param endpoint: Endpoint de la API
        :param params: Parámetros de consulta
        :param headers: Headers adicionales
        :return: Response object
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, params=params, headers=headers)
        return response

    def post(self, endpoint, data=None, json=None, headers=None):
        """
        Realiza una petición POST
        :param endpoint: Endpoint de la API
        :param data: Datos del formulario
        :param json: Datos en formato JSON
        :param headers: Headers adicionales
        :return: Response object
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, data=data, json=json, headers=headers)
        return response

    def put(self, endpoint, data=None, json=None, headers=None):
        """
        Realiza una petición PUT
        :param endpoint: Endpoint de la API
        :param data: Datos del formulario
        :param json: Datos en formato JSON
        :param headers: Headers adicionales
        :return: Response object
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.put(url, data=data, json=json, headers=headers)
        return response

    def patch(self, endpoint, data=None, json=None, headers=None):
        """
        Realiza una petición PATCH
        :param endpoint: Endpoint de la API
        :param data: Datos del formulario
        :param json: Datos en formato JSON
        :param headers: Headers adicionales
        :return: Response object
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.patch(url, data=data, json=json, headers=headers)
        return response

    def delete(self, endpoint, headers=None):
        """
        Realiza una petición DELETE
        :param endpoint: Endpoint de la API
        :param headers: Headers adicionales
        :return: Response object
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url, headers=headers)
        return response

    def validate_status_code(self, response, expected_status):
        """
        Valida el código de estado de la respuesta
        :param response: Objeto response
        :param expected_status: Código de estado esperado
        """
        assert response.status_code == expected_status, \
            f"Expected status code {expected_status}, but got {response.status_code}"

    def validate_json_keys(self, json_data, expected_keys):
        """
        Valida que el JSON tenga las claves esperadas
        :param json_data: Datos JSON
        :param expected_keys: Lista de claves esperadas
        """
        for key in expected_keys:
            assert key in json_data, f"Key '{key}' not found in response"
