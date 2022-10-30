from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from django.db import connections
from django.db.utils import OperationalError
from starwars.utils import get_swapi_data, format_results
from starwars.models import Film, Planet
from django.contrib.auth.models import User


class HealthCheck(APIView):
    def get(self, request):
        # Checking DB
        db_conn = connections['default']
        try:
            c = db_conn.cursor()
        except OperationalError:
            return Response(status=status.HTTP_403_FORBIDDEN)

        return Response(status=status.HTTP_200_OK)


class ListMovies(APIView):
    def get(self, request):
        search_term = request.GET.get("search")
        if search_term:
            movies = dict()
            film = Film.objects.filter(custom_title__icontains=search_term).first()
            film_id = film.film_id if film else None
            movies["results"] = [get_swapi_data("films", film_id)]
        else:
            movies = get_swapi_data("films")
        user_id = request.GET.get("user")
        user = User.objects.filter(id=user_id).first()
        if not movies:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if user:
            movies = format_results(movies["results"], user, "Film")
        return Response(movies, status=status.HTTP_200_OK)


class MovieDetails(APIView):
    def get(self, request, film_id):
        movies = get_swapi_data("films", film_id)
        user_id = request.GET.get("user")
        if not movies:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user = User.objects.filter(id=user_id).first()
        if user:
            movies = format_results([movies], user, "Film")
        return Response(movies, status=status.HTTP_200_OK)


class FavouriteMovie(APIView):

    def post(self, request, film_id):
        film = get_swapi_data("films", film_id)
        if not film:
            return Response({"ERROR": "Requested film not found!"}, status=status.HTTP_404_NOT_FOUND)
        user_id = request.data.get('user_id')
        custom_title = request.data.get('custom_title')
        is_favourite = request.data.get('is_favourite')
        if not User.objects.filter(id=user_id).exists():
            return Response({"ERROR": "Requested user not found!"}, status=status.HTTP_404_NOT_FOUND)
        film, created = Film.objects.get_or_create(film_id=film_id, user=User.objects.get(id=user_id))
        if is_favourite is not None:
            film.is_favourite = is_favourite 
        if custom_title:
            film.custom_title = custom_title 
        film.save()
        return Response(status=status.HTTP_200_OK)


class ListPlanets(APIView):
    def get(self, request):
        search_term = request.GET.get("search")
        if search_term:
            planets = dict()
            planet = Planet.objects.filter(custom_name__icontains=search_term).first()
            planet_id = planet.planet_id if planet else None
            planets["results"] = [get_swapi_data("planets", planet_id)]
        else:
            planets = get_swapi_data("planets")
        if not planets:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user_id = request.GET.get("user")
        user = User.objects.filter(id=user_id).first()
        if user:
            planets = format_results(planets["results"], user, "Planet")
        return Response(planets, status=status.HTTP_200_OK)


class PlanetDetails(APIView):
    def get(self, request, planet_id):
        planets = get_swapi_data("planets", planet_id)
        if not planets:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user_id = request.GET.get("user")
        user = User.objects.filter(id=user_id).first()
        if user:
            planets = format_results([planets], user, "Planet")
        return Response(planets, status=status.HTTP_200_OK)

    
class FavouritePlanet(APIView):

    def post(self, request, planet_id):
        planet = get_swapi_data("planets", planet_id)
        if not planet:
            return Response({"ERROR": "Requested planet not found!"}, status=status.HTTP_404_NOT_FOUND)
        user_id = request.data.get('user_id')
        custom_name = request.data.get('custom_name')
        is_favourite = request.data.get('is_favourite')
        if not User.objects.filter(id=user_id).exists():
            return Response({"ERROR": "Requested user not found!"}, status=status.HTTP_404_NOT_FOUND)
        planet, created = Planet.objects.get_or_create(planet_id=planet_id, user=User.objects.get(id=user_id))
        if is_favourite is not None:
            planet.is_favourite = is_favourite 
        if custom_name:
            planet.custom_name = custom_name 
        planet.save()
        return Response(status=status.HTTP_200_OK)


