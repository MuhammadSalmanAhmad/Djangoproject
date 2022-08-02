from django import urls
from django.urls import include, path
from movies.api.views import MovieViewSet
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register(r'movies',MovieViewSet,'MOVIES')
urlpatterns = [
    
    path('',include(router.urls))
]