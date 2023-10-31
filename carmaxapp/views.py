from django.shortcuts import render
from django.http import HttpResponse

# creating function to meet my request
def index(request):
    return HttpResponse('<h1>Seja Bem Vindo ao Carmax</h1>')