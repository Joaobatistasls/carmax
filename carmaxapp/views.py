from django.shortcuts import render

# creating function to meet my request
def index(request):
    # creating variable to store car models
    car = {
        1:'Gol',
        2: 'Fiat',
        3: 'Ford'
    }
    #creating variable car data
    dates = {
        'car_models': car
    }
    # using render to render my page
    return render(request, 'index.html', dates)

# creating my route register
def registercar(request):
    return render(request, 'register.html')

# creating my route car
def car(request):
    return render(request, 'car.html')