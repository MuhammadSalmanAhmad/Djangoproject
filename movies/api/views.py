"""
IN this python script we had created API view for our project
"""
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from movies.api.serializers import MovieSerializer
from movies.models import Movie
from rest_framework import status

class MovieViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing ,retrieving,editing,creating and deleting Movie records.
    """
    def list(self, request):
        """
        This function shows list of all records
        """
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk):
        """
        this function is used to retrieve a specific record through objects ID
        """
        try:
            movie=Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(Http404)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def create(self, request):
        """
        this function is used to create a model instance in database
        """
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self,request, pk):
        """
        THIS FUNCTION IS USED TO DELETE A SPECIFIC RECORD
        """
        object=Movie.objects.get(pk=pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        """
        this Function is used to update a model instance with new record
        """
        movieinstance=Movie.objects.get(pk=pk)
        serializer=MovieSerializer(movieinstance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
