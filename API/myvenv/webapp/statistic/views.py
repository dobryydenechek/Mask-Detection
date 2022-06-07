from django.shortcuts import render

def statistic_home(request):
    return render(request, 'statistic.html')
