from django.shortcuts import render
from django.http import HttpResponse
from .models import Employees, Offense, Cameras
import random
import pickle

def get_offences() -> list:
    data = [[], []]
    offenses = Offense.objects.all()
    for i in range(7):
        week = offenses.filter(offense_date__week_day=i)
        data[0].append(week.filter(type_offense='В маске').count())
        data[1].append(week.exclude(type_offense='В маске').count())
    return data

def get_offenses_persent() ->list:
    data = []
    types = ['В маске', 'Без маски', 'В неправильно надетой маске']
    offenses = Offense.objects.all()
    off_count = offenses.count()
    for t in range(len(types)):
        element = []
        element.append(types[t])
        print(offenses.filter(type_offense=types[t]).count())
        element.append(offenses.filter(type_offense=types[t]).count() / off_count * 100)
        data.append(element)
    print(data)
    return data

def index(request):
    top_employees = Employees.objects.order_by('number_of_offenses')[:10]
    index = random.randint(0, 3)
    videos = [
        "static/webapp/videos/Baiden.mp4",
        "static/webapp/videos/Trump.mp4",
        "static/webapp/videos/Putin.mp4",
        "static/webapp/videos/Putin2.mp4"
        ]
    video = videos[index]

    data = get_offences()
    data_persent = get_offenses_persent

    return render(request, 'main.html', {'top_employees':top_employees, 'video':video, 'data':data, 'data_persent': data_persent})
