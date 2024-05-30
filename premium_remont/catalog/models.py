from django.db import models

# Create your models here.

class First_page(models.Model):
    title=models.CharField(max_length=250, verbose_name='Наименование организации')
    text=models.CharField(max_length=250, verbose_name='Основной текст')
    preimushestva=models.CharField(max_length=250, verbose_name='Преимущества')
    img=models.ImageField(upload_to="catalog/img/", default='img')

class Second_page(models.Model):
    problems=models.TextField(verbose_name='Проблемы')

class Fourth_page(models.Model):
    title=models.CharField(max_length=250)
    list_title=models.CharField(max_length=250)
    list_text=models.TextField()