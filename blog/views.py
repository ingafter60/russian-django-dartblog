# blog/views
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Home page</h1>')