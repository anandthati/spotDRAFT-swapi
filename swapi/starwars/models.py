from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    edited = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True

class Film(BaseModel):
    custom_title = models.CharField(max_length=255, default="")
    film_id = models.IntegerField()
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.custom_title
    
    class Meta:
        db_table = 'film'


class Planet(BaseModel):
    custom_name = models.CharField(max_length=100, default="")
    planet_id = models.IntegerField()
    is_favourite = models.BooleanField(default=False)
    
    def __str__(self):
        return self.custom_name

    class Meta:
        db_table = 'planet'
