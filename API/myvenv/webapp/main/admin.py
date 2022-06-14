from django.contrib import admin

from .models import Employees, Offense, Cameras

admin.site.register(Employees)
admin.site.register(Offense)
admin.site.register(Cameras)
