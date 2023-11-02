from django.shortcuts import render

# creating function to meet my request
def index(request):
    # using render to render my page
    return render(request, 'index.html')

# creating my route register
def register(request):
    return render(request, 'register.html')

# creating my route car
def car(request):
    return render(request, 'car.html')