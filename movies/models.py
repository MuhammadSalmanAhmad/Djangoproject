"""
python script to define database models 
"""
from django.db import models
# Create your models here.
class Movie(models.Model):
    """
    class that defines our model : Movie and its attributes/fields
    """
    movie_title = models.CharField(max_length=50)
    director=models.TextField(max_length=100)
    actor=models.TextField(max_length=100)
    music_omposer=models.TextField(max_length=100,default= '')
    