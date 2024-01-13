from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def list(request):
    all_cars = models.Car.objects.all()
    context = {
        'all_cars': all_cars
    }
    return render(request, 'cars/list.html', context = context)

@csrf_exempt
def delete(request):
    if request.POST:
        car_id = request.POST['pk']
        try:
            car = models.Car.objects.get(id=car_id)
            car.delete()
            return redirect(reverse('cars:list'))
        except:
            print("Car not found")
            return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/delete.html')

# This decorator is used to allow POST request without csrf token
@csrf_exempt
def add(request):
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
        models.Car.objects.create(brand=brand, year=year)
        # If user submit a new car, redirect to the list page
        return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/add.html')
    