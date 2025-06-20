from django.db import models
from django.contrib import admin
class Movie(models.Model):
    title=models.CharField(max_length=100,primary_key=True)
    genre=models.CharField(max_length=50)
    release_date=models.DateField()
    rating=models.IntegerField()
class MovieAdmin(admin.ModelAdmin):
    list_display=('title','genre','release_date','rating')
# Create your models here.
