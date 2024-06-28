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


class Eighth_page(models.Model):
    p8title=models.CharField(max_length=250)
    p8image=models.ImageField(upload_to="catalog/img/", default='img')
    p8content=models.TextField()
    p8footer=models.TextField()

class Nine_page(models.Model): #Объекты
    p9_title=models.CharField(max_length=250)
    p9_1=models.ImageField(upload_to="catalog/img/", default='img', blank=True, null=True)
    p9_2=models.ImageField(upload_to="catalog/img/", default='img', blank=True, null=True)
    p9_3 = models.ImageField(upload_to="catalog/img/", default='img', blank=True, null=True)
    p9_4 = models.ImageField(upload_to="catalog/img/", default='img', blank=True, null=True)
    p9_5 = models.ImageField(upload_to="catalog/img/", default='img', blank=True, null=True)
    p9_6 = models.ImageField(upload_to="catalog/img/", default='img', blank=True, null=True)
    p9_7 = models.ImageField(upload_to="catalog/img/", default='img', blank=True, null=True)
    p9_8 = models.ImageField(upload_to="catalog/img/", default='img', blank=True, null=True)
    p9_9 = models.ImageField(upload_to="catalog/img/", default='img', blank=True, null=True)
    p9_10 = models.ImageField(upload_to="catalog/img/", default='img', blank=True, null=True)
    p9_11 = models.ImageField(upload_to="catalog/img/", default='img', blank=True, null=True)
    p9_12 = models.ImageField(upload_to="catalog/img/", default='img', blank=True, null=True)
    p9_13 = models.ImageField(upload_to="catalog/img/", default='img', blank=True, null=True)
    p9_14 = models.ImageField(upload_to="catalog/img/", default='img', blank=True, null=True)
    p9_15 = models.ImageField(upload_to="catalog/img/", default='img', blank=True, null=True)

    def __str__(self): # метод, который вместо id будет отображать поле p9_title, как более понятную и приёмлемую информацию
        return self.p9_title # тут в return и указывается какое поле необходимо возвращать вместо id

class Photo(models.Model):
    obect=models.ForeignKey(Nine_page, on_delete=models.PROTECT)
    photo=models.ImageField(upload_to="catalog/img/", default='img')

    def __str__(self): # метод, который вместо id будет отображать поле obect, как более понятную и приёмлемую информацию
        return str(self.obect)+' '+str(self.pk) # тут в return и указывается какое поле необходимо возвращать вместо id

class Ten_page(models.Model):
    p10_img=models.ImageField(upload_to="catalog/img/", default='img')
    p10_title=models.CharField(max_length=250)
    p10_content=models.CharField(max_length=250)