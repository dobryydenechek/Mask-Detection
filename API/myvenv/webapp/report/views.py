from django.shortcuts import render
from main.models import Employees, Offense, Cameras

def report_home(request):
    offenses = Offense.objects.all()
    
    return render(request, 'report.html', {'offenses':offenses})

