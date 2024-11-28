from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def captain(request):
    return HttpResponse('<h1>Ruturaj is the captain of the csk</h1>')
def vicecaptain(request):
    return HttpResponse('<h1>jadejais the vicecaptain of the csk</h1>')