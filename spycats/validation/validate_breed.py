import requests

API_BREEDS = 'https://api.thecatapi.com/v1/breeds/search'


def check_breed(value):
    try:
        response = requests.get(API_BREEDS, {"name": value.title()})
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Cats API request error: {e}")
        return None
