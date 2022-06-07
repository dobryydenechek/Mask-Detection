from django.shortcuts import render

def settings_home(request):
    return render(request, 'settings.html')

