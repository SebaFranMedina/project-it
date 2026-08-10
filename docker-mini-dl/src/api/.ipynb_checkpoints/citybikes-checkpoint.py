import requests


def get_networks():
    url = "https://api.citybik.es/v2/networks"

    response = requests.get(url, timeout=30)

    response.raise_for_status()

    return response.json()