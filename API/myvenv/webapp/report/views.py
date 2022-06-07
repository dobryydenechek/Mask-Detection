from django.shortcuts import render

def report_home(request):
    return render(request, 'report.html')

