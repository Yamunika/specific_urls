from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def captain(request):
    return HttpResponse('<h1>virat kohli is the captain of rcb</h1>')
def nextcaptain(request):
    return HttpResponse('<h1>faf du plessis is the next captain</h1>')