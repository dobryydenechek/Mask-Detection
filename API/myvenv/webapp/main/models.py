# import datetime

# from django.db import models


# class Employees(models.Model):
#     id_employee = models.AutoField(primary_key=True)
#     surname = models.CharField('Фамилия', max_length=20)
#     name = models.CharField('Имя', max_length=20)
#     patronymic = models.CharField('Отчество', max_length=20)
#     phone_number = models.CharField('Номер телефона', max_length=15)
#     department = models.CharField('Отдел', max_length=15)
#     photo = models.ImageField('Фотография')
#     email = models.EmailField('Электронная почта')
#     position = models.CharField('Должность', max_length=15)
#     number_of_offenses = models.IntegerField('Количество нарушений')

# class Offense(models.Model):
#     id_offense = models.AutoField(primary_key=True)
#     id_employee = models.ForeignKey('Offenders', on_delete=models.CASCADE)
#     id_camera = models.OneToOneField('Cameras', on_delete = models.SET_NULL, primary_key = True)
#     offense_date = models.DateField('Дата нарушения', default=datetime.date.today())
#     offense_time = models.TimeField('Время нарушения', default=datetime.datetime.now().time)
#     photo_offense = models.ImageField('Фотография нарушения')

# class Cameras(models.Model):
#     id_camera = models.AutoField(primary_key=True)
#     location = models.CharField('Местоположение камеры', max_length=20)
#     rtsp_address = models.CharField('RTSP адрес камеры', max_length=50)