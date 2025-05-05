# Ex02 Django ORM Web Application
## Date: 05-05-2025

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Movie,MovieAdmin

admin.site.register(Movie,MovieAdmin)

models.py

from django.db import models
from django.contrib import admin

class Movie(models.Model):
    title=models.CharField(max_length=150,primary_key='True')
    genre=models.CharField(max_length=100)
    release_date=models.DateField()
    rating=models.IntegerField()
    
class MovieAdmin(admin.ModelAdmin):
    list_display=('title','genre','release_date','rating')

```


## OUTPUT
![Screenshot 2025-05-05 110755](https://github.com/user-attachments/assets/33f7c008-4a80-400f-85d1-c37aa75c0e00)
![Screenshot 2025-05-05 110731](https://github.com/user-attachments/assets/49dc30fd-a209-4dab-be4b-6d39fe06cd90)


## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
