from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def captain(request):
    return HttpResponse('<h1>hardik pandya is captain of mi</h1>')
def vicecaptain(request):
    return HttpResponse('<h1>jasprit bumrah is the vice captain of mi</h1>')