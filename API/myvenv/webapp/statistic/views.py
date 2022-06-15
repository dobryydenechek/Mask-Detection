from django.shortcuts import render
from main.models import Employees, Offense, Cameras

def get_offences_for_cam() -> list:
    data = [[], [], []]
    types = ['В маске', 'Без маски', 'В неправильно надетой маске']
    offenses = Offense.objects.all()
    cam_ids = Cameras.objects.order_by().values('id_camera').distinct()
    for t in range(len(types)):
        offenses_by_type = offenses.filter(type_offense=types[t])

        for id in cam_ids:
            data[t].append(offenses_by_type.filter(id_camera=id['id_camera']).count())
    return data

def get_offences_for_department() -> list:
    data = [[], [], []]
    offenses = Offense.objects.all()
    departments = Employees.objects.order_by().values('department').distinct()
    types = ['В маске', 'Без маски', 'В неправильно надетой маске']
    for t in range(len(types)):
        offenses_by_type = offenses.filter(type_offense=types[t])

        for department in departments:
            data[t].append(offenses_by_type.filter(id_employee__department=department['department']).count())

    return data

def get_offenses_for_month() -> list:
    data = [[], [], []]
    offenses = Offense.objects.all()
    for i in range(1, 13):
        week = offenses.filter(offense_date__month=i)
        data[0].append(week.filter(type_offense='В маске').count())
        data[1].append(week.filter(type_offense='Без маски').count())
        data[2].append(week.filter(type_offense='В неправильно надетой маске').count())
    print(data)
    return data

def statistic_home(request):

    cam = get_offences_for_cam()
    dep = get_offences_for_department()
    month = get_offenses_for_month()

    return render(request, 'statistic.html', {'cam_offenses':cam, 'dep_offenses':dep, 'month':month})
