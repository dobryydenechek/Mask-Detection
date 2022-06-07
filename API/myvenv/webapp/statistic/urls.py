from django.urls import path
from . import views

urlpatterns = [
    path('', views.statistic_home, name='statistic_home'),
]