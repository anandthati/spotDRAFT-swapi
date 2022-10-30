from django.conf import settings
import requests
import json
from starwars.models import Film, Planet
from django.contrib.auth.models import User


def get_swapi_data(model, id=None):
    url = settings.SWAPI_URL[model]
    if id:
        url = url + f"{id}/"
    response = requests.get(url)
    if response.status_code == 404:
        return False
    return json.loads(response.content)


def format_results(arr, user, model):
    for element in arr:
        element_id = int(element["url"].split("/")[-2])
        if model == "Film":
            film = Film.objects.filter(user=user, film_id=element_id).first()
            if film:
                element["is_favourite"] = film.is_favourite
                element["custom_title"] = film.custom_title
        elif model == "Planet":
            planet = Planet.objects.filter(user=user, planet_id=element_id).first()
            if planet:
                element["is_favourite"] = planet.is_favourite
                element["custom_name"] = planet.custom_name
    return arr

