from django.shortcuts import render
from django.http import HttpResponse
from .models import Employees, Offense, Cameras

def index(request):
    offenses = Offense.objects.all()
    top_employees = Employees.objects.order_by('number_of_offenses')[:10]
    

    return render(request, 'main.html', {'top_employees':top_employees})
