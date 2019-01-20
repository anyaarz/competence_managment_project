from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class Knowledge(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name='Название')
    discription = models.TextField(max_length=500, blank=True, verbose_name='Описание' )

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Proficiency(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name='Название')
    discription = models.TextField(max_length=500, blank=True, verbose_name='Описание')
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Skills(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name='Название')
    discription = models.TextField(max_length=500, blank=True, verbose_name='Описание')
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Job(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Название')
    is_active = models.BooleanField(default=True, verbose_name='Действующий')
    discription = models.TextField(max_length=500, blank=True, verbose_name='Описание')
    knowledge = models.ManyToManyField(Knowledge, related_name = 'know_list', verbose_name='Знания')
    proficiency = models.ManyToManyField(Proficiency, related_name = 'prof_list',verbose_name='Умения')
    skills = models.ManyToManyField(Skills, related_name = 'skills_list',verbose_name='Навыки')
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    is_active = models.BooleanField(default=True, verbose_name='Действующий')
    education = models.TextField(max_length=500, blank=True, verbose_name='Образование')
    job_discription = models.TextField(max_length=500, blank=True, verbose_name='Опыт работы')
    location = models.CharField(max_length=30, blank=True, verbose_name='Локация')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    department = models.CharField(max_length=30, blank=True, verbose_name='Отдел')
    date_applyied = models.DateField(null=True, blank=True, verbose_name='Дата приема на работу')
    date_retired = models.DateField(null=True, blank=True, verbose_name='Дата увольнения')
    job = models.ForeignKey(Job,blank = True, null=True, help_text='Укажите должность сотрудника', verbose_name='Должность',on_delete=models.CASCADE,)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.user.username







