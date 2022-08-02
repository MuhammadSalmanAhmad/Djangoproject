"""
serializer to serialize our Model class :Movie
"""
from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    """
    meta class for defining our model and feilds to serialize
    """
    class Meta:
        model=Movie
        fields= '__all__'
