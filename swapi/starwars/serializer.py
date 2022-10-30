from starwars.models import Film, Planet
from rest_framework import status, serializers


class FilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = ['film_id', 'user', 'is_favourite']

    def validate(self):
        pass