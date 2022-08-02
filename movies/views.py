from django.http import HttpRequest,HttpResponse
from django.shortcuts import render

# Create your views here.
def get(request):
    return HttpResponse("welcome you are at homepage")