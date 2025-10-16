# Python - Desde cualquier PC
import requests

API_BASE = 'http://192.168.1.20:8090/api'

# Obtener datos
response = requests.get(f'{API_BASE}/collections/estados/records')
estados = response.json()

# Filtrar datos específicos
response = requests.get(f'{API_BASE}/collections/api_data/records?filter=api_name="comercio_internacional_neto"')
datos = response.json()