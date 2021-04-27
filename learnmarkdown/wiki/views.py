from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello(request):
    return HttpResponse("<h1>Hello, Rishi Baby.. Welcome to Django!</h1>")