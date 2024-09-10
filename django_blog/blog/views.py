from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("eyobed is comming")

# Create your views here.
