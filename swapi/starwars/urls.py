from django.urls import path
from starwars.views import (
    HealthCheck, ListMovies, MovieDetails, 
    ListPlanets, PlanetDetails, FavouriteMovie,
    FavouritePlanet, FavouriteMovie
)
from django.conf.urls import include


movie_urls = [
    path('', ListMovies.as_view(), name="list-films"),
    path('<int:film_id>/', MovieDetails.as_view(), name="get-film"),
    path('<int:film_id>/favourite/', FavouriteMovie.as_view(), name="favourite-film"),
]

planet_urls = [
    path('', ListPlanets.as_view(), name="list-planets"),
    path('<int:planet_id>/', PlanetDetails.as_view(), name="get-planet"),
    path('<int:planet_id>/favourite/', FavouritePlanet.as_view(), name="favourite-planet"),
]

urlpatterns = [
    path('v1/health_check/', HealthCheck.as_view(), name="health-check"),
    path('v1/films/', include((movie_urls, "movie_urls"))),
    path('v1/planets/', include((planet_urls, "planet_urls"))),
]
