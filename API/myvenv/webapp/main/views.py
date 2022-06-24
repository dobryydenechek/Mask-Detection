from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from .models import Employees, Offense, Cameras
import cv2
import numpy as np
import random
import pickle
import datetime
import base64
import io
import PIL.Image

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
        element.append(offenses.filter(type_offense=types[t]).count() / off_count * 100)
        data.append(element)
    return data

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


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

    if request.method == "POST":
        
        id_employee=int(request.FILES['photo'].name)
        
        employee = Employees.objects.filter(id_employee = id_employee)[0]

        offenses = Offense.objects.order_by('-offense_date')
        offendeDate = offenses.filter(id_employee=id_employee).values_list('offense_date')
        print(offendeDate)
        date_of_offence = offendeDate[0][0]
        print(date_of_offence)
        if ((date_of_offence - datetime.date.today()).days < 0):
            offense = Offense(id_employee=employee, photo_offense=request.FILES['photo'])
            offense.save()
        else:
            print("Too small difference")
        pass

    return render(request, 'main.html', {'top_employees':top_employees, 'video':video, 'data':data, 'data_persent': data_persent})
