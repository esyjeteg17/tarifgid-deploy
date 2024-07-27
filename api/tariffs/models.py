from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.

from django.db import models

class Tariff(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(blank=True, null=True)
    minutes = models.IntegerField(blank=True, null=True)
    gigabytes = models.IntegerField(blank=True, null=True)
    bonus = models.CharField(max_length=100, blank=True, default='')
    sms = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, default='')
    operator = models.CharField(max_length=100)
    head = models.CharField(max_length=100)
    bonustext = models.TextField(max_length=1000, blank=True, default='')
    region = models.ForeignKey('Region', on_delete=models.CASCADE, blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    tv = models.IntegerField(blank=True, null=True)
    isFavorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тарифы "Мобильные телефоны"'
        verbose_name_plural = 'Тарифы "Мобильные телефоны"'

class Region(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100, blank=True, default='')
    isPublic = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Регионы'
        verbose_name_plural = 'Регионы'

""" class ModemTariff(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(blank=True, null=True, default='')
    minutes = models.IntegerField(blank=True, null=True, default='')
    gigabytes = models.IntegerField(blank=True, null=True, default='')
    bonus = models.CharField(max_length=100, blank=True, default='')
    sms = models.IntegerField(blank=True, null=True, default='')
    link = models.CharField(max_length=100, blank=True, default='')
    operator = models.CharField(max_length=100)
    head = models.CharField(max_length=100)
    bonustext = models.CharField(max_length=1000, blank=True, default='')
    speed = models.IntegerField(blank=True, null=True, default='')
    tv = models.IntegerField(blank=True, null=True, default='')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тарифы "Модемы"'
        verbose_name_plural = 'Тарифы "Модемы"'


class HomephoneTariff(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(blank=True, null=True, default='')
    minutes = models.IntegerField(blank=True, null=True, default='')
    gigabytes = models.IntegerField(blank=True, null=True, default='')
    bonus = models.CharField(max_length=100, blank=True, default='')
    sms = models.IntegerField(blank=True, null=True, default='')
    link = models.CharField(max_length=100, blank=True, default='')
    operator = models.CharField(max_length=100)
    head = models.CharField(max_length=100)
    bonustext = models.CharField(max_length=1000, blank=True, default='')
    speed = models.IntegerField(blank=True, null=True, default='')
    tv = models.IntegerField(blank=True, null=True, default='')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тарифы "Домашние телефоны"'
        verbose_name_plural = 'Тарифы "Домашние телефоны"'


class TVTariff(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(blank=True, null=True, default='')
    minutes = models.IntegerField(blank=True, null=True, default='')
    gigabytes = models.IntegerField(blank=True, null=True, default='')
    bonus = models.CharField(max_length=100, blank=True, default='')
    sms = models.IntegerField(blank=True, null=True, default='')
    link = models.CharField(max_length=100, blank=True, default='')
    operator = models.CharField(max_length=100)
    head = models.CharField(max_length=100)
    bonustext = models.CharField(max_length=1000, blank=True, default='')
    speed = models.IntegerField(blank=True, null=True, default='')
    tv = models.IntegerField(blank=True, null=True, default='')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тарифы "Телевидение"'
        verbose_name_plural = 'Тарифы "Телевидение"'


class InternetTariff(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(blank=True, null=True, default='')
    minutes = models.IntegerField(blank=True, null=True, default='')
    gigabytes = models.IntegerField(blank=True, null=True, default='')
    bonus = models.CharField(max_length=100, blank=True, default='')
    sms = models.IntegerField(blank=True, null=True, default='')
    link = models.CharField(max_length=100, blank=True, default='')
    operator = models.CharField(max_length=100)
    head = models.CharField(max_length=100)
    bonustext = models.CharField(max_length=1000, blank=True, default='')
    speed = models.IntegerField(blank=True, null=True, default='')
    tv = models.IntegerField(blank=True, null=True, default='')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тарифы "Интернет"'
        verbose_name_plural = 'Тарифы "Интернет"'


class SmartTariff(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название тарифа")
    price = models.IntegerField(blank=True, null=True, default='', verbose_name="Цена")
    minutes = models.IntegerField(blank=True, null=True, default='')
    gigabytes = models.IntegerField(blank=True, null=True, default='')
    bonus = models.CharField(max_length=100, blank=True, default='')
    sms = models.IntegerField(blank=True, null=True, default='')
    link = models.CharField(max_length=100, blank=True, default='')
    operator = models.CharField(max_length=100)
    head = models.CharField(max_length=100)
    bonustext = models.CharField(max_length=1000, blank=True, default='')
    speed = models.IntegerField(blank=True, null=True, default='')
    tv = models.IntegerField(blank=True, null=True, default='')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тарифы "Смарт"'
        verbose_name_plural = 'Тарифы "Смарт"' """



