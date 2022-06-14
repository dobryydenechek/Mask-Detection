import datetime
from tabnanny import verbose
import django
from django.db import models


class Employees(models.Model):
    id_employee = models.AutoField(primary_key=True)
    surname = models.CharField('Фамилия', max_length=20)
    name = models.CharField('Имя', max_length=20)
    patronymic = models.CharField('Отчество', max_length=20)
    phone_number = models.CharField('Номер телефона', max_length=15)
    department = models.CharField('Отдел', max_length=15)
    photo = models.ImageField('Фотография', upload_to='img/', blank=True)
    email = models.EmailField('Электронная почта')
    position = models.CharField('Должность', max_length=30)
    number_of_offenses = models.IntegerField('Количество нарушений')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
    
    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
    

class Offense(models.Model):
    id_offense = models.AutoField(primary_key=True)
    id_employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    id_camera = models.ManyToManyField('Cameras')
    type_offense = models.CharField('Тип нарушения', max_length=30, default='В маске')
    offense_date = models.DateField('Дата нарушения', default=datetime.date.today())
    offense_time = models.TimeField('Время нарушения', default=django.utils.timezone.now)
    photo_offense = models.ImageField('Фотография нарушения', upload_to='img/', blank=True)

    
    class Meta:
        verbose_name = 'Нарушение'
        verbose_name_plural = 'Нарушения'

    @property
    def photo_url(self):
        if self.photo_offense and hasattr(self.photo_offense, 'url'):
            return self.photo_offense.url

class Cameras(models.Model):
    id_camera = models.AutoField(primary_key=True)
    location = models.CharField('Местоположение камеры', max_length=20)
    rtsp_address = models.CharField('RTSP адрес камеры', max_length=50)

    class Meta:
        verbose_name = 'Камера'
        verbose_name_plural = 'Камеры'